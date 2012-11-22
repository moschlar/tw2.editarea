from tw2.core.testbase import WidgetTest
from tw2.editarea import *

class TestEditarea(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Editarea
    # Initilization args. go here 
    attrs = {'id':'editarea-test'}
    params = {}
    expected = """<div id="editarea-test"></div>"""
