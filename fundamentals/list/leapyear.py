years=[1999,2000,2024,1998,2001,1900,1898]

for i in range(0,len(years)):
    if years[i]%100==0 and years[i]%400==0 or years[i]%100!=0 and years[i]%4==0:
        print(years[i]) 