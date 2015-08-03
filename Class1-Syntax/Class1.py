#Class 1: Syntax

def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0:  return '0' 
  else:
	max=int(num**(1/2))
	maxi=max+1
	digits=[]
	for i in range(0,maxi)[::-1]:
	   number=int(num/(2**(max)))
	   digits.append(str(number))
	   num=num%(2**(max))
		
  return ''.join(digits)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  else:
	max=int(num**(1/base))
	maxi=max+1
	digits=[]
	for i in range(0,maxi)[::-1]:
	   number=int(num/(base**(max)))
	   digits.append(str(number))
	   num=num%(base**(max))
		
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0
  number = 0
  length = len(string) - 1
  for letters in string:
     num = int(letters)*base**(length)
	 length -= 1
	 number += num
	 
  return number 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result1 = base_to_int(str1, base1)
  result2 = base_to_int(str2, base2)
  result = result1 + result2
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result1 = base_to_int(str1, base1)
  result2 = base_to_int(str2, base2)
  result = result1*result2
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  digits = (len(str(num))-1)
  number = num/digits
  
  
  result = ""
  return result
