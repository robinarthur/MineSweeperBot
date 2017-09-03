import autopy
import opencv

ay = autopy
width, height = ay.screen.get_size()
img = ay.bitmap.capture_screen().save('screengrab.png')

print(width,height)
print(width)
print(height)

blue_MIN = np.array([255, 176, 98])
blue_MAX = np.array([255, 211, 128])

for w_pixel in width:
    for h_pixel in height:
