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
	w2.newFrame("First column", (1, 1))
	w2.newFrame("Second column", (1, 2))
	w2.newFrame("Button frame", (5, 0))
	w.newFrame("Portrait frame", (1, 0))
	#w2.newFrame("Ninth Frame", (3, 1))

	w3.newFrame("table_frame", (0, 0))

	w2.frames["Button frame"].grid(columnspan=5, sticky=S)
	w.frames["Portrait frame"].grid(rowspan=2)
	#w2.frames["Ninth Frame"].grid(rowspan=5, sticky=N)

#student info widgets
	w2.frames["First column"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First column"].addWidget(firstName, (1, 0))
	w2.frames["First column"].addWidget(lastName, (2, 0))
	w2.frames["First column"].addWidget(chineseName, (3, 0))
	w2.frames["First column"].addWidget(dob, (4, 0))
	w2.frames["First column"].addWidget(age, (5, 0))
	w2.frames["First column"].addWidget(parentName, (6, 0))
	w2.frames["First column"].addWidget(cp, (7, 0))

#address widgets
	w2.frames["Second column"].addWidget(ainfo, (0, 0))
	ainfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Second column"].addWidget(city, (4, 0))
	w2.frames["Second column"].addWidget(state, (5, 0))
	w2.frames["Second column"].addWidget(zip, (6, 0))
	w2.frames["Second column"].addWidget(email, (7, 0))

#contact widgets
	w2.frames["First column"].addWidget(cinfo, (8, 0))
	cinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	cinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First column"].addWidget(pup, (9, 0))
	w2.frames["First column"].addWidget(hPhone, (10, 0))
	w2.frames["First column"].addWidget(cPhone, (11, 0))
	w2.frames["First column"].addWidget(cPhone2, (12, 0))

#database info widgets
	w2.frames["Second column"].addWidget(pinfo, (8, 0))
	pinfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["Second column"].addWidget(bCode, (9, 0))
	w2.frames["Second column"].addWidget(sid, (10, 0))
	
#payment widgets
	tpd = Datebox(text="Tuition Paid Day", lang=language, repr='tpd')
	tpd.mode = 'nonedit'
	w2.frames["Second column"].addWidget(tpd, (11, 0))
	w2.frames["Second column"].addWidget(tpa, (12, 0))
	w2.frames["Second column"].addWidget(tp, (13, 0))
	w2.frames["Second column"].addWidget(tpo, (14, 0))

#class widget
	w2.frames["Second column"].addWidget(sType, (19, 0))
	w2.frames["Second column"].addWidget(cAwarded, (20, 0))
	w2.frames["Second column"].addWidget(cRemaining, (21, 0))
	w2.frames["Second column"].addWidget(ctime, (22, 0))

#notes widget
	w2.frames["First column"].addWidget(ninfo, (13, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w2.frames["First column"].addWidget(notes, (14, 0))
	notes.label.grid_forget()
	notes.sentry.grid(column=0, columnspan=3)
	notes.config(height=8, width=32)


	baclass = Buttonbox(text='awardclass', lang=w2.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w2.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w2.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')
	add_90_button = Buttonbox(text='twoyear90', lang=lang, repr='add90')

	w2.frames["Second column"].addWidget(baoclass, (15, 0))
	w2.frames["Second column"].addWidget(bbasic, (15, 1))
	w2.frames["Second column"].addWidget(bgold, (16, 0))
	w2.frames["Second column"].addWidget(add_90_button, (16, 1))

	switch_frame_button = Buttonbox(text='Attendance Table', lang=w2.lang, repr='showstudentinfo')

	w.frames["Portrait frame"].addWidget(switch_frame_button, (2, 0))

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

	baoclass.config(cmd=caddone, width=15)
	bgold.config(cmd=lambda: caddx(60), width=15)
	bbasic.config(cmd=lambda: caddx(15), width=15)
	add_90_button.config(cmd=lambda: caddx(90), width=15)

	bbasic.selfframe.grid(padx=2, sticky=W)
	add_90_button.selfframe.grid(padx=2, sticky=W)

	w.frames["Portrait frame"].addWidget(portr, (0, 0))

	portr.resized = portr.picture.resize((200, 200), Image.ANTIALIAS)
	portr.image = ImageTk.PhotoImage(portr.resized)
	portr.label.config(image=portr.image)

	w2.attinfo = attinfo
	w3.frames["table_frame"].addWidget(w2.attinfo, (0, 0))

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
	w2.frames["Second column"].addWidget(w2.ren, (18, 0))
	w2.ren.selfframe.grid(sticky=W, columnspan=2)
	w2.ren.button.config(width=31)
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

	for cell_id, cell_val in w2.attinfo.cells.items():
		if cell_id[0] == 0:
			cur_text = cell_val.label.cget('text')
			cell_val.label.config(text=lang[cur_text])


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
	w2.frames["Second column"].addWidget(add_payment, (17, 0))
	add_payment.selfframe.grid(sticky=W, columnspan=2)
	add_payment.button.config(width=31)
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
	w2.frames["Button frame"].addWidget(sstudent, (0, 0))
	sstudent.config(cmd=collect)
	sstudent.selfframe.grid(padx=5)

	bclose = Buttonbox(text='close', lang=w2.lang, repr='bclose')
	w2.frames["Button frame"].addWidget(bclose, (0, 1))
	bclose.config(cmd=quit)

	w.frames["Portrait frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker)

	#set starting lang
	for frame in w2.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w2.lang)

	brwp.config(lang=w2.lang)
	switch_frame_button.config(lang=w2.lang)
	w2.attinfo.config(lang=w2.lang)
	
	t.mainloop()