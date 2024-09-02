#name=["kevin", "tom", "joy", [1 , 2, 3,4]]
#print(name[:::-1])
#n=5
#for i in range(n):
#for j in range(i,n):
#print("*", end=" ")
#print(" ")
num = 6
for i in range(6):
    print("*"*i)    
    if i == 5:        
        for j in reversed(range(num)):
            print("*"*j)
            num-=j
            

    # for j in range(i+1):
    #     print(" ", end=" ")
    # for j in range(i,n):
    #      print("*", end=" ")
    #     print(" ")



