import cgi

from docify.lib.formatter import Formatter
from docify import Document, components as c


DOC_TMPL = '''\
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Docify Document</title>
    </head>
    <body>
        <div id="container">
            {}
        </div>
    </body>
</html>
'''


class HTML(Formatter):
    '''HTML formatter to format document into plain HTML.'''
    pass


@HTML.handle(Document)
def handle_doc(state, obj):
    return DOC_TMPL.format(''.join(map(
        lambda c: HTML.f(state, c), obj.components)))


@HTML.handle(c.Text)
def handle_text(state, obj):
    return cgi.escape(obj.value)


