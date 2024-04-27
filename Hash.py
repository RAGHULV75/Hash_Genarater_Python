a = 1;
while a==1 :
    print('''\n\t\t\t Welcome to Hashing
         •Here we can able to hash the user values and validate
         •Here the data's will be store for the validation purpose .. ''')
    print('''
        •Press 1 to Get the hash value
        •Press 2 to validate the value with an already stored value
        •Press 3 to Exit

                ''')
    op=int(input("\n\t Select Your Operation : "))
    if(op==1):
        v=input("Enter The value : ")
        hs=str(hash(v))
        print("The string hash value is : " + str(hash(v)))
        with open("hash.txt","a") as file:
            file.write(hs)
            file.write(",")
        file.close()
    elif(op==3):
        exit

    elif(op==2):
        print("verify the value with hash value ")
        v=input("Enter the value : ")
        hsv=str(hash(v))
        with open(r'hash.txt', 'r') as file:
            content = file.read()
            if hsv in content:
                print('string exist')
            else:
                print('string does not exist')
                
