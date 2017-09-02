import autopy


ay = autopy
width, height = ay.screen.get_size()
img = ay.bitmap.capture_screen().save('screengrab.png')

print(width,height)
print(width)
print(height)
