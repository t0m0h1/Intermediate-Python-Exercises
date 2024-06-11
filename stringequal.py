def check_string_equality(str1: str, str2: str) -> bool:
    # Return False if either string is None or not an instance of str
    if not all(isinstance(s, str) for s in (str1, str2)):
        return False
    # Return True if both strings are equal
    return str1 == str2

def test_check_string_equality():
    test_cases = [
        ("hello", "hello", True),
        ("hello", "world", False),
        ("", "", True),
        (None, None, False),
        (None, "hello", False),
        ("hello", None, False),
        ("  hello", "hello", False),
        ("hello", "  hello", False),
        ("hello", "hello ", False),
        ("Hello", "hello", False),
        ("こんにちは", "こんにちは", True),
        ("hello", "こんにちは", False),
        ("", None, False),
        (None, "", False),
    ]

    for str1, str2, expected in test_cases:
        result = check_string_equality(str1, str2)
        assert result == expected, f"For input {str1!r}, {str2!r}, expected {expected} but got {result}"

if __name__ == "__main__":
    test_check_string_equality()