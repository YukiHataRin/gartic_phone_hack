import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

class Get_Pic():
    def __init__(self):
        self.url_front = "https://www.google.com/search?q="
        self.url_rear = "&sxsrf=ALiCzsbyg5fxzCHqN20BMGjAQkzW77Y01A:1655881041162&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjRtv7JvcD4AhWxUN4KHWWEBagQ_AUoAXoECAEQAw&biw=1488&bih=792&dpr=1.25"

    def get_pic(self, keyword):
        html = requests.get(self.url_front + keyword + self.url_rear)
        soup = BeautifulSoup(html.text, "html.parser")
        
        pic_html = soup.find_all("img")[1:]
        pic = []

        for p in pic_html:
            img = Image.open(BytesIO(requests.get(p.get("src")).content))
            pic.append(img.resize((img.size[0] * 2, img.size[1] * 2)))

        return pic