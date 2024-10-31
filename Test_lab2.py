import lab2  # Replace with your module name if different

def test_find_min_max():
    # Test with a sample list
    temp_list = [5, 67, 32, 2, 89]
    result = lab2.find_min_max(temp_list)
    assert result == [89, 2], f"Expected [89, 2], got {result}"

def test_calc_average():
    # Test with a sample list
    temp_list = [5, 67, 32, 2, 89]
    result = lab2.calc_average(temp_list)
    expected_average = sum(temp_list) / len(temp_list)
    assert result == expected_average, f"Expected {expected_average}, got {result}"

def test_calc_median_temperature():
    # Test with an odd number of elements
    temp_list_odd = [5, 67, 32, 2, 89]
    result_odd = lab2.calc_median_temperature(temp_list_odd)
    expected_median_odd = 32  # Sorted list is [2, 5, 32, 67, 89]
    assert result_odd == expected_median_odd, f"Expected {expected_median_odd}, got {result_odd}"

    # Test with an even number of elements
    temp_list_even = [5, 67, 32, 2]
    result_even = lab2.calc_median_temperature(temp_list_even)
    expected_median_even = (5 + 32) / 2  # Sorted list is [2, 5, 32, 67]
    assert result_even == expected_median_even, f"Expected {expected_median_even}, got {result_even}"
