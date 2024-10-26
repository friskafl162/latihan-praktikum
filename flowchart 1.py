a = int( input("masukan bilangan A: "))
b = int( input("masukan bilangan B: "))
c = int( input("masukan bilangan C: "))

if a > b:
    if a > c:
        print("terbesar adalah A")
        terbesar = a 
    else:
        print("terbesar adalah C")
        terbesar = c 
else:
    if b > c: 
        print("terbesar adalah B")
        terbesar = b
    else:
        print("terbesar adalah C")
        terbesar = c

print(f"bilangan terbesar adalah: {terbesar}")
