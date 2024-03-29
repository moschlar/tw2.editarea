"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

import widgets


class DemoEditAreaWidget(widgets.EditAreaWidget):
    # Provide default parameters, value, etc... here
    # default = <some-default-value>
    syntax = 'python'
    value = u'''
def hello():
    print u'Hello World!'
    return True
'''
