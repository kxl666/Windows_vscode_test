from PIL import Image, ImageDraw, ImageFilter

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
# im = Image.open('./File/spider.jpg')
# r, g, b = im.split()
# r.show()
# g.show()
# b.show()
# 合并图片的通道
# im2 = Image.merge('RGB', (r, g, b))
# im2.show()
# blend,多了一个参数，blend_alpha透明度
# im3 = Image.blend(im, im2, 0.3)
# im3.show()

# 模糊处理
# 模糊图片
blurImage = Image1.filter(ImageFilter.BLUR)
# blurImage.show()
# 浮雕图片
# embossImage = Image1.filter(ImageFilter.EMBOSS)
# embossImage.show()
# 轮廓图图片
# contourImage = Image1.filter(ImageFilter.CONTOUR)
# contourImage.show()
# 边缘检测图片
# detailImage = Image1.filter(ImageFilter.FIND_EDGES)
# detailImage.show()
# 高饱和度图片
# edgeImage = Image1.filter(ImageFilter.EDGE_ENHANCE)
# edgeImage.show()
# 平滑图片
# smoothImage = Image1.filter(ImageFilter.SMOOTH)
# smoothImage.show()

# 为图片添加水印
# ImageDraw
im = Image.new('RGB', (200, 200), color='gray')  # 创建一个灰色的图片
draw = ImageDraw.Draw(im)  # 创建一个画笔
# 以左上角为原点，绘制矩形。元组坐标序列表示矩形的位置、大小；fill设置填充色为红色，outline设置边框线为黑色。
# text	在图像上绘制文字，line	绘制直线、线段，eclipse	绘制椭圆形，rectangle	绘制矩形，polygon	绘制多边形
draw.rectangle((50, 100, 100, 150), fill=(255, 0, 0), outline=(0, 0, 0))
# im.show()
# ImageFont
