str=input("Enter String: ")
str=str.lower()
while str!="":
    temp_str = ""
    count = 0
    for j in str:
        if str[0]==j:
            count+=1
        else:
            temp_str+=j
    print(str[0],":",count)
    str=temp_str


