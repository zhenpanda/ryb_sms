from dataHandler import *
from statistics import *

def get_average(l):
	total = 0
	for i in l:
		total += i

	return total / len(l)

#load database
k = keeper.Keeper('keeper.db')
d = StudentDB(file=k.files['cfilepath'], cfile=k.fname)

timeslotsodd = {'9:30': '09:30', '1:00': '01:00', '2:30': '02:30', '4:00': '04:00'}
timeslotsgood = ['09:30', '11:00', '01:00', '02:30', '04:00']

bydate = {}


for student in d.studentList.values():
	for att in student.datapoints['attinfo'][1]:
		if len(att[0]) < 10: continue
		dtformat = datetime.strptime(att[0], '%m/%d/%Y')
		cintime = att[2] if att[1] == '' else att[1]
		
		if cintime[:4] in timeslotsodd:
			cintime = timeslotsodd[cintime[:4]]
		elif cintime[:5] in timeslotsgood:
			cintime = cintime[:5]
		else:
			continue
		
		bydate.setdefault(dtformat, []).append([dtformat, cintime, student.datapoints['bCode']])


#year to year
yty = {}

for date in bydate:
	y = date.year
	if y in yty:
		yty[y] += len(bydate[date])
	else:
		yty[y] = len(bydate[date])


#by check in time
bycheckin = {}
for date, checkin in bydate.items():
	for entry in checkin:
		bycheckin.setdefault(entry[1], []).append(entry)

#age group of each check in
agegroup = {}
for date, checkin in bycheckin.items():
	for entry in checkin:
		age = d.studentList[entry[2]].datapoints['age']
		if age < 2 or age > 20: continue
		agegroup.setdefault(date, []).append(age)

for time, group in agegroup.items():
	print(time, mean(group), mode(group), pstdev(group))
	#group.sort()
	#print(group)


#filter
#year
yearfilter = {}
for date, checkin in bydate.items():
	for entry in checkin:
		yearfilter.setdefault(date.year, []).append(entry)

monthfilter = {}
for date, checkin in bydate.items():
	for entry in checkin:
		monthfilter.setdefault(date.month, []).append(entry)

def return_bd(filteredlist):
	bd = {}
	for date in filteredlist:
		bd.setdefault(date[0], []).append(date)

	return bd

def return_year(attendancelist, year):
	yfilter = {}
	for date, checkin in attendancelist.items():
		for entry in checkin:
			yfilter.setdefault(date.year, []).append(entry)
	
	y = yfilter[year]
	return return_bd(y)

def return_month(attendancelist, month):
	mfilter = {}
	for date, checkin in attendancelist.items():
		for entry in checkin:
			mfilter.setdefault(date.month, []).append(entry)

	m = mfilter[month]
	bd = {}
	return return_bd(m)

def return_year_month(attendancelist, year, month):
	return return_month(return_year(attendancelist, year), month)


def return_check_in(attendancelist, time):
	bycheckin = {}
	for date, checkin in attendancelist.items():
		for entry in checkin:
			bycheckin.setdefault(entry[1], []).append(entry)

	t = bycheckin[time]
	return return_bd(t)


def return_agegroup(attendancelist, age):
	agegroup = {}
	for date, checkin in attendancelist.items():
		for entry in checkin:
			student_age = d.studentList[entry[2]].datapoints['age']
			if student_age < 2 or student_age > 20: continue
			agegroup.setdefault(student_age, []).append(entry)

	return agegroup[age]


def return_attribute_group(attendancelist, attribute, value):
	attribute_group = {}
	for date, checkin in attendancelist.items():
		for entry in checkin:
			student_attrib = d.studentList[entry[2]].datapoints[attribute]
			attribute_group.setdefault(student_attrib, []).append(entry)

	return attribute_group[value]

def return_studentlist(attendancelist):
	studentlist = {}
	for date in attendancelist:
		studentlist.setdefault(date[2], []).append(date)

	return studentlist


def return_attribute(studentlist, attribute):
	return {s: d.studentList[s].datapoints[attribute] for s in studentlist}

#print(return_year_month(bydate, 2001, 1))
v2014_6 = return_year_month(bydate, 2014, 6)
v2014_6_11 = return_check_in(v2014_6, '11:00')
v2014_6_11_7 = return_studentlist(return_attribute_group(v2014_6_11, 'age', 7))



cAwarded_v2011_10_11_7 = return_attribute(v2014_6_11_7, 'gender')

v2014_6_11_7_mode = mode([v for v in cAwarded_v2011_10_11_7.values()])
print(v2014_6_11_7_mode)
cAwarded_v2011_10_11_7 = {k: v for k, v in cAwarded_v2011_10_11_7.items() if v == v2014_6_11_7_mode}

zip_cAwarded = return_attribute(cAwarded_v2011_10_11_7, 'cAwarded')



print(zip_cAwarded)