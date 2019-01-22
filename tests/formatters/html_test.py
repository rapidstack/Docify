import unittest

from doc import doc
from docify.formatters.html import HTML


class HTMLTest(unittest.TestCase):

    def test_create(self):
        print(HTML(doc))


if __name__ == '__main__':
    unittest.main()
