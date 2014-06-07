from uiHandler22 import *
from dataHandler import *
from preBuilts2 import *
from tkinter import filedialog
from random import randrange
import os

def main(lang, d):

	def odb():
		try:
			w.fpath.setData(filedialog.askopenfile(mode='r').name)
		except:
			pass

#		nd = StudentDB(file='temp.db')

	def sp():
		w.frames["First Frame"].grid()
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()

		w.frames["Fourth Frame"].grid_forget()
		w.frames["Fifth Frame"].grid_forget()
		w.frames["Sixth Frame"].grid_forget()

	def pvdb():
		try:
			w.randfile = 'temp' + str(randrange(0, 10000)) + '.db'
			nd = StudentDB(file=w.randfile, cfile='')
			nd.importxlsx(fpath.getData())

			w.sL = []
			for s in nd.studentList.values():
				dp = s.datapoints
				w.sL.append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

			w.sL.sort()


			w.frames["First Frame"].grid_forget()
			w.frames["Second Frame"].grid_forget()
			w.frames["Third Frame"].grid_forget()

			w.frames["Fourth Frame"].grid()
			w.frames["Fifth Frame"].grid()
			w.frames["Sixth Frame"].grid()

			
			w.stable.setData((w.stableh, w.sL))
			w.stable.canvas.config(width=700)
		except:
			noimp(w.lang)

	def pdb():
		try:
			fpath2.setData(filedialog.asksaveasfilename())
		except:
			pass

	def sav():
		f = fpath2.getData().split('/')[-1] + '.db'
		nd = StudentDB(file=f, cfile='')
		
		if f == '.db':
			pchoosefile(w.lang)
			return

		nd.importxlsx(fpath.getData())
		os.remove(w.randfile)
		t.destroy()



	d.loadData()

	t = Window(top=True)
	t.geometry('900x500')
	t.attributes('-fullscreen', False)
	t.focus_set()
	t.grab_set()

	w = AppWindow(t.mainFrame)

	w.lang = lang

	w.sL = []

	w.stable = stable
	w.stableh = [w.lang['Barcode'], w.lang['First Name'], \
		w.lang['Last Name'], w.lang['Chinese Name'], w.lang['Date of Birth']]
	w.stable.build(headers=w.stableh, data=[[]])

#frame initialization
	w.newFrame("L Frame", (0, 0))
	w.newFrame("First Frame", (1, 0))
	w.newFrame("Second Frame", (2, 0))
	w.newFrame("Third Frame", (3, 0))
	w.newFrame("Sixth Frame", (3, 0))
	w.newFrame("Fourth Frame", (4, 0))
	w.newFrame("Fifth Frame", (5, 0))

#hide next frame
	w.frames["Fourth Frame"].grid_forget()
	w.frames["Fifth Frame"].grid_forget()
	w.frames["Sixth Frame"].grid_forget()


	Label(w.frames["First Frame"], text="Welcome to the Import wizard.\n\n\nPlease select the xls or xlsx file below.\nThen click Next.", justify=LEFT).grid()

	w.fpath = fpath

#intialize widgets
	w.bsav = bsav

	w.frames["Second Frame"].addWidget(w.fpath, (0, 0))
	w.frames["Second Frame"].addWidget(brw, (0, 3))
	w.frames["Third Frame"].addWidget(nxt, (0, 1))
	w.frames["Fourth Frame"].addWidget(w.stable, (0, 0))
	w.frames["Fifth Frame"].addWidget(fpath2, (0, 0))
	w.frames["Fifth Frame"].addWidget(brw2, (0, 3))
	w.frames["Fifth Frame"].addWidget(sepr, (1, 0))
	w.frames["Sixth Frame"].addWidget(bk, (2, 0))
	w.frames["Sixth Frame"].addWidget(w.bsav, (2, 1))

	bcancel1 = Buttonbox(text='Cancel', lang=w.lang, repr='cancel')
	bcancel2 = Buttonbox(text='Cancel', lang=w.lang, repr='cancel')

	w.frames["Third Frame"].addWidget(bcancel1, (0, 2))
	w.frames["Sixth Frame"].addWidget(bcancel2, (2, 2))

	brw.config(cmd=odb)
	brw2.config(cmd=pdb)
	bk.config(cmd=sp)
	nxt.config(cmd=pvdb)
	w.bsav.config(cmd=sav)
	bcancel1.config(cmd=t.destroy)
	bcancel2.config(cmd=t.destroy)

	brw.button.config(width=12)
	brw.button.grid(padx=10)
	brw2.button.config(width=12)
	brw2.button.grid(padx=10)
	bk.button.config(width=10)
	bk.button.grid(padx=10)
	nxt.button.config(width=10)
	nxt.button.grid(padx=10)
	w.bsav.button.config(width=10)
	w.bsav.button.grid(padx=10)
	bcancel1.button.config(width=10)
	bcancel1.button.grid(padx=10)
	bcancel2.button.config(width=10)
	bcancel2.button.grid(padx=10)

#set starting lang
	for frame in w.frames.values():
		for widget in frame.widgets.values():
			widget.config(lang=w.lang)

	
	t.mainloop()

if __name__ == '__main__':
	print(randrange(0, 10000))
	main(language)
