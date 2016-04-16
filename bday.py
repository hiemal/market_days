'''@bday.py
@author: zizhang hu
@date: April,2016

generate market days for U.S. equity.

@potential bug: the market calendar was different back to 20 century..

'''

from pandas.tseries.holiday import get_calendar, HolidayCalendarFactory, GoodFriday
from datetime import datetime,date,timedelta

calendar = get_calendar('USFederalHolidayCalendar')
calendar.rules.pop(6)
calendar.rules.pop(7)
trading_calendar = HolidayCalendarFactory('TradingCalendar',calendar,GoodFriday)

output = trading_calendar()
start = datetime(1980,1,1)
end = datetime(2030,1,1)
holidays = output.holidays(start,end)


nYears = 50
numdays = 365*50 + nYears/4 +1
base = date(2030,1,1)
date_list = [base - timedelta(days=x) for x in range(0, numdays)]


for date in date_list:
	if date not in holidays:
		print date

