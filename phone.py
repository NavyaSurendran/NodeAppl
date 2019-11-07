import sys
import phonenumbers

num = sys.argv[1]
cont = sys.argv[2]

y = phonenumbers.parse(num,cont)
ans = phonenumbers.is_valid_number(y)

if(ans == True):
	print("Valid")
else:
	print("Invalid")