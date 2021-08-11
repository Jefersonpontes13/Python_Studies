"""coding: utf-8"""

import itertools
import string

resultado = itertools.permutations(string.ascii_letters, 8)

for i in resultado:
    print(''.join(i))
