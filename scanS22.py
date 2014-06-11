from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

	d.loadData()

	w = AppWindow(t)

	w.bind("<Destroy>", lambda event: t2.destroy)

	w.lang = lang

#attendance table
	w.attinfo = Table(repr='attinfo', edit=True)
	w.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
	w.attinfo.build(headers=w.attinfoh, data=[[]])
	w.attinfo.clast = '#FF99FF'

#frame initialization
	w.newFrame("First Frame", (1, 1))
	w.newFrame("Second Frame", (1, 2))
	w.newFrame("Third Frame", (2, 1))
	w.newFrame("Fourth Frame", (2, 2))
	w.newFrame("Fifth Frame", (5, 0))
	w.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w.newFrame("Eigth Frame", (3, 1))
	w.newFrame("Ninth Frame", (3, 2))
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


#add widget to search for students
	w.frames["Tenth Frame"].addWidget(sby, (0, 0))

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
#payment widgets
	w.frames["Fourth Frame"].addWidget(tpd, (3, 0))
	w.frames["Fourth Frame"].addWidget(tpa, (4, 0))
	w.frames["Fourth Frame"].addWidget(tpo, (5, 0))

#class widget
	w.frames["Fourth Frame"].addWidget(sType, (6, 0))
	w.frames["Fourth Frame"].addWidget(cAwarded, (7, 0))
	w.frames["Fourth Frame"].addWidget(cRemaining, (8, 0))
	w.frames["Fourth Frame"].addWidget(ctime, (9, 0))

#notes widget
	Label(w.frames["Ninth Frame"], text='Notes').grid(row=0, columnspan=2, sticky=E+W)
	w.frames["Ninth Frame"].addWidget(notes, (1, 0))
	notes.label.grid_forget()
	notes.config(height=10, width=32)

#special
	spec = Labelbox(text='spec', lang=w.lang, repr='spec')
	w.frames["Eigth Frame"].addWidget(spec, (1, 0))
	spec.label.config(font=('Verdana', 15), wraplength=200, justify=LEFT)
	spec.label.grid(columnspan=2)

	w.portr = portr = Photo(repr='portr', path='monet_sm.jpg')
	w.frames["Third Frame"].addWidget(w.portr, (0, 0))
	w.portr.hide()

	w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
	w.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

	w.attinfo.editwidget=False
	w.attinfo.canvas.config(width=500, height=555)

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]


	def s():
		try:
			w.s = sby.getData()[1]

			print(sby.getData())


			if sby.getData()[0] != 'bCode':
				sty = sby.getData()[0]
				sdp = sby.getData()[1]

				sl = []

				for s in d.studentList:
					if d.studentList[s].datapoints[sty] == sdp:
						dp = d.studentList[s].datapoints
						sl.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName']])


				if len(sl) == 0:
					nos(w.lang)
					return

				w.s = sl[0][0]
				if len(sl) > 1:
					sl.sort()
					w.s = spicker(sl)
					if not w.s: return

			#reset portrait
			w.portr.setData('monet_sm.jpg')
			portr2.setData('monet_sm.jpg')

			#reset classes rem
			spec.setData("")

			#temp workaround while table is fixed
			for child in w.frames["Eleventh Frame"].winfo_children():
				child.destroy()

			w.attinfo.build(headers=w.attinfoh, data=[[]])
			w.frames["Eleventh Frame"].addWidget(w.attinfo, (0, 0))
			w.frames["Eleventh Frame"].grid(rowspan=4, sticky=W)

			w.attinfo.editwidget=False
			w.attinfo.canvas.config(width=500, height=555)
			#

			#temp workaround while table is fixed
			for child in w2.frames["Third Frame"].winfo_children():
				child.destroy()

			w2.attinfo.build(headers=w2.attinfoh, data=[[]])
			w2.frames["Third Frame"].addWidget(w2.attinfo, (0, 0))
			w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

			w2.attinfo.editwidget=False
			w2.attinfo.canvas.config(width=500, height=500)
			#
			dp = d.studentList[w.s].datapoints

			w.populate(dp)
			w2.populate(dp)

			#if amount owed is larger than amount paid, color amount owed in red
			if dp['tpa'] < dp['tpo']: tpo.entry.config(bg='red')
			else: tpo.entry.config(bg='white')

			sby.entry.delete(0, END)

			if cs(d.studentList[w.s].datapoints['firstName'], w.lang): ss()
		except:
			nos(w.lang)
			pass


	def ss():
		d.scanStudent(w.s, xtra=w.lang['Auto'] if sby.getData()[0] == 'bCode' else w.lang['Manual'])
		d.saveData()
		
		#show alert if classes remaining is less than 2
		cRem = d.studentList[w.s].datapoints['cRemaining']
		if cRem <= 2:
			spec.show()
			spec.setData(w.lang['Classes remaining for this student'] + ': ' + str(cRem))
			spec.label.config(fg='red', font=('Verdana', 15))
		else:
			#hide, show will work better once window size is set
			pass

		#update cRemaining
		cRemaining.setData(str(cRem))

		w.frames['Eleventh Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])
		w2.frames['Third Frame'].widgets['attinfo'].setData(d.studentList[w.s].datapoints['attinfo'])

		#auto scroll to last position
		w.attinfo.canvas.yview_moveto(1.0)
		w2.attinfo.canvas.yview_moveto(1.0)

		#reset Scan By to Barcode
		sby.b.set(sby.rads[0][1])


	def z():
		try:
			ss() if cs(d.studentList[w.s].datapoints['firstName'], w.lang) else False
		except:
			print("error-105")


		

		print(sby.getData())

	w.frames["Tenth Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	w.frames["Tenth Frame"].addWidget(bsearch, (1, 0))
	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

#collect and check in button
	def collect():
		try:
			s = d.studentList[w.s]
			if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w.lang): return
			s.datapoints = dict(list(s.datapoints.items()) + list(w.collect(s.datapoints).items()))
			d.saveData()
		except:
			return

	sstudent = Buttonbox(text='savestudent', lang=w.lang, repr='sstudent')
	w.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)

	bcheck = Buttonbox(text='cinstudent', lang=language, repr='bcheck')
	w.frames["Fifth Frame"].addWidget(bcheck, (0, 1))
	bcheck.config(cmd=z)






#t2 window
	t2 = Window(top=True)
	t2.attributes('-fullscreen', False)
	t2.geometry('1200x800')

#remove close button function
	t2.protocol('WM_DELETE_WINDOW', lambda: False)

#set minimum height
	t2.update_idletasks()
	t2.after_idle(lambda: t2.minsize(t2.winfo_width(), t2.winfo_height()))

	w2 = AppWindow(t2.mainFrame)

	w2.lang = lang

#attendance table
	w2.attinfo = Table(repr='attinfo', edit=True)
	w2.attinfoh = [language['Date'], language['Check-In Time'], language['Class Time']]
	w2.attinfo.build(headers=w2.attinfoh, data=[[]])
	w2.attinfo.clast = '#FF99FF'

#frame initialization
	w2.newFrame("First Frame", (0, 0))
	w2.newFrame("Second Frame", (1, 0))
	w2.newFrame("Third Frame", (0, 1))

	firstName2 = Textbox(text="First Name", lang=language, repr='firstName')
	lastName2 = Textbox(text="Last Name", lang=language, repr='lastName')
	chineseName2 = Textbox(text="Chinese Name", lang=language, repr='chineseName')
	bCode2 = Textbox(text="Barcode", lang=language, repr='bCode')
	sid2 = IntTextbox(text="Old Student ID", lang=language, repr='sid')
	dob2 = Datebox(text="Date of Birth", lang=language, repr='dob')
	portr2 = Photo(repr='portr', path='monet_sm.jpg')

	w2.frames["First Frame"].addWidget(portr2, (0, 0))

#basic info widgets
	w2.frames["Second Frame"].addWidget(firstName2, (0, 0))
	w2.frames["Second Frame"].addWidget(lastName2, (1, 0))
	w2.frames["Second Frame"].addWidget(chineseName2, (2, 0))

	w2.frames["Second Frame"].addWidget(sepr, (5, 0))

	w2.frames["Second Frame"].addWidget(bCode2, (6, 0))
	w2.frames["Second Frame"].addWidget(sid2, (7, 0))

	w2.frames["Second Frame"].addWidget(sepr, (8, 0))

	w2.frames["Second Frame"].addWidget(dob2, (10, 0))

#att table widget
	w2.frames["Third Frame"].addWidget(w.attinfo, (0, 0))
	w2.frames["Third Frame"].grid(rowspan=100, sticky=W)

	w2.attinfo.editwidget=False
	w.attinfo.canvas.config(width=500, height=500)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)
	for frame in w2.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	return t2


	





	


if __name__ == '__main__':
	t = Window()
	t.attributes('-fullscreen', False)
	t.geometry('1000x700')

	main(t.mainFrame, language)

	t.mainloop()

	print('abcd'[:3])

