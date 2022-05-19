from sqlite3 import ProgrammingError
from turtle import width
from moviepy.editor import *
from datetime import datetime
import os
from pytz import timezone

duration = 5

# Load template video
clip = VideoFileClip("video/template.mp4").subclip(0,duration)

# Load fonts
font_regular = 'signika/Signika-Regular.otf'
font_lite = 'signika/Signika-Lite.otf'
font_bold = 'signika/Signika-Bold.otf'
font_semibold = 'signika/Signika-Semibold.otf'
font_museo_sans = 'signika/MuseoSansRounded-300.ttf'

# Default settings for date text
date_font_size = 40
date_font_y = 1112
date_font = font_museo_sans
date_font_color = b'gray45'

# Default settings for name text
name_font_size = 57
name_font_y = 1206
name_font = font_museo_sans
name_font_color = b'white'

# Default settings for number text
number_font_size = 38
number_font_y = 1282
number_font = font_museo_sans
number_font_color = b'gray51'

# Default settings for amount text
amount_font_size = 94
amount_font_y = 1375
amount_font = font_museo_sans
amount_font_color = b'white'

class Payment:
    @classmethod
    def __init__(self,namn,nummer,belopp,created_at,id):

        self.date_text = get_text(get_date(created_at),date_font,date_font_size,date_font_color,date_font_y)
        self.name_text = get_text(get_name(namn),name_font,name_font_size,name_font_color,name_font_y)
        self.number_text = get_text(get_number(nummer),number_font,number_font_size,number_font_color,number_font_y)
        self.amount_text = get_text(get_amount(belopp),amount_font,amount_font_size,amount_font_color,amount_font_y)

        self.outname = f"video/{id}"
        self.mp4 = self.outname+".mp4"

        self.video = CompositeVideoClip([clip, self.date_text , self.name_text , self.number_text , self.amount_text])

        self.video.write_videofile(self.mp4,fps=15)
        
    
    def close(self):
        self.video.close()

        if os.path.exists(self.mp4):
            os.remove(self.mp4)

def get_date(time: datetime):
    swishday = {
        "Sun": "Sön",
        "Mon": "Mån",
        "Tue": "Tis",
        "Wed": "Ons",
        "Thu": "Tor",
        "Fri": "Fre",
        "Sat": "Lör",
    }
    time = time.astimezone(timezone("Europe/Stockholm"))
    return time.strftime("%d ")+ time.strftime("%b.").lower() +time.strftime(" %Y, kl %H:%M")

def get_name(name):
    return str(name).title()

def get_number(number):
    number =  str(number)
    return number

def get_amount(amount):
    return str(amount)+" kr"

def get_text(text,font,fontsize,color,y):
    txt_clip = TextClip(text,font = font,fontsize=fontsize,color=color)
    txt_clip = txt_clip.set_position(('center',y)).set_duration(duration)
    return txt_clip