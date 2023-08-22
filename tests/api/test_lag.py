from pprint import pprint


class TestSaiLag:
    # object with no attributes

    def test_lag_create(self, npu):
        commands = [
            {
                'name': 'lag_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_LAG',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_lag_remove(self, npu):
        commands = [{'name': 'lag_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
