import os.path
import json

from lightLytics.baselight import baseLightlytics


class utils(baseLightlytics):
    def __init__(self, path):
        self.path = path
        is_exist = os.path.exists(path)
        assert True is is_exist, 'log file did not found as expected'

    event_id = 0

# analyze  for scanning per each row
    def is_scanned_from_line(self, line,info):
        if 'Scanning' in line:
            info['scan'] = True
        else:
            info['scan'] = False
        return info

# parsing the action/aws_event_name per each row
    def get_action_from_line(self, line,info):
        info['aws_event_name'] = ""

        if baseLightlytics.paterrn_actions in line:
            index1 = line.index(baseLightlytics.paterrn_actions) + len(baseLightlytics.paterrn_actions)
            index2 = line.index('in', index1)

            action = line[index1:index2].strip()
            info['aws_event_name'] = action
        return info


# parsing the dates data per each tested row
    def get_dates_from_line(self, line,info):
        is_correct = True
        indx1 = line.index(' ')
        date = line[:indx1]
        time = line[indx1 + 1:line.index(' - ')]
        info['date'] = date
        info['time'] = time
#  prepare to not add to result if date is missed, not ready
        if (info['date'] != "") | (info['time'] != ""):
            is_correct = False
        return info

# parsing the attribute json per each tested log  - not needed
    def get_attribute_from_line(self,line,info):
        inex1 = line.index(' - ')
        inex2 = line.find('[', inex1)+1
        attribute = line[inex2:]
        attribute = attribute[:-1]
        info['event_attr'] = attribute
        return info

# parsing the event  resource  per each tested log
    def get_event_from_line(self, line,action,info):
         inex1 = line.index(action)
         inex2 = line.find(' ', inex1+len(action)+3)
         attribute = line[inex1:inex2]
         attribute=attribute.replace(action,"").strip()
         info['event_resource'] = attribute
         return info

# generate event from info dict.
    def generate_event(self,info,id):
        name = 'event_'+str(id)
        info['name'] = name
        json_object = json.dumps(info)
        return json_object

    def generate_eventV1(self,info,id):
        line= 'event_'+str(id) + ':{'

        for k, v in info.items():
            pair = k + ':' + v + ','
            line = line + pair
        line = '{' + line +  '}},'
        return line


    def generate_events(self,event,json_objects):
        x=json_objects.load(json_objects)
        x=x.update(event)
        return x


# prapare to wrote into result file
    def write_json_to_file(self,json,url):
        # jsonString = json.dumps(json)
        jsonFile = open(url, "w")
        jsonFile.write(json)
        jsonFile.close()

    def test_start(self):
        print ('test start')

    def test_end(self):
        print ('test end')


