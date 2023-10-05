from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiAclEntry:
    # object with parent SAI_OBJECT_TYPE_ACL_TABLE

    def test_acl_entry_create(self, npu):
        commands = [
            {
                'name': 'acl_table_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            },
            {
                'name': 'acl_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_ENTRY',
                'attributes': ['SAI_ACL_ENTRY_ATTR_TABLE_ID', '$acl_table_1'],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_acl_entry_remove(self, npu):
        commands = [
            {
                'name': 'acl_entry_1',
                'op': 'remove',
            },
            {
                'name': 'acl_table_1',
                'op': 'remove',
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
