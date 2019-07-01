import csv 

class map_reduce(object):

	def __init__(self):
		pass 

	def load_data(self, dataset):
		agg_row = []
		with open(dataset) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				print (row)
				agg_row.append(row[0])
		return agg_row 

	def map(self, agg_row):
		print (agg_row)
		for row in agg_row:
			print ('%s\t%s' % (row, 1))

	def reduce(self, agg_row):
		current_word = None
		current_count = 0 
		word = None 
		for row in agg_row:
			#word, count = row.split('\t', 1)
			word, count = row.split('\t', 1)[0], 1 
			print (word, count)
			if word == current_word:
				current_count = current_count + count 
			else:
				if current_word:
					print ('%s\t%s' % (current_word, current_count))
			current_count = count 
			current_word = word 
		if current_word == word:
			print ('%s\t%s' % (current_word, current_count))

if __name__ == '__main__':
	mapreduce = map_reduce()
	agg_row = mapreduce.load_data('map_reduce.csv')
	#mapreduce.map(agg_row)
	mapreduce.reduce(agg_row)
