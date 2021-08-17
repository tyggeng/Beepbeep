import cv2 as cv
from windowcapture import WindowCapture
import winsound
import os
import global_
import time


def startApp() :
    try :
        wincap = WindowCapture()

        # TODO: Allow users to choose the folder for the primary scan (drop-down list to choose things to scan for)
        dir = 'primary_scans'
        print('Waiting for rune...')

        while True :
            screenshot = wincap.get_screenshot()
            offset = wincap.get_offset()

            for filename in os.listdir(dir) :
                f = os.path.join(dir, filename)
                scan_temp = cv.imread(f)
                result = cv.matchTemplate(screenshot, scan_temp, cv.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

                if max_val >= 0.85 :
                    identifier = filename.split('.')[0][:2]
                    print(f'Detected: {identifier}\nScreen Loc: {offset}\nLocation of item: {max_loc}\n')
                    if identifier == 'gu' or identifier == 'pu' :
                        winsound.PlaySound(os.path.join(os.getcwd(), 'player_alarm.wav'), winsound.SND_FILENAME)
                    else :
                        winsound.PlaySound(os.path.join(os.getcwd(), 'alarm.wav'), winsound.SND_FILENAME)
                        # TODO: Keyboard press having issues -> sending the f5 when the maplestory window is not up
                        if filename[:2] == "ld" :
                            print("LD detected...")
                            # pause the macro, click, type in stuffs (random) > will crash maple
                            time.sleep(1)
                            print(f'Screen clicked at {max_loc}')
                            print('typing to crash... jKFllmP')

                            time.sleep(15)
                            global_.BOT_RUNNING = False
                            exit()
                        else :
                            print("pressing pause on rune...")
                            time.sleep(3)

    except :
        pass

    finally :
        exit()


if __name__ == '__main__' :
    startApp()
