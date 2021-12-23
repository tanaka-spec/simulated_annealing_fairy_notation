class Board:
	def __init__(self, size=8):
		self.size = size
		self.array = [[0 for i in range(size)] for j in range(size)]
		self.num_piece = 0


	def __str__(self):
		return str(self.array)


	def __len__(self):
		return self.size ** 2


	def __eq__(self, other):
		if type(self) != type(other) or self.size != other.size or self.num_piece != other.num_piece:
			return False
		for i in range(self.size):
			for j in range(self.size):
				if self.array[i][j] != other.array[i][j]:
					return False
		return True


	def place_board(self, pieces: list):
		self.reset_board()
		for i, j in pieces:
			if 0 <= i < self.size and 0 <= j < self.size:
				self.num_piece += 1
				self.array[i][j] = 1
		return


	def reset_board(self):
		self.array = [[0 for i in range(self.size)] for j in range(self.size)]
		self.num_piece = 0
		return


	def position_piece(self):
		output = []
		for i in range(self.size):
			for j in range(self.size):
				if self.array[i][j] == 1:
					output.append((i, j))
		return output


	def remove(self, x, y):
		if self.array[x][y] == 1:
			self.array[x][y] = 0
			self.num_piece -= 1
		else:
			error('Removing values not on board!')
		return


	def add(self, x, y):
		if self.array[x][y] == 0:
			self.array[x][y] = 1
			self.num_piece += 1
		else:
			error('Adding values not on board!')
		return


	def copy(self):
		output = Board(size=self.size)
		output.size = self.size
		output.num_piece = self.num_piece

		for i in range(self.size):
			output.array[i] = self.array[i].copy()
		return output


if __name__ == '__main__':
	hl = Board()
	hl.place_board([(0, 4),(1,6),(2,1),(3,5),(4,2),(-1,0),(1,3),(-10,7)])
	print(hl)