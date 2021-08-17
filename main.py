import tkinter as tk
import threading
import app
import global_
import locker


LABEL = "Beep Beep Bot, press run to begin..."  # Set Welcome Message
LABELF = "This is not the original copy, please find @ristoniamage to get your hands on the bot today"
BACKGROUND_URL = 'logo.png' # Ensure that its the same folder // provide full path
ERROR_MSG = "Click Exit to restart BEEP BEEP BOT / start Ristonia if its not yet running"
WINDOW_SIZE = '420x200'
ICON2_NAME = 'spotify.ico'


class App :
    def __init__(self, master) :
        self.master = master

        self.label = tk.Label(self.master, text=LABEL, font="Roboto 12 bold")
        self.label.pack(pady=5)

        self.t1 = threading.Thread(target=app.startApp)
        self.t1.daemon = True
        self.font = ("Roboto", 10)

        # PLAY/PAUSE BUTTON
        """
        self.pause_button = tk.StringVar()
        self.pause_button.set('Set your macro-pause button') #default key
        self.pause_options = tk.OptionMenu(self.master, self.pause_button, *global_.KEYBOARD_KEYS)
        self.pause_options.config(font=self.font, bg='black', fg="white")
        self.pause_options.pack()
        """

        self.start_btn = tk.Button(self.master,
                                   state=tk.NORMAL,
                                   text="Start Detector",
                                   font=self.font,
                                   bg='black',
                                   fg="white",
                                   width=15,
                                   command=self.start_app)
        self.start_btn.pack(pady=2)

        self.end_btn = tk.Button(self.master,
                                 state=tk.DISABLED,
                                 text="Exit",
                                 font=self.font,
                                 bg='black',
                                 fg='white',
                                 width=15,
                                 command=self.quit_app)
        self.end_btn.pack(pady=2)


    def start_app(self) :
        if self.start_btn['state'] == tk.NORMAL :
            # global_.PAUSE_BUTTON = self.pause_button.get()
            global_.BOT_RUNNING = True
            self.t1.start()
            self.start_btn['state'] = tk.DISABLED
            self.end_btn['state'] = tk.NORMAL
            self.label['text'] = "Scanning in progress..."
            print(f'Thread started... \n Pause button: {global_.PAUSE_BUTTON} \n BOT STATUS: {global_.BOT_RUNNING}')
            if not self.t1.is_alive():
                global_.BOT_RUNNING = False
                self.label['text'] = "Error: Ristonia not found / Client error (please restart)"



    def quit_app(self) :
        del self.t1
        self.master.destroy()


if __name__ == "__main__" :
    is_licensed = locker.test_activation()
    if is_licensed:
        window = tk.Tk()
        window.iconbitmap(ICON2_NAME)
        window.title("Spotify")
        window.geometry(WINDOW_SIZE)

        # place the background
        bg = tk.PhotoImage(file=BACKGROUND_URL)
        background = tk.Label(window, image=bg)
        background.place(x=0, y=0)

        app = App(window)
        window.mainloop()
    else:
        window = tk.Tk()
        window.iconbitmap(ICON2_NAME)
        window.title("Copyrighted by Ristoniamage")
        labelF = tk.Label(window, text=LABELF, font="Roboto 12 bold")
        labelF.pack(pady=5)
        window.mainloop()
