from pprint import pprint


class TestSaiMcastFdbEntry:
    # object with parent SAI_OBJECT_TYPE_L2MC_GROUP

    def test_mcast_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            },
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'attributes': [
                    'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
                    '$l2mc_group_1',
                    'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_mcast_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
                'op': 'remove',
            },
            {'name': 'l2mc_group_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
