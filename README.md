# BMI Calculator

## Introduction

The **BMI Calculator** is a web application that allows users to calculate their Body Mass Index (BMI) based on their weight and height. It features a frontend built with Streamlit and a backend API powered by FastAPI. Users can select different height measurement formats (centimeters, meters, or feet), and the app will compute the BMI and categorize the result.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Features

- Interactive UI for BMI input and display using Streamlit.
- RESTful API built with FastAPI.
- Supports input in centimeters, meters, or feet.
- Categorizes BMI into medically recognized ranges.
- Error handling for invalid inputs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bmi-calculator.git
   cd bmi-calculator
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the FastAPI Backend

```bash
uvicorn main:app --reload
```

### Run the Streamlit Frontend

```bash
streamlit run BMI_Calculator.py
```

Make sure the FastAPI server is running before launching the Streamlit frontend, as it communicates with the backend via HTTP requests.

## Dependencies

The main dependencies are:

- `fastapi`
- `uvicorn`
- `streamlit`
- `pydantic`
- `requests`
- `blinker`

All dependencies are listed in `requirements.txt` and `pyproject.toml`.

## Configuration

- Ensure the backend is accessible at `http://127.0.0.1:8000` for local development.
- The endpoint used by the Streamlit app is hardcoded as `/bmi_calculator`.

## API Documentation

FastAPI automatically generates interactive API documentation at:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### POST `/bmi_calculator`

**Request Body:**
```json
{
  "weight": 70,
  "height": 170,
  "status": "cms"
}
```

**Response:**
```json
{
  "bmi": 24.22,
  "category": "Healthy"
}
```

## Examples

You can test different combinations directly in the Streamlit app:

- Weight: `70`
- Height: `170`
- Format: `cms`
- Output: `BMI: 24.22`, Category: `Healthy`

## Troubleshooting

- **Connection Error:** Ensure the FastAPI backend is running and accessible.
- **Height Zero Error:** Input height must be greater than zero.
- **Port Conflict:** Change the port in the `uvicorn` command if `8000` is already in use.

## Screenshots

![App Screenshot][def]

![App Screenshot][def2]

![App Screenshot][def3]

[def]: ./assets/bmi1.png

[def2]: ./assets/bmi2.png

[def3]: ./assets/bmi3.png



