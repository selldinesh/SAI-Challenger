from pprint import pprint


class TestSaiIpsecSa:
    # object with parent SAI_OBJECT_TYPE_IPSEC

    def test_ipsec_sa_create(self, npu):
        commands = [
            {
                'name': 'ipsec_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC',
                'attributes': ['SAI_IPSEC_ATTR_EXTERNAL_SA_INDEX_ENABLE', 'True'],
            },
            {
                'name': 'ipsec_sa_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_IPSEC_SA',
                'attributes': [
                    'SAI_IPSEC_SA_ATTR_IPSEC_DIRECTION',
                    'SAI_IPSEC_DIRECTION_EGRESS',
                    'SAI_IPSEC_SA_ATTR_IPSEC_ID',
                    '$ipsec_1',
                    'SAI_IPSEC_SA_ATTR_IPSEC_SPI',
                    '10',
                    'SAI_IPSEC_SA_ATTR_ENCRYPT_KEY',
                    'typedef UINT8   sai_encrypt_key_t[32]',
                    'SAI_IPSEC_SA_ATTR_SALT',
                    '10',
                    'SAI_IPSEC_SA_ATTR_AUTH_KEY',
                    'typedef UINT8   sai_auth_key_t[16]',
                    'SAI_IPSEC_SA_ATTR_TERM_DST_IP',
                    '180.0.0.1',
                    'SAI_IPSEC_SA_ATTR_TERM_VLAN_ID',
                    '10',
                    'SAI_IPSEC_SA_ATTR_TERM_SRC_IP',
                    '180.0.0.1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_ipsec_sa_remove(self, npu):
        commands = [
            {'name': 'ipsec_sa_1', 'op': 'remove'},
            {'name': 'ipsec_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
