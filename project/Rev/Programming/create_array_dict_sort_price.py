# python 3  



# time complexity :  O(N)
def funcV1(array):
	order_price = []
	output = []

	for i in array:
		#print (i['data']['price'])
		order_price.append(i['data']['price'])
		order_price = sorted(order_price)
	for i in range(len(order_price)):
		if array[i]['data']['price']  == order_price[i]:
			output.append(array[i])
		else:
			pass
	return  output
    



my_array = [{'id': 879, 'data': {'price': 18.90, 'date': '1980-01-01', 'zipcode': 'SE65L8'}},
            {'id': 981, 'data': {'price': 19.00, 'date': '1981-01-01', 'zipcode': 'SE65L9'}}, 
            {'id': 752, 'data': {'price': 20.00, 'date': '1985-01-01', 'zipcode': 'SE65L10'}}]

















	 