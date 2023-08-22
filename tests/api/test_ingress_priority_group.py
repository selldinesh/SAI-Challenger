from pprint import pprint


class TestSaiIngressPriorityGroup:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_ingress_priority_group_create(self, npu):
        commands = [
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'ingress_priority_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_INGRESS_PRIORITY_GROUP',
                'attributes': [
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_PORT',
                    '$port_1',
                    'SAI_INGRESS_PRIORITY_GROUP_ATTR_INDEX',
                    '1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ingress_priority_group_remove(self, npu):
        commands = [
            {'name': 'ingress_priority_group_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
