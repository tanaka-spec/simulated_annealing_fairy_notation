from sa import *


def main():
	import optparse
	usageStr = """
	USAGE:      python sa_main.py <options>
	EXAMPLES:	(1) python sa_main.py
				- starts a value with queen and size 8 board
			(2) 
	"""
	parser = optparse.OptionParser(usageStr)
	parser.add_option('-s', '--size', dest='size', type='int',
						help='width and height of the board', default=8)
	parser.add_option('-n', '--notation', dest='notation', type='str',
						help="Parlett's movement notation", default='n*')
	parser.add_option('-t', '--temp', dest='temp', type='float',
						help='initial temperature of the annealing', default=10000)
	parser.add_option('-f', '--final', dest='final_temp', type='float',
						help='final temperature of the annealing', default=0.01)
	parser.add_option('-c', '--cooling', dest='cooling', type='str',
						help='cooling function of the temperature (linear, geometric, slow)', default='geometric')
	parser.add_option('-e', '--epoch', dest='iteration_per_temp', type='int',
						help='iteration per temperature decrease (epoch)', default=10)

	(options, args) = parser.parse_args()
	size = options.size
	notation = options.notation
	temp = options.temp
	final_temp = options.final_temp
	cooling_name = options.cooling
	iteration_per_temp = options.iteration_per_temp

	function = create_fairy_piece(notation)
	cooling = name_to_function(cooling_name)

	run(size=size, function=function, temp=temp, final_temp=final_temp, 
		cooling=cooling, iteration_per_temp=iteration_per_temp)


if __name__ == '__main__':
	main()