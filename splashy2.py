from tkinter import *
from uiHandler22 import *
from dataHandler import *
from languages import *
from labelWidgets2 import *
from photoWidget2 import *
from preBuilts2 import ret
import addS3
import scanS22
import sDb22
import tools2

def main():

#clang
	def clang():
		if w.lang['self'] == 'english':
			w.lang = languages['chinese']
		else:
			w.lang = languages['english']
		for frame in w.frames.values():
			for widget in frame.widgets.values():
				widget.config(lang=w.lang)


	t = Window(top=False)

	t.con = False

	def showWindow(f):
		if (f.__doc__) == 'addS3': t.con = True
		else: t.con = False
		w.frames["First Frame"].grid_forget()
		w.t = f(w.frames["Second Frame"], w.lang, w.d)
		w.frames["Second Frame"].grid()
		w.frames["Third Frame"].grid()


	def showMain():
		if t.con:
			if not ret('a', w.lang): return

		w.frames['Second Frame'].grid_forget()
		try:
			w.t.destroy()
		except:
			pass
		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.frames['Second Frame'].destroy()
		w.newFrame("Second Frame", (1, 0))
		w.frames['Second Frame'].grid_forget()

		w.frames["First Frame"].grid()
		w.frames['Third Frame'].grid_forget()

		w.k.files['cfilepath'] = w.d.file
		w.k.save()
		


	w = AppWindow(t.mainFrame)
	w.lang = languages['english']

	w.k = keeper.Keeper('keeper.db')
	w.d = StudentDB(file=w.k.files['cfilepath'], cfile=w.k.fname)


	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (2, 0))


	w.frames['Second Frame'].grid_forget()
	w.frames['Third Frame'].grid_forget()

	bsadd = Buttonbox(text='Add Students', lang=w.lang, repr='bsadd')
	bsscan = Buttonbox(text='Scan Students', lang=w.lang, repr='bsscan')
	bssdb = Buttonbox(text='Student Database', lang=w.lang, repr='bssdb')
	bstools = Buttonbox(text='Tools', lang=w.lang, repr='bstools')
	bsbmm = Buttonbox(text='Back to Main Menu', lang=w.lang, repr='bsbmm')
	bsexit = Buttonbox(text='Exit', lang=w.lang, repr='bsexit')
	bclang = Buttonbox(text='changelanguage', lang=w.lang, repr='bclang')

	w.p = Photo(repr='splash', path='icc.jpg')

	w.frames["First Frame"].addWidget(bsadd, (0, 0))
	w.frames["First Frame"].addWidget(bsscan, (1, 0))
	w.frames["First Frame"].addWidget(bssdb, (2, 0))
	w.frames["First Frame"].addWidget(bstools, (3, 0))
	w.frames["Third Frame"].addWidget(bsbmm, (0, 0))
	w.frames["First Frame"].addWidget(bsexit, (5, 0))
	w.frames["First Frame"].addWidget(bclang, (4, 0))
	w.frames["First Frame"].addWidget(w.p, (0, 1))
	
	bsadd.config(cmd=lambda: showWindow(addS3.main))
	bsscan.config(cmd=lambda: showWindow(scanS22.main))
	bssdb.config(cmd=lambda: showWindow(sDb22.main))
	bstools.config(cmd=lambda: showWindow(tools2.main))
	bsbmm.config(cmd=showMain)
	bsexit.config(cmd=t.destroy)
	bclang.config(cmd=clang)

	w.p.label.grid(rowspan=100, padx=20)
	
	
	t.mainloop()


if __name__ == '__main__':
	main()

	