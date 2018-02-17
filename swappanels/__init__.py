from fman import DirectoryPaneCommand


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
            if lpane_cursor is not None:
                rpane.place_cursor_at(lpane_cursor)
            for url in lpane_selection:
                rpane.toggle_selection(url)

        def _setRightPaneSelections():
            if rpane_cursor is not None:
                lpane.place_cursor_at(rpane_cursor)
            for url in rpane_selection:
                lpane.toggle_selection(url)

            if panes[0] == currentPane:
                panes[1].focus()
            else:
                panes[0].focus()

        rpane.set_path(lpane_path, _setLeftPaneSelections)
        lpane.set_path(rpane_path, _setRightPaneSelections)
