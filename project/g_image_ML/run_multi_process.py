# python 3 

import argparse
import os                                                                       
from multiprocessing import Pool                                                
       

print ('*'*70)
print (' run "python run_multi_process.py  --h" for help msg ')
print ('*'*70)



# ----------------------------------------------
# get args 
parser = argparse.ArgumentParser()
parser.add_argument('--process', required=True, help='How many processes plan to run on the same time')
args = parser.parse_args()
process  = args.process 
# ----------------------------------------------




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
