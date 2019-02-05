import re

from docify.lib.formatter import Formatter
from docify import Document, components as c


class Markdown(Formatter):
    '''Markdown formatter to format document into plain markdown.'''

    newline_types = set([
        c.Blockquote, c.Break, c.Footer, c.Header1,
        c.Header2, c.Header3, c.Header4, c.Header5,
        c.Header6, c.HorizontalRule, c.OrderedList,
        c.Paragraph, c.Pre, c.Section, c.Table, c.UnorderedList
    ])

    def __init__(self, *args, **kwargs):
        self._last = None
        self._doc = ''
        super(Markdown, self).__init__(*args, **kwargs)
    
    def render(self, component, fmt='{}'):
        '''Helps rendering component
        
        :param Component component: Component to render
        '''
        if self._last is not None:
            if type(self._last) in self.newline_types:
                fmt = '\n' + fmt
            if (type(component) in self.newline_types
                and type(self._last) not in self.newline_types):
                fmt = '\n' + fmt
        self._last = component
        return fmt.format(self.f(component))

    def update_handlers(self):
        '''Overriding parent method'''

        super(Markdown, self).update_handlers()

        @self.handle(Document)
        def handle_doc(self, obj):
            return ''.join(map(self.render, obj.components))

        @self.handle(c.Text)
        def handle_text(self, obj):
            return re.sub(r'((([_*]).+?\3[^_*]*)*)([_*])', r'\g<1>\\\\\g<4>', obj.value)

        @self.handle(c.Nbsp)
        def handle_nbsp(self, obj):
            return ' '

        @self.handle(c.Break)
        def handle_br(self, obj):
            return '\n\n'

        @self.handle(c.HorizontalRule)
        def handle_hr(self, obj):
            return '--------------------\n'

        @self.handle(c.Anchor)
        def handle_a(self, obj):
            return '[{}]({})'.format(self.f(obj.value), obj.props['href'])

        @self.handle(c.Image)
        def handle_img(self, obj):
            return '![{}]({})'.format(obj.props['alt'], obj.props['src'])

        @self.handle(c.Footer, c.Small, c.Section, c.Paragraph, c.Span)
        def handle_default(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)))

        @self.handle(c.Header1)
        def handle_h1(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)),
                '{}\n===============\n')

        @self.handle(c.Header2)
        def handle_h2(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)),
                '{}\n---------------\n')

        @self.handle(c.Header3)
        def handle_h3(self, obj):
            return self.render(obj.components, '### {}\n')

        @self.handle(c.Header4)
        def handle_h4(self, obj):
            return self.render(obj.components, '#### {}\n')

        @self.handle(c.Header5)
        def handle_h5(self, obj):
            return self.render(obj.components, '##### {}\n')

        @self.handle(c.Header6)
        def handle_h6(self, obj):
            return self.render(obj.components, '###### {}\n')

        @self.handle(c.Cite, c.Italic)
        def handle_cite_i(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)), '*{}*')

        @self.handle(c.Bold)
        def handle_b(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)), '**{}**')

        @self.handle(c.Blockquote)
        def handle_blockquote(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)), '> {}\n')

        @self.handle(c.Pre)
        def handle_pre(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)), '```\n{}\n```\n')

        @self.handle(c.Code)
        def handle_code(self, obj):
            if type(obj.parent) != c.Pre:
                return self.render(
                    ''.join(map(self.f, obj.components)), '```\n{}\n```\n')
            return self.render(
                ''.join(map(self.f, obj.components)))

        @self.handle(c.Del)
        def handle_del(self, obj):
            return self.render(
                ''.join(map(self.f, obj.components)), '~~{}~~')

        # @self.handle(c.OrderedList)
        # def handle_ol(self, obj):
        #     return self.tag('ol', obj.components, obj.props)

        # @self.handle(c.UnorderedList)
        # def handle_ul(self, obj):
        #     return self.tag('ul', obj.components, obj.props)

        # @self.handle(c.ListItem)
        # def handle_li(self, obj):
        #     return self.tag('li', obj.components, obj.props)

        # @self.handle(c.Table)
        # def handle_table(self, obj):
        #     return self.tag('table', obj.components, obj.props)

        # @self.handle(c.TableHeader)
        # def handle_th(self, obj):
        #     return self.tag('th', obj.components, obj.props)

        # @self.handle(c.TableRow)
        # def handle_tr(self, obj):
        #     return self.tag('tr', obj.components, obj.props)

        # @self.handle(c.TableData)
        # def handle_td(self, obj):
        #     return self.tag('td', obj.components, obj.props)