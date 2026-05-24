import argparse
import sys
from cli_toolkit.utils import number_utils as nu
from cli_toolkit.utils import file_utils as fu
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Number utility tool")
    parser.add_argument("number", type=int, help="The number to process")
    args = parser.parse_args()

    num = args.number
    logger.debug(f"Received argument : {num}")

    even_odd = nu.is_even_or_odd(num)
    logger.info(f"Given number {num} is {even_odd}")

    factorial = nu.factorial(num)
    logger.info(f"Factorial of the given number {num} is {factorial}")

    if num > 10:
        logger.warning(f"Large number {num} -- Factorial will be very big")

    # test file_exists

    logger.info(f"Does README.md exist: {fu.file_exists('README.md')}")
    logger.info(f"Does fake.txt exist: {fu.file_exists('fake.txt')}")

    # test create_folder
    fu.create_folder("temp/test_folder")
    logger.info("Created temp/test_folder")


if __name__ == "__main__":
    main()
