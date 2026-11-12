s=int(input("Nhập thời gian: "))
h=s//3600
p=(s%3600)//60
m=s%60
print(f"{h}:{p}:{m}")
