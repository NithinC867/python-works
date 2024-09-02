def last_dig_max(num1,num2):
    return num1 if num1%10>num2%10 else num2
print(last_dig_max(127,480))