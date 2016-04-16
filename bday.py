'''@bday.py
@author: zizhang hu
@date: April,2016

generate market days for U.S. equity from 1980 - 2030.

@potential bug: the market calendar was different back to 20 century..

'''

from bdateutil import isbday
import holidays
import datetime
from dateutil.easter import *
from datetime import timedelta

# good friday
d = timedelta(days=-2)

nYears = 50
numdays = 365*50 + nYears/4 +1
base = datetime.date(2030,1,1)
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

for date in date_list:
	if isbday(date,holidays=holidays.US()) and date!=easter(date.year)+d:
		print date

