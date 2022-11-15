import camelcase
from camelcase import CamelCase

c = CamelCase()
s  = 'this is a sentence that needs CamelCasing!'
print(c.hump(s))