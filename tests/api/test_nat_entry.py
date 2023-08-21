from pprint import pprint


class TestSaiNatEntry:
    # object with no attributes

    def test_nat_entry_create(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NAT_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'nat_type': 'TODO',
                    'data': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_nat_entry_remove(self, npu):
        commands = [
            {
                'name': 'nat_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'nat_type': 'TODO',
                    'data': 'TODO',
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
