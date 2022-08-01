from PIL import Image

# 1.处理Image数据类型
Image = Image.open('./File/test.png')  # 打开图片
print(Image.size)  # (width, height)
print(Image.mode)  # 'RGB'
print(Image.format)  # 'PNG'
print(Image.getpixel((0, 0)))  # (255, 255, 255)
print(Image.format_description)  # 'PNG (Portable Network Graphics)'
print(Image.info)  # 查看图片相关信息
# Image.save('./File/test.png')

# 2.处理图像数据类型
