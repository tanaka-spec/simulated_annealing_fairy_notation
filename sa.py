from piece import *
from board import Board
import math
import random


def dominated_space(size: int, function):
	output = [[0 for i in range(size)] for j in range(size)]
	for x in range(size):
		for y in range(size):
			output[x][y] = function(x, y, size)
	return output


def evaluation_function(board: Board, domination):
	v = len(board) # number of all the nodes
	
	# finding number of dominated nodes
	ps = set() 
	positions = board.position_piece()
	for x, y in positions:
		ps.update(domination[x][y])
	n = len(ps) # number of dominated nodes

	g = board.num_piece # number of piece on the board

	try:
		output = n / v + 1 / (g * v)
	except ZeroDivisionError:
		output = -float('inf')

	return output


def remove_piece(board: Board, domination):
	pick = []
	beta = 100 # something to divide it by to make it a whole number
	output = board.copy()
	positions = board.position_piece()
	for x, y in positions:
		probability = beta / len(domination[x][y])
		hold = [(x, y)] * int(round(probability))
		pick.extend(hold)
	x, y = random.choice(pick)
	output.remove(x, y)
	return output


def add_piece(board: Board, domination):
	pick = []
	beta = 100 # something to divide it by to make it a whole number
	output = board.copy()
	positions = board.position_piece()
	for x in range(board.size):
		for y in range(board.size):
			if (x, y) not in positions:
				probability = len(domination[x][y])
				hold = [(x, y)] * probability
				pick.extend(hold)
	x, y = random.choice(pick)
	output.add(x, y)
	return output


def swap_piece(board: Board, domination):
	while True:
		output = remove_piece(board, domination)
		output = add_piece(output, domination)
		if output != board:
			return output


def linear_reduction(t, alpha=1):
	return t - alpha


def geometric_reduction(t, alpha=0.99):
	return t * alpha


def slow_decrease(t, beta=0.99):
	return t / (1 + beta * t)


def name_to_function(name: str):
	if name == 'linear':
		return linear_reduction
	if name == 'slow':
		return slow_decrease
	return geometric_reduction


def run(size=8, function=queen, temp=10000, final_temp=0.0001, cooling=geometric_reduction, iteration_per_temp=10):
	board = Board(size=size)
	domination = dominated_space(size, function)
	path = [board]
	while temp > final_temp:
		for i in range(iteration_per_temp):
			e = evaluation_function(board, domination)

			if e >= 1: # node removing
				new_board = remove_piece(board, domination)
				new_e = evaluation_function(new_board, domination)
				delta_e = new_e - e
				if delta_e > 0:
					board = new_board
					continue
				
				p = math.exp(delta_e / temp)
				if random.random() < p:
					board = new_board

			else: # node addition or swapping
				new_board = add_piece(board, domination)
				new_e = evaluation_function(new_board, domination)
				
				if new_e > e: # node addition
					board = new_board
					continue

				if new_e < e: # node swapping
					new_board = swap_piece(board, domination)
					new_e = evaluation_function(new_board, domination)
					delta_e = new_e - e
					if delta_e > 0:
						board = new_board
						continue

				p = math.exp(delta_e / temp)
				if random.random() < p:
					board = new_board
			path.append(board)
		temp = cooling(temp)

	ps = set() # to check domination count
	positions = board.position_piece()
	for x, y in positions:
		ps.update(domination[x][y])
	n = len(ps) # number of dominated nodes
	print(n)

	return board, path

if __name__ == '__main__':
	board, path = run(size=10)
	print(board)

