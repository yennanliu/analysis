#!/bin/sh


echo 'plz make sure you are using python 3 '
echo ''
echo '--------------------------------'
# install python 3 env 
echo 'install needed packages....'
echo ''
echo '--------------------------------'

#pip install pandas numpy 


# make sure needed data exist (csv)


# create needed files (if no exist)
echo 'create needed folders....'
echo ''
echo '--------------------------------'


mkdir output
mkdir data


# make sure needed csv are in the files 
echo 'check needed data....'
echo ''
echo '--------------------------------'



# get current csv in /data as list 
current_csv_list=(data/*)
#echo ${current_csv_list[@]}

# set needed csv as list 
needed_csv_list=('data/ATO.csv' 
				'data/All_CustomersExcCorporateAccounts.csv' 
				'data/CityPostcodecsv.csv'
				'data/Latebycollectionanddelivery.csv'
				'data/NoofTickets.csv'
				'data/RecleanedOrders.csv'
				'data/Top_Products.csv'
				'data/cancalledOrders.csv'
				'data/voucherused.csv' )

# for loop check if needed csv exist 
for (( k=0 ; k <${#current_csv_list[@]}; ++k ));
	do 

		for (( k=0 ; k <${#needed_csv_list[@]}; ++k ));

			do
				if [[ "${current_csv_list[k]}" = "${needed_csv_list[k]}" ]]; then
					#echo "${current_csv_list[k]}" 'match !'
					echo ' file exist OK... '  "${current_csv_list[k]}"
				fi 

				if [[ "${current_csv_list[k]}" != "${needed_csv_list[k]}" ]]; then
					echo "${current_csv_list[k]}" 'not found !'
				fi 


			done 

	done 
















