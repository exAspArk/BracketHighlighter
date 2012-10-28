import bh_plugin
import sublime


class SelectBracket(bh_plugin.BracketPluginCommand):
    def run(self, edit, name, select=''):
        left, right = self.left, self.right
        first, last = left.end, right.begin
        if select == 'left':
            if name == "angle" and left.size() > 1:
                first, last = left.begin + 1, left.begin + 1
            else:
                first, last = left.end, left.end
        elif select == 'right':
            if left.end != right.end:
                if name == "angle" and left.size() > 1:
                    first, last = right.begin + 1, right.begin + 1
                else:
                    first, last = right.begin, right.begin
            else:
                # There is no second bracket, so just select the first
                if name == "angle" and left.size() > 1:
                    first, last = left.begin + 1, left.begin + 1
                else:
                    first, last = right.end, right.end

        self.selection = [sublime.Region(first, last)]


def plugin():
    return SelectBracket