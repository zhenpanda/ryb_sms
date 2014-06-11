from datetime import datetime, time, timedelta
import keeper
import pickle
import xlrd

#log all changes






#colorCode = {5: {time(10, 59): "#ff00ff",
#                 time(12, 29): "#9900ff",
#                 time(14, 29): "#073763",
#                 time(15, 59): "#0000ff",
#                 time(17, 29): "#4a86e8",
#                 time(23, 59): "#000000"},
#             
#             6: {time(10, 59): "#ff0000",
#                 time(12, 29): "#980000",
#                 time(14, 29): "#783f04",
#                 time(15, 59): "#274e13",
#                 time(17, 29): "#6aa84f",
#                 time(23, 59): "#000000"},
#
#             0: {time(23, 59): "#000000"},
#             1: {time(23, 59): "#000000"},
#             2: {time(23, 59): "#000000"},
#             3: {time(23, 59): "#000000"},
#             4: {time(23, 59): "#000000"}}
#
#sortedColorCode = {key: [t for t in value] for (key, value) in colorCode.items()}
#for v in sortedColorCode.values(): v.sort()




class StudentInfo:

    '''

    Class info: Handles information of students.

    student_attr:
        DICTIONARY of student attributes.
        Correlates to "fields".

    attendance:
        LIST of attendance dates and times.

    add_attendance():
        Appends to "attendance" as a 2D array,
        current date and time.

    '''

    def __init__(self):
        self.datapoints = {
            "lastName": '',
            "firstName": '',
            "chineseName": '',
            "schoolLoc": '',
            "bCode": '',
            "sid": 0,
            "dob": '1/1/1900',
            "age": 0,
            "gender": '',
            "parentName": '',
            "hPhone": 0,
            "cPhone": 0,
            "cPhone2": 0,
            "pup": '',
            "addr": '',
            "state": '',
            "city": '',
            "zip": 0,
            "wkdwknd": '',
            "tpd": '1/1/1900',
            "tpa": 0,
            "tpo": 0,
            "email": '',
            "sType": '',
            "cAwarded": 0,
            "cRemaining": 0,
            "findSchool": '',
            "notes": '',
            "attinfo": [['Date', 'Check-In Time', 'Class Time'], []],
            "portr": '',
            "ctime": ''
            }

        self.dpalias = {
            "Last Name": "lastName",
            "First Name": "firstName",
            "Chinese Name": "chineseName",
            "School Location": "schoolLoc",
            "Barcode": "bCode",
            "Student Number": "sid",
            "Date of Birth": "dob",
            "Age": "age",
            "Gender": "gender",
            "Parent Name": "parentName",
            "Home Phone": "hPhone",
            "Cell Phone": "cPhone",
            "Cell Phone 2": "cPhone2",
            "Pick Up Person": "pup",
            "Address": "addr",
            "State": "state",
            "City": "city",
            "Zip": "zip",
            "Weekday/Weekend": "wkdwknd",
            "Payment Date": "tpd",
            "Payment Method": "Payment Method: ",
            "Payment Amount": "tpa",
            "Payment Owed": "tpo",
            "Email": "email",
            "Service Type": "sType",
            "Classes Awarded": "cAwarded",
            "Classes Remaining": "cRemaining",
            "How did you hear about the school?": "findSchool",
            "Notes": "notes"
        }


class StudentDB:

    '''

    Class info: Handles student database.

    studentList:
        DICTIONARY item of students.
        Key = barcode
        Value = StudentInfo

    scan_student:
        Scans the students by calling the
        "add_attendance()" function of StudentInfo.

    add_student:
        Adds a new student to the "studentList".

        ##needs fix, should ask for confirmation in UI
        If the barcode already exists, it will
        overwrite the existing student.

    pickle_list:
        Pickles "studentList" for storage into a file.

    unpickle_list:
        Unpickles filename and stores it in "studentList".

    export:
        Exports the list into an Excel(xls) file.

    import:
        ##not implemented yet
        Imports an Excel (xls) file.

    '''

    def __init__(self, **kwargs):
        self.file = kwargs['file']
        self.cfile = kwargs['cfile']
        
        try:
            self.loadData()
        except:
            self.studentList = {}
            self.saveData()
            print(self.file + " file not found, new file was created")
   

        #
        self.fcell = {1: lambda y: str(y), 2: lambda y: int(y), 3: lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%y")}
        self.setLast()

       

        #try:
        #self.loadData()
        #    print("database loaded")
        #except:
        #    self.saveData()
        #    print("database could not be loaded, new database created")
        
    
    def setLast(self):
        try:
            t = sorted(self.studentList.keys())[-1]
            self.pre = t[:3]
            self.last = int(t[4:7] + t[8:]) + 1
            #print(self.pre, self.last)
        except:
            self.pre = 'UNK'
            self.last = 0
            pass  


    def formatCode(self):
        t = str(self.last)
        while len(t) < 6:
            t = '0' + t
        t = self.pre + '-' + t[:3] + '-' + t[3:]

        return t


    def checkDate(self, barcode):
        checkedInToday = 0

        today = '{:%m/%d/%Y}'.format(datetime.now())
        attinfo = self.studentList[barcode].datapoints['attinfo'][1]

        for att in attinfo:
            print(att[0])
            if att[0] == today: checkedInToday += 1

        if checkedInToday > 0: return checkedInToday
        return True


    def findTimeSlot(self, time):
        h, m, p = '{:%I}'.format(time), '{:%M}'.format(time), '{:%p}'.format(time)
        m = int(m)

        if m > 40:
            m = '00'
            h = str(int(h) + 1)
        elif m > 10:
            m = '30'
        else:
            m = '00'

        return h + ':' + m + ' ' + p


    def scanStudent(self, barcode, xtra=False):
        #try:
        cdt = datetime.now()

        timeslot = self.findTimeSlot(cdt)
        time = '{:%I:%M %p}'.format(cdt)
        date = '{:%m/%d/%Y}'.format(cdt)

        data = [date, time, timeslot]
        if xtra: data.append(xtra)

        s = self.studentList[barcode].datapoints
        s['attinfo'][1].append(data)
        s['cRemaining'] -= 1
        if s['cRemaining'] < 0: s['cRemaining'] = 0
        #except:
            #return print("Student doesn't exist")


    def checkCode(self, barcode):
        return barcode in self.studentList

    def addStudent(self, barcode, student):
        self.studentList[barcode] = student
        self.last += 1

    #def edit_student(self, barcode, student_attr):
        #self.studentList[barcode].student_attr = student_attr


    def saveData(self):
        pickle.dump(self.studentList, open(self.file, "wb"))


    def loadData(self):
        self.studentList = pickle.load(open(self.file, "rb"))
        self.setLast()


    def format(self, ctype, value):
        try:
            return self.fcell[ctype](value)
        except:
            return
            if ctype == 0: print("cell is empty, not added to database")
            else: print("cell could not be formatted")


    def exportxlsx(self, filename):
        #to excel file
        return


    def importxlsx(self, filename):        

        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)

        repr, headers = {}, [cell.value for cell in worksheet.row(0)]
        for h in headers:
            repr[headers.index(h)] = StudentInfo().dpalias[h]


        sraw = [worksheet.row(rx) for rx in range(1, worksheet.nrows)]
        sinfo = [[self.format(cell.ctype, cell.value) for cell in row] for row in sraw]

        for info in sinfo:
            newS = StudentInfo()
            for dp in info:
                newS.datapoints[repr[info.index(dp)]] = dp
            newS.datapoints['attinfo'][0] = ['Date', 'Time', 'Check-In Time']
            if newS.datapoints['bCode'][:3] != 'FLU': continue
            self.addStudent(newS.datapoints['bCode'], newS)


        #print(repr, headers, sinfo)

        self.saveData()

        return


    def importtimexlsx(self, filename):

        workbook = xlrd.open_workbook(filename)
        worksheet = workbook.sheet_by_index(0)

        repr, headers = {}, [cell.value for cell in worksheet.row(0)][:4]
        for h in headers:
            repr[headers.index(h)] = StudentInfo().dpalias[h]


        sraw = [worksheet.row(rx) for rx in range(1, worksheet.nrows)]
        sinfo = [[self.format(cell.ctype, cell.value) for cell in row] for row in sraw]

        ns, nt = 0, 0

        for info in sinfo:
    
            bCode = info[0]
            try:
                cAward = info[3]
            except:
                cAward = 0
            tdata = info[4:]

            if bCode not in self.studentList: continue

            ftdata = []
            for td in tdata:
                try:
                    dt = td.split(' ')
                    date = dt[0]
                    time = dt[1]
                except:
                    continue

                ftdata.append([date, '', time])

            #print(bCode, ftdata)
            dp = self.studentList[bCode].datapoints
            
            dp['cAwarded'] = cAward
            try:
                dp['cRemaining'] = int(cAward) - len(ftdata) if int(cAward) > len(ftdata) else 0
            except:
                dp['cRemaining'] = 0
            dp['attinfo'] = []
            dp['attinfo'].append(['Date', 'Check-In Time', 'Class Time'])
            dp['attinfo'].append(ftdata)

            ns += 1
            nt += len(ftdata)

            #print(self.studentList[bCode].datapoints['attinfo'])
            #for data in ftdata:
                


            #for dp in info:
             #   newS.datapoints[repr[info.index(dp)]] = dp
           #self.addStudent(newS.datapoints['bCode'], newS)


        #print(repr, headers, sinfo)

        self.saveData()

        return ns, nt



    #def modData(self):
    #    self.loadData()
    #    self.saveData()
    #    self.loadData()
        



#Pull settings.
#settings = Settings()

#file is unused
#file = settings.config["dbFile"]

#rybDB = StudentDB()


#s = StudentInfo()
#s.datapoints['barcode'] = '1234'

#print(s.config['dbFile'])

#k = keeper.Keeper('keeper.db')
#k.files['cfilepath'] = 't2.db'

#d = StudentDB(file=k.files['cfilepath'], cfile=k.fname)
#d.loadData()
#d.addStudent(s.datapoints['barcode'], s)
#d.scanStudent('1234')
#d.scanStudent('1234')

#print(d.checkDate('1234'))
#print(d.studentList['1234'].datapoints['attinfo'])
#print(['05/20/2014', '02:21', '02:30'][0])

#d.importxlsx('sdt1.xls')
#d.importtimexlsx('at.xls')

#d.importxlsx('sdt.xls')

#date = datetime.strptime('1/1/1900', "%m/%d/%Y")
#edate = date + timedelta(days=38779-2)

#print(edate)

#print(d.studentList['FLU-000-002'].datapoints)
#x = {'1': lambda y: str(y), '2': lambda y: int(y), '3': lambda y: (datetime.strptime('1/1/1900', "%m/%d/%Y") + timedelta(days=y-2)).strftime("%m/%d/%y")}

#print(x['3'](41653.0))
#print(datetime.strftime)
#print(d.studentList['FLU-000-006'].datapoints['firstName'])