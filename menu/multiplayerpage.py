from yyagl.lib.gui import Btn
from yyagl.engine.gui.page import Page, PageFacade
from yyagl.gameobject import GameObject
from .thankspage import ThanksPageGui


class MultiplayerPageGui(ThanksPageGui):

    def __init__(self, mediator, mp_props):
        self.props = mp_props
        ThanksPageGui.__init__(self, mediator, mp_props.gameprops.menu_props)

    def show(self):
        ThanksPageGui.show(self)
        self.build()

    def build(self):
        lmp_cb = lambda: self.notify('on_push_page', 'localmp',
                                     [self.props])
        omp_cb = lambda: self.notify('on_push_page', 'online',
                                     [self.props])
        menu_data = [
            ('Local', _('Local'), lmp_cb),
            ('Online', _('Online'), omp_cb)]
        widgets = [
            Btn(text=menu[0], pos=(0, .3-i*.28), cmd=menu[2],
                **self.props.gameprops.menu_props.btn_args)
            for i, menu in enumerate(menu_data)]
        self.add_widgets(widgets)
        ThanksPageGui.build(self)


class MultiplayerPage(Page):
    gui_cls = MultiplayerPageGui

    def __init__(self, mp_props):
        init_lst = [
            [('event', self.event_cls, [self])],
            [('gui', self.gui_cls, [self, mp_props])]]
        GameObject.__init__(self, init_lst)
        PageFacade.__init__(self)
        # invoke Page's __init__

    def destroy(self):
        GameObject.destroy(self)
        PageFacade.destroy(self)
