n1=int(input("Enter The First Number : " ))
n2=int(input("Enter The Second NUmber : " ))
n3=input("Enter The Function(+ - * /) : " )

all_n1= id(n1)
print("Location of  n1" ,all_n1)

hex_n1= hex(n1)
print("Location of  n1" ,hex_n1)

all_n2= id(n2)
print("Location of  n1" ,all_n2)

hex_n2= hex(n2)
print("Location of  n1" ,hex_n2)

def add(n1,n2):
    ans=n1+n2
    print("Answer =",ans)
    all_ans= id(ans)
    print("Location of  Answer =" ,all_ans)

    hex_ans= hex(ans)
    print("Location of  Answer =" ,hex_ans)
    
def sub(n1,n2):
    if n1>n2:
        ans=n1-n2
        print("Answer =",ans)
        all_ans= id(ans)
        print("Location of  Answer =" ,all_ans)

        hex_ans= hex(ans)
        print("Location of  Answer =" ,hex_ans)
    elif n1<n2:
        ans=n2-n1
        print("Answer =",ans)
        all_ans= id(ans)
        print("Location of  Answer =" ,all_ans)

        hex_ans= hex(ans)
        print("Location of  Answer =" ,hex_ans)

def multi(n1,n2):
    ans=n1*n2
    print("Answer =",ans)
    all_ans= id(ans)
    print("Location of  Answer =" ,all_ans)

    hex_ans= hex(ans)
    print("Location of  Answer =" ,hex_ans)
   
def devide(n1,n2):
    ans=n1/n2
    print("Answer =",ans)
    all_ans= id(ans)
    print("Location of  Answer =" ,all_ans)

    hex_ans= hex(int(ans))
    print("Location of  Answer =" ,hex_ans)
    
if n3 == "+":
    add(n1,n2)
    
elif n3 == "-":
    sub(n1,n2)
    
elif n3 == "*":
    multi(n1,n2)

elif n3 == "/":
    devide(n1,n2)



        
    
    
    
    





