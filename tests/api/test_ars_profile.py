from pprint import pprint
import pytest


@pytest.fixture(scope='module', autouse=True)
def skip_all(testbed_instance):
    testbed = testbed_instance
    if testbed is not None and len(testbed.npu) != 1:
        pytest.skip('invalid for {} testbed'.format(testbed.name))


@pytest.mark.npu
class TestSaiArsProfile:
    # object with no attributes

    def test_ars_profile_create(self, npu):
        commands = [
            {
                'name': 'ars_profile_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ARS_PROFILE',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_ars_profile_remove(self, npu):
        commands = [{'name': 'ars_profile_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
