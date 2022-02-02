from flask import Flask, render_template, request, Response, redirect, url_for

app = Flask(__name__, template_folder='templates')


def register_meal():
  print("ola")


@app.route("/")
def main():
  return render_template('index.html', foods=get_recent_meals())


@app.route("/recentMeals", methods=["GET"])
def get_recent_meals():
  print('ola1')
  try:
    return 'ola' 
  except Exception:
      print("exception")

@app.route("/registerMeal", methods=["POST"])
def register_meal():
  print('registrado')
  print(request.form['food'])
  try:
    return 'ola' 
  except Exception:
      print("exception")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
