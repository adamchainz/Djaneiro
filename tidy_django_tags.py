# coding=utf-8
import re
import sublime
import sublime_plugin


class TidyDjangoTagsCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()

        bad_tag_res = [r"(\{[\{\%])([^ ](.+)[^ ])([\}|\%]\})",
                       r"(\{[\{\%]) ([^ ](.+)[^ ])([\}|\%]\})",
                       r"(\{[\{\%])([^ ](.+)[^ ]) ([\}|\%]\})"]
        good_tag_re = r"\1 \2 \4"

        edit = view.begin_edit()

        for bad_tag_re in bad_tag_res:
            found = view.find_all(bad_tag_re, sublime.IGNORECASE)

            for f in reversed(found):
                string = view.substr(f)
                replaced = re.sub(bad_tag_re, good_tag_re, string)
                view.replace(edit, f, replaced)

        view.end_edit(edit)

