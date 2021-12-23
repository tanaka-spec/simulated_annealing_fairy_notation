import re


def diagonal(x, y, size, limit1=-1, limit2=-1, limit3=-1, limit4=-1):
	output = set()
	
	output.add((x, y))

	if limit1 == -1:
		limit1 = size
	for i in range(1, limit1 + 1): # left-up
		if 0 <= x - i < size and 0 <= y - i < size: 
			output.add((x - i, y - i))

	if limit2 == -1:
		limit2 = size
	for i in range(1, limit2 + 1): # right-up
		if 0 <= x + i < size and 0 <= y - i < size: 
			output.add((x + i, y - i))

	if limit3 == -1:
		limit3 = size
	for i in range(1, limit3 + 1): # left-down
		if 0 <= x - i < size and 0 <= y + i < size: 
			output.add((x - i, y + i))

	if limit4 == -1:
		limit4 = size
	for i in range(1, limit4 + 1): # right-down
		if 0 <= x + i < size and 0 <= y + i < size: 
			output.add((x + i, y + i))

	return output


def lateral(x, y, size, limit1=-1, limit2=-1, limit3=-1, limit4=-1):
	output = set()
	
	output.add((x, y))

	if limit1 == -1:
		limit1 = size
	for i in range(1, limit1 + 1): # up
		if 0 <= x < size and 0 <= y - i < size: 
			output.add((x, y - i))

	if limit2 == -1:
		limit2 = size
	for i in range(1, limit2 + 1): # right
		if 0 <= x + i < size and 0 <= y < size: 
			output.add((x + i, y))

	if limit3 == -1:
		limit3 = size
	for i in range(1, limit3 + 1): # down
		if 0 <= x < size and 0 <= y + i < size: 
			output.add((x, y + i))

	if limit4 == -1:
		limit4 = size
	for i in range(1, limit4 + 1): # left
		if 0 <= x - i < size and 0 <= y < size: 
			output.add((x - i, y))

	return output


def leap_diagonal(x, y, size, limit1, limit2, limit3, limit4):
	output = set()

	output.add((x, y))
	if 0 <= x - limit1 < size and 0 <= y - limit1 < size: # up
		output.add((x - limit1, y - limit1))

	if 0 <= x + limit2 < size and 0 <= y - limit2 < size: # right
		output.add((x + limit2, y - limit2))

	if 0 <= x - limit3 < size and 0 <= y + limit3 < size: # down 
		output.add((x - limit3, y + limit3))

	if 0 <= x + limit4 < size and 0 <= y + limit4 < size: 
		output.add((x + limit4, y + limit4))

	return output


def leap_lateral(x, y, size, limit1, limit2, limit3, limit4):
	output = set()

	output.add((x, y))
	if 0 <= x < size and 0 <= y - limit1 < size: # up
		output.add((x, y - limit1))

	if 0 <= x + limit2 < size and 0 <= y < size: # right
		output.add((x + limit2, y))

	if 0 <= x - limit3 < size and 0 <= y + limit3 < size: # down 
		output.add((x, y + limit3))

	if 0 <= x - limit4 < size and 0 <= y < size: 
		output.add((x - limit4, y))

	return output


def queen(x, y, size):
	output = set()
	output.update(diagonal(x, y, size))
	output.update(lateral(x, y, size))
	return output


def create_fairy_piece(notation: str):
	notations = notation.split(', ')
	def fairy_piece(x, y, size):
		output = set()
		for n in notations:
			# orthogonally or diagonally (all eight possible directions)
			if n == 'n*':
				output.update(queen(x, y, size))
			elif re.search(r"[1-9][0-9]*\*$", n):
				limit = int(n[:-1])
				output.update(diagonal(x, y, size, limit1=limit, limit2=limit, limit3=limit, limit4=limit))
				output.update(lateral(x, y, size, limit1=limit, limit2=limit, limit3=limit, limit4=limit))

			# orthogonally (four possible directions)
			elif n == 'n+':
				output.update(lateral(x, y, size))
			elif re.search(r"[1-9][0-9]*\+$", n):
				limit = int(n[:-1])
				output.update(lateral(x, y, size, limit1=limit, limit2=limit, limit3=limit, limit4=limit))

			# orthogonally forwards
			elif n == 'n>':
				output.update(lateral(x, y, size, limit2=0, limit3=0, limit4=0))
			elif re.search(r"[1-9][0-9]*>$", n):
				limit = int(n[:-1])
				output.update(lateral(x, y, size, limit1=limit, limit2=0, limit3=0, limit4=0))

			# orthogonally backwards
			elif n == 'n<':
				output.update(lateral(x, y, size, limit1=0, limit2=0, limit4=0))
			elif re.search(r"[1-9][0-9]*>$", n):
				limit = int(n[:-1])
				output.update(lateral(x, y, size, limit1=0, limit2=0, limit3=limit, limit4=0))

			# orthogonally forwards and backwards
			elif n == 'n<>':
				output.update(lateral(x, y, size, limit2=0, limit4=0))
			elif re.search(r"[1-9][0-9]*<>$", n):
				limit = int(n[:-2])
				output.update(lateral(x, y, size, limit1=limit, limit2=0, limit3=limit, limit4=0))

			# orthogonally sideways (used here instead of Parlett's divide symbol.)
			elif n == 'n=':
				output.update(lateral(x, y, size, limit1=0, limit3=0))
			elif re.search(r"[1-9][0-9]*=$", n):
				limit = int(n[:-1])
				output.update(lateral(x, y, size, limit1=0, limit2=limit, limit3=0, limit4=limit))

			# orthogonally forwards or sideways
			elif n == 'n>=':
				output.update(lateral(x, y, size, limit3=0))
			elif re.search(r"[1-9][0-9]*>=$", n):
				limit = int(n[:-2])
				output.update(lateral(x, y, size, limit1=limit, limit2=limit, limit3=0, limit4=limit))

			# orthogonally backwards or sideways
			elif n == 'n<=':
				output.update(lateral(x, y, size, limit1=0))
			elif re.search(r"[1-9][0-9]*<=$", n):
				limit = int(n[:-2])
				output.update(lateral(x, y, size, limit1=0, limit2=limit, limit3=limit, limit4=limit))

			# diagonally (four possible directions)
			elif n == 'nX':
				output.update(diagonal(x, y, size))
			elif re.search(r"[1-9][0-9]*X$", n):
				limit = int(n[:-1])
				output.update(diagonal(x, y, size, limit1=limit, limit2=limit, limit3=limit, limit4=limit))

			# diagonally forwards
			elif n == 'nX>':
				output.update(diagonal(x, y, size, limit3=0, limit4=0))
			elif re.search(r"[1-9][0-9]*X>$", n):
				limit = int(n[:-2])
				output.update(diagonal(x, y, size, limit1=limit, limit2=limit, limit3=0, limit4=0))

			# diagonally backwards
			elif n == 'nX<':
				output.update(diagonal(x, y, size, limit1=0, limit2=0))
			elif re.search(r"[1-9][0-9]*X<$", n):
				limit = int(n[:-2])
				output.update(diagonal(x, y, size, limit1=0, limit2=0, limit3=limit, limit4=limit))
		return output
	return fairy_piece