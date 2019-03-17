n=int(input('enter the input'))
c=0
a1=list()
while n!=0:
    n1,a,b,k=raw_input().split(" ")

    n1=int(n1)

    a=int(a)

    b=int(b)

    k=int(k)

for i in range(1,n1):

    if(i%a==0):

        c+=1

    elif(i%b==0):

        c+=1

    if(i%a==0 and i%b==0):

        c-=1

    if(c==k):

        a1.append('Win')

    else:

        a1.append('Lose')

        n-=1

        c=0

for i in range(len(a1)):

    print a1[i]
