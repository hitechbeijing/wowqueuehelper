import sys,os,re,time,pyautogui
from config import config
class wow_reconnect(config):
    def __init__(self):
        super(wow_reconnect, self).__init__(config)
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        rootPath = sys.path[0]
        os.chdir(rootPath)
    def check_state(self):
        while True:
            try:
                with open(self.log_path.replace('\\',''), 'r') as f:
                    lines = f.readlines()
                    last_line = lines[-1]
                    print(self)
                if last_line is not None and last_line!='':
                   pattern = re.compile('Destroy|Destroyed')
                   m = pattern.search(str(last_line))
                   print(last_line)
                   if m is not None:
                      self.killAll()
                      self.restartGame()
                      break
                      exit()
                   else:
                      print("尚未掉线")
                else:
                    print("游戏还未运行")
                    break
                    exit()
                time.sleep(60)
            except(KeyboardInterrupt):
                print("Mission abort")
                exit()

    def killAll(self):
        os.system("ps -ef | grep "+self.wow_app_name+" | awk '{print $2}' | xargs kill -9")
        os.system("ps -ef | grep "+self.launcher_name+" | awk '{print $2}' | xargs kill -9")
    def restartGame(self):
        os.system("open "+self.launcher_path+" --args "+self.args)
        time.sleep(10)
        coords = pyautogui.locateOnScreen(self.start_button_img)
        x,y=pyautogui.center(coords)
        pyautogui.leftClick(x/2,y/2)
        print("游戏重启完成")