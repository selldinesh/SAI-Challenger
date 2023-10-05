from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiPolicer:
    # object with no parents

    def test_policer_create(self, npu):
        commands = [
            {
                'name': 'policer_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_POLICER',
                'attributes': [
                    'SAI_POLICER_ATTR_METER_TYPE',
                    'SAI_METER_TYPE_PACKETS',
                    'SAI_POLICER_ATTR_MODE',
                    'SAI_POLICER_MODE_SR_TCM',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_policer_remove(self, npu):
        commands = [
            {
                'name': 'policer_1',
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
