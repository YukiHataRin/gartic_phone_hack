from PIL import Image, ImageFilter
import keyboard
import mouse
import threading
import time
import os
import random

class Auto_Drawing():
    def __init__(self):
        pass

    def run(self, pic):
        pic = pic.convert("L")
        self.width, self.height = pic.size
        self.pix = pic.load()
        self.__auto_draw()
        pic.save(os.path.join("img", "result.jpg"))

    def __auto_draw(self):
        keyboard.wait('ctrl')
        start_pos = mouse.get_position()
        point_pos = []

        for i in range(self.width):
            for j in range(self.height):
                if self.pix[i, j] <= 200:
                    point_pos.append((i, j))

        random.shuffle(point_pos)
        self.count = 0

        for i in point_pos:
            mouse.move(start_pos[0] + i[0], start_pos[1] + i[1])
            mouse.click()
            self.count += 1

            if self.count % 10 == 0:
                time.sleep(0.01)
                self.count = 0