from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiMacsec:
    # object with no parents

    def test_macsec_create(self, npu):
        commands = [
            {
                'name': 'macsec_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MACSEC',
                'attributes': [
                    'SAI_MACSEC_ATTR_DIRECTION',
                    'SAI_MACSEC_DIRECTION_EGRESS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_macsec_remove(self, npu):
        commands = [{'name': 'macsec_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
