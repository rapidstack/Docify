import os
import sys
from subprocess import Popen


EXAMPLES = [
    '0_quickstart',
    '1_readme'
]

FORMATS = [
    'markdown',
    'html',
    'htmlbootstrap'
]

if __name__ == '__main__':

    for e in EXAMPLES:
        examplepath = os.path.join('.', 'examples', e, 'doc.py')

        sys.stdout.write('\n* ' + examplepath + '-------------\n')

        assert Popen(['python', examplepath]).wait() == 0
        for f in FORMATS:
            assert Popen(['python', examplepath, f]).wait() == 0