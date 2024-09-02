num=[2,4,5,6,2,1]

sqares=[n**2 for n in num]
qube=[n**3 for n in num]

print(sqares)
print(qube)

oddnum=[n for n in num if n%2==0]
print(oddnum)