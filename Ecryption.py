#Encryption Algorithm - basic 
#Started 18/6/22
#Commented out code may have been used for debugging
#or general comments about abbreviations used

import time

def main():

    users = [
        ['TMazzag','StrongPassword'],
        ['Guest','S1mple'],
        ['Other','Rand0m']
        ]

    #print(len(users))
    #print(len(users[0]))

    valid = False
    attempts = 0

    #Checking user isnt using unlimited attempts
    while attempts <= 4:

        Username = input("Enter Username: ")
        Password = input("Enter Password: ")

        #Username Selected list idex
        uS = 1
        #Password Selected list idex, only used for debugging
        pS = 2

        for x in range(0,len(users)):
            if Username == users[x][0]:
                uS = x

        for x in range(0,len(users)):
            if Password == users[x][1]:
                pS = x

        #print(uS,pS)
        #print(Password)
        #print(users[uS][1])

        time.sleep(1)
        
        if Password == users[uS][1]:
            print('Welcome', users[uS][0],'!')
            attempts = 5
        else:
            attempts += 1
            if attempts == 5:
                print('Too many attempts')
                break
            elif attempts > 2:
                print('Username or Password incorrect try again')
                print('You have', (5 - attempts), 'attempts remaining')
                print('\n')
            else:
                print('Username or Password incorrect try again')
                print('\n')

        time.sleep(1)


    print("\nTime to encrypt password")

        
        


    
main()




