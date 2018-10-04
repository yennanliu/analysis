# python 3 

import os                                                                       
from multiprocessing import Pool                                                
       

def run_process(process):                                                             
	os.system('python {}'.format(process))                                       

def collect_processes():
	return processes 


def main(processes):
	processes = ()
	pool = Pool(processes=processes)                                                        
	pool.map(run_process, processes)


if __name__ == '__main__':
	main()
