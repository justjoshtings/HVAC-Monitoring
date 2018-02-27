import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#function to prompt user: period of days
def how_long():
	d1d, d1m, d1yr, d2d, d2m, d2yr, = [int(x) for x in input("Enter the first and last day in the following format: dd1,mm1,yy1,dd2,mm2,yy2 \n").split(',')]
	d1 = datetime.date(d1yr, d1m, d1d)
	d2 = datetime.date(d2yr, d2m, d2d)
	delta_days = d2 - d1
	d1m_str = str(d1m)
	d2m_str = str(d2m)
	d1d_str = str(d1d)
	d2d_str = str(d2d)
	if len(str(abs(d1m))) != 2:
		d1m_str = "0"+str(d1m)
	if len(str(abs(d2m))) != 2:
		d2m_str = "0"+str(d2m)
	if len(str(abs(d1d))) != 2:
		d1d_str = "0"+str(d1d)
	if len(str(abs(d2d))) != 2:
		d2d_str = "0"+str(d2d)
	return [delta_days.days, d1d_str, d1m_str, d1yr, d2d_str, d2m_str, d2yr]

#function to count how many items in observations
def countfn(data_in):
	counter = 0
	for item in data_in["history"]["observations"]:
		counter += 1
	return counter

#function to parse through JSON data
def parse_json(counter_in, data_in):
	real_count = counter_in - 3
	temp_list = {"pretty":[0]*real_count, "year":[0]*real_count, "month":[0]*real_count, "day":[0]*real_count, "hour":[0]*real_count, "mins":[0]*real_count, "temp":[0]*real_count}
	for i in range(0,real_count):
		temp_list["pretty"][i] = data_in["history"]["observations"][i]['date']['pretty']
		temp_list["year"][i] = data_in["history"]["observations"][i]['date']['year']
		temp_list["month"][i] = data_in["history"]["observations"][i]['date']['mon']
		temp_list["day"][i] = data_in["history"]["observations"][i]['date']['mday']
		temp_list["hour"][i] =data_in["history"]["observations"][i]['date']['hour']
		temp_list["mins"][i] = data_in["history"]["observations"][i]['date']['min']
		temp_list["temp"][i] = data_in["history"]["observations"][i]['tempi']
	return temp_list #(pretty,year,month,day,hour,mins,temp)

# formatting into better lists
def format_fn(temp_list_master, day_list):
	temp_actual = [0]*(day_list[0]*24)
	hours_actual = [0]*(day_list[0]*24)
	year_actual = [0]*(day_list[0]*24)
	months_actual = [0]*(day_list[0]*24)
	days_actual = [0]*(day_list[0]*24)
	print(day_list[0])
	print(len(temp_actual))
	counter = 0
	for i in range(0,day_list[0]):
		for j in range(0,24):
			temp_actual[counter] = temp_list_master[i]["temp"][j] #list of all temps for all days
			hours_actual[counter] = temp_list_master[i]["hour"][j]
			year_actual[counter] = temp_list_master[i]["year"][j]
			months_actual[counter] = temp_list_master[i]["month"][j]
			days_actual[counter] = temp_list_master[i]["day"][j]
			counter += 1
	date_actual = [0]*(day_list[0]*24)
	for k in range(0,day_list[0]*24):
		date_actual[k] = datetime.datetime(int(year_actual[k]), int(months_actual[k]), int(days_actual[k]), int(hours_actual[k]), 0, 0)
	return temp_actual, date_actual

def setpoint_fn(day_list):
	try:
		st_pt = float(input("Enter setpoint: "))
	except ValueError:
		raise ValueError ("Enter a number!")
	except Exception:
		raise Exception ("Unknown error entering setpoint")
	st_pt_list = [0]*(day_list[0]*25)
	for i in range(0,(day_list[0]*25)):
		st_pt_list[i] = st_pt
	return st_pt_list

#plotting date and temp
def od_temp_plot_fn(temp_actual, date_actual, build, st_pt_list):
	fig, ax = plt.subplots(1)
	fig.autofmt_xdate()
	plt.plot(date_actual, temp_actual, c='#FB5633', label="Outdoor Temp")
	plt.plot(date_actual, st_pt_list, c='#000000', label="Setpoint Temp")

	xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
	ax.xaxis.set_major_formatter(xfmt)

	max_day = len(date_actual)-1
	plt.title("{:s} for {:02d}/{:02d}/{:02d} to {:02d}/{:02d}/{:02d}".format(build, date_actual[0].day, date_actual[0].month, date_actual[0].year,date_actual[max_day].day, date_actual[max_day].month, date_actual[max_day].year), fontsize = 15)
	plt.ylabel(r'Temperature ($^\circ$F)', fontsize = 10)
	# plt.grid(True)

	# plt.ylim(0,80)
	# ax.set_ylim(0,80)

	plt.show()

#plot: cutoff, indoor temp, boiler on?
# temp idk yet but great job yesterday!
