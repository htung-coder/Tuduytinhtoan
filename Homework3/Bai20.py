n=int(input("Nhập số nguyên dương n: "))
while n<=0:
    n=int(input("Nhập lại số nguyên dương n: "))
else:
    s=0
    a=n
    while a>0:
        m=a%10
        if m in (2, 3, 5, 7):
            s+=1
        a//=10
print(f"{n} có {s} chữ số nguyên tố.")



