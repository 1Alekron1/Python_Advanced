import logging
import sys

import logging_tree
import contextlib
from logging_tree import printout

logging.getLogger('a')
logging.getLogger('a.b').setLevel(logging.DEBUG)
logging.getLogger('x.c')

with open("logging_tree.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        printout()