import cgi

from docify import Document, components as c
from docify.lib.formatter import Formatter


DOC_TMPL = '''\
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <title>Docify Document</title>
    </head>
    <body>
        <div>
{}
            <footer>
                <p>&nbsp;</p>
                <small>
                    <cite>
                        This document generated using
                        <a href="https://github.com/rapidstack/docify">
                            Docify
                        </a>
                    </cite>
                </small>
            </footer>
        </div>
    </body>
</html>
'''


class HTML(Formatter):
    '''HTML fomatter to format `Document`'''

    @classmethod
    def handlers(cls):
        '''Get the component handlers'''

        return {
            str: cgi.escape,

            Document: lambda x: DOC_TMPL.format('\n'.join(map(cls.f, x.components))),

            c.Nbsp: lambda x: '&nbsp;',

            c.Li: lambda x: '{0}<li>\n{1}\n{0}</li>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.A: lambda x: '{0}<a href="{1}">\n{2}\n{0}</a>'.format(
                cls.i(x.depth), x.href.replace('"', '\\"'), cls.f(x.element)),

            c.P: lambda x: '{0}<p>\n{1}\n{0}</p>'.format(
                cls.i(x.depth), '\n'.join(map(cls.f, x.children))),

            c.Ol: lambda x: '{0}<ol>\n{1}\n{0}</ol>'.format(
                cls.i(x.depth), '\n'.join(map(cls.f, x.children))),

            c.Ul: lambda x: '{0}<ul>\n{1}\n{0}</ul>'.format(
                cls.i(x.depth), '\n'.join(map(cls.f, x.children))),

            c.H1: lambda x: '{0}<h1>\n{1}\n{0}</h1>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.H2: lambda x: '{0}<h2>\n{1}\n{0}</h2>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.H3: lambda x: '{0}<h3>\n{1}\n{0}</h3>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.H4: lambda x: '{0}<h4>\n{1}\n{0}</h4>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.H5: lambda x: '{0}<h5>\n{1}\n{0}</h5>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.H6: lambda x: '{0}<h6>\n{1}\n{0}</h6>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.I: lambda x: '{0}<i>\n{1}\n{0}</i>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.B: lambda x: '{0}<b>\n{1}\n{0}</b>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.Br: lambda x: '{0}<br />'.format(cls.i(x.depth)),

            c.Hr: lambda x: '{0}<hr />'.format(cls.i(x.depth)),

            c.Code: lambda x: '<code>{}</code>'.format(cls.f(x.element)),

            c.Pre: lambda x: '{0}<pre>{1}</pre>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.Blockquote: lambda x: '{0}<blockquote>\n{1}\n{0}</blockquote>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.Del: lambda x: '{0}<del>\n{1}\n{0}</del>'.format(
                cls.i(x.depth), cls.f(x.element)),

            c.Span: lambda x: '{0}<span>\n{1}\n{0}</span>'.format(
                cls.i(x.depth), '\n'.join(map(cls.f, x.children))),

            c.Img: lambda x: '{0}<img src="{1}" alt="{2}" />'.format(
                cls.i(x.depth), x.src.replace('"', '\\"'),
                x.alt.replace('"', '\\"'))
        }

    @staticmethod
    def i(depth):
        '''Create indentation based on depth.

        :param int depth: Depth of object.
        '''
        return ' ' * (8 + (depth * 4))
