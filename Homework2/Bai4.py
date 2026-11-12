a, b=map(float, input().split())
if a==0 and b!=0:
    print("Phương trình vô nghiệm.")
elif a==0 and b==0:
    print("Phương trình có vô số nghiệm.")
else:
    x=-b/a
    print(f"Nghiệm của phương trình là: {x:.2f}.")

