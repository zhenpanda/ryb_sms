from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *


def main(lang, d, top=False, i=0):

	d.loadData()

	t = Window(top=top)
	t.attributes('-fullscreen', False)
	t.geometry('1280x740+1+1')
	t.resizable(0, 0)
	t.grab_set()
	t.focus_set()
	t.titleFrame.config(height=1)
	t.wintitle.place_forget()

	w = AppWindow(t.mainFrame)
	w2 = AppWindow(t.mainFrame)
	w3 = AppWindow(t.mainFrame)

	#w.pack_forget()
	w.pack(anchor=N)
	w3.pack_forget()

	w2.lang = lang
	w2.s = i

#frame initialization
	w2.newFrame("First Frame", (1, 1))
	w2.newFrame("Second Frame", (1, 2))
	w2.newFrame("Third Frame", (2, 1))
	w2.newFrame("Fourth Frame", (2, 2))
	w2.newFrame("Fifth Frame", (5, 0))
	w2.newFrame("Sixth Frame", (4, 2))
	w.newFrame("Seventh Frame", (1, 0))
	w2.newFrame("Eigth Frame", (3, 2))
	w2.newFrame("Tenth Frame", (0, 1))
	w2.newFrame("Eleventh Frame", (1, 3))
	w2.newFrame("Twelfth Frame", (3, 0))
	#w2.newFrame("Ninth Frame", (3, 1))

	w3.newFrame("table_frame", (0, 0))

	w2.frames["Fifth Frame"].grid(columnspan=5, sticky=S)
	w.frames["Seventh Frame"].grid(rowspan=2)
	w2.frames["Tenth Frame"].grid(columnspan=5)
	w2.frames["Eleventh Frame"].grid(sticky=N)
	w2.frames["Eigth Frame"].grid(sticky=N, columnspan=5)
	w2.frames["Eleventh Frame"].columnconfigure(0, weight=5, minsize=520)
	#w2.frames["Ninth Frame"].grid(rowspan=5, sticky=N)

#student info widgets
	w2.frames["First Frame"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First Frame"].addWidget(firstName, (1, 0))
	w2.frames["First Frame"].addWidget(lastName, (2, 0))
	w2.frames["First Frame"].addWidget(chineseName, (3, 0))
	w2.frames["First Frame"].addWidget(dob, (4, 0))
	w2.frames["First Frame"].addWidget(age, (5, 0))
	w2.frames["First Frame"].addWidget(parentName, (6, 0))
	w2.frames["First Frame"].addWidget(cp, (7, 0))

#address widgets
	w2.frames["Second Frame"].addWidget(ainfo, (0, 0))
	ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Second Frame"].addWidget(city, (4, 0))
	w2.frames["Second Frame"].addWidget(state, (5, 0))
	w2.frames["Second Frame"].addWidget(zip, (6, 0))
	w2.frames["Second Frame"].addWidget(email, (7, 0))

#contact widgets
	w2.frames["Third Frame"].addWidget(cinfo, (0, 0))
	cinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	cinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Third Frame"].addWidget(pup, (1, 0))
	w2.frames["Third Frame"].addWidget(hPhone, (2, 0))
	w2.frames["Third Frame"].addWidget(cPhone, (3, 0))
	w2.frames["Third Frame"].addWidget(cPhone2, (4, 0))

#database info widgets
	w2.frames["Fourth Frame"].addWidget(pinfo, (0, 0))
	pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Fourth Frame"].addWidget(bCode, (1, 0))
	w2.frames["Fourth Frame"].addWidget(sid, (2, 0))
	
#payment widgets
	tpd = Datebox(text="Tuition Paid Day", lang=language, repr='tpd')
	tpd.mode = 'nonedit'
	w2.frames["Fourth Frame"].addWidget(tpd, (6, 0))
	w2.frames["Fourth Frame"].addWidget(tpa, (7, 0))
	w2.frames["Fourth Frame"].addWidget(tp, (8, 0))
	w2.frames["Fourth Frame"].addWidget(tpo, (9, 0))

#class widget
	w2.frames["Fourth Frame"].addWidget(sType, (13, 0))
	w2.frames["Fourth Frame"].addWidget(cAwarded, (14, 0))
	w2.frames["Fourth Frame"].addWidget(cRemaining, (15, 0))
	w2.frames["Fourth Frame"].addWidget(ctime, (16, 0))

#notes widget
	w2.frames["Third Frame"].addWidget(ninfo, (5, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Third Frame"].addWidget(notes, (6, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=3)
	notes.config(height=8, width=32)


	baclass = Buttonbox(text='awardclass', lang=w2.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w2.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w2.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')

	w2.frames["Fourth Frame"].addWidget(bgold, (11, 0))
	w2.frames["Fourth Frame"].addWidget(bbasic, (11, 0))
	w2.frames["Fourth Frame"].addWidget(baoclass, (11, 0))

	bgold.selfframe.grid(sticky=W, columnspan=2)
	bbasic.selfframe.grid(sticky=N, columnspan=2)
	baoclass.selfframe.grid(sticky=E, columnspan=2)


	switch_frame_button = Buttonbox(text='Attendance Table', lang=w2.lang, repr='showstudentinfo')
	#show_table = Buttonbox(text='Attendance Table', lang=w2.lang, repr='showtable')

	w.frames["Seventh Frame"].addWidget(switch_frame_button, (2, 0))
	#w2.frames["Seventh Frame"].addWidget(show_table, (3, 0))

	t.current_shown = 'w2'
	def switch_frame():
		if t.current_shown == 'w2':
			w2.pack_forget()
			w3.pack(side=LEFT)
			t.current_shown = 'w3'
			switch_frame_button.button.config(text=w2.lang['Student Information'])
		elif t.current_shown == 'w3':
			w3.pack_forget()
			w2.pack(side=LEFT)
			t.current_shown = 'w2'
			switch_frame_button.button.config(text=w2.lang['Attendance Table'])
		return

	switch_frame_button.config(cmd=switch_frame)

	baoclass.config(cmd=caddone, width=12)
	bgold.config(cmd=lambda: caddmorex(60), width=12)
	bbasic.config(cmd=lambda: caddmorex(15), width=12)

	baoclass.selfframe.grid(padx=2)
	bgold.selfframe.grid(padx=2)
	bbasic.selfframe.grid(padx=2)
	
	
	#w2.frames["Sixth Frame"].addWidget(baclass, (0, 0))
	#w2.frames["Sixth Frame"].addWidget(baac, (2, 0))
	#baclass.config(cmd=lambda: cpicker(w2.lang))
	#baac.config(cmd=cadd)

	w.frames["Seventh Frame"].addWidget(portr, (0, 0))

	portr.resized = portr.picture.resize((200, 200), Image.ANTIALIAS)
	portr.image = ImageTk.PhotoImage(portr.resized)
	portr.label.config(image=portr.image)

	w2.attinfo = attinfo
	w3.frames["table_frame"].addWidget(w2.attinfo, (0, 0))
	#w3.frames["table_frame"].grid(rowspan=100, sticky=W)

#renew classes button
	def renC():
		try:
			d.studentList[w2.s]
		except:
			return

		r = renew(w2.lang)
		dp = d.studentList[w2.s].datapoints
		dp['cRemaining'] = dp['cRemaining'] + r
		dp['cAwarded'] = dp['cAwarded'] + r
		dp['expire'] = d.calcExpir(datetime.now().date(), r)
		cRemaining.setData(dp['cRemaining'])
		cAwarded.setData(dp['cAwarded'])

	w2.ren = Buttonbox(text='Renew classes', lang=w2.lang, repr='ren')
	w2.frames["Fourth Frame"].addWidget(w2.ren, (12, 0))
	w2.ren.selfframe.grid(columnspan=3)
	w2.ren.config(cmd=renC)

	w2.attinfo.editwidget=False
	w2.attinfo.canvas.config(width=500, height=500)

	#reset portrait
	portr.setData('monet_sm.jpg')

	s = d.studentList[i]
	#print(s.datapoints['attinfo'])
	print(s.datapoints['notes'])
	w2.populate(s.datapoints)
	w3.populate(s.datapoints)

	tdp = dict(w2.collect(s.datapoints))

	#if amount owed is larger than amount paid, color amount owed in red
	if s.datapoints['tpa'] < s.datapoints['tpo']: tpo.entry.config(bg='red')

	def collect():
		if not changed():
			t.destroy()
			return
		if not conS(s.datapoints['firstName'] + ' ' + s.datapoints['lastName'], w2.lang): return

		#if the barcode changes
		cbcode = bCode.getData()
		if s.datapoints['bCode'] != cbcode:
			if not ase(d.studentList[cbcode].datapoints['firstName'], w2.lang):
				return
			else:
				dbcode = s.datapoints['bCode']
				d.studentList[cbcode] = s
				del d.studentList[dbcode]

		s.datapoints = dict(list(s.datapoints.items()) + list(w2.collect(s.datapoints).items()))
		d.saveData()

		t.destroy()

#add payment
	def add_payment_():
		w.s = i
		if not hasattr(w, 's') or (w.s not in d.studentList): return

		payment_data = add_payment_prompt(lang, d, w.s)

		if payment_data == None: return

		payment_info = payment_data[0]
		payment_datapoints = payment_data[1]

		d.studentList[w.s].datapoints['payment_info'].append(payment_info)		
		payment_successful(lang)

		print('payment added')

		date = d.studentList[w.s].datapoints['payment_info'][-1]['date'].strftime("%m/%d/%Y").split('/')
		month = date[0]
		day = date[1]
		year = date[2]

		tpd.config(m=month, d=day, y=year)
		tpa.setData(payment_datapoints['tpa'])
		tpo.setData(payment_datapoints['tpo'])
		tp.setData(payment_datapoints['tp'])

		d.studentList[w.s].datapoints['tpa'] = payment_datapoints['tpa']
		d.studentList[w.s].datapoints['tpo'] = payment_datapoints['tpo']
		d.studentList[w.s].datapoints['tp'] = payment_datapoints['tp']

		d.saveData()

	add_payment = Buttonbox(text='Add Payment', lang=w2.lang, repr='addpayment')
	w2.frames["Fourth Frame"].addWidget(add_payment, (10, 0))
	add_payment.selfframe.grid(columnspan=2)
	add_payment.button.config(width=20)
	add_payment.config(cmd=add_payment_)

	def changed():
		ctdp = dict(w2.collect(s.datapoints))
		#print(ctdp)
		for key in tdp.keys():
			if ctdp[key] != tdp[key]:
				return True
		return False


	def quit():
		if not changed():
			t.destroy()
		elif ret('a', w2.lang):
			t.destroy()


	sstudent = Buttonbox(text='savestudent', lang=w2.lang, repr='sstudent')
	w2.frames["Fifth Frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	bclose = Buttonbox(text='close', lang=w2.lang, repr='bclose')
	w2.frames["Fifth Frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	w.frames["Seventh Frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w2.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w2.lang)

	brwp.config(lang=w2.lang)
	switch_frame_button.config(lang=w2.lang)
	w2.attinfo.config(lang=w2.lang)
	
	t.mainloop()