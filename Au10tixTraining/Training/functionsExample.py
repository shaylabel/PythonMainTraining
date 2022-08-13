def check_numbers (param1,param2):

    res=0
    if (param1!=0):
        res=param1+param2
    else :
        res=param1*param2
    return res


def print_num(param_to_print):
    print (param_to_print)

def find_string (param1):
    param1.count('r')

def word_analyzer(word):

    if (word.count<3):
        print ("word length is lower than 3")
        return 3
    else:
        return 45

def get_details_from_db(id):
    first_name='John'  # demo for read from DB
    last_name='Smith'
    id_from_db=id
    list_res=[first_name,last_name,id_from_db]
    return list_res


# the code start from here

list_from_db = get_details_from_db(1)
first_name_from_db = list_from_db[0]
print ('end test ' )
