import pytesseract
from PIL import Image
import requests

re = requests.get('http://my.cnki.net/elibregister/CheckCode.aspx')
with open('code.jpg', 'wb') as f:
    f.write(re.content)
