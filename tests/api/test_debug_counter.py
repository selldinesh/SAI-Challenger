from pprint import pprint

import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiDebugCounter:
    # object with no parents

    def test_debug_counter_create(self, npu):
        commands = [
            {
                'name': 'debug_counter_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_DEBUG_COUNTER',
                'attributes': [
                    'SAI_DEBUG_COUNTER_ATTR_TYPE',
                    'SAI_DEBUG_COUNTER_TYPE_PORT_IN_DROP_REASONS',
                ],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_debug_counter_remove(self, npu):
        commands = [
            {
                'name': 'debug_counter_1',
                'op': 'remove',
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
