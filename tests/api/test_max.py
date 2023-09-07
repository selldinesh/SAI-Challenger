from pprint import pprint


class TestSaiMax:
    # object with no attributes

    def test_max_create(self, npu):
        commands = [
            {
                'name': 'max_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MAX',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_max_remove(self, npu):
        commands = [{'name': 'max_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
