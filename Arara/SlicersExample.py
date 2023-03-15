# print sub string
pattern = "May the Forces be with you."
print(pattern[2:10])
print(pattern[2:])  # print from place 2 to the end
print(pattern[:2])  # print from the begining to place 2
print(pattern[-3])  # print only single  letter ,  3 places from the string end
print(pattern[-3:-1]) # print sub string from -3 to -1 (2 letters)
index1=pattern.index('be')
index2=pattern.index('you')


example  = 'Hello Wolrd,I feel good'
price = 'the price of the shirt is 250$'

partial_exmple= example[0:11]

from_begin_exmple= example[:5]
print (from_begin_exmple)

to_end_exmple1= example[5:]
print (to_end_exmple1)

single_letter= example[-5:]
print (single_letter)

index1= price.index("$")
index2= price.index("is")

price_final = price[index2+3:index1]
len_price = len(price_final)

print (price_final)
print ('$$$$$',example[-3:])

print ('test End')