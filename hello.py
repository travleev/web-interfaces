# Script to be used in hello.html and a template for brython scripts

from browser import document
import sys
import package1
c = package1.C1()


def print_hallo(event):
    document['r1'].textContent = "Hello, {}!".format(document['i1'].value)
    return


def print_path(event):
    document['r2'].text = ' '.join([str(sys.version), c.p, c.m])
    return


def load_cpu(event):
    n = int(document['i3'].value)
    document['r3'].text = ''
    c.load_cpu(n)
    document['r3'].text = str(n)
    return

document['b1'].bind('click', print_hallo)
document['b2'].bind('click', print_path)
document['b3'].bind('click', load_cpu)
