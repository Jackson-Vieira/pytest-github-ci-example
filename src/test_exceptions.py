import pytest
# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# test pytest raises any exception
def test_raises_any_exception():
    with pytest.raises(Exception) as excp:
        raise Exception("something is wrong")
    assert str(excp.value) == "something is wrong"


def validate_age(age):
    if age < 18:
        raise InvalidAgeException()
    return True

# test pytest raises custom exception
# @pytest.mark.parametrize()
def test_raises_custom_exception():
    with pytest.raises(InvalidAgeException):
        validate_age(15)
