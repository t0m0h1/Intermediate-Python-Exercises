def check_string_equality(str1: str, str2: str) -> bool:
    # Return False if either string is None or not an instance of str
    if not all(isinstance(s, str) for s in (str1, str2)):
        return False
    # Return True if both strings are equal
    return str1 == str2

if __name__ == "__main__":
    # Test cases
    print(check_string_equality("hello", "hello"))  # Should return True
    print(check_string_equality("hello", "hella"))  # Should return False
    print(check_string_equality("hello", "helloo")) # Should return False
    print(check_string_equality("hello", "helo"))   # Should return False
    print(check_string_equality("hello", None))     # Should return False
    print(check_string_equality(None, "hello"))     # Should return False
    print(check_string_equality("hello", 12345))    # Should return False
    print(check_string_equality(12345, "hello"))    # Should return False