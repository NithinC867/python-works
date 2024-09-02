employee={"name":"hari","dept":"r and d","salary":50000,"combo offer":1000,"extra_working_day":3}

for k,v in employee.items():
    print(k,v)

if "extra_working_day" in employee:
    combo=employee.get("salary")+employee.get("combo offer")*employee.get("extra_working_day")
    print(combo)