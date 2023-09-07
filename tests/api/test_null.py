from pprint import pprint


class TestSaiNull:
    # object with no attributes

    def test_null_create(self, npu):
        commands = [
            {
                'name': 'null_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_NULL',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_null_remove(self, npu):
        commands = [{'name': 'null_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
