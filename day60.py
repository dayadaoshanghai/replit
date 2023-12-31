import datetime

today = datetime.datetime.today() 

holiday = datetime.date(year = 2022, month = 12, day = 20) 

if holiday < today: 
  print("Coming soon")
elif holiday > today: 
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")