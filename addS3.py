from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
import tkinter.ttk as ttk


def main(t, lang, d, sM):
	'''addS3'''
	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#frame initialization
	w.newFrame("Portrait frame", (0, 0))
	w.newFrame("First column", (0, 1))
	w.newFrame("Second column", (0, 2))
	#w.newFrame("First column", (2, 1))
	#w.newFrame("Second column", (0, 2))
	#w.newFrame("Second column", (1, 2))
	#w.newFrame("Second column", (2, 2))
	w.newFrame("Button frame", (3, 0))

#title
	w.frames["Portrait frame"].grid(rowspan=5, sticky=N)
	w.frames["Button frame"].grid(columnspan=5, sticky=S)
	#w.frames["Second column"].grid(rowspan=2)
	#w.frames["First column"].grid(rowspan=2, sticky=E)
	#w.frames["Second column"].grid(rowspan=2, sticky=N)

#debugging
	#w.frames["First column"].config(bg='lightgrey')

	w.sectioncolor = "#3B5C8D"
	#3B5C8D

#student info widgets
	w.frames["First column"].addWidget(sinfo, (0, 0))
	sinfo.label.config(bg=w.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'), text=w.lang['Student information'])
	sinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First column"].addWidget(firstName, (1, 0))
	w.frames["First column"].addWidget(lastName, (2, 0))
	w.frames["First column"].addWidget(chineseName, (3, 0))
	w.frames["First column"].addWidget(dob, (4, 0))
	w.frames["First column"].addWidget(age, (5, 0))
	w.frames["First column"].addWidget(parentName, (6, 0))
	w.frames["First column"].addWidget(cp, (7, 0))

#address widgets
	w.frames["Second column"].addWidget(ainfo, (0, 0))
	ainfo.label.config(bg=w.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'))
	ainfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["Second column"].addWidget(addr, (1, 0))
	w.frames["Second column"].addWidget(city, (2, 0))
	w.frames["Second column"].addWidget(state, (3, 0))
	w.frames["Second column"].addWidget(zip, (4, 0))
	w.frames["Second column"].addWidget(email, (5, 0))

#contact widgets
	w.frames["First column"].addWidget(cinfo, (8, 0))
	cinfo.label.config(bg=w.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'))
	cinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First column"].addWidget(pup, (9, 0))
	w.frames["First column"].addWidget(hPhone, (10, 0))
	w.frames["First column"].addWidget(cPhone, (11, 0))
	w.frames["First column"].addWidget(cPhone2, (12, 0))

#database info widgets
	w.frames["Second column"].addWidget(pinfo, (6, 0))
	pinfo.label.config(bg=w.sectioncolor, fg='white', font=('Jumbo', '11', 'bold'))
	pinfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["Second column"].addWidget(bCode, (7, 0))
	w.frames["Second column"].addWidget(sid, (8, 0))

	bCode.setData(d.formatCode())

#payment widgets
	w.frames["Second column"].addWidget(tpd, (9, 0))
	w.frames["Second column"].addWidget(tpa, (10, 0))
	w.frames["Second column"].addWidget(tp, (11, 0))
	w.frames["Second column"].addWidget(tpo, (12, 0))
	w.frames["Second column"].addWidget(pay_by, (13, 0))
	

#class widget
	w.frames["Second column"].addWidget(sType, (16, 0))
	w.frames["Second column"].addWidget(cAwarded, (17, 0))
	w.frames["Second column"].addWidget(cRemaining, (18, 0))
	w.frames["Second column"].widgets['cRemaining'].hide()
	#w.frames["Second column"].addWidget(ctime, (7, 0))

#notes widget
	w.frames["First column"].addWidget(ninfo, (13, 0))
	ninfo.label.config(bg='#3B5C8D', fg='white', font=('Jumbo', '11', 'bold'))
	ninfo.label.grid(columnspan=2, sticky=E+W, pady=3)
	w.frames["First column"].addWidget(notes, (14, 0))
	notes.label.grid_forget()
	notes.sentry.grid(row=14, column=0, columnspan=2)
	notes.config(height=8, width=32)

	pay_by.entry.config(state=DISABLED)
	def change_pay_by_state(state):
		if pay_by.entry.cget('state') == NORMAL and state == NORMAL:
			return
		else:
			pay_by.entry.delete(0, END)
			pay_by.entry.config(state=state)

	def add_class_():
		if class_assoc[w.class_stringvar.get()] == 1:
			caddone()
		else:
			caddx(class_assoc[w.class_stringvar.get()])
		#return


	pay_by.label_entry_frame.pack_forget()
	pay_by.selfframe.grid(columnspan=2, sticky=E)
	pay_by.label_entry_frame.pack(side=TOP)
	pay_by.label.grid(row=0, column=0)
	pay_by.entry.grid(row=0, column=1)
	pay_by.brads[0].bind('<Button-1>', lambda event: change_pay_by_state(DISABLED))
	pay_by.brads[1].bind('<Button-1>', lambda event: change_pay_by_state(NORMAL))


	#add_class = Buttonbox(text='Add class', lang=w.lang, repr='aclass')
	baclass = Buttonbox(text='awardclass', lang=w.lang, repr='aclass')
	baoclass = Buttonbox(text='awardoneclass', lang=w.lang, repr='aoclass')
	baac = Buttonbox(text='awardaddclass', lang=w.lang, repr='baaclasses')
	bgold = Buttonbox(text='gold60', lang=lang, repr='bgold')
	bbasic = Buttonbox(text='basic15', lang=lang, repr='bbasic')
	add_90_button = Buttonbox(text='twoyear90', lang=lang, repr='add90')

	'''
	w.class_stringvar = StringVar()
	class_input = ttk.Combobox(
		w.frames["Second column"],
		textvariable=w.class_stringvar, width=20, state='readonly')
	class_input.grid(row=11, column=0, columnspan=2, sticky=W, padx=(2, 0))

	if lang['self'] == 'chinese':
		class_input['values'] = ('添加一课 (+1)', '基本卡 (+15)', '年卡 (+60)', '兩年卡 (+90)')
		w.class_stringvar.set('添加一课 (+1)')
	elif lang['self'] == 'english':
		class_input['values'] = ('Single (+1)', 'Basic (+15)', 'Yearly (+60)', 'Two Year (+90)')
		w.class_stringvar.set('Single (+1)')

	class_assoc = {
		'添加一课 (+1)': 1, '基本卡 (+15)': 15, '年卡 (+60)': 60, '兩年卡 (+90)': 90,
		'Single (+1)': 1, 'Basic (+15)': 15, 'Yearly (+60)': 60, 'Two Year (+90)': 90
	}

	w.frames["Second column"].addWidget(add_class, (11, 0))
	add_class.config(cmd=add_class_, width=12)
	add_class.selfframe.grid(padx=2, columnspan=2, sticky=E)
	'''

	w.frames["Second column"].addWidget(baoclass, (14, 0))
	w.frames["Second column"].addWidget(bbasic, (14, 1))
	w.frames["Second column"].addWidget(bgold, (15, 0))
	w.frames["Second column"].addWidget(add_90_button, (15, 1))

	baoclass.config(cmd=caddone, width=15)
	bgold.config(cmd=lambda: caddx(60), width=15)
	bbasic.config(cmd=lambda: caddx(15), width=15)
	add_90_button.config(cmd=lambda: caddx(90), width=15)

	bbasic.selfframe.grid(padx=2, sticky=W)
	add_90_button.selfframe.grid(padx=2, sticky=W)

	w.frames["Portrait frame"].addWidget(portr, (0, 0))
	portr.label.config(bg='black')

	portr.resized = portr.picture.resize((200, 200), Image.ANTIALIAS)
	portr.image = ImageTk.PhotoImage(portr.resized)
	portr.label.config(image=portr.image)


#collect student information
#and save it into database
	def collect():
		
		ns = StudentInfo()
		ns.datapoints = dict(list(ns.datapoints.items()) + list(w.collect(ns.datapoints).items()))
		#print(ns.datapoints)
		ns.datapoints['payment_info'] = []
		payment_info = {
			'date': datetime.now().date(),
			'payment_type': pay_by.getData()[0],
			'check_num': None if pay_by.getData()[0] == 'Cash' else pay_by.getData()[1],
			'total_amount': float(tpa.getData()),
			'amount_paid': float(tp.getData()),
			'amount_owed': float(tpo.getData()),
			#'paid_on_date': float(tp.getData())
		}
		ns.datapoints['payment_info'].append(payment_info)
		print('payment added', payment_info)

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

		sM(False)

#save and add button widgets
	sadd = Buttonbox(text='addstudent', lang=language, repr='sadd')
	w.frames["Button frame"].addWidget(sadd, (0, 0))
	sadd.button.config(height=5, font=('Verdana', '12'))
	sadd.config(cmd=collect)

	w.frames["Portrait frame"].addWidget(brwp, (1, 0))
	brwp.config(cmd=ppicker, width=14)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			#print(widget.repr)
			widget.config(lang=w.lang)