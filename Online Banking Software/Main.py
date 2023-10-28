import pickle
import time

#checks if the lengths of phone number, password, pin and account number are valid or not
def check_len(category,variable):
    if category=="password":
        l=8
        p="Your password is not of 8 characters. Please enter a password consisting of 8 characters: "
    elif category=="phone_number":
        l=10
        p="Enter a valid 10 digit phone number: "
    elif category=="pin":
        l=5
        p="Your pin is not of 5 digits. Please enter a valid 5 digit pin: "
    elif category=="acc_no":
        l=5
        p="Enter only the last 5 characters of your bank account number: "
    c=0
    if len(str((variable)))!=l:
        c=1
        while True:
            variable=int(input(p))
            if len(str(variable))==l:
                c=0
                break
    if category=="phone_number" or category=="acc_no":
        return c,variable
    else:
        return variable

#To open a new online bank account for the customer with unique username and password:-
def create_account_customer():       
    firstname=input("Enter your 1st name: ")
    lastname=input("Enter your last name: ")
    password=input("Create your password of 8 characters: ")
    password=check_len("password",password)
    pin=abs(int(input("Enter a 5 digit pin for account recovery and transactional actions: ")))
    pin=check_len("pin",pin)
    counter=1
    filehandle=open("UserID.dat",'rb+')
    try:
        while True:
            contents=pickle.load(filehandle)
            counter+=1
    except:
        pass
    username=firstname+'@'+str(counter)+lastname
    records={}
    records={"Sl. no.":counter,"Category":"Customer","Username":username,"Password":password,"PIN":pin}
    pickle.dump(records,filehandle)
    filehandle.close()
    print ("Your username:",username,',',"password:",password)
    print ("Congratulations, your account is created. Please exit and log in again to continue.")

    
#Checks if the user-entered password is correct:-
def check_password(username,password):
    filehandle=open("UserID.dat",'rb')
    check=3
    try:
        while True:
             contents=pickle.load(filehandle)
             if contents["Username"]==username and contents["Password"]!=password:
                 check=2
                 break
             if contents["Username"]!=username:
                 check=3
             if contents["Username"]==username and contents["Password"]==password:
                 check=1
                 break
    except:
        filehandle.close()
    return check

def check_pin(pin):
    filehandle=open("UserID.dat",'rb')
    check=3
    try:
        while True:
             contents=pickle.load(filehandle)
             if contents["PIN"]==pin:
                 check=1
                 break
             elif contents["PIN"]!=pin:
                 check=2
                 break
    except:
        filehandle.close()
    return check

#checks if unique phone number and account number are entered or not            
def check_uniqueness(category,variable,contents):
    if category=="acc_no":
        p="Enter another account number: "
        p1="account"
    else:
        p="Enter another phone number: "
        p1="phone"
    for j in contents:
        if category=="acc_no":
            i=j[5:10]
        else:
            i=j
        if str(variable)==str(i):
            while True:
                print("This",p1,"number is already in use.")
                variable=int(input(p))
                e=check_len(category,variable)
                if str(i)!=str(e[1]) and e[0]==0:
                    variable=e[1]
                    break
    return variable

        
#To enter initial account details of the customer:-
def enter_customer_account_details(username):
    print("Enter account details: ")
    phn,acc=[],[]
    filehandle3=open("Customer Account Details.dat",'rb')
    try:
        while True:
             contents=pickle.load(filehandle3)
             phn.append(contents["Phone Number"])
             acc.append(contents["Account No."])
    except:
        filehandle3.close()
    phone_number=abs(int(input("Enter the phone number linked with bank: ")))
    d=check_len("phone_number",phone_number)
    if d[0]==0:
        phone_number=check_uniqueness("phone_number",d[1],phn)
    acc_no=int(input("Enter last 5 digits of your bank account number: "))
    f=check_len("acc_no",acc_no)
    if f[0]==0:
        acc_no=check_uniqueness("acc_no",f[1],acc)
    final_acc_no="A0NBI"+str(acc_no)
    balance=abs(int(input("Enter your current balance for verification: Rs. ")))
    record={"Username":username,"Account No.":final_acc_no,"Current Balance":balance,"Phone Number":phone_number}
    filehandle=open("Customer Account Details.dat",'ab')
    pickle.dump(record,filehandle)
    filehandle.close()
    print ("Account details taken successfully.\nThe details of your account are: \n",record)

#Retrieves bank account details of the customer according to the username entered:-
def check_account_details(username):
    filehandle=open("Customer Account Details.dat",'rb')
    check=2
    details={}
    try:
        while True:
            contents=pickle.load(filehandle)
            if contents['Username']==username:
                details=contents.copy()
                print("Account Details:")
                trash=details.pop("Current Balance")
                print(details)
                check=1
    except:
        filehandle.close()
    return check

#To deposit or withdraw money from customer's bank account:-
def deposit_or_withdraw_or_loan(username,amount,task):
    filehandle=open("Customer Account Details.dat",'rb+')
    check_invalid=1
    try:
        while True:
            position=filehandle.tell()
            contents=pickle.load(filehandle)
            if contents['Username']==username:
                if task=="Withdrawal":
                    pin=int(input("Enter your 5 digit pin: "))
                    check=check_pin(pin)
                    if check==1:
                        amount=abs(int(input("Enter the amount of money you want to withdraw: Rs. ")))
                        if amount>contents["Current Balance"]:
                            print("Enough funds unavailable.")
                            check_invalid=0
                        else:
                            contents["Current Balance"]-=amount
                    else:
                        print("Invalid pin entered. Please try again.") 
                        check_invalid=0                      
                else:
                    contents["Current Balance"]+=amount
        
                if check_invalid!=0:
                    filehandle.seek(position)
                    pickle.dump(contents,filehandle)
                    updated_balance=contents["Current Balance"]
                    print ("Your updated balance is: Rs.",updated_balance)
    except:
        filehandle.close()
    if check_invalid!=0:
        filehandle2=open("Customer Transaction Details.dat",'ab+')
        records={"Username":username,"Transaction Type":task,"Amount":amount,"Current Balance":updated_balance}
        pickle.dump(records,filehandle2)
        filehandle2.close()

#Displays the transaction history of the required bank account:-
def view_transaction_history(username):
    filehandle=open("Customer Transaction Details.dat",'rb')
    check=1
    list=[]
    try:
        while True:
            contents=pickle.load(filehandle)
            if contents['Username']==username:  
                list.append(contents)
                check=2
    except:
        filehandle.close()
    pin=int(input("Enter your 5 digit pin: "))
    checkpin=check_pin(pin)
    if checkpin==1:
        print ("Transaction History:")
        for contents in list:
            print (contents)
    elif checkpin==2:
        print("Invalid pin entered. Please try again.") 
        check=3  
    return check   


#If the customer wants to change his/her password or to reset the password for account recovery:-
def change_or_reset_password(category, username):
    check=0
    if category=="change":
        pin=int(input("Enter your 5 digit pin: "))
        check=check_pin(pin)
    filehandle=open("UserID.dat",'rb+')
    try:
        while True:
             position=filehandle.tell()
             contents=pickle.load(filehandle)
             if contents['Username']==username:
                 if check==2:
                     print ("Invalid pin entered. Please try again.")
                 elif check==0 or check==1:
                    new_password=input("Enter new password: ")
                    new_password=check_len("password",new_password)
                    contents["Password"]=(new_password)
                    filehandle.seek(position)
                    pickle.dump(contents,filehandle)
                    print ("Password successfully changed. Please log in again to continue.")                
             else:
                 pass         
    except:
        filehandle.close()


#If the customer wishes to apply for a loan:-
def personal_car_home_education_loan(username,choice):
    filehandle=open("Customer Account Details.dat",'rb')
    if choice==1:
        minimum_balance=15000
        rate_of_interest=15
        type_of_loan="Personal Loan"
    elif choice==2:
        minimum_balance=75000
        rate_of_interest=8.25
        type_of_loan="Car Loan"        
    elif choice==3:
        minimum_balance=55000
        rate_of_interest=7.5
        type_of_loan="Home Loan"
    elif choice==4:
        minimum_balance=40000
        rate_of_interest=7.1
        type_of_loan="Educational Loan"
    check=0
    try:
        while True:
            contents=pickle.load(filehandle)
            if contents['Username']==username:
                if contents["Current Balance"]>=minimum_balance:
                    check=1
                else:
                    check=0
    except:
        filehandle.close()
    if check==1:
        amount=abs(int(input("Enter the amount of loan you need: Rs. ")))
        years=abs(int(input("Enter the number of years for which you need the loan (max. 5 years): ")))
        if years<=5 and years>0:
            print ("You will be charged an interest rate of",rate_of_interest,"% p.a. and a processing fee of 1.25%")
            total_amount=int(amount+((rate_of_interest*amount*years)/100)+(0.0125*amount))
            monthly_amount=int((total_amount/12)/years)
            print ("So, you will have to pay a total sum of Rs.",total_amount,"in monthly installments of Rs.",monthly_amount,"via cash or cheque.")
            choice=input("Do you agree to the terms and conditions? (y/n): ")
            if choice in ('y','Y'):
                print("The amount of Rs.",amount,"has been credited to your account.")
                deposit_or_withdraw_or_loan(username,amount,type_of_loan)
            else:
                print ("Loan application terminated.")
        else:
            print ("Invalid Input")
            print ("Loan application unsuccessful. Please retry")
    elif check==0:
        print ("You do not have the minimum account balance required for loan application")

#Loan options(personal,car,home or education):-
def loan(username):
    choice=int(input('''Enter 1 for personal loan,
Enter 2 for car loan,
Enter 3 for home loan,
Enter 4 for educational loan: '''))
    if choice not in (1,2,3,4):
        print ("Invalid Input. Try again.")
    else:
        personal_car_home_education_loan(username,choice)    
        
#Customer care details:-  
def customer_care():
    print ('''To contact us, write to us at customersupport@nbi.in or
contact us at 033 6571 8888/8889. Thank you.''')


print ("Welcome to National Bank of India's Online Banking System")
username=input("Enter your username: ")
password=input("Enter your password: ")
check=check_password(username,password)
if check==1:
    acc_details=check_account_details(username)
    if acc_details==2:
        print ("Account Details not found.")
        enter_customer_account_details(username)
    while True:
        choice=int(input('''Enter 1 for viewing your account details,
Enter 2 to to deposit money,
Enter 3 to withdraw money,
Enter 4 for viewing your transaction history and checking balance,
Enter 5 for loan,
Enter 6 for changing password,
Enter 7 to contact us at our customer care,
Enter 8 to log out: '''))
        if choice in (1,2,3,4,5,6,7,8):
            if choice==2:
                amount=abs(int(input("Enter the amount of money you want to deposit: Rs. ")))
                task="Deposit"
                deposit_or_withdraw_or_loan(username,amount,task)
            if choice==3:
                amount=0
                task="Withdrawal"
                deposit_or_withdraw_or_loan(username,amount,task)
            if choice==4:
                transaction_history=view_transaction_history(username)
                if transaction_history==1:
                    print ("No transaction details found")
            if choice==6:
                change_or_reset_password("change",username)
                break          
            if choice==1:
                acc_details=check_account_details(username)
                if acc_details==2:
                    print ("Account Details not found.")
            if choice==7:
                customer_care()
            if choice==5:
                loan(username)
            if choice==8:
                print ("Successfully Logged Out. Please do not share your username or password with anyone.")
                break
        else:
            print ("Invalid Input")
        time.sleep(2)
elif check==3:
    print ("Username does not exist.")
    choice=input("Do you want to create a new account? (y/n): ")
    if choice in ('y','Y'):
        create_account_customer()
elif check==2:
    print ("Invalid Password")
    choice=input("To reset your password press '1':")
    if choice=='1':
        for i in range (1,4):
            pin=int(input("Enter your 5 digit pin: "))
            checkpin=check_pin(pin)
            if checkpin==1:
                change_or_reset_password("reset",username)
                c=1
                break
            elif checkpin==2:
                print("Invalid pin entered.") 
                print (3-i,"attempt(s) left.")
            if i==3:
                print("Please contact our branch with valid documents to recover account.")
