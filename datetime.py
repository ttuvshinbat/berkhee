from datetime import datetime, timedelta,time

now =datetime.now()
ergelzee = time(12,0)
dayErgelzee =datetime(2022,11,12,1,12,13)

yesterday = now - timedelta(days=1)
tomorrow = now +timedelta(days=1)
tsagiinDaraa= now +timedelta(hours=1)
day0 = datetime.isocalendar(now)
day1 = datetime.isoweekday(now)
day2 = datetime.isoformat(now)
day3 = datetime.ctime(now)
alarm_time = datetime(year=tomorrow.year,month=tomorrow.month,day=tomorrow.day,hour=8,minute=15)
print(ergelzee)
print(dayErgelzee)
print(day0)
print(now)
print(yesterday)
print(tomorrow)
print(day1)
print(day2)
print(day3)
print(tsagiinDaraa)
tomorrow = now + timedelta(days=1)
print(alarm_time)

# Маргааш өглөө 08:00 цаг болгож тохируулна
import time
while datetime.now() < alarm_time:
    time.sleep(10)
    print("⏰ Сэрүүлэг: Цаг боллоо!")
