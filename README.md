🧠 Smart Data Validator

A Python-based data validation system designed to check data integrity using custom exceptions, modular programming, and error handling — built as part of a deep dive into Python’s core engineering concepts.

📘 Project Overview

The Smart Data Validator simulates a real-world data quality pipeline.

It:

Validates multiple fields (name, age, score)

Uses custom exception classes for different types of errors

Produces clear reports showing valid and invalid entries

Demonstrates modular structure used in backend and ML pipelines

🧩 Features

✅ Checks for missing fields
✅ Detects incorrect data types
✅ Validates numeric value ranges
✅ Handles errors using custom exception hierarchy
✅ Prints total count of valid and invalid records

📁 Project Structure
SmartDataValidator/
│
├── main.py              # Entry point of the project
├── data_validator.py    # Validation logic
├── exceptions.py        # Custom exception classes
├── .gitignore           # Ignored folders (venv, cache, etc.)
└── README.md            # Project documentation

⚙️ How to Run
1️⃣ Clone the Repository
git clone https://github.com/sreeranga-chippala/SmartDataValidator.git
cd SmartDataValidator

2️⃣ Run the Project
python3 main.py

💡 Sample Output
🧠 Smart Data Validator 🧠
=========================

✅ Valid record → {'name': 'Ravi', 'age': 21, 'score': 88}
❌ Invalid record → 'age' value -3 is out of range (5-100).
❌ Invalid record → Missing required field: name

📊 Summary:
✅ Total Valid Records  : 1
❌ Total Invalid Records: 2

Validation completed.

🧠 Concepts Demonstrated
Concept	Description
Custom Exceptions	Created user-defined error classes (MissingFieldError, InvalidTypeError, OutOfRangeError).
Modular Programming	Split logic into reusable modules (exceptions.py, data_validator.py).
Error Handling	Used try, except, and raise to manage invalid data gracefully.
Validation Logic	Applied structured checks similar to real ML preprocessing.
🧰 Technologies Used

🐍 Python 3.14
💻 VS Code
🔗 Git & GitHub

💡 Future Scope

✨ Add CSV input and output support
✨ Log invalid data to a .txt or .csv file
✨ Integrate with Pandas for preprocessing before ML models
✨ Extend for real-time API data validation

👨‍💻 Author

Chippala Sree Ranganath
🎓 B.E. in Artificial Intelligence & Machine Learning (MSRIT)
📘 Trained under NxtWave CCBP 4.0 Technologies

🔗 GitHub: sreeranga-chippala

🧩 Message

“Clean code is not just about correctness —
it’s about clarity, reliability, and scalability.
This project builds the mindset that turns simple code into production systems.”
