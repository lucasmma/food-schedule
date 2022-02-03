from flask import Flask, render_template, request, Response, redirect, url_for, abort
from infra import append_data_on_database, read_database
from utils import get_todays_timestamp, get_current_date, date_to_timestamp, get_current_timestamp
import traceback
from datetime import date

app = Flask(__name__, template_folder='templates')

database = 'database.json'

def register_meal():
  print("ola")


@app.route("/")
def main():
  return render_template('index.html', foods=get_recent_meals(), date= date.today().strftime("%d/%m/%Y"))


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
      # append_data_on_database(data)
      return data
  except Exception as err:
    print(traceback.format_exc())

if __name__ == "__main__":
    app.run(debug=True, port=3000, host='0.0.0.0')
