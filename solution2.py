def convert(n):
  return[int(num) for num in str(n)[::-1]]
 
  
 
print(convert(56789))
print(convert(1234))
 
