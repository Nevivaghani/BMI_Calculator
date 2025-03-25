from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserInput(BaseModel):
    weight: float
    height: float
    status: str

def calculate_bmi(weight: float, height: float, status: str) -> dict:
    try:
        if status == "cms":
            height = height / 100
        elif status == "feet":
            height = height / 3.2808  

        bmi = weight / (height ** 2)

        if bmi < 16:
            category = "Extremely Underweight"
        elif bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Healthy"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Extremely Overweight"

        return {"bmi": round(bmi, 2), "category": category}

    except ZeroDivisionError:
        return {"error": "Height cannot be zero"}


@app.post("/bmi_calculator")
def bmi_calculator(data: UserInput):
    return calculate_bmi(data.weight, data.height, data.status)
