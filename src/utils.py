from datetime import datetime
import time

def get_current_date():
  return datetime.now().replace(hour=0, minute=0, second=0)

def get_todays_timestamp():
  date = get_current_date()
  return date_to_timestamp(date)

def date_to_timestamp(date):
  return time.mktime(date.timetuple())

def get_current_timestamp():
  return date_to_timestamp(datetime.now())