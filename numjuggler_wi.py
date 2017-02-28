"""
Script to process input files with numjuggler.
"""

from browser import document as doc
from browser import window

reader = window.reader


def show_content_when_loaded(evt):
    """
    Triggered when the reader completes loading the file.
    """
    p1.text = 'Content of {}:'.format(evt.target.file_local_name)
    ta1.text = evt.target.result
    sss = ''
    n = 0
    for l in evt.target.result.splitlines():
        sss += '{}\n'.format(repr(l))
        n += 1
    ta2.text = sss
    p2.text = 'has {} lines'.format(n)

    # for l in evt.target.result.splitlines():
    #     ta1.text += repr(l) + '\n'
    return

reader.onload = show_content_when_loaded
reader.name = ''


def handleFileSelect(evt):
    evt.stopPropagation()
    evt.preventDefault()
    fl = evt.dataTransfer.files
    for fn in fl:
        reader.file_local_name = fn.name
        reader.readAsText(fn)
    return


def handleDragOver(evt):
    """
    Without binding this function to dragover, the file is simply opened in
    chrome.
    """
    evt.stopPropagation()
    evt.preventDefault()
    evt.dataTransfer.dropEffect = 'copy'
    ta1.text = 'go-on!'
    return


def run_numjuggler(evt):
    """
    Take MCNP input from ta1 and process with numjuggler --mode info
    """
    import sys
    sss = '\n'.join(sys.path)
    ta2.text = sss
    import numjuggler
    ta2.text += str(dir(numjuggler))
    return


ta1 = doc['ta1']
ta2 = doc['ta2']
p1 = doc['p1']
p2 = doc['p2']
b1 = doc['b1']

ta1.bind('drop', handleFileSelect)
ta1.bind('dragover', handleDragOver)

b1.bind('click', run_numjuggler)
