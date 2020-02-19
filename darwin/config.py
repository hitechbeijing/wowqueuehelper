class config:
    def __init__(self,parent=None):
        #魔兽世界启动器路径
        self.launcher_path="/Applications/Battle.net.app"
        #魔兽世界启动器名称
        self.launcher_name="Battle.net.app"
        #启动参数(--gamepath改成魔兽世界所在目录)
        self.args="--game=wow_zhcn --gamepath=/Applications/World\ of\ Warcraft"
        #魔兽主程序路径
        self.wow_path="/Applications/World\ of\ Warcraft/_classic_/World\ of\ Warcraft\ Classic.app"
        #魔兽主程序名称
        self.wow_app_name="World\ of\ Warcraft\ Classic.app"
        #排队开始时间,格式%Y-%m-%d %H:%M:%S
        self.start_time="2020-2-17 16:30:00"
        #魔兽世界客户端日志路径
        self.log_path="/Applications/World\ of\ Warcraft/_classic_/Logs/Client.log"
        #开始游戏按钮截图
        self.start_button_img="./button.jpg"
        #账号输入框图片
        self.account_img="./account.jpg"
        #密码输入框图片
        self.password_img="./password.jpg"
        #游戏登陆按钮图片
        self.login_img="./login.jpg"
        #以下选项仅在启用自动登陆时需要
        #游戏账号
        self.account=""
        #游戏密码
        self.password=""