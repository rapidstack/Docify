from docify.lib.components import Text


class Document(object):
    '''The base document object.
    It can be passed as input to different formatters which can parse
    it into various formats.

    :param Component[] components: Components to be added in the document.
    
    Example usage: ::

        doc = Document(P('Hail Docify!'))
        print(HTML(doc))
        print(Markdown(doc))
        print(Whatever(doc))
    '''

    def __init__(self, *components):
        self.components = []
        self.depth = 0
        for c in components:
            self.add(c)

    def __repr__(self):
        return '{}(\n{}{})'.format(
            self.__class__.__name__, ' ' * (self.depth + 1) * 4,
            ('\n' + (' ' * (self.depth + 1) * 4)).join(map(str, self.components)))

    def add(self, component):
        '''Adds a component in the doc.

        :param Component component: Component to be added
        '''
        if isinstance(component, str):
            component = Text(component)
        component.setparent(self)
        component.setdepth(self.depth+1)
        
        if len(self.components) > 0:
            self.components[-1].setnext(component)
        
        self.components.append(component)
