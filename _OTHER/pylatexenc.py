import re, sys
from pylatexenc.latex2text import LatexNodes2Text
# Reads MD, converts $latex$ to Unicode
print(re.sub(r'\$(.*?)\$', lambda m: LatexNodes2Text().latex_to_text(m.group(1)), sys.stdin.read()))