import sys
import clipboard
import json

data = clipboard.paste()
print(data)

clipboard.copy("abc")