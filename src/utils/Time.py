import datetime

time = datetime.datetime.now()
month = (time.strftime("%B"))

#no leading 0 if day <10
day = (time.strftime("%e")).strip()
date = (f"{month} {day},")
