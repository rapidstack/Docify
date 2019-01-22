import unittest

from doc import doc
from docify.formatters.html_bootstrap import HTMLBootstrap


class HTMLBootstrapTest(unittest.TestCase):

    def test_create(self):
        print(HTMLBootstrap(doc))


if __name__ == '__main__':
    unittest.main()
