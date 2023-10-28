import pickle

def whatsapp_insert_records():
    rec=1

    file = open("E:\\JARVIS\\Jarvis UI 2\\whatsapp_records.dat", 'ab')

    print ("Enter the details of the person: ")

    while True:
        print(f"Record #{rec}:")
        name = input("\tEnter name of the person: ")
        num = int(input("\tEnter the 10 digit phone number of the person: "))
        if len(str(num)) != 10:
            while True:    
                num = int(input("\tEnter a valid 10 digit phone number: "))
                if len(str(num)) == 10:
                    break
                else:
                    continue
        num = '+91' + str(num)
        print ("Name:", name, "and Phone number:", num)
        data = {'name': name.lower(), 'phone_number': num}
        pickle.dump(data, file)
        choice = input("Do you want to continue(y/n): ")
        rec += 1
        if choice not in ('y', 'Y'):
            break
    file.close()
    print ("Records successfully entered.")


