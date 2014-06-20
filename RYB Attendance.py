from tkinter import *
from uiHandler22 import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
from photoWidget2 import *
from preBuilts2 import ret, titlePic
import addS3
import scanS22
import sDb22
import tools2

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

#confirm closing of the add student window
	t.con = False

#show and hide sub-windows
	def showWindow(f):
		try:
			w.frames["Title Frame"].grid_forget()
			w.frames["First Frame"].grid_forget()
			if (f.__doc__) == 'addS3':
				t.con = True
				w.t = f(w.frames["Second Frame"], w.lang, w.d, showMain)
			else:
				t.con = False
				w.t = f(w.frames["Second Frame"], w.lang, w.d)
			w.frames["Second Frame"].grid()
			w.frames["Third Frame"].grid()
		except:
			print('unknown error', 'error in function showWindow', f.__doc__)

#show and hide main window
	def showMain(con):
		if con:
			if not ret('a', w.lang): return

		w.frames['Second Frame'].grid_forget()
		print('called')
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

		w.frames["Title Frame"].grid(row=0, columnspan=4, sticky=E+W, pady=20)

		w.k.files['cfilepath'] = w.d.file
		w.k.save()
		

#main window and starting language
	w = AppWindow(t.mainFrame)
	w.lang = languages['chinese']

#load current database
	w.k = keeper.Keeper('keeper.db')
	w.d = StudentDB(file=w.k.files['cfilepath'], cfile=w.k.fname)

#frame creation and positions
	w.newFrame("Title Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (3, 0))

#experimental material
	#to create background on title frame
	#current limitation: frame scaling according to window size change
	#title
	#titleImg = ImageTk.PhotoImage(titlePic)
	w.frames["Title Frame"].grid(columnspan=4, sticky=E+W)
	Label(w.frames["Title Frame"], text=w.lang['RYB Student Management'], bg='#3B5C8D', fg='white', \
		height=3, font=('Jumbo', '12', 'bold')).pack(fill='both', expand=True)

#hide sub-frames
	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

#buttons to call sub-windows
	bsadd = Buttonbox(text='Add Students', lang=w.lang, repr='bsadd') #Add Student
	bsscan = Buttonbox(text='Scan Students', lang=w.lang, repr='bsscan') #Scan Student
	bssdb = Buttonbox(text='Student Database', lang=w.lang, repr='bssdb') #Student Database
	bstools = Buttonbox(text='Tools', lang=w.lang, repr='bstools') #Database Management
	bsbmm = Buttonbox(text='Back to Main Menu', lang=w.lang, repr='bsbmm') #Return to Main Menu
	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit') #Exit
	bclang = Buttonbox(text='changelanguage', lang=w.lang, repr='bclang') #Change Language

#background image
	w.p = Photo(repr='splash', path='background_IMG.jpg')

#place buttons and background image
	w.frames["First Frame"].addWidget(bsadd, (0, 0))
	w.frames["First Frame"].addWidget(bsscan, (1, 0))
	w.frames["First Frame"].addWidget(bssdb, (2, 0))
	w.frames["First Frame"].addWidget(bstools, (3, 0))
	w.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	w.frames["First Frame"].addWidget(bsexit, (5, 0))
	w.frames["First Frame"].addWidget(bclang, (4, 0))
	w.frames["First Frame"].addWidget(w.p, (0, 2))
	Label(w.frames["First Frame"], text='  ').grid(column=1) #separator between buttons and background image

#set commands for each button
	bsadd.config(cmd=lambda: showWindow(addS3.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=lambda: showMain(t.con))
	bsexit.config(cmd=t.destroy)
	bclang.config(cmd=clang)
	bstools.selfframe.grid_forget()
	#secret configuration to call Database Management
	w.p.label.bind('<Control-Alt-Shift-D>', lambda e: showWindow(tools2.main))

	w.p.label.grid(rowspan=100, sticky=E)

#experimental button
	#custom X button
	#t.exit.bind('<ButtonRelease-1>', lambda e: t.destroy())

	#showWindow(tools2.main)
	#showMain(False)

	w.frames['Title Frame'].grid_forget()

	t.mainloop()


if __name__ == '__main__':
	main()	