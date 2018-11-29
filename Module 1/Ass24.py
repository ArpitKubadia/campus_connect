student={"John":86.5,"Jack":91.2,"Jill":84.5,"Harry":72.1,"Joe":80.5}
print(student)
print(sorted(student, key=student.get, reverse=True)[:2])
avg=0
for key in student.keys():
    avg+=student[key]

avg=avg/len(student)
print(avg)