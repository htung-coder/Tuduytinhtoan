c=input("Nhập 1 chữ cái in hoa:")
if c=='A':
    print('z')
else:
    ct=c.lower()
    print(chr(ord(ct)-1))
    