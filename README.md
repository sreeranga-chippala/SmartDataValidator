# 🧠 Smart Data Validator

> **A Python-based intelligent data validation engine** that ensures dataset integrity and reliability using custom exceptions, modular design, and scalable error handling — a must-have foundation for AI/ML data pipelines.

---

## 🚀 Overview

The **Smart Data Validator** automates the detection of common data issues in structured datasets.  
It identifies and reports:

- 🧩 **Missing fields** (e.g., missing name or score)
- ⚙️ **Invalid data types** (e.g., string instead of integer)
- ⚠️ **Out-of-range values** (e.g., negative marks or unrealistic scores)

This project demonstrates **how modular programming and clean exception handling** can build the backbone of robust AI/ML preprocessing and data quality systems.

---

## 🧩 Features

| Feature | Description |
|----------|-------------|
| 🧱 Modular Architecture | Clean separation of logic, exceptions, and driver code |
| ⚙️ Custom Exceptions | Handles missing, invalid, and out-of-range data gracefully |
| 🧠 Smart Error Handling | Uses `try-except-else-finally` for structured validation |
| 📊 Summary Reports | Displays total valid/invalid records |
| 🔄 Extensible Design | Can integrate easily with Pandas, APIs, or file systems |

---

## 📁 Project Structure

SmartDataValidator/
│
├── main.py # Entry point - executes validation
├── data_validator.py # Core validation logic
├── exceptions.py # Custom exception classes
└── README.md # Documentation (you’re reading it!)


---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/sreeranga-chippala/SmartDataValidator.git
cd SmartDataValidator

2️⃣ Create & Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

3️⃣ Run the Program

python3 main.py

🧠 Sample Output

🧠 Smart Data Validator 🧠

✅ Valid record → {'name': 'Ravi', 'age': 21, 'score': 88}
❌ Invalid record → The value -3 is out of range. The minimum is 5 and maximum is 100
❌ Invalid record → Field 'score' is missing

📊 Summary:
✅ Total Valid Records  : 1
❌ Total Invalid Records: 2

Validation completed successfully.


🧰 Concepts Demonstrated

| Concept                    | Description                                                                         |
| -------------------------- | ----------------------------------------------------------------------------------- |
| 🧠 **Custom Exceptions**   | User-defined classes for `MissingFieldError`, `InvalidTypeError`, `OutOfRangeError` |
| 🧩 **Modular Design**      | Split logic across multiple reusable files                                          |
| ⚙️ **Error Handling**      | Managed invalid inputs using structured `try/except/raise`                          |
| 🧮 **Scalable Validation** | Emulates real-world ML preprocessing patterns                                       |


🧱 Technologies Used

🐍 Python 3.14

💻 VS Code

🔗 Git & GitHub

⚙️ Virtual Environments

🧩 Object-Oriented Programming

💡 Future Enhancements

📁 Validate CSV/Excel file inputs

🧮 Integrate with Pandas for large datasets

🧾 Add structured logging for error tracking

📊 Build Streamlit dashboard for visualization

☁️ Deploy as a Flask/FastAPI microservice

👨‍💻 Author

Chippala Sree Ranganath
🎓 B.E. in Artificial Intelligence and Machine Learning – MSRIT
🏫 Trained under NxtWave CCBP 4.0 Technologies
🌍 Passionate about AI systems, clean code, and scalable design

📧 Email: chippalasreeranganath@gmail.com

🔗 GitHub: sreeranga-chippala

🌟 Professional Message

“Anyone can write working code —
Engineers write reliable, readable, and scalable code.”


