from flask import render_template, request, abort
from infra.db import *
from utils.datetime_handler import get_todays_timestamp, get_current_timestamp, get_current_date_formated
from main import app
import traceback

@app.route("/")
def main():
  return render_template('index.html', foods=get_recent_meals(), date= get_current_date_formated())

@app.route("/recentMeals", methods=["GET"])
def get_recent_meals():
  try:
    db = read_database()
    current_timestamp = get_todays_timestamp()
    todays_meals = []
    for data in db:
      if current_timestamp <= data['date']:
        todays_meals.append(data)

    return todays_meals

  except Exception:
    print(traceback.format_exc())

@app.route("/registerMeal", methods=["POST"])
def register_meal():
  try:
    food = request.form['food']
    schedule = request.form['schedule']
    if len(food) > 10 or not('R' in food or 'RM' in food or 'B' in food or 'A' in food or 'L' in food or '/' in food) or len(food) == 10:
      return 'erro', 400
    else:
      data = {
        'food': food,
        'schedule': schedule,
        'date': get_current_timestamp()
      }
      append_data_on_database(data)
      return data
  except Exception as err:
    print(traceback.format_exc())