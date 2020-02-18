# wowqueuehelper
魔兽世界排队助手
魔兽怀旧服每天上午11点不到就开始排队，到了中午更是需要排队5小时以上，不得已写了这个程序。
<p>功能</p>
1、设置时间自动排队
2、掉线重新启动游戏（掉线15分钟内免排队）
![alt](https://github.com/hitechbeijing/wowqueuehelper/raw/master/cmd.png)
<p>依赖说明</p>
python 3.6+
使用pip3 install -r requirements.py安装依赖库
<p><b>强烈建议配置阿里巴巴开源镜像库：<b></p>
、、、shell
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
、、、
<p>使用说明</p>
配置config.py
使用python3 main.py --queue启动自动排队
使用python3 main.py --reconnect自动重连

