import sys

from docify import Document, components as c
from docify.formatters.html import HTML
from docify.formatters.markdown import Markdown
from docify.formatters.html_bootstrap import HTMLBootstrap


doc = Document(
    c.H1('Header 1'),
    c.H2('Header 2'),
    c.H3('Header 3'),
    c.H4('Header 4'),
    c.H5('Header 5'),
    c.H6('Header 6'),
    c.I('Italic'),
    c.B('Bold'),
    c.B(c.I('Italic') + c.Nbsp() + c.Span('inside bold')),
    c.I(c.Div(c.B('Bold'), c.Span(' inside italic'))),
    c.Blockquote('Blockquote'),
    c.Del('Strikethrough'),
    c.Pre('# Code block\n:(){ :|:& };:'),
    c.Span('Inline code: ') + c.Code(':(){ :|:& };:'),
    c.Ol(
        c.Li('Item 1'),
        c.Li(c.A('Item 2', href='#')),
        c.Ul(
            c.Li('Item 2.1'),
            c.Li(c.A('Item 2.2', href='#')),
            c.Ol(
                c.Li('Item 2.2.1'),
                c.Li(c.A('Item 2.2.2', href='#'))))),
    c.Img(
        src='https://img.shields.io/badge/docify-image_test-green.svg',
        alt='Image Test'),
    c.Hr(),
    c.A('google', href='https://google.com'),
    c.A(c.Img(
        src='https://img.shields.io/badge/docify-image_test-green.svg',
        alt='Image Test'),
        href='https://img.shields.io/badge/docify-image_test-green.svg'))


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

