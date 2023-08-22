from pprint import pprint


class TestSaiFdbEntry:
    # object with no parents

    def test_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_FDB_ENTRY',
                'attributes': ['SAI_FDB_ENTRY_ATTR_TYPE', 'SAI_FDB_ENTRY_TYPE_DYNAMIC'],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'fdb_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
