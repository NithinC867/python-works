last_digit_max=lambda n1,n2:n1 if n1%10>n2%10 else n2
print(last_digit_max(127,872))

#odd or even

odd_or_even=lambda n1:"even" if n1%2==0 else "odd"
print(odd_or_even(3))