#!/usr/bin/env python
truth =  "/usr/bin/env python shebang says use the current environment's python version to execute. "
print(truth)

#!/Users/huntaj/dev/pythoncertification/venv/bin/python3.7
from helpers.strings import extract_lower
from helpers import variables
from helpers import * # the __init__.py file in helpers will provide us with the extract_upper method as part of __all__
import helpers
# variables imports helpers again, but helpers doesn't print anything this time.
# Any subsequent imports of the same module don't need to be read-in again because the interpreter has
# already read it in as part of the application
name = "Austin Hunt"
print(f"__name__ in main.py: {__name__}")
print(f"Lowercase letters: {extract_lower(variables.name)}")
print(f"Uppercase letters: {extract_upper(variables.name)}")
print(f"From helpers: {helpers.strings.extract_lower(variables.name)}")

