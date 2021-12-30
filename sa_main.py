from sa import *
from gui import Window
import time


def main():
	import optparse
	usage_str = """
python sa_main.py <options>
EXAMPLES:	(1) python sa_main.py
			- starts a value with queen and size 8 board
		(2) python sa_main.py -s 10 -n nX
			- starts a value with bishop and size 10 board
	"""
	parser = optparse.OptionParser(usage_str)
	parser.add_option('-s', '--size', dest='size', type='int',
						help='width and height of the board', default=8)
	parser.add_option('-n', '--notation', dest='notation', type='str',
						help="Parlett's movement notation", default='n*')
	parser.add_option('-t', '--temp', dest='temp', type='float',
						help='initial temperature of the annealing', default=50)
	parser.add_option('-f', '--final', dest='final_temp', type='float',
						help='final temperature of the annealing', default=0.01)
	parser.add_option('-c', '--cooling', dest='cooling', type='str',
						help='cooling function of the temperature (linear, geometric, slow)', default='geometric')
	parser.add_option('-e', '--epoch', dest='iteration_per_temp', type='int',
						help='iteration per temperature decrease (epoch)', default=10)
	parser.add_option('-d', '--display', action='store_false', dest='display',
						help='not shows the path of the annealing', default=True)
	parser.add_option('-o', '--outline', action='store_false', dest='outline',
						help='not shows the outline of dominated space', default=True)
	parser.add_option('-r', '--framerate', dest='rate', type='int',
						help='framerate of the animation (ms)', default=0.01)

	(options, args) = parser.parse_args()
	size = options.size
	notation = options.notation
	temp = options.temp
	final_temp = options.final_temp
	cooling_name = options.cooling
	iteration_per_temp = options.iteration_per_temp
	display = options.display
	outline = options.outline
	rate = options.rate

	function = create_fairy_piece(notation)
	cooling = name_to_function(cooling_name)

	board, path = run(size=size, function=function, temp=temp, final_temp=final_temp, 
		cooling=cooling, iteration_per_temp=iteration_per_temp)

	if display:
		if outline:
			d = dominated_space(size, function)
			
		w = Window(name="Simulated Annealing")
		for i, elem in enumerate(path):
			if outline:
				domination = covers(elem, d)
			else:
				domination = None
			w.draw_board(elem, domination)
			time.sleep(rate)

		w.draw_board(board)
		w.mainloop()
	else:
		print(board)


if __name__ == '__main__':
	main()