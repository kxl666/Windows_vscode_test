from PIL import Image

# 1.处理Image数据类型
Image = Image.open('./File/test.png')  # 打开图片
print(Image.size)  # (width, height)
print(Image.mode)  # 'RGB'
print(Image.format)  # 'PNG'
print(Image.getpixel((0, 0)))  # (255, 255, 255)
print(Image.format_description)  # 'PNG (Portable Network Graphics)'

Im = Image.new('RGBA', (100, 100), '#FF0000')  # 创建一个新图片
Im.save('./File/test02.png')  # 保存图片
