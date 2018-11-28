inp=input("Enter string: ")
rev=""
for i in inp:
	rev=i+rev
print(rev)

if inp.lower() == rev.lower():
	print("String is Palindrome")
else:
	print("String is not a Palindrome")