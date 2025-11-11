from data_validator import validate_record
from exceptions import DataValidationError

records = [
    {"name": "Ravi", "age": 21, "score": 88},       
    {"name": 123, "age": 25, "score": 77},          
    {"age": 19, "score": 92},                       
    {"name": "Anjali", "age": -3, "score": 95},   
    {"name": "Sree", "age": 20, "score": "High"},   
    {"name": "Teja", "age": 23, "score": 105}    
]

print("🧠 Smart Data Validator 🧠")
v=0
iv=0
for record in records:
    try:
        validate_record(record)
        print(f"✅ Valid record : {record}")
        v+=1
    except DataValidationError as e:
        print(f"❌ Invalid record : {e}")
        iv+=1
print("The count of valid and invalid:")
print(f"Valid:{v}\nInvalid:{iv}")
print("\nValidation completed.")
