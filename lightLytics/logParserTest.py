import json

import self

from lightLytics.baselight import baseLightlytics
from lightLytics.utils import utils


class logParserTest(baseLightlytics):
    utils = utils(baseLightlytics.path_logs)
    data = baseLightlytics.data

    utils.test_start()
    file = open(baseLightlytics.path_logs, 'r')
    lines = file.readlines()

    json_object_events = ""
    line_count = 0
    id = 0

    for line in lines:
        line = line.strip()
        for action in baseLightlytics.actions_to_find:

            if (action) in line:
                id += 1
                data['event_type'] = action.replace('-', '').strip()
                data = utils.get_dates_from_line(line, data)
                data = utils.get_event_from_line(line, action, data)
                data = utils.get_attribute_from_line(line, data)

                # getting data from Prev. and next lines only if lines available
                if (line_count > 0):
                    data = utils.get_action_from_line(lines[line_count - 1], data)

                # if (line_count != len(lines)):
                    # data = utils.is_scanned_from_line(lines[line_count + 1], data)

                # json_object_event = utils.generate_event(data, id)
                json_object_event = utils.generate_eventV1(data, id)

                # utils.generate_events(json_object_event,json_object_event)
                json_object_events=json_object_events+json_object_event
                break

        line_count += 1
    utils.write_json_to_file(json_object_events,"files/result.json")
    print(json_object_events)
    file.close()
    utils.test_end()
