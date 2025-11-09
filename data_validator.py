from exceptions import OutOfRangeError,MissingValueError,InvalidTypeError

def validate_record(record):
    required=["name","age","score"]
    for field in required:
        if field not in record:
            raise MissingValueError(field)
    if not isinstance(record["name"], str):
        raise InvalidTypeError("name", "string", type(record["name"]).__name__)
    if not isinstance(record["age"], int):
        raise InvalidTypeError("age", "integer", type(record["age"]).__name__)
    if not isinstance(record["score"], (int, float)):
        raise InvalidTypeError("score", "number", type(record["score"]).__name__)
    if record["age"] < 5 or record["age"] > 100:
        raise OutOfRangeError("age", record["age"], 5, 100)
    if record["score"] < 0 or record["score"] > 100:
        raise OutOfRangeError("score", record["score"], 0, 100)

    
    
    

