"""
Script to test possibilities to import from user-installed packages
"""
import io  # this assumes brython_stdlib
import sys
from browser import document as doc
import tovtk


def run_script(e):
    # print everything here
    t = io.StringIO()
    # replace default stdout with my file-like object
    tmp = sys.stdout
    sys.stdout = t

    for n in dir():
        print(n)

    doc['ou1'].text = t.getvalue()
    t.close()
    sys.stdout = tmp
    return


doc['b0'].bind('click', run_script)
