from app.validators import validate, validate_priority

title_test_cases = [
    ("Learn Python", "Accepted"),
    ("  Learn Python  ", "Accepted"),
    ("", "Rejected"),
    ("   ", "Rejected"),
]

priority_test_cases = [
    (1, "Accepted"),
    (5, "Accepted"),
    (0, "Rejected"),
    (6, "Rejected"),
    ("3", "Rejected"),
    (True, "Rejected"),
]

for inp, expected in title_test_cases:
    result = validate(inp)
print(
    f"Input: {repr(inp):<20} -> Result: {result:<25} (Match: {True if result == expected else False})"
)

for inp, expected in priority_test_cases:
    result = validate_priority(inp)
    print(
        f"Input: {repr(inp):<20} -> Result: {result:<25} (Match: {True if result == expected else False})"
    )
