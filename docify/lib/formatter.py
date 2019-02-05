import re
from copy import deepcopy

from docify.lib.document import Document


class Formatter(object):
    '''Abstract class for formatter. Do not use it directly.

    :param Document document: Document to format.
    '''

    handlers = {}

    def __init__(self, document):
        self.doc = self.format(deepcopy(document))

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