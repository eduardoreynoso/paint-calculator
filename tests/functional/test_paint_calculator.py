import json
import unittest2 as unittest
from pprint import pformat

from app.run import calculate_feet
from tests.helpers import setup_logger

logger = setup_logger(__name__)


class TestPaintCalculatorUnitTests(unittest.TestCase):
    """
    Test class for Paint Calculator that covers unit tests
    """

    def test_functional_calculate_feet(self):
        """
        Loads a fixture and tries out every combination in the fixture and asserts the output
        Note: This does not generate a test case for every combination which is not ideal
        In order to achieve this, a custom test runner can be implemented and every combination
        of input/output could be added as a separate test case
        """
        with open('tests/functional/data_fixture.json', 'r') as f:
            data = json.load(f)

        index = 1
        for test_case in data['test_functional_calculate_feet']:
            data = test_case['input']
            output = test_case['output']

            logger.info('Test case [{}]:\ninput:\n{}\noutput:\n{}\n'.format(
                index, pformat(data), pformat(output)
            ))
            index += 1
            self.assertEqual(
                calculate_feet(data), output)
