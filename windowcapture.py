import win32gui, win32ui, win32con
import numpy as np

WINDOW_NAME = 'XXX'


class WindowCapture:
    h = 0
    w = 0
    hwnd = None
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name=WINDOW_NAME):
        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception(f"Window not found: {window_name}")

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        self.offset_y = window_rect[1]
        self.offset_x = window_rect[0]

    @staticmethod
    def list_window_names() :
        def winEnumHandler(hwnd, ctx) :
            if win32gui.IsWindowVisible(hwnd) :
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screenshot(self) :
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (0, 0), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # Drop the alpha channel
        img = img[..., :3]
        img = np.ascontiguousarray(img)

        return img


    def get_offset(self):
        return self.offset_x, self.offset_y



