import datetime
import matplotlib


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

	#plot temp vs time
def od_temp_plot(temp_list_master, day_list):
	day_list_master = [0]*day_list[0]
	for i in range(0,day_list[0]):
			day_list_master[i] = temp_list_master[]
	return day_list_master

# uhhhh how to plot x axis time and y axis date, for time use date time and + days loop
#temp idk yet but great job yesterday! :)
