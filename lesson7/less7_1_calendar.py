import calendar

cal = calendar.Calendar(0)
print([day for day in cal.itermonthdays(2019, 1)])
print([day for day in cal.itermonthdays2(2019, 1)])
print([day for day in cal.itermonthdays3(2019, 1)])
print([day for day in cal.itermonthdays4(2019, 1)])

tcal = calendar.TextCalendar(0)
cal = tcal.prmonth(2019, 1)
print(cal)

s = tcal.formatmonth(2019, 1)
print(s)
