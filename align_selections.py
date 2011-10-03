import sublime_plugin


class AlignSelectionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        maxCol = 0
        regions = v.sel()
        blocks = []
        for r in regions:
            _, col = v.rowcol(r.begin())
            maxCol = max(col, maxCol)
            blocks.append(r)

        blocks.reverse()
        for r in blocks:
            _, col = v.rowcol(r.begin())
            v.insert(edit, r.begin(), " " * (maxCol - col))
