# python 3  



# time complexity :  O(nlogn)
def funcV2(array):
	return sorted(array, key=lambda k: k['data']['price']) 

 
my_array = [{'id': 1, 'data': {'price': 100.00, 'date': '1980-01-01', 'zipcode': 'SE65L8'}},
            {'id': 2, 'data': {'price': 40.00, 'date': '1981-01-01', 'zipcode': 'SE65L9'}}, 
            {'id': 3, 'data': {'price': 130.00, 'date': '1985-01-01', 'zipcode': 'SE65L10'}}]







	 