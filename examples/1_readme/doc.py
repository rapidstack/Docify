import sys

from docify import Document, components as c
from docify.formatters.html import HTML
from docify.formatters.markdown import Markdown
from docify.formatters.html_bootstrap import HTMLBootstrap


doc = Document(
    c.Section(
        c.H1('Docify')
        + c.Span('Simple, flexible python document generator'),
        c.A(c.Img(alt='PyPI version', src='https://img.shields.io/pypi/v/Docify.svg'),
            href='https://pypi.org/project/Docify')
        + c.Nbsp()
        + c.A(c.Img(
            alt='Build Status',
            src='https://travis-ci.org/rapidstack/Docify.svg?branch=master'),
            href='https://travis-ci.org/rapidstack/Docify')
        + c.Nbsp()
        + c.A(c.Img(
            alt='Documentation Status',
            src='https://readthedocs.org/projects/docify/badge/?version=latest'),
            href='https://docify.readthedocs.io/en/latest/?badge=latest')),

    c.Section(
        c.H2('Introduction')
        + c.Span('Docify helps you write documents in different formats from a ')
        + c.B('Python object.'),
        c.Blockquote(
            c.B('Note:')
            + c.Nbsp()
            + c.Span('It\'s not a document ')
            + c.I('converter')
            + c.Span(', neither a ')
            + c.I('documentation')
            + c.Span(' generator, nor a document ')
            + c.I('parser'))),

    c.Section(
        c.H2('Installation')
        + c.Pre(c.Code('pip install docify'))),

    c.Section(
        c.H2('Usage & Examples')
        + c.Span(
            c.B(c.A('Read API documentation on Read the Docs',
                    href='https://docify.readthedocs.io')),
            c.Br(),
            c.B(c.A('Find quickstart and more examples here',
                    href='https://github.com/rapidstack/docify/tree/master/examples')))
        + c.Br(),
        c.B('Try examples like this'),
        c.Pre(c.Code('python doc.py markdown\npython doc.py htmlbootstrap'))))


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
