"""
Script to read files drag-and-dropped onto a div element.
"""

from browser import document as doc
from browser import window

# I did not find the brython implementation of FileReader. THerefore,
# I use an object created in a javascript on the same page. See in files.html
# script defining the reader variable. This variable than is used here to
# organize reading of the file and its output.
reader = window.reader


def show_content_when_loaded(evt):
    """
    Triggered when the reader completes loading the file.
    """

    # evt.target refers to the object issuing the event, i.e. reader?
    # doc <= SAMP(repr(evt.target.file_local_name))
    # doc <= SAMP(repr(evt.target.result))
    doc['ou0'].text = 'Content of {}:'.format(evt.target.file_local_name)
    doc['ou1'].text = evt.target.result
    return

reader.onload = show_content_when_loaded
reader.name = ''


def handleFileSelect(evt):
    # don't pass the event to the parent html element, see
    # https://www.brython.info/static_doc/en/events.html
    evt.stopPropagation()
    # prevent default behaviuor triggered by the event
    evt.preventDefault()

    # See https://www.brython.info/static_doc/en/drag_events.html
    # This is already file objects!
    fl = evt.dataTransfer.files
    for fn in fl:
        # WHen reading completes, the reader trigger the onload event.
        # Additional data for the funcion bond to this event can be
        # passed as attributes
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
    o = doc['ou1']
    o.text = 'go-on!'
    return


dz = doc['dz1']
dz.bind('drop', handleFileSelect)
dz.bind('dragover', handleDragOver)
