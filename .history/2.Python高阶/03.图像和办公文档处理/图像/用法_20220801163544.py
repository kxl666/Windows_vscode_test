from PIL import Image

# from PIL.Image import

# 查看图像的基本信息
Image1 = Image.open('./File/test.png')  # 打开图片
print(Image1.size)  # (width, height)
print(Image1.mode)  # 'RGB'
print(Image1.format)  # 'PNG'
print(Image1.getpixel((0, 0)))  # (255, 255, 255)
print(Image1.format_description)  # 'PNG (Portable Network Graphics)'
print(Image1.info)  # 查看图片相关信息
# Image.save('./File/test.png')

# 处理图像数据类型
# 剪切图片
cropImage = Image1.crop((0, 0, 600, 600))
# cropImage.show()

# 缩放图片
resizeImage = Image1.resize((600, 600))
# resizeImage.show()

# 旋转图片
rotateImage = Image1.rotate(45)
# rotateImage.show()
# 水平翻转图片
# transposeImage = Image1.transpose(Image.FLIP_LEFT_RIGHT)
# transposeImage.show()
# 垂直翻转图片
# transverseImage = Image1.transverse(Image.FLIP_TOP_BOTTOM)
# transverseImage.show()

# 复制粘贴图片
copyImage = cropImage.copy()
pasteImage = Image1.copy()
# pasteImage.paste(copyImage, (400, 500))
# pasteImage.show()
# 铺满图片
# copyHigh, copyWidth = copyImage.size
# pasteHigh, pasteWidth = pasteImage.size
# pasteImage2 = pasteImage.copy()
# for left in range(0, pasteWidth, copyWidth):
#     for top in range(0, pasteHigh, copyHigh):
#         pasteImage2.paste(copyImage, (left, top))
# pasteImage2.show()

# 模式转换
# 将图片转换为灰度图
# grayImage = Image1.convert('L')
# grayImage.show()
# 将图片转换为黑白图
# blackWhiteImage = Image1.convert('1')
# blackWhiteImage.show()
# 将图片转换为彩色图
# colorImage = Image1.convert('RGB')
# colorImage.show()

# 分离与合并
# 分离图片的通道
im = Image.open('./File/spider.jpg')
r, g, b = im.split()
r.show()
# g.show()
# b.show()
