#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

class map_reduce(object):

    def __init__(self):
        pass

    def Load_data(self, dataset):
        agg_row = []
        with open(dataset) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print (row)
                agg_row.append([row[0], row[1]])
        return agg_row

    def Map(self, agg_row):
        print (agg_row)
        for row in agg_row:
            print ('%s\t%s' % (row, 1))

    def Reduce(self, agg_row):
        word = None
        word_dict = {}
        for index, row in enumerate(agg_row):
            word, count = row[0] + row[1], 1
            print (word, count)
            if word in word_dict:
                # if word already in word_list : count + 1 
                word_dict[word] += 1 
            else:
                # if word is not in word_list : add it with count = 1 
                word_dict[word] = 1 
        return word_dict

if __name__ == '__main__':
    mapreduce = map_reduce()
    agg_row = mapreduce.Load_data('map_reduce.csv')
    word_dict = mapreduce.Reduce(agg_row)
    print ('word_count : ', word_dict)
