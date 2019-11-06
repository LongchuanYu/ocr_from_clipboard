import tkinter
import time
import win32clipboard as w
from PIL import Image,ImageGrab
from pytesseract import image_to_string

# top = tkinter.Tk()
def get_gray_image_from_cb():
    img = ImageGrab.grabclipboard()
    if isinstance(img,Image.Image):
        return img.convert('L')
    return None
def get_image_from_local():
    img = Image.open('3.png')
    text = image_to_string(img)
    return text

def main():
    img = get_gray_image_from_cb()
    if not img:
        return 
    try:
        txt = image_to_string(img)
        print(txt)
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardText(txt)
        w.CloseClipboard()
    except:
        pass
while True:
    main()
    time.sleep(2)
# B = tkinter.Button(top, text ="点我", command = get_image_from_cb)
# B.pack()
# top.mainloop()