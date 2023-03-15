class baseLightlytics:


    path_logs = 'files/exercise.log'

    # define the pattern to find tested log, '-' added in order to prevent find not needed logs
    actions_to_find = ['- create', '- delete', '- add', '- remove', '- modify', '- hard-modify']
    data_as_list = ['date', 'time', 'aws_event_name','event_type','event_resource','event_attr']
    data = dict.fromkeys(data_as_list)

    paterrn_actions = 'performed'
    graph_x_label = 'X - Occurancy'
    graph_title = 'X - Occurancy'




