import pickle

def whatsapp_find(name):
    found = 0
    num = 0
    f=open("E:\\JARVIS\\Jarvis UI 2\\whatsapp_records.dat",'rb')
    try:
        while True:
            data = pickle.load(f)
            c=data['name']
            n = c.split(' ')
            if name.lower() == n[0] or name.lower() == c:
                found = 1
                num = data['phone_number']              
                break
            else:
                num=0
    except:
        f.close()
    return num

