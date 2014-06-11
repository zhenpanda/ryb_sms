from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):
	'''addS22'''

	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	w.newFrame("First Frame", (1, 1))
	w.newFrame("Second Frame", (1, 2))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (2, 2))
	w.newFrame("Fifth Frame", (5, 0))
	w.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w.newFrame("Eigth Frame", (3, 2))
	w.newFrame("Ninth Frame", (3, 1))

	w.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Seventh Frame"].grid(rowspan=2)
	w.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	#w.frames["Sixth Frame"].grid(rowspan=2, sticky=N)

#student info widgets
	w.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.grid(columnspan=2, sticky=E+W)
	w.frames["First Frame"].addWidget(firstName, (1, 0))
	w.frames["First Frame"].addWidget(lastName, (2, 0))
	w.frames["First Frame"].addWidget(chineseName, (3, 0))
	w.frames["First Frame"].addWidget(dob, (4, 0))
	w.frames["First Frame"].addWidget(age, (5, 0))
	w.frames["First Frame"].addWidget(parentName, (6, 0))

#address widgets
	w.frames["Second Frame"].addWidget(ainfo, (0, 0))
	ainfo.label.grid(columnspan=2, sticky=E+W)
	w.frames["Second Frame"].addWidget(addr, (3, 0))
	w.frames["Second Frame"].addWidget(city, (4, 0))
	w.frames["Second Frame"].addWidget(state, (5, 0))
	w.frames["Second Frame"].addWidget(zip, (6, 0))
	w.frames["Second Frame"].addWidget(email, (7, 0))

#contact widgets
	w.frames["Third Frame"].addWidget(cinfo, (0, 0))
	cinfo.label.grid(columnspan=2, sticky=E+W)
	w.frames["Third Frame"].addWidget(pup, (1, 0))
	w.frames["Third Frame"].addWidget(hPhone, (2, 0))
	w.frames["Third Frame"].addWidget(cPhone, (3, 0))
	w.frames["Third Frame"].addWidget(cPhone2, (4, 0))

#database info widgets
	w.frames["Fourth Frame"].addWidget(pinfo, (0, 0))
	pinfo.label.grid(columnspan=2, sticky=E+W)
	w.frames["Fourth Frame"].addWidget(bCode, (1, 0))
	w.frames["Fourth Frame"].addWidget(sid, (2, 0))

	bCode.setData(d.formatCode())
#payment widgets
	w.frames["Fourth Frame"].addWidget(tpd, (6, 0))
	w.frames["Fourth Frame"].addWidget(tpa, (7, 0))
	w.frames["Fourth Frame"].addWidget(tpo, (8, 0))

#class widget
	w.frames["Sixth Frame"].addWidget(sType, (4, 0))
	w.frames["Sixth Frame"].addWidget(cAwarded, (5, 0))
	w.frames["Sixth Frame"].addWidget(cRemaining, (6, 0))
	w.frames["Sixth Frame"].widgets['cRemaining'].hide()
	w.frames["Sixth Frame"].addWidget(ctime, (7, 0))

#notes widget
	Label(w.frames["Ninth Frame"], text='Notes').grid(row=0, columnspan=2, sticky=E+W)
	w.frames["Ninth Frame"].addWidget(notes, (1, 0))
	notes.label.grid_forget()
	notes.config(height=10, width=32)





	baclass = Buttonbox(text='awardclass', lang=w.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')

	w.frames["Eigth Frame"].addWidget(bgold, (1, 0))
	w.frames["Eigth Frame"].addWidget(bbasic, (1, 1))
	w.frames["Eigth Frame"].addWidget(baoclass, (1, 2))

	baoclass.config(cmd=caddone, width=12)
	bgold.config(cmd=lambda: caddx(60), width=12)
	bbasic.config(cmd=lambda: caddx(15), width=12)

	baoclass.selfframe.grid(padx=2)
	bgold.selfframe.grid(padx=2)
	bbasic.selfframe.grid(padx=2)
	
	
	#w.frames["Sixth Frame"].addWidget(baclass, (0, 0))
	#w.frames["Sixth Frame"].addWidget(baac, (2, 0))
	#baclass.config(cmd=lambda: cpicker(w.lang))
	#baac.config(cmd=cadd)






	w.frames["Seventh Frame"].addWidget(portr, (0, 0))

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
	w.frames["Fifth Frame"].addWidget(sadd, (0, 0))
	sadd.button.config(height=5, font=('Verdana', '12'))
	sadd.config(cmd=collect)

	w.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker, width=12)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

if __name__ == '__main__':
	t = Tk()
	main(t, language)
	t.mainloop()
