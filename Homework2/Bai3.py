a, b, c=map(int, input().split())
if a+b>c and a+c>b and b+c>a:
    cv=a+b+c
    p=cv/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    if a==b==c:
        print(f"Tam giac deu có dien tich la {s:.2f} va chu vi {cv:.2f}.")
    elif a==b or b==c or a==c:
        print(f"Tam giac can co dien tich la {s:.2f} va chu vi {cv:.2f}.")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print(f"Tam giac vuong co dien tich la {s:.2f} va chu vi {cv:.2f}.")
    else:
        print(f"Tam giac thuong co dien tich la {s:.2f} va chu vi {cv:.2f}.")
else:
    print("Khong la ba canh cua mot tam giac.")
    