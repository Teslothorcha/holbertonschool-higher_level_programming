#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        return fct(*args)
    except Exception as tool:
        print("Exception: {}".format(str(tool)), file=sys.stderr)
        return None
