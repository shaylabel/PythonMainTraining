tested_num =35;
txt = "The best things in life are free!"

print ('test start')
def dived(num):
    for x in range (0,num):
        print('tested number is ', x)
        if (x - 7 == 10):
            print('17 found ')

        if (x % 7 ==0) :
            print ('num found,num= ',x)

        if "7"  in str(x):
            print("yes, 7 is present into ",x)

     

dived(tested_num)

print ('test end')
