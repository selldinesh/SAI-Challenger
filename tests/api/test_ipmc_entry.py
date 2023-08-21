from pprint import pprint


class TestSaiIpmcEntry:
    # object with parent SAI_OBJECT_TYPE_RPF_GROUP

    def test_ipmc_entry_create(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_RPF_GROUP',
                'attributes': [],
            },
            {
                'name': 'ipmc_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPMC_ENTRY',
                'attributes': [
                    'SAI_IPMC_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                    'SAI_IPMC_ENTRY_ATTR_RPF_GROUP_ID',
                    '$rpf_group_1',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipmc_entry_remove(self, npu):
        commands = [
            {
                'name': 'ipmc_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'vr_id': 'TODO',
                    'type': 'TODO',
                    'destination': 'TODO',
                    'source': 'TODO',
                },
                'op': 'remove',
            },
            {'name': 'rpf_group_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
