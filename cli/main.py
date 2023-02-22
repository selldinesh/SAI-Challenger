#!/usr/bin/python3

import click
import json
import os
import shutil

from saichallenger.common.sai_data import SaiObjType
from saichallenger.common.sai import Sai
from saichallenger.common.sai_npu import SaiNpu
from saichallenger.common.sai_testbed import SaiTestbedMeta
from saichallenger.common.sai_testbed import SaiTestbed

VERSION = '0.1'

sai_c_path = "/etc/sai-c"
sai_c_cfg_file = sai_c_path + "/cfg.json"

exec_params = {
    # Generic parameters
    "traffic": False,
    "testbed": None,
     # DUT specific parameters
    "alias": "dut",
    "asic": None,
    "target": None,
    "sku": None,
    "client": {
        "type": "redis",
        "config": {
            "ip": "localhost",
            "port": 6379,
            "loglevel": "NOTICE",
        }
    }
}

# This is our main entrypoint - the main 'sai' command
@click.group()
def cli():
    pass


@cli.group()
def testbed():
    """Manage SAI testbed"""
    pass


# 'testbed set' command
@testbed.command()
@click.argument('testbed', metavar='<name>', required=True, type=str)
def set(testbed):
    """Set SAI testbed"""

    cfg = {
        "testbed": testbed
    }
    if os.path.exists(sai_c_path):
        shutil.rmtree(sai_c_path)
    os.makedirs(sai_c_path)
    with open(sai_c_cfg_file, "w+") as f:
        f.write(json.dumps(cfg, indent=4) + "\n")


def get_sai_testbed() -> SaiTestbed:
    cfg = None
    try:
        with open(sai_c_cfg_file, "r") as f:
            cfg = json.load(f)
    except:
        return None

    testbed = None
    if cfg:
        testbed_name = cfg.get("testbed", "undefined")
        if testbed_name != "undefined":
            testbed = SaiTestbed("/sai-challenger", testbed_name, False, True)
            testbed.spawn()
    return testbed


def get_sai_entity() -> Sai:
    testbed = get_sai_testbed()
    if testbed:
        # TODO: Retrieve SAI entiry by alias or by type and index
        return testbed.npu[0]
    # fall back to the default
    return SaiNpu(exec_params)


# 'testbed info' command
@testbed.command()
def info():
    """Print SAI testbed details"""

    click.echo()
    try:
        with open(sai_c_cfg_file, "r") as f:
            cfg = json.load(f)
    except:
        click.echo("SAI testbed name:   undefined")
        click.echo()
        return False

    testbed = cfg.get("testbed", "undefined")
    click.echo("SAI testbed name:      {}".format(testbed))
    if testbed == "undefined":
        click.echo()
        return False

    meta = SaiTestbedMeta("/sai-challenger", testbed)
    target_type = "npu"
    cfg = meta.config.get(target_type, None)
    if not cfg:
        target_type = "dpu"
        cfg = meta.config.get(target_type, None)
    if not cfg:
        target_type = "phy"
        cfg = meta.config.get(target_type, None)
    if not cfg:
        click.echo()
        return True

    click.echo("Active target type:    {}".format(target_type))
    click.echo("Active target name:    {}".format(cfg[0]["alias"]))
    click.echo("Active target API:     {}".format(cfg[0]["client"]["type"]))
    click.echo("Active target IP:      {}".format(cfg[0]["client"]["config"]["ip"]))
    click.echo("Active target HWSKU:   {}".format(cfg[0]["sku"]))
    click.echo()


# 'testbed init' command
@testbed.command()
def init():
    """Initialize testbed"""

    click.echo()
    testbed = get_sai_testbed()
    if not testbed:
        click.echo("The testbed is undefined!\n")
        return False

    testbed.init()
    click.echo("The testbed \"{}\" initialization completed!\n".format(testbed.name))


@cli.group()
def dut():
    """Manage SAI DUT"""
    pass


# DUT 'init' command
@dut.command()
@click.argument('dut', metavar='[<DUT alias>]', required=False, type=str)
def init(dut):
    """Initialize DUT environment that some number of SAI devices"""

    if not dut:
        dut = "default"

    testbed = get_sai_testbed()
    if not testbed:
        click.echo(f"Failed to initialize {dut} DUT. The testbed is undefined!\n")
        return False

    if not testbed.dut:
        click.echo(f"Failed to initialize {dut} DUT. The DUT is undefined!\n")
        return False

    if dut == "default":
        testbed.dut[0].init()
        click.echo()
        return True

    for item in testbed.dut:
        if item.alias == dut:
            item.init()
            click.echo()
            return True

    click.echo(f"Unknown DUT {dut}!\n")
    return False


# DUT 'set' command
@dut.command()
@click.argument('dut', metavar='[<DUT alias>]', required=True, type=str)
@click.argument('asic', metavar='[<ASIC alias>]', required=False, type=str)
def set(dut, asic):
    click.echo("Not implemented\n")
    return False


# 'init' command
@cli.command()
def init():
    """Initialize SAI switch"""

    click.echo()

    sai = get_sai_entity()
    if not sai:
        click.echo("SAI entity is undefined!\n")
        return False

    sai.reset()
    asic = sai.cfg.get("asic", "generic SAI switch")
    target = sai.cfg.get("target", "generic target")
    click.echo("Initialized {} on {}\n".format(asic, target))


# 'get' command
@cli.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
@click.argument('attrs', metavar='<attr-1> .. <attr-n>', required=True, type=str, nargs=-1)
def get(oid, attrs):
    """Retrieve SAI object's attributes"""

    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    sai = get_sai_entity()

    obj_type = sai.vid_to_type(oid)
    for attr in attrs:
        attr_type = sai.get_obj_attr_type(obj_type, attr)
        if attr_type is None:
            click.echo("Unknown SAI object's attribute {}\n".format(attr))
            return False

        status, data = sai.get_by_type(oid, attr, attr_type, False)
        if status != "SAI_STATUS_SUCCESS":
            click.echo(status + '\n')
            return False

        data = data.to_json()
        click.echo("{:<48} {}".format(data[0], data[1]))

    click.echo()


# 'set' command
@cli.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
@click.argument('attr', metavar='<attr>', required=True, type=str)
@click.argument('value', metavar='<value>', required=True, type=str)
def set(oid, attr, value):
    """Set SAI object's attribute value"""

    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    if not attr.startswith("SAI_"):
        click.echo("Invalid SAI object's attribute {} provided\n".format(attr))
        return False

    sai = get_sai_entity()
    status = sai.set(oid, [attr, value], False)
    click.echo(status + '\n')


# 'create' command
@cli.command()
@click.argument('obj_type', metavar='<SAI object type>', required=True, type=str)
@click.argument('attrs', metavar='<attr> <value>', required=True, type=str, nargs=-1)
def create(obj_type, attrs):
    """Create SAI object"""

    click.echo()
    obj_type = obj_type.upper()
    try:
        obj_type = SaiObjType[obj_type]
    except KeyError:
        click.echo("Unknown SAI object type '{}'\n".format(obj_type))
        return False

    if len(attrs) % 2 != 0:
        click.echo("Invalid SAI object's attributes {} provided\n".format(attrs))
        return False

    sai = get_sai_entity()
    status, oid = sai.create(obj_type, attrs, False)
    if status == "SAI_STATUS_SUCCESS":
        click.echo("Created SAI object {} with {}\n".format(obj_type.name, oid))
    else:
        click.echo(status + '\n')


# 'remove' command
@cli.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
def remove(oid):
    """Remove SAI object"""

    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    sai = get_sai_entity()
    status = sai.remove(oid, False)
    click.echo(status + '\n')


# 'list' command
@cli.command()
@click.argument('obj_type', metavar='[<SAI object type>]', required=False, type=str)
def list(obj_type):
    """List SAI object IDs"""

    click.echo()
    if obj_type is None:
        for obj in SaiObjType:
            click.echo(obj.name.lower())
        click.echo()
        return

    obj_type = obj_type.upper()
    try:
        obj_type = SaiObjType[obj_type]
    except KeyError:
        if obj_type != "ALL":
            click.echo("Unknown SAI object type '{}'\n".format(obj_type))
            return False
        obj_type = None

    sai = get_sai_entity()

    oids = sai.get_oids(obj_type)
    for key, oids in oids.items():
        click.echo(key)
        for idx, oid in enumerate(oids):
            click.echo("{:>8})  {}".format(idx + 1, oid))
        click.echo()


# 'dump' command
@cli.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
def dump(oid):
    """ List SAI object's attribute value"""
    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    sai = get_sai_entity()
    obj_type = sai.vid_to_type(oid)
    meta = sai.get_meta(obj_type)

    for attr in meta['attributes']:
        status, data = sai.get_by_type(oid, attr['name'], attr['properties']['type'], False)
        if status == "SAI_STATUS_SUCCESS":
            data = data.to_json()
            click.echo("{:<50} {}".format(data[0], data[1]))
        else:
            click.echo("{:<50} {}".format(attr['name'], status))
    click.echo()


@cli.group()
def stats():
    """Manage SAI object's stats"""
    pass


# 'stats get' command
@stats.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
@click.argument('cntrs', metavar='<cntrs>', required=True, type=str, nargs=-1)
def get(oid, cntrs):
    """Get SAI object's stats"""

    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    sai = get_sai_entity()

    attrs = []
    for cntr in cntrs:
        attrs.append(cntr)
        attrs.append('')

    status, data = sai.get_stats(oid, attrs, False)
    if status != "SAI_STATUS_SUCCESS":
        click.echo(status + '\n')
        return False

    data = data.counters()
    for cntr in cntrs:
        click.echo("{:<48} {:>8}".format(cntr, data[cntr]))
    click.echo()


# 'stats clear' command
@stats.command()
@click.argument('oid', metavar='<oid>', required=True, type=str)
@click.argument('cntrs', metavar='<cntrs>', required=True, type=str, nargs=-1)
def clear(oid, cntrs):
    """Clear SAI object's stats"""

    click.echo()
    if not oid.startswith("oid:"):
        click.echo("SAI object ID must start with 'oid:' prefix\n")
        return False

    sai = get_sai_entity()

    attrs = []
    for cntr in cntrs:
        attrs.append(cntr)
        attrs.append('')

    status = sai.clear_stats(oid, attrs, False)
    click.echo(status + '\n')


# 'version' subcommand
@cli.command()
def version():
    """Display version info"""
    click.echo("SAI CLI version {0}".format(VERSION))


if __name__ == "__main__":
    cli()
