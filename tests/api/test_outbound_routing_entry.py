from pprint import pprint


class TestSaiOutboundRoutingEntry:
    # object with no attributes

    def test_outbound_routing_entry_create(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_OUTBOUND_ROUTING_ENTRY',
                'attributes': [],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'destination': 'TODO',
                },
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_outbound_routing_entry_remove(self, npu):
        commands = [
            {
                'name': 'outbound_routing_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'eni_id': 'TODO',
                    'destination': 'TODO',
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
