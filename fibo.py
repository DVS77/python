n = int(input(" enter no of terms: "))
a1 = 0
a2 = 1
i = 0
while i<n:
    print(a1)
    s = a1 + a2
    a1 = a2
    a2 = s
    i+= 1
