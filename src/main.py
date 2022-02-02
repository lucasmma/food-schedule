from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route("/")
def main():
  return render_template('index.html', recent_meals=get_recent_meals())


@app.route("/recentMeals", methods=["POST", "GET"])
def get_recent_meals():
    try:
      return 'ola' 
    except Exception:
        print("exception")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
