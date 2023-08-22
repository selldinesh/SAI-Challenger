from pprint import pprint


class TestSaiMacsecPort:
    # object with parent SAI_OBJECT_TYPE_PORT

    def test_macsec_port_create(self, npu):
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
                'name': 'macsec_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_PORT',
                'attributes': [
                    'SAI_MACSEC_PORT_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_PORT_ATTR_PORT_ID',
                    '$port_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_macsec_port_remove(self, npu):
        commands = [
            {'name': 'macsec_port_1', 'op': 'remove'},
            {'name': 'port_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)

