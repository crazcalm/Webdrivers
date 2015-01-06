from selenium.webdriver import Chrome
from selenium.webdriver import firefox
from selenium.webdriver import Ie
import config
import os


DRIVERS = {"chrome": Chrome,
           "IEDriv": Ie}


class Browser:
    def __init__(self, name, driver):
        self.name = name
        self.driver = driver


def _driver_name(path):
    head, tail = os.path.split(path)
    return tail


def main():
    for driver_path in config.main():

        test = Browser(_driver_name(driver_path),
                       DRIVERS[_driver_name(driver_path)[:6]](driver_path))
        test.driver.close()


if __name__ == "__main__":
    main()