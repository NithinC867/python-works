#dict={key:value}
student={"name":"sreekumar","place":"palakkad","course":"full stack","age":23}



# student["name"]="hari"
# student["place"]="kollam"

# new=student.items()
# student.pop("place")  #remove the key:value from thr dictionary if its present

# print(new)
# for i in student:
#     if i == "place":
#         student[i]="fullstack"
# print(student)


# for i in student:
#     print(f"{i} = {student[i]}")

for i in student:
    if i == "place":
        student.pop(i)
print(student)