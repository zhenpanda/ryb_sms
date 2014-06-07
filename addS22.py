from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):
	'''addS22'''

	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (1, 1))
	w.newFrame("Third Frame", (3, 1))
	w.newFrame("Fourth Frame", (2, 0))

	w.frames["Fourth Frame"].grid(sticky=W)


#basic info widgets
	w.frames["First Frame"].addWidget(firstName, (0, 0))
	w.frames["First Frame"].addWidget(lastName, (1, 0))
	w.frames["First Frame"].addWidget(chineseName, (2, 0))
	w.frames["First Frame"].addWidget(parentName, (3, 0))
	w.frames["First Frame"].addWidget(pup, (4, 0))

	w.frames["First Frame"].addWidget(sepr, (5, 0))

	w.frames["First Frame"].addWidget(bCode, (6, 0))
	w.frames["First Frame"].addWidget(sid, (7, 0))

	w.frames["First Frame"].addWidget(dob, (10, 0))
	w.frames["First Frame"].addWidget(age, (11, 0))

	w.frames["First Frame"].addWidget(sepr, (12, 0))

	w.frames["First Frame"].addWidget(notes, (14, 0))

	notes.config(height=5, width=10)

	w.frames["First Frame"].addWidget(sepr, (15, 0))

#award class widgets
	w.frames["First Frame"].addWidget(sType, (16, 0))
	w.frames["First Frame"].addWidget(cAwarded, (17, 0))
	w.frames["First Frame"].addWidget(cRemaining, (17, 0))
	w.frames["First Frame"].widgets['cRemaining'].hide()
	w.frames["First Frame"].addWidget(tpd, (16, 2))
	w.frames["First Frame"].addWidget(tpa, (17, 2))
	w.frames["First Frame"].addWidget(tpo, (18, 2))


	baclass = Buttonbox(text='awardclass', lang=w.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')

	w.frames["Fourth Frame"].addWidget(bgold, (0, 0))
	w.frames["Fourth Frame"].addWidget(bbasic, (1, 0))
	#w.frames["Fourth Frame"].addWidget(baclass, (0, 0))
	w.frames["Fourth Frame"].addWidget(baoclass, (2, 0))
	#w.frames["Fourth Frame"].addWidget(baac, (2, 0))

	baclass.config(cmd=lambda: cpicker(w.lang))
	baoclass.config(cmd=caddone)
	bgold.config(cmd=lambda: caddx(60))
	bbasic.config(cmd=lambda: caddx(15))
	#baac.config(cmd=cadd)

#address widgets
	w.frames["First Frame"].addWidget(addr, (0, 2))
	w.frames["First Frame"].addWidget(city, (1, 2))
	w.frames["First Frame"].addWidget(state, (2, 2))
	w.frames["First Frame"].addWidget(zip, (3, 2))
	w.frames["First Frame"].addWidget(email, (4, 2))


	w.frames["First Frame"].addWidget(hPhone, (6, 2))
	w.frames["First Frame"].addWidget(cPhone, (7, 2))
	w.frames["First Frame"].addWidget(cPhone2, (8, 2))


	w.frames["Second Frame"].addWidget(portr, (0, 0))

#collect student information
#and save it into database
	def collect():
		
		ns = StudentInfo()
		ns.datapoints = dict(list(ns.datapoints.items()) + list(w.collect(ns.datapoints).items()))
		#print(ns.datapoints)

		nsbcode = ns.datapoints['bCode']

		if d.checkCode(nsbcode):
			if not ase(d.studentList[nsbcode].datapoints['firstName'], w.lang):
				return
		else:
			if not con(ns.datapoints['firstName'], w.lang):
				return

		ns.datapoints['attinfo'] = [['Date', 'Check-In Time', 'Class Time'], []]
		d.addStudent(ns.datapoints['bCode'], ns)
		d.saveData()

		sa(ns.datapoints['firstName'], w.lang)

		#print(w.collect(StudentInfo().datapoints))

		#add this to top of every frame containing picture
		portr.setData('monet_sm.jpg')

#save and add button widgets
	sadd = Buttonbox(text='addstudent', lang=language, repr='sadd')
	w.frames["Third Frame"].addWidget(sadd, (0, 0))
	sadd.config(cmd=collect)

	w.frames["Second Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

if __name__ == '__main__':
	t = Tk()
	main(t, language)
	t.mainloop()
