🧠 Smart Data Validator

A Python-based data validation system designed to ensure data integrity using custom exceptions, modular programming, and robust error handling.
This project demonstrates how Python’s exception handling and modular structure can be applied to build clean, reliable, and production-ready systems.

🚀 Project Overview

The Smart Data Validator simulates a real-world data quality pipeline.
It automatically checks for:

Missing fields (e.g., name, age, score)

Invalid data types (e.g., age given as a string instead of an integer)

Out-of-range values (e.g., negative marks or unrealistic numbers)

💡 This project helps you understand how custom exception classes can make debugging and data validation more structured and scalable — a critical concept for AI/ML pipelines, data preprocessing, and backend validation systems.

🧩 Features

✅ Modular structure with separate files for logic and exceptions
✅ Handles missing, invalid, and out-of-range data gracefully
✅ Provides clear, human-readable error messages
✅ Demonstrates use of try-except-else-finally blocks
✅ Extensible design for real-world data workflows

📁 Project Structure
SmartDataValidator/
│
├── main.py               # Entry point - runs validation
├── data_validator.py     # Core logic for validating data
├── exceptions.py         # Custom exception classes
└── README.md             # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository

git clone https://github.com/sreeranga-chippala/SmartDataValidator.git

cd SmartDataValidator

2️⃣ Create and Activate Virtual Environment

python3 -m venv venv

source venv/bin/activate

3️⃣ Run the Program

python3 main.py

🧠 Sample Output

🧠 Smart Data Validator 🧠

✅ Valid record → {'name': 'Ravi', 'age': 21, 'score': 88}

❌ Invalid record → The value -3 is out of range. The minimum is 5 and 

maximum is 100

❌ Invalid record → Field 'score' is missing

✅ Summary: 1 valid, 2 invalid

🧰 Concepts Demonstrated

Concept	Description

Custom Exceptions	Defines reusable, domain-specific error classes

Modular Design	Separates logic for clarity and reusability

Error Handling	Demonstrates nested and chained exception handling

Input Validation	Simulates real-world data checks

Clean Code Principles	Readable, scalable, and production-oriented structure

🛠️ Tech Stack

🐍 Python 3.14

🧱 VS Code

🔗 Git & GitHub

💡 Future Enhancements

✨ Add CSV file input validation

✨ Integrate with Pandas for dataset validation

✨ Log validation results into external files

✨ Build Streamlit dashboard for visual error reports

👨‍💻 Author

Chippala Sree Ranganath

🎓 B.E. in Artificial Intelligence and Machine Learning – MSRIT

📘 Trained under NxtWave CCBP 4.0 Technologies

🔗 GitHub: https://github.com/sreeranga-chippala