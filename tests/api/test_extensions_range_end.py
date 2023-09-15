from pprint import pprint


class TestSaiExtensionsRangeEnd:
    # object with no attributes

    def test_extensions_range_end_create(self, npu):
        commands = [
            {
                'name': 'extensions_range_end_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_EXTENSIONS_RANGE_END',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)

    def test_extensions_range_end_remove(self, npu):
        commands = [{'name': 'extensions_range_end_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
