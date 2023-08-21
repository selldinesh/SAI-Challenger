from pprint import pprint


class TestSaiMacsecSc:
    # object with parent SAI_OBJECT_TYPE_MACSEC_FLOW

    def test_macsec_sc_create(self, npu):
        commands = [
            {
                'name': 'macsec_flow_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_FLOW',
                'attributes': [
                    'SAI_MACSEC_FLOW_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            },
            {
                'name': 'macsec_sc_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SC',
                'attributes': [
                    'SAI_MACSEC_SC_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SC_ATTR_FLOW_ID',
                    '$macsec_flow_1',
                    'SAI_MACSEC_SC_ATTR_MACSEC_SCI',
                    '10',
                    'SAI_MACSEC_SC_ATTR_MACSEC_CIPHER_SUITE',
                    'SAI_MACSEC_CIPHER_SUITE_GCM_AES_128',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_macsec_sc_remove(self, npu):
        commands = [
            {'name': 'macsec_sc_1', 'op': 'remove'},
            {'name': 'macsec_flow_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
