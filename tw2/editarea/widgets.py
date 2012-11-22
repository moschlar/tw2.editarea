import tw2.core as twc


class Editarea(twc.Widget):
    template = "genshi:tw2.editarea.templates.editarea"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/editarea.js'),
        twc.CSSLink(modname=__name__, filename='static/editarea.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Editarea, self).prepare()
        # put code here to run just before the widget is displayed
