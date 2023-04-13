from vhive import Utils

# martin@vhive.ai



with open('example.txt') as f:
    lines = f.readlines()

    for line in lines:
        line_as_list = Utils.line_analyzer(line)

    Utils.json_creator();

print('test end ')
