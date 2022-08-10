import random
def NoGuess():
    print("Guess THe NO")
    z=5
    i=random.randint(0,100)
    if (i>=50):
        print("Clue:\n No is Greater Than Equals To 50")
    else:
        print("Clue:\n No is Less Than  50")
    k=int(input("Enter Your Choice:"))
    if(k!=i):
        print("Wrong No Score Reduced")
        z=z-1
        print(z,"/5")
        print("Hint:\n ")
        for j in range(1,25):
            if (i%j == 0):
                print("It Is A multiple Of ",j)
        k=int(input("Enter Your No:"))
        if(k!=i):
            print("Wrong No Score Reduced")
            z=z-1
            print(z,"/5")
            for q in range(1,50):
                if (i%q ==0):
                    print("It is Divisible by:",q)
            k=int(input("Enter The Guess No:"))
            if (k!=i):
                print("Wrong No Score Reduced")
                z=z-1
                print(z,"/5")
                flag = False
                if i > 1:
                    for m in range(2, i):
                        if (i % m) == 0:
                            flag = True
                            break
                if flag:
                    print("It is not a prime number")
                else:
                    print("It is a prime number")
                k=int(input("Enter Your Guess:"))
                if(k!=i):
                    print("Wrong No Score Reduced")
                    z=z-1
                    print(z,"/5")
                    for p in range(0,100):
                        if(p == i):
                            print("The Sqaure Of the No is:",p**2)
                    k=int(input("Enter Your Guess:"))
                    if(k!=i):
                        print("Wrong No Score Reduced")
                        z=z-1
                        print(z,"/5")
                        print("Loser Chal Nikal Saale Ek No Guess Nhi kr Paya")
                        print("The No Was:",i)
                    else:
                        print("Congrats")
                        print(z,"/5")
                else:
                    print("Congrats You Win")
                    print("Score = ",z)
            else:
                print("Congrats You Win")
                print("Score = ",z)
        else:
            print("Congrats You Win")
            print("Score = ",z)
    else:
        print("Congrats You Win")
        print("Score = ",z)
    print("Do u Wish To Continue Y or N \n")
    e=str(input("Y or N: "))
    if (e=='y'):
        NoGuess()
    else:
        print("See U Later:")
    
                        
                             
                        
                    
        
            
        
NoGuess()
    
        
    
