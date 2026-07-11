from flask import Flask, render_template, request
import joblib
from datetime import datetime

app = Flask(__name__)

model = joblib.load("model/hdi_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/predict", methods=["POST"])
def predict():

    life = float(request.form["life"])
    mean = float(request.form["mean"])
    expected = float(request.form["expected"])
    income = float(request.form["income"])

    prediction = model.predict([[life, mean, expected, income]])[0]
    prediction = round(float(prediction), 3)

    if prediction < 0.55:
        category = "🔴 Low Human Development"
    elif prediction < 0.70:
        category = "🟡 Medium Human Development"
    elif prediction < 0.80:
        category = "🟢 High Human Development"
    else:
        category = "🏆 Very High Human Development"

    progress = int(prediction * 100)

    return render_template(
        "index.html",
        prediction=prediction,
        category=category,
        progress=progress,
        date=datetime.now().strftime("%d-%m-%Y %I:%M %p")
    )


if __name__ == "__main__":
    app.run(debug=True)