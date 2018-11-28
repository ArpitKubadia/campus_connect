inp=input("Enter String: ")
res=""
inp_2=""
for i in inp:
    if(i==" "):
        continue
    else:
        inp_2+=i;
for i in range(0,len(inp_2),2):
        res+=inp_2[i]
out=""
for i in res:
    out=i+out

print(out)


