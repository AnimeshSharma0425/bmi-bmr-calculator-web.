# BMI & BMR Calculator

A beginner-friendly web app that calculates Body Mass Index (BMI), shows the BMI category, estimates Basal Metabolic Rate (BMR) and works out daily calorie needs from activity level. Built with Python, FastAPI, HTML, CSS and JavaScript.

The web version uses the same formulas and checks as the original console program, which is kept unchanged in `original_console.py`.

## Features

- BMI with category (Underweight, Normal weight, Overweight, Obesity)
- BMR using the Mifflin-St Jeor equation
- Daily calorie needs for four activity levels
- FastAPI backend with a plain HTML/CSS/JS frontend

## Project Structure

```
.
├── main.py              # FastAPI app and /calculate endpoint
├── original_console.py  # The original console program (unchanged)
├── requirements.txt     # Python dependencies
├── render.yaml          # Render deployment config
├── .python-version      # Python version for deployment
└── static/
    ├── index.html
    ├── style.css
    └── script.js
```

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## API

`POST /calculate`

```json
{
  "age": 25,
  "gender": "male",
  "weight": 70,
  "height": 175,
  "activity": 1
}
```

Response:

```json
{
  "bmi": 22.86,
  "category": "Normal weight",
  "bmr": 1673.75,
  "daily_calories": 2008.5
}
```

Valid `gender` values: `male`, `female`. Valid `activity` values: `1` Sedentary, `2` Lightly Active, `3` Moderately Active, `4` Very Active.

Invalid gender or activity returns a 400 error with the message `Invalid gender!` or `Invalid activity level!`.

## Deploy on Render

Push this folder to the root of a GitHub repo (`main.py` and `static/` must be at the top level), create a new Web Service on Render and connect the repo. `render.yaml` already sets the build and start commands.

## License

MIT
