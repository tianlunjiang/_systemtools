import re

RE_SUB = re.compile('\d+\.\d+')

str_code = "__VERSION__		= '13.1'"

new = RE_SUB.sub('2.5', str_code)
print(new)