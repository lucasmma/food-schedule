from datetime import datetime, date
import time

def get_current_day():
  return datetime.now().replace(hour=0, minute=0, second=0)

def get_current_date_formated():
  return date.today().strftime("%d/%m/%Y")

def get_todays_timestamp():
  date = get_current_day()
  return date_to_timestamp(date)

def date_to_timestamp(date):
  return time.mktime(date.timetuple())

def get_current_timestamp():
  return date_to_timestamp(datetime.now())