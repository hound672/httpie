#!/usr/bin/env python
"""The main entry point. Invoke as `http' or `python -m httpie'.

"""
import sys
from time import time


def main():
    try:
        from .core import main
        start_time = time()
        exit_status = main()
        end_time = time()
        elapsed_time = end_time - start_time
        print('\033[92mElapsed time:\033[0m {0}'.format(elapsed_time))

    except KeyboardInterrupt:
        from httpie.status import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    sys.exit(exit_status.value)


if __name__ == '__main__':
    main()
