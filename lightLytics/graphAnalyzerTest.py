from datetime import datetime
from lightLytics.baselight import baseLightlytics

import matplotlib.pyplot as plt
import numpy as np
from lightLytics.utils import utils

# the occurncy is the ID of each founded log

class graphAnalyzerTest(baseLightlytics):

    utils = utils(baseLightlytics.path_logs)

    utils.test_end()
    file = open(baseLightlytics.path_logs, 'r')
    lines = file.readlines()
    data = baseLightlytics.data
    time_line = []
    occurrence = []

    line_count = 0
    match_count = 0

    for line in lines:
        line = line.strip();

        for action in baseLightlytics.actions_to_find:
            if (action) in line:
                match_count += 1
                data = utils.get_dates_from_line(line, data)
                occurrence.append(match_count)
                time_line.append(data['date'] + data['time'])

        line_count += 1

    xpoints = np.array(occurrence)
    ypoints = np.array(time_line)
    plt.plot(xpoints, ypoints)



    # setting title and X-axis
    print('Graph process start')
    plt.gca().get_yaxis().set_visible(False)  # disable the visuality of Y axis , it displayed unclear (contains date+time- too large )
    plt.xlabel(baseLightlytics.graph_x_label)
    plt.title(baseLightlytics.graph_title)
    plt.show()
    print('Graph process completed')


    file.close()
    utils.test_end()
