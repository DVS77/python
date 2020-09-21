n = int(input(" enter no of terms: "))
a1 = 0
a2 = 1
i = 0
if n<=0:
    print("enter a natural number:")
elif n==1:
    print("fibonacci series:", a2)
else:
    while i<n:
        print(a1)
        s = a1 + a2
        a1 = a2
        a2 = s
        i+= 1
