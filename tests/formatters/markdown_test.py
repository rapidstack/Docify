import unittest

from doc import doc
from docify.formatters.markdown import Markdown


class MarkdownTest(unittest.TestCase):

    def test_create(self):
        print(Markdown(doc))


if __name__ == '__main__':
    unittest.main()
