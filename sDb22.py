from uiHandler22 import *
import editS2
from dataHandler import *
from preBuilts2 import *


def main(t, lang, d):

#
	d.loadData()

	w = AppWindow(t)

	w.lang = lang

#sT
	w.sT = Table(repr='stable', edit=False)
	stableh = [language['Barcode'], language['First Name'], \
	language['Last Name'], language['Chinese Name'], language['Date of Birth']]
	w.sT.build(headers=stableh, data=[[]])

	def sTbind(f):
		def fsb(p):
			i = w.sT.data[p[0]-1][0]
			try:
				f(i)
			except:
				print(w.sT.data[p[0]-1][0])

		try:
			for pos, cell in w.sT.cells.items():
				cell.config(bind=('<Double-Button-1>', lambda event, pos=pos: fsb(pos)))
		except:
			print("cells could not be bound")

#
	w.newFrame("First Frame", (0, 0))
	w.newFrame("Second Frame", (1, 0))
	w.newFrame("Third Frame", (1, 1))
	w.newFrame("Fourth Frame", (3, 1))
	w.newFrame("Fifth Frame", (2, 0))

#
	w.frames["Fifth Frame"].grid(columnspan=3)

#widget for scan
	w.frames["First Frame"].addWidget(sby, (0, 0))
	w.frames["First Frame"].addWidget(bsearch, (1, 0))
	
#buttons for scrolling db
	fward = Buttonbox(text='>> Next 30 >>', lang=w.lang, repr='>>')
	bward = Buttonbox(text='<< Previous 30 <<', lang=w.lang, repr='<<')
	w.frames["Fifth Frame"].addWidget(fward, (1, 1))
	w.frames["Fifth Frame"].addWidget(bward, (1, 0))


	w.frames["Second Frame"].addWidget(w.sT, (2, 0))

	sby.rads=[('Barcode', 'bCode'), ('First Name', 'firstName'), ('Last Name', 'lastName'), ('Chinese Name', 'chineseName')]

	sL = [[]]
	for s in d.studentList.values():
		dp = s.datapoints
		sL[0].append([dp['bCode'], dp['firstName'], dp['lastName'], dp['chineseName'], dp['dob']])

	sL[0].sort()

#create pages
	#print(len(sL[0]))
	if len(sL[0]) > 30:
		l = []
		for s in sL[0]:
			l.append(s)
			if len(l) >= 30:
				sL.append(l)
				l = []
		sL.append(l)

	w.pNum = 1

		
	def toPage(p):
		#temp workaround while table is fixed
		for child in w.frames["Second Frame"].winfo_children():
			child.destroy()

		w.sT.build(headers=stableh, data=sL[p])
		w.frames["Second Frame"].addWidget(w.sT, (2, 0))
		w.sT.canvas.config(width=700, height=700)
		sTbind(lambda i: editS2.main(w.lang, top=True, i=i, d=d))
		
		#w.sT.setData((stableh, sL[p]))
		#w.sT.canvas.config(width=700, height=700)
		#sTbind(lambda i: editS2.main(w.lang, top=True, i=i, d=d))

	def f():
		if w.pNum == len(sL) - 1: return
		toPage(w.pNum + 1)
		w.pNum = w.pNum + 1
		
	def b():
		if w.pNum == 1: return
		toPage(w.pNum - 1)
		w.pNum = w.pNum - 1
		

	if len(sL[0]) > 30:
		toPage(1)
		fward.config(cmd=f)
		bward.config(cmd=b)
	else:
		toPage(0)
#
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

			print(w.s)
			editS2.main(w.lang, d=d, top=True, i=w.s)
		except:
			nos(w.lang)
			return


	w.frames["First Frame"].widgets['sby'].entry.bind("<Return>", lambda x: s())

	bsearch.button.config(width=20)
	bsearch.config(cmd=s)

	#button for scan
	#Button(w.frames["First Frame"], text="try", command=s).grid()




if __name__ == '__main__':
	t = Window()
	main(t, language)

	t.mainloop()


