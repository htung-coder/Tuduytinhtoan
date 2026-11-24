n=int(input("Nhập vào số nguyên dương n: "))
chan=0
le=0
while n<=0:
    n=int(input("Nhập lại số nguyên dương n: "))
else:
    a=n
    while a>0:
        m=a%10
        if m%2==0:
            chan+=1
        else:
            le+=1
        a//=10
print(f"{n} có {chan} chữ số chẵn, {le} chữ số lẻ.")
