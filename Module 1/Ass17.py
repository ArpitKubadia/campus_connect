a = input("String 1: ")
b = input("String 2: ")
ans=""
for i in a:
    if i.isupper():
        ans+=i

for i in b:
    if i.isupper():
        ans+=i

print(ans)