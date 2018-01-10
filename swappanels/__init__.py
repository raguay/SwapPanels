from fman import DirectoryPaneCommand

class SwapPanel(DirectoryPaneCommand):
    def __call__(self):
        panes = self.pane.window.get_panes()
        rpane = panes[0].get_path()
        lpane = panes[1].get_path()
        panes[0].set_path(lpane)
        panes[1].set_path(rpane)