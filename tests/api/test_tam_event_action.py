from pprint import pprint


class TestSaiTamEventAction:
    # object with parent SAI_OBJECT_TYPE_TAM_REPORT

    def test_tam_event_action_create(self, npu):
        commands = [
            {
                'name': 'tam_report_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_REPORT',
                'attributes': ['SAI_TAM_REPORT_ATTR_TYPE', 'SAI_TAM_REPORT_TYPE_SFLOW'],
            },
            {
                'name': 'tam_event_action_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TAM_EVENT_ACTION',
                'attributes': [
                    'SAI_TAM_EVENT_ACTION_ATTR_REPORT_TYPE',
                    '$tam_report_1',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_tam_event_action_remove(self, npu):
        commands = [
            {'name': 'tam_event_action_1', 'op': 'remove'},
            {'name': 'tam_report_1', 'op': 'remove'},
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'
