from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiSamplepacket:
    # object with no parents

    def test_samplepacket_create(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SAMPLEPACKET',
                'attributes': ['SAI_SAMPLEPACKET_ATTR_SAMPLE_RATE', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_samplepacket_remove(self, npu):
        commands = [
            {
                'name': 'samplepacket_1',
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
