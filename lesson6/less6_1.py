import datetime as dt
from datetime import datetime

d = dt.date(2019, 1, 21)

print(d)

print(d.year)

print(d.month)
print(d.day)
print(d.weekday())

d2 = d.replace(month=2)

print(d2)

t = dt.time(20, 0, 0, 0)


print(str(t))

print(t.hour)

print(t.minute)
print(t.second)
print(t.microsecond)

##t.fold --> указывает, что произошел перевод времени назад

d1 = datetime.now()

d2 = datetime.now()

print(d1, d2)

d = datetime(2019, 5, 28, 3, 14, 40, 7)
print(d)

print(d.date())
print(d.time())
print(d.weekday())

print(d.replace(year=2018))

print(d1.timestamp(),d2.timestamp(),d.now().timestamp())

print(datetime.fromtimestamp(datetime.timestamp(datetime.now())))

print(datetime.now() - d1)

from datetime import timedelta

dt1 = timedelta(days=2, hours=8, minutes=20)

print(dt1, '* 2 = ', dt1*2)

d = datetime.now()
dt = timedelta(days=1000)
print(d, d - dt)


from datetime import timezone

novt = timezone(timedelta(hours=7))
msk = timezone(timedelta(hours=3))

dnsk = datetime.now(novt)
dmsk = datetime.now(msk)

print('NSK', dnsk, 'MSK', dmsk)

print(dnsk == dmsk)

import pytz
novt = pytz.timezone('Asia/Novosibirsk')
msk = pytz.timezone('Europe/Moscow')

print('NOVT', novt, 'MSK', msk)

dnsk = novt.localize(datetime.now())
dmsk = msk.localize(datetime.now())

print('NSK', dnsk, 'MSK', dmsk)

print(dnsk == dmsk)

