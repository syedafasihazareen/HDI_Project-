# AI Based Human Development Index (HDI) Prediction System

## Project Description
This project predicts the Human Development Index (HDI) using Machine Learning. A Random Forest Regression model is trained on HDI data and deployed using a Flask web application.

## Features
- Predicts HDI score
- User-friendly Flask web interface
- Uses Random Forest Regression
- Displays HDI category and prediction result

## Technologies Used
- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS

## Project Structure

HDI_Project/
│
├── app.py
├── train_model.py
├── requirements.txt
├── dataset/
├── templates/
├── static/
└── README.md

## Dataset
Dataset used: **hdr_general.csv**

## How to Run

1. Install the required packages:

```
pip install -r requirements.txt
```

2. Train the model:

```
python train_model.py
```

3. Run the Flask application:

```
python app.py
```

4. Open your browser and visit:

```
http://127.0.0.1:5000
```

## Note

The trained model (`hdi_model.pkl`) is not included in this repository because of GitHub's file size limit. Generate it by running:

```
python train_model.py
```

## Author

**Syeda Fasiha Zareen**

B.Tech Computer Science and Engineering

Ravindra College of Engineering for Women
