#!/usr/bin/env python3.7

from cli import main
from cli.errors import ArgumentError
import sys
try:
    main()
except ArgumentError as err:
    print(f"Error: {err}")
    sys.exit(1)