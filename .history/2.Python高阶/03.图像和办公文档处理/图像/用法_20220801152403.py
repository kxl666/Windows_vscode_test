from PIL import Image

# 1.处理Image数据类型
Image = Image.open('./File/test.png')  # 打开图片
print(Image.size)  # (width, height)
print(Image.mode)  # 'RGB'
print(Image.format)  # 'PNG'
print(Image.getpixel((0, 0)))  # (255, 255, 255)
print(Image.format_description)  # 'PNG (Portable Network Graphics)'

# 创建一个新图片
Image2 = Image.new('RGB', (200, 200), '#FF0000')
Image2.save('./File/test2.png')  # 保存图片
