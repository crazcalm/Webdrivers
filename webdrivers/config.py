import sys
import os


PLATFORM = {'linux': 'linux',
            'win32': 'win',
            'darwin': 'mac'}

BITS = {2**31 - 1: "32bit",
        2**63 - 1: "64bit"}


def _platform():
    """
    Returns the platform name

    :return: string
    """
    return sys.platform


def _bits():
    """
    Returns the systems max integer size, which is used to figure out if the sys is
    32 bit or 64 bit

    :return: int
    """
    return sys.maxsize


def _path(platform, bit):
    """
    Returns the path of the directory where the web drivers are located

    :param platform: string
    :param bit: string
    :return: string
    """
    current_dir = os.path.dirname(__file__)
    driver_path = os.path.join(current_dir, 'drivers', platform, bit)
    return driver_path


def _driver_file(path):
    """
    Returns a list of the paths to possible web drivers

    :param path: string
    :return: list
    """
    results = []
    for driver in os.listdir(path):
        results.append(os.path.join(path, driver))
    return results


def main():
    """
    Figures out which platform you are running and returns a list os possible
    web drivers that you may use.

    :return: list
    """
    platform = PLATFORM[_platform()]
    bit = BITS[_bits()]
    driver_path = _path(platform, bit)
    return _driver_file(driver_path)

if __name__ == "__main__":
    print(_platform())
    print(_bits())
    print(main())