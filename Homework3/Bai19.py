A=int(input("Nhập vào số nguyên dương A: "))
a=1
b=1
while A<=0:
    A=int(input("Nhập lại số nguyên dương A: "))
else:
    while a+b<=A:
        c=a+b
        a=b
        b=c
print(f"Só trong dãy số fibonacci lớn nhất nhưng không vượt quá {A} là: {b}")
