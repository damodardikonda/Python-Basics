import datetime
import pytz


dates=datetime.date(2020,6,23)#dont pass zero in eg.06
print(dates)

print('if you want to display today date')
tod_day=datetime.date.today();
print(tod_day)

print('suppose we want to dispaly a year')
print(tod_day.year)

print('suppose we want to dispaly a day')
print(tod_day.day)


print(tod_day.weekday())#modnday 0 and sunday 6
print(tod_day.isoweekday())#moday=1 sunday=0

print("printing date after 7 days");
timedel=datetime.timedelta(days=7)
print(tod_day+timedel);

print("day before 7 days");
print(tod_day-timedel)

print('printing seconds');
#tt=tod_day.total_seconds()

#print(tt)


print('\n\n Working on time\n\n')

tym=datetime.time(9,45,50,10000)#h,m,s,microsec
print(tym)

print('printing only hours');
print(tym.hour)

print('\n\n for both date and time');
dt=datetime.datetime(2008,8,28,12,8,49,1000);
print(dt)

print("only date:-",dt.date())
print('only time:-',dt.time())

print('only year:-',dt.year)

print('\n\n timedelta in datetime')

td=datetime.timedelta(days=7);

trr=dt+td
print(trr)

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()



print(dt_today)
print(dt_now)
print(dt_utcnow)

print('current dte')
dt=datetime.datetime( 2016,7,24,tzinfo=pytz.UTC)#tzinfo is an subclass of tzinfo class..it capture information about the offset from UTC time, the time zone name,
print(dt)
