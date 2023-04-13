import json

High = []
Medium = []
Low = []

def line_analyzer(line):
    indx = line.index(":")
    val = line[:indx]
    sev = line[indx:]



    if (sev.count("High") > 0):
        sev_as_int = 2
        High.append(val)

    elif (sev.count("Medium") > 0):
        sev_as_int = 1
        Medium.append(val)

    else :
        sev_as_int = 0
        Low.append(val)

    line_as_list = []
    line_as_list.append(sev_as_int)
    line_as_list.append(val)

    return line_as_list

def json_creator():
    low_json = json.dumps(Low)
    med_json = json.dumps(Medium)
    high_json = json.dumps(High)
    json.dumps(Low)

    with open("result", "w") as outfile:
        json.dump(high_json, outfile)
    print("stop here ")
