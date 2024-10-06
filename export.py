from Crypto.Cipher import AES
import pickle
# import xlrd
# import xlsxwriter

def loadData(): 
    # print(pickle)

    iv = b't\xd4\xbc\xee~\xa2\xc2\xc1\x14T\x91\xcfd\x95/\xfc'
    # key = "1234567890123456"
    key = b'1234567890123456'

    cipher = AES.new(key, AES.MODE_CFB, iv)
    file = "C:/Users/zhent/OneDrive/Desktop/RYB_Backup/build backend/RYB Student Backup - Flushing_Active_Database.rybdb"
    try:
        f = open(file, 'rb')
        print('opened')
    except:
        print('error')
    
    decrypted = cipher.decrypt(f.read())
    # print(decrypted)

    studentList = pickle.loads(decrypted)
    # print('student_list', studentList)

    #self.studentList = pickle.loads(cipher.decrypt(f.read()))

    #print(self.studentList)

    # self.setLast()

    with open('testdb.txt', 'wb') as handle:
        pickle.dump(studentList, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # f.write(bytearray(self.key))
    # f.close()

loadData()