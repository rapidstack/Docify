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

    tmpl = DOC_TMPL
    indent = 4
    initial_spacing = 12

    def __init__(self, *args, **kwargs):
        self._spacing = self.initial_spacing
        super(HTML, self).__init__(*args, **kwargs)

    def tag(self, tag, components=[], properties={}):
        return '<{0}{1}>{2}</{0}>'.format(
            tag, ' ' + (' '.join(
                '{}="{}"'.format(k, v.replace('"', '\\"'))
                for k, v in properties.items()))
                if len(properties) > 0 else '',
            ''.join([self.f(c) for c in components]))


@HTML.handle(Document)
def handle_doc(state, obj):
    state._spacing
    return state.tmpl.format(('\n' + (' ' * state._spacing)).join(
        [state.f(c) for c in obj.components]))


@HTML.handle(c.Text)
def handle_text(state, obj):
    return cgi.escape(obj.value)


@HTML.handle(c.Nbsp)
def handle_nbsp(state, obj):
    return '&nbsp;'


@HTML.handle(c.Break)
def handle_br(state, obj):
    return '<br />'


@HTML.handle(c.HorizontalRule)
def handle_hr(state, obj):
    return '<hr />'


@HTML.handle(c.Anchor)
def handle_a(state, obj):
    return '<a href="{}">{}</a>'.format(
        obj.href.replace('"', '\\"'), state.f(obj.value))


@HTML.handle(c.Image)
def handle_img(state, obj):
    return '<img src="{}" alt="{}" />'.format(
        obj.src.replace('"', '\\"'), obj.alt.replace('"', '\\"'))


@HTML.handle(c.Header1)
def handle_h1(state, obj):
    return state.tag('h1', obj.components)


@HTML.handle(c.Header2)
def handle_h2(state, obj):
    return state.tag('h2', obj.components)


@HTML.handle(c.Header3)
def handle_h3(state, obj):
    return state.tag('h3', obj.components)


@HTML.handle(c.Header4)
def handle_h4(state, obj):
    return state.tag('h4', obj.components)


@HTML.handle(c.Header5)
def handle_h5(state, obj):
    return state.tag('h5', obj.components)


@HTML.handle(c.Header6)
def handle_h6(state, obj):
    return state.tag('h6', obj.components)


@HTML.handle(c.Footer)
def handle_footer(state, obj):
    return state.tag('footer', obj.components)


@HTML.handle(c.Small)
def handle_small(state, obj):
    return state.tag('small', obj.components)


@HTML.handle(c.Cite)
def handle_cite(state, obj):
    return state.tag('cite', obj.components)


@HTML.handle(c.Italic)
def handle_i(state, obj):
    return state.tag('i', obj.components)


@HTML.handle(c.Bold)
def handle_b(state, obj):
    return state.tag('b', obj.components)


@HTML.handle(c.Blockquote)
def handle_blockquote(state, obj):
    return state.tag('blockquote', obj.components)


@HTML.handle(c.Pre)
def handle_pre(state, obj):
    return state.tag('pre', obj.components)


@HTML.handle(c.Code)
def handle_code(state, obj):
    return state.tag('code', obj.components)


@HTML.handle(c.Del)
def handle_del(state, obj):
    return state.tag('del', obj.components)


@HTML.handle(c.Section)
def handle_section(state, obj):
    return state.tag('section', obj.components)


@HTML.handle(c.Paragraph)
def handle_p(state, obj):
    return state.tag('p', obj.components)


@HTML.handle(c.Span)
def handle_span(state, obj):
    return state.tag('span', obj.components)


@HTML.handle(c.OrderedList)
def handle_ol(state, obj):
    return state.tag('ol', obj.components)


@HTML.handle(c.UnorderedList)
def handle_ul(state, obj):
    return state.tag('ul', obj.components)


@HTML.handle(c.ListItem)
def handle_li(state, obj):
    return state.tag('li', obj.components)


@HTML.handle(c.Table)
def handle_table(state, obj):
    return state.tag('table', obj.components)


@HTML.handle(c.TableHeader)
def handle_th(state, obj):
    return state.tag('th', obj.components)


@HTML.handle(c.TableRow)
def handle_tr(state, obj):
    return state.tag('tr', obj.components)


@HTML.handle(c.TableData)
def handle_td(state, obj):
    return state.tag('td', obj.components)