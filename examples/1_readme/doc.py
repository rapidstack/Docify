import sys

from docify import Document, components as c
from docify.formatters.html import HTML
from docify.formatters.markdown import Markdown
from docify.formatters.html_bootstrap import HTMLBootstrap


doc = Document(
    c.H1('Docify'),
    c.Span('Simple, flexible python document generator'),
    c.Div(c.Nbsp()),
    c.Div(
        c.A(c.Img(alt='PyPI version', src='https://img.shields.io/pypi/v/docify.svg'),
            href='https://pypi.org/project/docify'),
        c.Nbsp(),
        c.A(c.Img(alt='Build Status',
                  src='https://travis-ci.org/rapidstack/docify.svg?branch=master'),
            href='https://travis-ci.org/rapidstack/docify'),
        c.Nbsp(),
        c.A(c.Img(alt='Documentation Status',
                  src='https://readthedocs.org/projects/docify/badge/?version=latest'),
            href='https://docify.readthedocs.io/en/latest/?badge=latest')),
    c.Div(c.Nbsp()),
    c.H2('Introduction'),
    c.Div(
        c.Span('Docify helps you write documents in different formats from a'),
        c.Nbsp(),
        c.Bold('Python object')),
    c.Div(c.Nbsp()),
    c.Blockquote(
        c.B('Note:')
        + c.Nbsp()
        + c.Span('It\'s not a document ')
        + c.I('converter')
        + c.Span(', neither a ')
        + c.I('documentation')
        + c.Span(' generator, nor a document ')
        + c.I('parser')),
    c.Div(c.Nbsp()),
    c.H2('Installation'),
    c.Pre('pip install docify'),
    c.Div(c.Nbsp()),
    c.H2('Usage & Examples'),
    c.B(c.A('Read API documentation on Read the Docs',
            href='https://docify.readthedocs.io')),
    c.Div(c.Nbsp()),
    c.B(c.A('Find quickstart and more examples here',
            href='https://github.com/rapidstack/docify/tree/master/examples')),
    c.Div(c.Nbsp()),
    c.B('Try examples like this'),
    c.Pre('python doc.py markdown\n\npython doc.py htmlbootstrap'))


if __name__ == '__main__':
    formatters = {
        'html': HTML,
        'markdown': Markdown,
        'htmlbootstrap': HTMLBootstrap
    }

    if len(sys.argv) > 1:
        sys.stdout.write(str(formatters[sys.argv[1]](doc)) + '\n')
    else:
        sys.stdout.write(str(doc) + '\n')
