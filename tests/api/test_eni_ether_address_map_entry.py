from pprint import pprint


class TestSaiEniEtherAddressMapEntry:
    # object with no attributes

    def test_eni_ether_address_map_entry_create(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ENI_ETHER_ADDRESS_MAP_ENTRY',
                'attributes': [],
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_eni_ether_address_map_entry_remove(self, npu):
        commands = [
            {
                'name': 'eni_ether_address_map_entry_1',
                'key': {'switch_id': '$SWITCH_ID', 'address': 'TODO'},
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
