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
	w.newFrame("L Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (1, 1))
	w.newFrame("Third Frame", (3, 0))
	w.newFrame("Fourth Frame", (2, 0))
	w.newFrame("Fifth Frame", (0, 2))

	w.frames["Fourth Frame"].grid(sticky=W)
	w.frames["Third Frame"].grid(columnspan=3)

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
	w.frames["First Frame"].addWidget(cRemaining, (18, 0))
	w.frames["First Frame"].addWidget(tpd, (16, 2))
	w.frames["First Frame"].addWidget(tpa, (17, 2))
	w.frames["First Frame"].addWidget(tpo, (18, 2))


	baoclass = Buttonbox(text='awardoneclass', lang=w.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w.lang, repr='baaclasses')

	w.frames["Fourth Frame"].addWidget(baoclass, (1, 0))
	w.frames["Fourth Frame"].addWidget(baac, (2, 0))

	baoclass.config(cmd=caddone)
	baac.config(cmd=lambda: cadd(w.lang))

	#
	w.frames["First Frame"].addWidget(addr, (0, 2))
	w.frames["First Frame"].addWidget(city, (1, 2))
	w.frames["First Frame"].addWidget(state, (2, 2))
	w.frames["First Frame"].addWidget(zip, (3, 2))
	w.frames["First Frame"].addWidget(email, (4, 2))


	w.frames["First Frame"].addWidget(hPhone, (6, 2))
	w.frames["First Frame"].addWidget(cPhone, (7, 2))
	w.frames["First Frame"].addWidget(cPhone2, (8, 2))


	w.frames["Second Frame"].addWidget(portr, (0, 0))

	w.attinfo = attinfo
	#w.attinfo.deleteAll()
	w.frames["Fifth Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Fifth Frame"].grid(rowspan=100, sticky=W)

	w.attinfo.editwidget=True
	w.attinfo.canvas.config(width=500, height=500)

	#reset portrait
	portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w.populate(s.datapoints)

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def collect():
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return
		s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()


	sstudent = Buttonbox(text='savestudent', lang=w.lang, repr='sstudent')
	w.frames["Third Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)

	bclose = Buttonbox(text='close', lang=w.lang, repr='bclose')
	w.frames["Third Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=t.destroy)

	w.frames["Second Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()



	



if __name__ == '__main__':
	main(languages['chinese'], i='FLU-000-001')
	

