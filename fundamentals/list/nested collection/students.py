students=[

    {"id":100,"name":"vipin","course":"django","mark":450},

    {"id":101,"name":"shibin","course":"django","mark":424},

    {"id":102,"name":"bibin","course":"django","mark":400},

    {"id":103,"name":"shyam","course":"django","mark":385},

    {"id":104,"name":"rahul","course":"django","mark":410},

    {"id":105,"name":"raj","course":"django","mark":399},

    {"id":106,"name":"sam","course":"django","mark":420},

]

def mark(top):
    return top.get("mark")
topstudent=max(students,key=mark)
print(topstudent)
