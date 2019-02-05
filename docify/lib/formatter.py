import re
from copy import deepcopy

from docify import Document, components as c


class Formatter(object):
    '''Abstract class for formatter. Do not use it directly.

    :param Document document: Document to format.
    :param bool cite: Whether to add the grumpy citation. Default is True.
    '''

    handlers = {}

    def __init__(self, document, cite=True):
        raw_doc = deepcopy(document)
        if cite:
            raw_doc.add(c.Hr())
            raw_doc.add(c.Footer(c.P(c.Small(c.Cite(
                'This document was generated with ',
                c.A('https://github.com/rapidstack/Docify', 'Docify'))))))
        self.doc = self.format(raw_doc)

    @classmethod
    def handle(cls, *items):
        '''handle decorator. Register a handler for given item.
        
        :param list items: List of items to handle.

        Example usage: ::

            @MyFormatter.handle(Document)
            def handle_doc(state, doc):
                return str(doc)
        '''
        return lambda func: [cls.handlers.update({i: func}) for i in items]

    def format(self, obj):
        '''Parse and format an object.

        :param Component|Document obj: Object to format.
        '''
        otype = type(obj)
        if otype not in self.handlers:
            return str(obj)
        return self.handlers[otype](self, obj)

    def __repr__(self):
        return self.doc


# Alias for format method
Formatter.f = Formatter.format