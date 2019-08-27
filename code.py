import pandas as pd#importing the data
import datetime
import csv
import numpy as np
from pandas import Series
from matplotlib import pyplot
from datetime import datetime, timedelta#from datetime import datetime

#reading csv file
data = pd.read_csv('Desktop\Power-Networks-LCL.csv')

#getting LCLid 
household_id =  data['LCLid']

#changing the date datatype
date_datetime = data['DateTime']
data_datetime = pd.Series(date_datetime)
data_datetime = pd.to_datetime(date_datetime)

#converting kwh column into float32
data_kwh = np.float32(data['KWh'])

#getting acorn
Acorn = data['Acorn']

#getting acorn_groups
Acorn_groups =  data['Acorn_grouped']

#values for  each variables
l = 1
m = 2
k = 3

#forming lsit for all values
column_0 = []
column_1 = []
column_2 = []
column_3 = []
column_4 = []
    
#checking the time and converting into the hourly basis
for i in range(1,len(data_datetime),2):
    
    time_xc = datetime.strptime(str(data_datetime[l]),'%Y-%m-%d %H:%M:%S')
    time_yc = datetime.strptime(str(data_datetime[m]),'%Y-%m-%d %H:%M:%S')
    time_zc = datetime.strptime(str(data_datetime[k]),'%Y-%m-%d %H:%M:%S')
    
    time_def = time_yc - time_xc#finding timing intervel between two times
    time_def = str(time_def)
    time_comp = time_zc - time_yc#finding timing interval between two times
    time_comp = str(time_comp)
    
    #checking the time interval    
    if time_def == '0:30:00' and time_comp == '0:30:00':
        time_def = datetime.strptime(str(time_def),'%H:%M:%S')
        ai = time_xc + timedelta(hours = time_def.hour, minutes=time_def.minute, seconds=time_def.second)#Date and time is added 
        ae = float(data_kwh[l]) + float(data_kwh[m])

        #Appending the  values to list 
        column_0.append(household_id[l])
        column_1.append(ai)
        column_2.append(np.float32(ae))
        column_3.append(Acorn[l])
        column_4.append(Acorn_groups[l])
        
    #checking time interval    
    elif time_comp == '1:00:00':
        ai = str(data_datetime[m]) 
        w = float(data_kwh[l]) + float(data_kwh[m])
        ar = str(data_datetime[k])
        ae = float(data_kwh[k])
        
        #Appending the  values to list
        column_0.append(household_id[m])
        column_0.append(household_id[k])
        column_1.append(ai)
        column_1.append(ar)
        column_2.append(np.float32(w))
        column_2.append(np.float32(ae))
        column_3.append(Acorn[m])
        column_3.append(Acorn[k])
        column_4.append(Acorn_groups[m])
        column_4.append(Acorn_groups[k])
         
        
        #values are increamented,to skip the row has 1 hr variation        
        l += 1
        m += 1
        k += 1
        
    #checking time interval
    
    elif time_def == '0:00:00':
        
        #values are increamented,to skip the row has 1 hr variation
        l -= 1
        m -= 1
        k -= 1
        
    #checking time interval        
    elif time_def == '1:00:00':
        ar = str(data_datetime[l])
        ae = float(data_kwh[l])
        
        #Appending the  values to list
        column_0.append(household_id[l])
        column_1.append(ar)
        column_2.append(np.float32(ae))
        column_3.append(Acorn[l])
        column_4.append(Acorn_groups[l])

        
        #values are increamented,to skip the row has 1 hr variation
        l -=1
        m -=1
        k -=1
        
    l += 2
    m += 2
    k += 2
    
disct = {'LCLid': column_0,'DateTime': column_1,'KWh' : column_2,'Acorn': column_3,'Acorn_groups': column_4}
    
#The data that has changed in hourly basis & saveed as csv     
df = pd.DataFrame(disct)
df.to_csv(r'Desktop\hourly_dataset.csv', index=False)

# print(column_1)
# print(column_2)
print('done')