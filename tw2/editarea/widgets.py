import os
import tw2.core as twc


editarea_js = twc.JSLink(
    modname=__name__,
    filename='static/edit_area_full.js',
    init=twc.js_function('editAreaLoader.init')
    )

editarea_langs = dict(
    (f.rstrip('.js'), twc.CSSLink(modname=__name__, filename=os.path.join('static/langs', f)))
    for f in os.listdir(os.path.join(os.path.dirname(__file__), 'static/langs')))
editarea_reg_syntaxes = dict(
    (f.rstrip('.js'), twc.CSSLink(modname=__name__, filename=os.path.join('static/reg_syntax', f)))
    for f in os.listdir(os.path.join(os.path.dirname(__file__), 'static/reg_syntax')))

editarea_images = twc.DirLink(
    modname=__name__,
    filename='static/images',
    )


class EditAreaWidget(twc.Widget):
    template = "tw2.editarea.templates.editarea"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [editarea_js]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(EditAreaWidget, self).prepare()
        # put code here to run just before the widget is displayed
        self.add_call(editarea_js.init({'id': self.compound_id, 'syntax': 'Python', 'start_highlight': True}))
