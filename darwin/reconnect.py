import sys,os,re,time,pyautogui
from config import config
class wow_reconnect(config):
    def __init__(self):
        super(wow_reconnect, self).__init__(config)
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        rootPath = sys.path[0]
        os.chdir(rootPath)
    def check_state(self,login=False):
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
                   if m is not None and login==False:
                       self.killAll()
                       self.restartGame()
                       break
                       exit()
                   elif m is not None and login==True:
                       self.killAll()
                       self.autoLogin()
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
    def autoLogin(self):
        if self.account and self.password:
            os.system("open "+self.wow_path)
            time.sleep(10)
            coords_account = pyautogui.locateOnScreen(self.account_img,confidence=0.9)
            account_input_x, account_input_y = pyautogui.center(coords_account)
            pyautogui.leftClick(account_input_x/2,account_input_y/2)
            pyautogui.write(self.account, interval=0.25)
            time.sleep(2)
            coords_password = pyautogui.locateOnScreen(self.password_img,confidence=0.9)
            password_input_x, password_input_y = pyautogui.center(coords_password)
            pyautogui.leftClick(int(password_input_x/2),int(password_input_y/2))
            pyautogui.write(self.password, interval=0.25)
            time.sleep(2)
            coords_login = pyautogui.locateOnScreen(self.login_img,confidence=0.9)
            login_x, login_y = pyautogui.center(coords_login)
            pyautogui.leftClick(login_x/2,login_y/2)
            print("游戏重启完成")
            return True
        else:
            print("游戏账号信息未填写")
            return False
