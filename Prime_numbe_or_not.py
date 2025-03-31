n1=int(input("Enter any number : "))
if n1>1:
    for i in range(2,int(n1/2)+1):
        if (n1%i)==0:
            print(f"{i}, its not a prime number")
            break
    else:
        print(f"{i}, its a prime number")
else:
    print("Its not a prime number")