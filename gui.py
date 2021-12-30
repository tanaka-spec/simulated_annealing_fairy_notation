import tkinter as tk
from board import Board


class Window():
	def __init__(self, name='tk',width=500):
		self.root = tk.Tk()
		self.root.title(name)
		self.width = width
		self.canvas = tk.Canvas(self.root, height=width, width=width)
		self.canvas.pack()


	def draw_board(self, board: Board, dominance=None):
		self.canvas.delete("all")
		length = self.width / board.size
		color = 'black'
		for y in range(board.size):
			for x in range(board.size):
				x1 = x * length
				y1 = y * length
				x2 = x1 + length
				y2 = y1 + length

				if dominance is not None and (x, y) in dominance:
					outline = 'red'
				else:
					outline = color

				self.canvas.create_rectangle((x1, y1, x2, y2), fill=color, outline=outline)

				if board.piece_exist(x, y):
					self.canvas.create_oval((x1, y1, x2, y2), fill="yellow")

				if color == 'white':
					color = 'black'
				else:    
					color = 'white'
			if color == 'white':
				color = 'black'
			else:    
				color = 'white'
		self.root.update()


	def mainloop(self):
		self.root.mainloop()
