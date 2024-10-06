from tkinter import *
from uiHandler22 import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
from photoWidget2 import *
from preBuilts2 import ret, bexp, password_prompt, wrong_password, pw_reset_confirm, print_succesful, database_backup_successful, already_running_
from tkinter import filedialog
import addS3
import scanS22
import sDb22
import tools2
import preBuilts2

def main():

#language changer
	def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)


	t = Window(top=False)
	t.attributes('-fullscreen', False)
	t.geometry('1280x740+1+1')
	t.wm_title("RYB Student Attendance")

#confirm closing of the add student window
	t.con = False

#show and hide sub-windows
	def showWindow(f):
		t.titleFrame.config(height=1)
		t.wintitle.place_forget()
		w.frames["First Frame"].grid_forget()
		print(f.__doc__)
		if (f.__doc__) == 'addS3':
			t.con = True
			w.t = f(w.frames["Second Frame"], w.lang, w.d, showMain)
		elif (f.__doc__) == 'tools2':
			if w.k.files['resetpw'] == True:
				new_pw = password_prompt(w.lang, w.k.files['dbpw'])
				if new_pw == 'cancel' or w.k.hashpw(new_pw[0]) != w.k.files['dbpw']:
					wrong_password(w.lang)
					showMain(t.con)
					return
				w.k.files['dbpw'] = w.k.hashpw(new_pw[1])
				w.k.files['resetpw'] = False
				w.k.save()
				pw_reset_confirm(w.lang)
			else:
				pw_input = password_prompt(w.lang, False)
				if not w.k.hashpw(pw_input) == w.k.files['dbpw'] or pw_input == 'cancel':
					wrong_password(w.lang)
					showMain(t.con)
					return
			w.t = f(w.frames["Second Frame"], w.lang, w.d, w.k)
		else:
			t.con = False
			w.t = f(w.frames["Second Frame"], w.lang, w.d)
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()

#show and hide main window
	def showMain(con):
		if con:
			if not ret('a', w.lang): return

		w.frames['Second Frame'].grid_forget()
		t.titleFrame.config(height=60)
		t.wintitle.place(in_=t.titleFrame, anchor="c", relx=.5, rely=.5)
		try:
			#to destroy the extra window in scan student
			w.t.destroy()
		except:
			pass

		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.frames['Second Frame'].destroy()
		w.newFrame("Second Frame", (2, 0))
		w.frames['Second Frame'].grid_forget()

		w.frames["First Frame"].grid(row=1)
		w.frames['Third Frame'].grid_forget()

		w.k.files['cfilepath'] = w.d.file
		w.k.save()

		print(w.d.school)
		w.p.config(path=w.k.files['bg_img'][w.d.school])

#print report prompt
	def printPrompt():
		output_path = filedialog.askdirectory()
		if output_path != '':
			w.d.exportreport(output_path, datetime.strftime(datetime.now(), '%m/%d/%Y'))
		else:
			return
		print_succesful(w.lang)
		
	def choose_school(event):
		school = preBuilts2.choose_school(w.lang)
		w.k.files['school'] = 'Flushing' if school == 'cancel' else school
		w.d.school = w.k.files['school']
		w.k.save()

		return
		
	def expf():
		try:
			fpath = filedialog.askdirectory()
			today = datetime.now()
			date = today.strftime('%m.%d.%y')
			time = today.strftime('%I.%M.%p')
			w.d.exportdb(fpath + '/RYB Student Backup - ' + w.d.school + ' ' + date + ' ' + time + '.rybdb')			
			database_backup_successful(w.lang)
		except:
			print('database export unsuccessful')

#main window and starting language
	w = AppWindow(t.mainFrame)
	w.lang = languages['english']

#title
	t.wintitle.config(text=w.lang['RYB Student Management'])


#load current database
	w.k = keeper.Keeper('keeper.db')
	w.d = StudentDB(file=w.k.files['cfilepath'], pwfile=w.k.files['pwfile'], cfile=w.k.fname)

	if 'school' not in w.k.files:
		w.k.files['school'] = preBuilts2.choose_school(w.lang)
		w.d.school = w.k.files['school']
		w.k.save()
	else:
		w.d.school = w.k.files['school']

#frame creation and positions
	#w.newFrame("Title Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (3, 0))

#hide sub-frames
	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

#buttons to call sub-windows
	bchoose_school = Buttonbox(text='Choose School', lang=w.lang, repr='bcschool')
	bsadd = Buttonbox(text='Add Students', lang=w.lang, repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Scan Students', lang=w.lang, repr='bsscan') #Scan Student
	bssdb = Buttonbox(text='Student Database', lang=w.lang, repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', lang=w.lang, repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to Main Menu', lang=w.lang, repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit') #Exit
	bclang = Buttonbox(text='changelanguage', lang=w.lang, repr='bclang') #Change Language
	bprint = Buttonbox(text='print report', lang=w.lang, repr='bprint') #Print end of day report
	bexp = Buttonbox(text='expxls', lang=w.lang, repr='bexp')

#background image
	w.p = Photo(repr='splash', path=w.k.files['bg_img'][w.d.school])#'background_IMG.jpg')

#place buttons and background image
	#w.frames["First Frame"].addWidget(bchoose_school, (0, 0))
	w.frames["First Frame"].addWidget(bsadd, (1, 0))
	w.frames["First Frame"].addWidget(bsscan, (2, 0))
	w.frames["First Frame"].addWidget(bssdb, (4, 0))
	w.frames["First Frame"].addWidget(bstools, (5, 0))
	w.frames["First Frame"].addWidget(bexp, (6, 0))
	w.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	w.frames["First Frame"].addWidget(bclang, (7, 0))
	w.frames["First Frame"].addWidget(bprint, (8, 0))
	w.frames["First Frame"].addWidget(bsexit, (9, 0))
	w.frames["First Frame"].addWidget(w.p, (0, 2))
	Label(w.frames["First Frame"], text='  ').grid(column=1) #separator between buttons and background image

#set commands for each button
	#bchoose_school.config(cmd=lambda: choose_school(w.lang))
	bsadd.config(cmd=lambda: showWindow(addS3.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=lambda: showMain(t.con))
	bprint.config(cmd=printPrompt)
	bsexit.config(cmd=t.destroy)
	bclang.config(cmd=clang)
	bexp.config(cmd=expf)
	bstools.selfframe.grid_forget()
	#secret configuration to call Database Management
	# w.p.label.bind('<Control-Alt-Shift-D>', lambda e: showWindow(tools2.main))

	# w.p.label.grid(rowspan=100, sticky=E)

	w.mmbuttoncol = '#E3E9F9'
	w.mmbuttonfg = 'black'

	bsbmm.idlebg = w.mmbuttoncol
	bsbmm.fg = w.mmbuttonfg
	bsbmm.hoverfg = 'white'
	bsbmm.button.config(bg=bsbmm.idlebg, fg=bsbmm.fg)

	bsadd.idlebg = w.mmbuttoncol
	bsadd.fg = w.mmbuttonfg
	bsadd.hoverfg = 'white'
	bsadd.button.config(bg=bsadd.idlebg, fg=bsadd.fg)

	bsscan.idlebg = w.mmbuttoncol
	bsscan.fg = w.mmbuttonfg
	bsscan.hoverfg = 'white'
	bsscan.button.config(bg=bsscan.idlebg, fg=bsscan.fg)

	bssdb.idlebg = w.mmbuttoncol
	bssdb.fg = w.mmbuttonfg
	bssdb.hoverfg = 'white'
	bssdb.button.config(bg=bssdb.idlebg, fg=bssdb.fg)

	bclang.idlebg = w.mmbuttoncol
	bclang.fg = w.mmbuttonfg
	bclang.hoverfg = 'white'
	bclang.button.config(bg=bclang.idlebg, fg=bclang.fg)

	bsexit.idlebg = w.mmbuttoncol
	bsexit.fg = w.mmbuttonfg
	bsexit.hoverfg = 'white'
	bsexit.button.config(bg=bsexit.idlebg, fg=bsexit.fg)

	bprint.idlebg = w.mmbuttoncol
	bprint.fg = w.mmbuttonfg
	bprint.hoverfg = 'white'
	bprint.button.config(bg=bprint.idlebg, fg=bprint.fg)

	bstools.idlebg = w.mmbuttoncol
	bstools.fg = w.mmbuttonfg
	bstools.hoverfg = 'white'
	bstools.button.config(bg=bstools.idlebg, fg=bstools.fg)

	bexp.idlebg = w.mmbuttoncol
	bexp.fg = w.mmbuttonfg
	bexp.hoverfg = 'white'
	bexp.button.config(bg=bexp.idlebg, fg=bexp.fg)

	t.iconbitmap('RYB_Attendance.ico')
	t.mainloop()

import subprocess
cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

num_instances = 0

for line in proc.stdout:
	if b'RYB Student Attendance.exe' in line:
		num_instances += 1

if num_instances > 1:
	already_running_(languages['english'])
else:
	main()