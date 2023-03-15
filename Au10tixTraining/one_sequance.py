def find_sequance(under_test, start_search) :
    res={'start_point':0,
         'end_point':0,
         }
    print ('try to find sequance at ',under_test)
    res_start= under_test.index("1",start_search)
    for indx in range(res_start,len(under_test)):
        if (under_test[indx] == "0"):
            res_end = indx
            break
        # else:
            # res_end=len(under_test)
    seq_length = res_end-res_start
    res['start_point']=res_start
    res['end_point']=res_end

    print ('debug point')

    return seq_length

def find_all_start(under_test):
    all_start=[0]
    pattern= '101'
    indx=0
    amount = under_test.count(pattern)
    for i in range(amount):
        indx=under_test.index(pattern,indx+1)
        all_start.append(indx+1)
    return all_start



under_test='1101111111011111011110011101001100111000111110001110111'
final_res=0
start_search=0
final=[]

if (under_test.count('0')==0|(under_test.count('00')==0)):
    final_res=len(under_test)
else:
    under_test = under_test.replace('101', '111')
    all_start=find_all_start(under_test)

    for start_point in all_start:
        res = find_sequance(under_test, start_point)
        final.append(res)
        final.sort(reverse = True)

    # for i in range(1,len(under_test),1):
        # char_before=under_test[i-1]
        # char_after=under_test[i+1]
        # sub=char_before+under_test[i]+char_after
        # if (sub=='101'):


print("test end, the result is  ",final[0])
