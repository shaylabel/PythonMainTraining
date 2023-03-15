test_string = "GFG"
  
add_string = " is best"
  
print("The original string : " + str(test_string)) 
  
# printing original add string  
print("The add string : " + str(add_string)) 

final1="".join((test_string, add_string)) # join 
print("after add:",final1) 
before_join = ['a','b','c','d','e']  # join over list 
print (''.join(before_join))

txt = "abcdef"

x = txt.replace("b", "bctttttt")

print(x)
