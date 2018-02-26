#program to retreieve hourly weather data in Boston for specified time from wunderground.com using API key and visualizing this data

#import modules
import requests
import json
import pickle
import wufunc
import datetime
import time

#current datetime & start timing
current_dt = datetime.datetime.now()
print(current_dt)
start_time = time.time()

#how_long fn: prompt how long period of days and does some formatting with datetime
day_list = wufunc.how_long() #delta_day, d1dstr, d1mstr, d1yr, d2dstr, d2mstr, d2yr
temp_list_master = [0]*day_list[0]
first_day = datetime.date(day_list[3],int(day_list[2]),int(day_list[1])) #datetime format of first day

for i in range(0,day_list[0]):
	day_list_tempo2 = str.replace(str(first_day + datetime.timedelta(days=i)), '-', '') #removing - between dates
	
	#get data in JSON format using requests.get module
	if day_list[3] == day_list[6] and day_list[2] == day_list[5]:
		r = requests.get("http://api.wunderground.com/api/86b63b60aa6f9abc/history_"+day_list_tempo2+"/q/MA/Boston.json")
		r.text

	#check connection status
	if r.status_code != 200:
		print('There was an error! \nError is {:d} in line {:d}'.format(r.status_code, i))

	#read data into wu_data variable & print type of data: dict, list, ...
	wu_data = json.loads(r.text)
	# print('Data type:',type(wu_data))

	#counter function: how many items in "observations" key
	counter = wufunc.countfn(wu_data)

	#parse JSON data function: output as dictionary of (pretty,year,month,day,hour,mins,temp) x 24
	temp_list = wufunc.parse_json(counter, wu_data)
	temp_list_master[i] = temp_list
	#Can be used to find out keywords of list
	# data_list = list(wu_data["history"]["observations"][0].keys())
	# print(data_list)

print(temp_list_master)

#plot od temp fn
# day_list_master = wufunc.od_temp_plot(temp_list_master, day_list)
# print(day_list_master)

#end time
end_time = time.time()
print("{:.3f}s".format(end_time - start_time))


# https://my.radiothermostat.com/rtcoa/rest/gateways/2002af7707fb/usagecsv?bucket-size=PT60M&days=30&unit=F  179BSR
# https://my.radiothermostat.com/rtcoa/rest/gateways/2002af76b4b2/usagecsv?bucket-size=PT60M&days=30&unit=F  139BSR