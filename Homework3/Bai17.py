n=int(input("Nhập vào số nguyên dương n: "))
s=0
while n<=0:
    n=int(input("Nhập lại số nguyên dương n: "))
else:
    a=n
    while a>0:
        m=a%10
        s+=m
        a//=10
print(f"Tổng các chữ số của {n} là: {s}")
