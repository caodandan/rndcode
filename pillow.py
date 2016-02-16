from PIL import Image, ImageFilter
im=Image.open('test.jpg')
w,h=im.size
print('original image size: %sx%s'%(w,h))
im.thumbnail((w//3,h//2))
print('resuze image to: %sx%s'%(w//3,h//2))
im.save('thumbnail.jpg','jpeg')

im1=Image.open('test.jpg')
im2=im1.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
print('blur image is below:')