from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiVlan:
    # object with no parents

    def test_vlan_create(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)


    @pytest.mark.dependency(name='test_sai_vlan_attr_max_learned_addresses_set')
    def test_sai_vlan_attr_max_learned_addresses_set(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'set',
                'attributes': ['SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values set =======')
        pprint(results)

    @pytest.mark.dependency(depends=['test_sai_vlan_attr_max_learned_addresses_set'])
    def test_sai_vlan_attr_max_learned_addresses_get(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'get',
                'attributes': ['SAI_VLAN_ATTR_MAX_LEARNED_ADDRESSES'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        for command in results:
            for attribute in command:
                pprint(attribute.raw())
        r_value = results[0][0].value()
        print(r_value)
        assert r_value == '0', 'Get error, expected 0 but got %s' % r_value


    def test_vlan_remove(self, npu):
        commands = [{'name': 'vlan_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
