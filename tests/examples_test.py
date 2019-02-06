import os
import sys
from subprocess import Popen, PIPE


EXAMPLES = [
    '0_quickstart',
    '1_readme'
]

FORMATS = {
    'markdown': 'result.md',
    'html': 'result.html',
    'htmlbootstrap': 'result.withbootstrap.html',
    'raw': 'result.raw.txt'
}

if __name__ == '__main__':

    for e in EXAMPLES:
        examplepath = os.path.join('examples', e)
        docpath = os.path.join(examplepath, 'doc.py')

        sys.stdout.write('\n* ' + docpath + ' -------------\n')

        assert Popen(['python', docpath]).wait() == 0
        for f in FORMATS:
            resultpath = os.path.join(examplepath, FORMATS[f])
            p = Popen(['python', docpath, f], stdout=PIPE)
            stdout, _ = p.communicate()
            assert p.returncode == 0

            with open(resultpath, 'wb') as f:
                f.write(stdout)
