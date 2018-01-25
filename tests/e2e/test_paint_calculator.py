import os

from selenium import webdriver
import unittest2 as unittest

from tests.helpers import setup_logger
from tests.e2e.controllers.paint_calculator_controller import PaintCalculatorController

logger = setup_logger(__name__)


class TestPaintTestCalculatorE2E(unittest.TestCase):

    def setUp(self):
        """
        Initalizes a web driver object
        :return:
        """
        logger.debug('Initializing web driver')
        # Initialize the web driver
        self.driver = webdriver.Chrome(os.path.join(
            os.getcwd(), 'drivers/chromedriver'))
        self.controller = PaintCalculatorController(self.driver)

    def test_single_room(self):
        self.driver.get('http://127.0.0.1:5000/')

        self.controller.set_number_of_rooms(2)
        self.controller.set_room_dimensions(
            [
                {
                    'length': 40,
                    'width': 50,
                    'height': 12
                },
                {
                    'length': 40,
                    'width': 60,
                    'height': 14
                },
            ])
        feet_per_room = self.controller.get_feet_per_room()
        gallons_per_room = self.controller.get_gallons_per_room()
        total_gallons = self.controller.get_total_gallons()
        self.assertEqual(feet_per_room, ['2160', '2800'])
        self.assertEqual(gallons_per_room, ['6', '7'])
        self.assertEqual(total_gallons, '13')

    def tearDown(self):
        self.driver.quit()
