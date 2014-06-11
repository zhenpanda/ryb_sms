from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(lang, d, top=False, i=0):

	d.loadData()

	t = Window(top=top)
	t.attributes('-fullscreen', False)
	t.geometry('1900x900')
	#t.resizable(0, 0)
	t.grab_set()
	t.focus_set()

	w = AppWindow(t.mainFrame)

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
	w.newFrame("Tenth Frame", (0, 1))
	w.newFrame("Eleventh Frame", (1, 3))

	w.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Seventh Frame"].grid(rowspan=2)
	w.frames["Ninth Frame"].grid(rowspan=2, sticky=E)
	w.frames["Tenth Frame"].grid(columnspan=5)
	w.frames["Eleventh Frame"].grid(sticky=N)
	w.frames["Eigth Frame"].grid(sticky=N)
	w.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=520)
	#w.frames["First Frame"].grid(columnspan=5)
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
#payment widgets
	w.frames["Fourth Frame"].addWidget(tpd, (6, 0))
	w.frames["Fourth Frame"].addWidget(tpa, (7, 0))
	w.frames["Fourth Frame"].addWidget(tpo, (8, 0))

#class widget
	w.frames["Sixth Frame"].addWidget(sType, (4, 0))
	w.frames["Sixth Frame"].addWidget(cAwarded, (5, 0))
	w.frames["Sixth Frame"].addWidget(cRemaining, (6, 0))
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
	bgold.config(cmd=lambda: caddmorex(60), width=12)
	bbasic.config(cmd=lambda: caddmorex(15), width=12)

	baoclass.selfframe.grid(padx=2)
	bgold.selfframe.grid(padx=2)
	bbasic.selfframe.grid(padx=2)
	
	
	#w.frames["Sixth Frame"].addWidget(baclass, (0, 0))
	#w.frames["Sixth Frame"].addWidget(baac, (2, 0))
	#baclass.config(cmd=lambda: cpicker(w.lang))
	#baac.config(cmd=cadd)






	w.frames["Seventh Frame"].addWidget(portr, (0, 0))

	w.attinfo = attinfo
	#w.attinfo.deleteAll()
	w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Eleventh Frame"].grid(rowspan=100, sticky=W)

	w.attinfo.editwidget=True
	w.attinfo.canvas.config(width=500, height=500)

	#reset portrait
	portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w.populate(s.datapoints)

	tdp = dict(w.collect(s.datapoints))

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def collect():
		if not changed():
			t.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return

		cbcode = dict(w.collect(s.datapoints))['bCode']
		if s.datapoints['bCode'] != cbcode:
			if not ase(d.studentList[cbcode].datapoints['firstName'], w.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				d.studentList[cbcode] = s
				del d.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()


	def changed():
		ctdp = dict(w.collect(s.datapoints))
		#print(ctdp)
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False


	def quit():
		if not changed():
			t.destroy()
		elif ret('a', w.lang):
			t.destroy()


	sstudent = Buttonbox(text='savestudent', lang=w.lang, repr='sstudent')
	w.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)

	bclose = Buttonbox(text='close', lang=w.lang, repr='bclose')
	w.frames["Fifth Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	w.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()



	



if __name__ == '__main__':
	main(languages['chinese'], i='FLU-000-001')
	

