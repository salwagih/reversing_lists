def convert(n):
  
    
 # create empty list
 result =[]
    
 # loop on string 
 for num in str(n): 
        
       
   result.insert(0, int(num))
       
    # [] 
    # [1, 2, 3, 4, 5]
    
    
    
 return result
#  testing output
print(convert(564987654))
print(convert(529132))
