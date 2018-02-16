from fman import DirectoryPaneCommand
import os


class SwapPanel(DirectoryPaneCommand):
    def __call__(self):
        panes = self.pane.window.get_panes()

        lpane = panes[0]
        lpane_path = lpane.get_path()
        lpane_selection = lpane.get_selected_files()

        rpane = panes[1]
        rpane_path = rpane.get_path()
        rpane_selection = rpane.get_selected_files()

        def _setLeftPaneSelections():
            if(lpane_selection):
                for url in lpane_selection:
                    try:
                        rpane.toggle_selection(url)
                    except:
                        pass

        def _setRightPaneSelections():
            if(rpane_selection):
                for url in rpane_selection:
                    try:
                        lpane.toggle_selection(url)
                    except:
                        pass

        lpane.set_path(rpane_path, _setLeftPaneSelections)
        rpane.set_path(lpane_path, _setRightPaneSelections)
