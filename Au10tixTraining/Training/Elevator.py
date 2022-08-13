import math
import random
parking = 3

def get_floor(elav,start,end):
    is_parking_start=is_parking(start)
    is_parking_end=is_parking(end)


    if (start<end):
        return 0
    if (end<start):
        floor=random.randint(start, end)
        print (elav+'floor is ')
        return floor

def is_parking(floor):
    if (floor==parking):
        return 0
    elif (floor!=parking):
        return floor




class Elevator:
    print (' start test')
    f1=get_floor('elav1',0,10)
    f2=get_floor('elav2',2,12)
    f1=is_parking(f1)
    f2=is_parking(f2)
    assert 4==5

    print ('end test')