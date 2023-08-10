import io

with io.StringIO('Hello World') as s:
    s.seek(11)
    print(s.read())
    s.write('BLA')
    print(s.tell())
    print(s.read())
    print(s.getvalue())
    print(s.closed)
print(s.closed)

import requests
