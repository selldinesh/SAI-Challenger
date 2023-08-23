from pprint import pprint


class TestSaiRpfGroup:
    # object with no attributes

    def test_rpf_group_create(self, npu):
        commands = [
            {
                'name': 'rpf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_RPF_GROUP',
                'attributes': [],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_rpf_group_remove(self, npu):
        commands = [{'name': 'rpf_group_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
