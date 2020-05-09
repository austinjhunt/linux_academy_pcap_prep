#!/usr/bin/env python3.7
import sys
try:
    print("First arg {}".format(sys.argv[1]))
    args = sys.argv
    random.shuffle(args)
    print("Random argument: {}".format(args[0]))
except (IndexError,KeyError) as err:
    print("error: no argumnets provided. provide at least one. ({})".format(err))
    sys.exit(1)
except NameError:
    print("Error: random module not loaded.")

else:
    print("Was able to make it through full try block with no error. ")

finally:
    print("Executing 'finally' block regardless of error (as long as script is still executing, no sys.exit)")