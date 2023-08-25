from pprint import pprint


class TestSaiMacsecSa:
    # object with parent SAI_OBJECT_TYPE_MACSEC_SC

    def test_macsec_sa_create(self, npu):
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
            {
                'name': 'macsec_sa_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC_SA',
                'attributes': [
                    'SAI_MACSEC_SA_ATTR_MACSEC_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                    'SAI_MACSEC_SA_ATTR_SC_ID',
                    '$macsec_sc_1',
                    'SAI_MACSEC_SA_ATTR_AN',
                    '1',
                    'SAI_MACSEC_SA_ATTR_SAK',
                    'typedef UINT8   sai_macsec_sak_t[32]',
                    'SAI_MACSEC_SA_ATTR_SALT',
                    'typedef UINT8   sai_macsec_salt_t[12]',
                    'SAI_MACSEC_SA_ATTR_AUTH_KEY',
                    'typedef UINT8   sai_macsec_auth_key_t[16]',
                    'SAI_MACSEC_SA_ATTR_MACSEC_SSCI',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_macsec_sa_remove(self, npu):
        commands = [
            {'name': 'macsec_sa_1', 'op': 'remove'},
            {'name': 'macsec_sc_1', 'op': 'remove'},
            {'name': 'macsec_flow_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
