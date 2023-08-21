from pprint import pprint


class TestSaiSystemPort:
    # object with no parents

    def test_system_port_create(self, npu):
        commands = [
            {
                'name': 'system_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_SYSTEM_PORT',
                'attributes': ['SAI_SYSTEM_PORT_ATTR_CONFIG_INFO', 'TODO'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_system_port_remove(self, npu):
        commands = [{'name': 'system_port_1', 'op': 'remove'}]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
