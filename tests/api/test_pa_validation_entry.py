from pprint import pprint


class TestSaiPaValidationEntry:
    # object with no attributes

    def test_pa_validation_entry_create(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PA_VALIDATION_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_pa_validation_entry_remove(self, npu):
        commands = [
            {
                'name': 'pa_validation_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'vnet_id': 'TODO', 'sip': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
