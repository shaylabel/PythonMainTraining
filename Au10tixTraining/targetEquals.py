

nums= [1,2,3,7,8,6,10,5]
target = 14
is_found=False

for loop1 in range (0, len(nums)):
    for loop2 in range (0, len(nums)):
        num1= nums[loop1]
        num2=nums[loop2]
        if (loop1==loop2):
            continue
        if (num1+num2==target):
            is_found=True
            print ('match found at the following indexes :', loop1, 'and', loop2)
            break
    if is_found:
        break