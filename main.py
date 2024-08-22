#For generating an A.P
def generate_ap(ap):
    if (n1==0):
        for i in range(10):
            if (i==0):
                ap.append(a1)
            else:
                ap.append(ap[i-1]+d1)         
        
        print(str(ap)+"..........")


    else:
        for i in range(n1):
            if (i==0):
                ap.append(a1)
            else:
                ap.append(ap[i-1]+d1)
        
        print(ap1)








print("Welcome to program for Arthimatuc Progressions !!\n")

main_inp = int(input("Enter 1 for generating an A.P or \nEnter 2 for getting values of an AP by giving an A.P in input\nEnter 3 for generating sum of an A.P (by giving A.P directly) or\nEnter 4 for generating sum of an A.P (by giving formula values)\n : "))

if (main_inp==1):
    a1 = int(input("Enter the firt term of the A.P : "))
    d1 = int(input("Enter the common difference of the A.P : "))
    n1 = int(input("Enter the number of terms of the A.P (press 0 for infinte A.P) : "))

    ap1 = []

    generate_ap(ap1)

    
