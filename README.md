# Final Project - Emotion Detection Web Application

This repository contains the completed Final Project submission for the "Developing AI Applications with Python and Flask" course on Coursera, developed in partnership with IBM Skills Network.

The public repository hosted at https://github.com/voravan/oaqjp-final-project-emb-ai represents the independent development, execution, and deployment of the required application architecture.

---

## Project Description
A lightweight, responsive web application developed with Python and Flask that leverages the Watson NLP Emotion Detection service. The application analyzes user-submitted textual statements and outputs precise operational metric breakdowns for five core emotional spectrums: **Anger**, **Disgust**, **Fear**, **Joy**, and **Sadness**, alongside identifying the overall **Dominant Emotion**.

---

## Final Project Summary & Core Workflow
The project demonstrates a complete end-to-end software engineering workflow:
1. Building an application package using modular Python structures.
2. Integrating external cloud APIs (Watson NLP runtime services via JSON/REST interfaces).
3. Implementing functional web microframework services utilizing Flask routing.
4. Setting up strict input error validation rules for server stability.
5. Performing static code analysis via pylint to ensure institutional-grade PEP 8 compliance.

---

## Key Features
* Real-time Emotion Analysis: Seamless backend pipeline communicating directly with the Watson NLP Prediction service apiary layer.
* Intuitive Web UI: Form-based responsive front-end dashboard built with HTML, CSS, and embedded JavaScript.
* Robust Input Validation: Dynamic error handling infrastructure to manage edge cases and intercept empty strings or missing payload fields.
* Strict Quality Standards: Backend components fully compliant with PEP 8 layout conventions, verified to achieve a 10.00/10 static code linter score.

---

## Prerequisites & Setup

Ensure you have Python 3.8+ deployed in your workspace architecture.

1. Environment Installation
Install the necessary system dependencies and framework bindings within your active terminal context:
pip install flask requests pylint

2. Launching the Application
Execute the localized network deployment target using the explicit Python runtime engine:
python3.8 server.py

*The microframework infrastructure will automatically bind to local addresses routing requests natively on port 5000.*

---

## Usage Profiles & API Endpoints

### Direct Web Interface
1. Navigate to your local preview engine or application container via http://localhost:5000.
2. Enter any textual statement inside the diagnostic input bar (e.g., "I am glad this happened").
3. Click Submit to process and view structural formatting metrics dynamically.

### System Validation Constraints
If a query parameter is submitted completely blank or containing whitespace padding, the platform gracefully catches the invalid request parameter state and returns a standardized handling output directly inside the UI matrix:

Invalid text! Please try again!

---

## Code Diagnostics Quality Testing
The system maintains highly strict structural code rules. To test file layouts against clean Python PEP 8 conventions:
pylint server.py

Expected Diagnostic Output Benchmark:
Your code has been rated at 10.00/10
