from docify import Document, components as c


doc = Document(
    c.H1('Header 1'),
    c.H2('Header 2'),
    c.H3('Header 3'),
    c.H4('Header 4'),
    c.H5('Header 5'),
    c.H6('Header 6'),

    c.Section(
        c.I('Italic'),
        c.B('Bold'),
        c.B(c.I('Italic') + c.Nbsp() + 'inside bold'),
        c.I(c.B('Bold') + ' inside italic'),
        c.Blockquote('Blockquote'),
        c.Del('Strikethrough')),

    c.Pre(c.Code('# Code block\n:(){ :|:& };:')),

    c.Section(
        c.Span('Inline code:', c.Code(':(){ :|:& };:')),
        c.Span('Span', '->', c.Span('Nested span'))),

    c.Ol(
        c.Li('Item 1'),
        c.Li(c.A('Item 2', href='#')),
        c.Ul(
            c.Li('Item 2.1'),
            c.Li(c.A('Item 2.2', href='#')),
            c.Ol(
                c.Li('Item 2.2.1'),
                c.Li(c.A('Item 2.2.2', href='#'))))),

    c.Br(),

    c.Img(
        src='https://img.shields.io/badge/docify-image_test-green.svg',
        alt='Image Test'),

    c.Hr(),

    c.A('google', href='https://google.com'),

    c.Br(),

    c.A(c.Img(
        src='https://img.shields.io/badge/docify-image_test-green.svg',
        alt='Image Test'),
        href='https://img.shields.io/badge/docify-image_test-green.svg'))
