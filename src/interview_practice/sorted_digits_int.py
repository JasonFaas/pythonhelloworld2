# are the digits in an integer sorted?

def are_int_digits_sorted(value):
    if value < 100:
        return True

    moving_value = value
    first_value = moving_value % 10
    second_value = int(moving_value / 10) % 10
    is_desc = first_value > second_value

    while moving_value > 9:
        if is_desc and first_value < second_value \
                or not is_desc and first_value > second_value:
            return False
        moving_value = int(moving_value / 10)
        first_value = moving_value % 10
        second_value = int(moving_value / 10) % 10

    return True


assert are_int_digits_sorted(2)
assert are_int_digits_sorted(21)
assert are_int_digits_sorted(12)
assert are_int_digits_sorted(123)
assert not are_int_digits_sorted(121)
assert are_int_digits_sorted(210)
assert not are_int_digits_sorted(312)

assert are_int_digits_sorted(12345678)
assert not are_int_digits_sorted(123485678)
