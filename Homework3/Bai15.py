n=int(input("Nhập vào số nguyên dương n: "))
s=0
a=n
while n<=0:
    n=int(input("Nhập lại số nguyên dương n: "))
else:
    while a>0:
        a//=10
        s+=1
print(f"{n} có {s} chữ số.")

      
      