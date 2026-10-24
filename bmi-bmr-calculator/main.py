from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent


def find_static_dir() -> Path:
    # Works whether index.html is in static/ or in static/static/
    for candidate in (BASE_DIR / "static", BASE_DIR / "static" / "static"):
        if (candidate / "index.html").exists():
            return candidate
    return BASE_DIR / "static"


STATIC_DIR = find_static_dir()

app = FastAPI(title="BMI & BMR Calculator")


class UserData(BaseModel):
    age: int = Field(..., gt=0, lt=130)
    gender: str
    weight: float = Field(..., gt=0)   # kg
    height: float = Field(..., gt=0)   # cm
    activity: int                      # 1-4


@app.post("/calculate")
def calorie_calculator(data: UserData):
    # Same logic as the original console program (original_console.py)
    age = data.age
    gender = data.gender.lower()
    weight = data.weight
    height = data.height
    activity = data.activity

    height_m = height / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    if gender == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    elif gender == "female":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    else:
        raise HTTPException(status_code=400, detail="Invalid gender!")

    if activity == 1:
        calories = bmr * 1.2

    elif activity == 2:
        calories = bmr * 1.375

    elif activity == 3:
        calories = bmr * 1.55

    elif activity == 4:
        calories = bmr * 1.725

    else:
        raise HTTPException(status_code=400, detail="Invalid activity level!")

    return {
        "bmi": round(bmi, 2),
        "category": category,
        "bmr": round(bmr, 2),
        "daily_calories": round(calories, 2),
    }


# check_dir=False so the server still starts (and shows a clear message)
# even if the static folder was not uploaded
app.mount("/static", StaticFiles(directory=STATIC_DIR, check_dir=False), name="static")


@app.get("/")
def home():
    index = STATIC_DIR / "index.html"
    if index.exists():
        return FileResponse(index)
    return {"error": "index.html not found in the static folder"}
