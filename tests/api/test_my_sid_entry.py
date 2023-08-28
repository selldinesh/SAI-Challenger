from pprint import pprint


class TestSaiMySidEntry:
    # object with no parents

    def test_my_sid_entry_create(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MY_SID_ENTRY',
                'attributes': [
                    'SAI_MY_SID_ENTRY_ATTR_ENDPOINT_BEHAVIOR',
                    'SAI_MY_SID_ENTRY_ENDPOINT_BEHAVIOR_E',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'locator_block_len': 'TODO',
                    'locator_node_len': 'TODO',
                    'function_len': 'TODO',
                    'args_len': 'TODO',
                    'sid': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_my_sid_entry_remove(self, npu):
        commands = [
            {
                'name': 'my_sid_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'locator_block_len': 'TODO',
                    'locator_node_len': 'TODO',
                    'function_len': 'TODO',
                    'args_len': 'TODO',
                    'sid': 'TODO',
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
