from fman import DirectoryPaneCommand
from time import sleep


class SwapPanel(DirectoryPaneCommand):
    def __call__(self):
        panes = self.pane.window.get_panes()

        currentPane = self.pane
        lpane = panes[0]
        lpane_path = lpane.get_path()
        lpane_selection = lpane.get_selected_files()
        lpane_cursor = lpane.get_file_under_cursor()

        rpane = panes[1]
        rpane_path = rpane.get_path()
        rpane_selection = rpane.get_selected_files()
        rpane_cursor = rpane.get_file_under_cursor()

        def _setLeftPaneSelections():
            trying = True
            while(trying):
                try:
                    rpane.place_cursor_at(lpane_cursor)
                    trying = False
                except:
                    sleep(0.1)
                    trying = True
            if(lpane_selection):
                for url in lpane_selection:
                    trying = True
                    while(trying):
                        try:
                            rpane.toggle_selection(url)
                            trying = False
                        except:
                            sleep(0.1)
                            trying = True

        def _setRightPaneSelections():
            trying = True
            while(trying):
                try:
                    lpane.place_cursor_at(rpane_cursor)
                    trying = False
                except:
                    sleep(0.1)
                    trying = True
            if(rpane_selection):
                for url in rpane_selection:
                    trying = True
                    while(trying):
                        try:
                            lpane.toggle_selection(url)
                            trying = False
                        except:
                            sleep(0.1)
                            trying = True
            if panes[0] == currentPane:
                panes[1].focus()
            else:
                panes[0].focus()

        lpane.set_path(rpane_path, _setLeftPaneSelections)
        rpane.set_path(lpane_path, _setRightPaneSelections)
