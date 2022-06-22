import cls
import os
import threading
import keyboard

def force_exit():
    keyboard.wait("ctrl+z")
    os._exit(0)

app = cls.MainWindow.MainWindow()
threading.Thread(target = force_exit, daemon = True).start()
app.start_app()
