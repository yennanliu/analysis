
import seaborn as sns
import matplotlib.pyplot as plt
%pylab inline 
import pandas as pd , numpy as np 

column = ['Condition Code', 'Extension number', 'Trunk line number',
'Telephone number', 'Ring time', 'Date', 'Start time of a call', 'Duration Talk time',
'Account Code', 'Reverse polarity detection', 'The end of jump']

# read the data 

df = pd.read_csv('~/Desktop/phone_record.txt' , names = column, sep= '|')
df = df.replace(r'^\s+$', np.nan, regex=True)


# analyze the data with 'Condition Code' == "OE"
Outgoing_End_date = df[df['Condition Code'] == "OE"]
Outgoing_End_date = Outgoing_End_date[['Condition Code','Date', 'Start time of a call', 'Telephone number', 'Extension number']]
Outgoing_End_hh = df[df['Condition Code'] == "OE"]
Outgoing_End_hh = Outgoing_End_hh[['Date',  'Extension number', 'Start time of a call']]
new = []
for item in Outgoing_End_hh['Start time of a call']:
	new.append( str(item[0:2]))

Outgoing_End_hh['hh'] =  new 
Outgoing_End_hh.Date = pd.to_datetime(Outgoing_End_hh.Date)
first = Outgoing_End_hh['Date']
second = Outgoing_End_hh['hh']
Outgoing_End_hh['Date'] = [x.strftime('%Y-%m-%d ') + y for x, y in zip(first, second)]

Outgoing_End_hh.Date = pd.to_datetime(Outgoing_End_hh.Date)
Outgoing_End_hh  =  Outgoing_End_hh  
dfc = Outgoing_End_hh.groupby(['Date','Extension number']).count().reset_index()
dfc = dfc.drop('hh', 1)
dfp=dfc.pivot(index="Date",columns="Extension number")
dfp = dfp.replace('NaN', 0 )


dfp.plot(figsize = (15,5), stacked= True )
dfp
dfp.columns = dfp.columns.get_level_values(1)


Incoming_End_date = df[df['Condition Code'] == "IE"]
Incoming_End_date = Incoming_End_date[['Condition Code','Date', 'Start time of a call', 'Telephone number', 'Extension number','Ring time','Duration Talk time']]
Incoming_End_date = Incoming_End_date[Incoming_End_date.Date != 'OE']



Incoming_End_date['Date'] = Incoming_End_date['Date'].astype(datetime64)
Incoming_End_hh = Incoming_End_date[['Date',  'Extension number', 'Start time of a call']]


new = []
for j in Incoming_End_hh['Start time of a call']:
	new.append( str(j[0:2]))

Incoming_End_hh['hh'] =  new 
first = Incoming_End_hh['Date']
second = Incoming_End_hh['hh']
Incoming_End_hh['Date'] = [x.strftime('%Y-%m-%d ') + y for x, y in zip(first, second)]

Incoming_End_hh.Date = pd.to_datetime(Incoming_End_hh.Date)

dd  =  Incoming_End_hh 
dfc = dd.groupby(['Date','Extension number']).count().reset_index()
dfc = dfc.drop('hh', 1)
dfp=dfc.pivot(index="Date",columns="Extension number")
dfp = dfp.replace('NaN', 0 )
dfp.plot(figsize = (15,5), stacked= True)
dfp.columns = dfp.columns.get_level_values(1)
dfp 











