import unittest2 as unittest

from app.run import calculate_feet, calculate_gallons_required, sanitize_input, extract_room_info


class TestPaintCalculatorUnitTests(unittest.TestCase):
    """
    Test class for Paint Calculator that covers unit tests
    """

    def test_calculate_feet(self):
        """
        Documentation defines the calculation as `((Length * 2) + (Width * 2)) * Height`
        Expects data in a dictionary containing 'length', 'width' and 'height'
        For l=2, w=3, h=4 we have
        `((2 * 2) + (3 * 2)) * 4` = 40
        :return:
        """
        data = {
            'length': 2,
            'width': 3,
            'height': 4
        }
        expected_result = 40

        calculated_result = calculate_feet(data)
        self.assertEqual(expected_result, calculated_result)

    def test_calculate_gallons(self):
        """
        1 gallon of paint covers 400ft
        For 1200 ft we need 3 gallons
        :return:
        """
        data = {
            'ft': 1200
        }
        expected_result = 3
        calculated_result = calculate_gallons_required(data)
        self.assertEqual(expected_result, calculated_result)

    def test_sanitize_input(self):
        """
        Function gets the absolute value of a number
        -666 should return 666
        :return:
        """
        data = -666
        expected_result = 666
        calculated_result = sanitize_input(data)
        self.assertEqual(expected_result, calculated_result)

    def test_extract_room_info(self):
        """
        Function extracts the data from a dictionary that has the room number as a part of the key
        It also sanitizes the inputs and converts them to ints
        A dictionary that has:
        {
            'length-0': '2',
            'width-0': '3',
            'height-0': '4'
        }
        Should be converted to:
        {
            'lenght': 2,
            'width': 3,
            'height' : 4,
        }
        :return:
        """
        data = {
            'length-0': '2',
            'width-0': '3',
            'height-0': '4'
        }
        expected_result = {
            'length': 2,
            'width': 3,
            'height': 4,
        }
        calculated_result = extract_room_info(data, 0)
        self.assertEqual(expected_result, calculated_result)
