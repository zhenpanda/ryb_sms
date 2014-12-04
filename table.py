'''


'''
from tkinter import *


class QuickTable:

	def __init__(self, parent, grid_row, grid_column):

		self.selfframe = Frame(parent)
		self.selfframe.grid(row=grid_row, column=grid_column)

		self.canvas = Canvas(self.selfframe)
		self.canvas.pack()

		self.rows = {}
		self.cells = {}

		self.row = 0

	def setData(self, data):

		for row in data:
			row_frame = Frame()
			row_frame.pack()
			self.rows[self.row] = row_frame
			col = 0
			for cell_data in row:
				cell = Label(row_frame, text=cell_data)
				cell.pack()
				self.cells[(self.row, col)] = cell
				col += 1
			self.row += 1

	def getData(self):
		return

	def addRow(self, data):

		row_frame = Frame()
		row_frame.pack()
		self.rows[self.row] = row_frame
		col = 0
		for cell_data in data:
			cell = Label(row_frame, text=cell_data)
			cell.pack()
			self.cells[(self.row, col)] = cell
			col += 1
		self.row += 1

	def set_column_width(self, column_num, width):

		for cell_id, cell in self.cells.items():
			if cell_id[1] == column_num:
				cell.config(width=width)

	#def place(self, )