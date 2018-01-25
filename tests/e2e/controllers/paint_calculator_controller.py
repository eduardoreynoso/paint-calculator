from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.common.by import By

from tests.helpers import setup_logger

logger = setup_logger(__name__)


class PaintCalculatorController(object):
    """
    A page object to interact with the paint calculator
    """
    # A reference to the web driver
    driver = None

    # Locators
    LOCATORS = {
        'room_number_textfield': (By.NAME, 'rooms'),
        'submit_room_number': (By.ID, 'submit_room_number'),
        'dimensions_table': (By.NAME, 'dimensions_table'),
        'length_room_value': (By.NAME, 'length-{}'),
        'width_room_value': (By.NAME, 'width-{}'),
        'height_room_value': (By.NAME, 'height-{}'),
        'submit_dimensions': (By.ID, 'submit_dimensions'),
        'feet_per_room': (By.XPATH, '//*[@data-test="feet"]'),
        'gallons_per_room': (By.XPATH, '//*[@data-test="gallons"]'),
        'total_gallons': (By.XPATH, '//*[@data-test="total"]')
    }

    def __init__(self, driver):
        self.driver = driver

    def set_number_of_rooms(self, number):
        self.get_element(self.LOCATORS['room_number_textfield']).send_keys(number)
        self.get_element(self.LOCATORS['submit_room_number']).click()

    def set_room_dimensions(self,dimensions):
        self.get_element(self.LOCATORS['dimensions_table'])

        for number, data in enumerate(dimensions):
            self.driver.find_element(self.LOCATORS['length_room_value'][0],
                                     self.LOCATORS['length_room_value'][1].format(number)).send_keys(
                data['length'])
            self.driver.find_element(self.LOCATORS['width_room_value'][0],
                                     self.LOCATORS['width_room_value'][1].format(number)).send_keys(
                data['width'])
            self.driver.find_element(self.LOCATORS['height_room_value'][0],
                                     self.LOCATORS['height_room_value'][1].format(number)).send_keys(
                data['height'])

        self.get_element(self.LOCATORS['submit_dimensions']).click()

    def get_feet_per_room(self):
        return [x.text for x in self.get_elements(self.LOCATORS['feet_per_room'])]

    def get_gallons_per_room(self):
        return [x.text for x in self.get_elements(self.LOCATORS['gallons_per_room'])]

    def get_total_gallons(self):
        return self.get_element(self.LOCATORS['total_gallons']).text

    def get_element(self, locator, timeout=5):
        """
        Retrieves an element by the given locator
        Checks if the element is present in the DOM and later if the element is visible (in the viewport)
        :param locator:
        :param timeout:
        :return:
        """
        element = WebDriverWait(self.driver, timeout).until(
            conditions.presence_of_element_located(locator))
        WebDriverWait(self.driver, timeout).until(
            conditions.visibility_of(element))
        return element

    def get_elements(self, locator):
        """
        Retrieves a collection of web elements that match the given locator
        :param locator:
        :return:
        """
        return WebDriverWait(self.driver, 5).until(
            conditions.presence_of_all_elements_located(locator))
