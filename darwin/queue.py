import time,subprocess,datetime,json,os,sys
from config import config
from pykeyboard import PyKeyboard
import pyautogui
class wow_queue(config):
    # def __init__(self,parent=None):
    #     self.start_time='2020-02-20 10:40:00'
    #     self.timeArray = time.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        
    def config_queue(self):
        rootPath = sys.path[0]
        os.chdir(rootPath)
        try:
            self.timeArray = time.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        except(ValueError):
            print("开始时间格式错误")
            exit()
        self.tm_year=int(self.timeArray.tm_year)
        self.tm_mon=int(self.timeArray.tm_mon)
        self.tm_mday=int(self.timeArray.tm_mday)
        self.tm_hour=int(self.timeArray.tm_hour)
        self.tm_min=int(self.timeArray.tm_min)
        self.tm_ts=int(time.mktime(self.timeArray))
        print("排队开始时间为："+self.start_time)
        while True:
            try:
                now=int(time.time())
                if self.tm_ts-now<=0:
                   self.start_queue()
                if self.tm_ts<now:
                   print("排队开始时间小于当前时间")
                   break
                   exit()
                time_left=self.tm_ts-now
                m, s = divmod(time_left, 60)
                h, m = divmod(m, 60)
                print("距离排队开始还有：%02d时%02d分%02d秒" % (h, m, s))
                time.sleep(60)
                self.start_queue()
            except(KeyboardInterrupt):
                print("定时中止")
                break
                exit()
            
            
    def start_queue(self):
        try:
            os.system('/usr/bin/open '+self.launcher_path+" --args "+self.args)
            time.sleep(10)
            pyautogui.FAILSAFE = True
            pyautogui.PAUSE = 0.5
            coords = pyautogui.locateOnScreen('./button.jpg')
            x,y=pyautogui.center(coords)
            pyautogui.leftClick(x/2,y/2)
            # k = PyKeyboard()
            # k.tap_key('Return')
            exit()
        except(KeyboardInterrupt):
            print("定时中止")
            exit()

