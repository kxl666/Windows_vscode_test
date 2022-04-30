import base64

content = 'Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight nowledge, exceeds the short vehemence of any carnal pleasure.'
print(base64.b64encode(content.encode()), "\n")
content = base64.b64encode(content.encode())
print(base64.b64decode(content).decode())
