import sys
from cli_toolkit.utils import number_utils as nu
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        logger.debug(f"Received argument : {num}")
        even_odd = nu.is_even_or_odd(num)
        logger.info(f"Given number {num} is {even_odd}")
        factorial = nu.factorial(num)
        logger.info(f"Factorial of the given number {num} is {factorial}")
        if num > 10:
            logger.warning(f"Large number {num} -- Factorial will be very big")
    else:
        logger.error(f"correct usage: python {sys.argv[0]} [num]")


if __name__ == "__main__":
    main()
