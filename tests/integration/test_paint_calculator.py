import unittest2 as unittest

from app.run import calculate_result
from tests.helpers import setup_logger

logger = setup_logger(__name__)


class TestPaintCalculatorIntegration(unittest.TestCase):
    """
    Test class for Paint Calculator that covers unit tests
    """

    def test_functional_calculate_gallons(self):
        """
        Asserts the processing of the data and the final output
        :return:
        """
        data = {
            'length-0': '40',
            'width-0': '50',
            'height-0': '12',
            'length-1': '40',
            'width-1': '60',
            'height-1': '14',
        }
        expected_result = 13
        result = calculate_result(data)
        logger.debug(result)
        self.assertEqual(result[1], expected_result)
