def bubble(l):
    for i in range(len(l)-1):
        k=0
        for j in range(len(l)-1-i):
            if l[j]>l[j+1]:
                l[j], l[j+1]=l[j+1],l[j]
                k=1
        if k!=1:
            break

a=input("Enter numbers:").split()
a=list(map(int,a))
bubble(a)
print(a)