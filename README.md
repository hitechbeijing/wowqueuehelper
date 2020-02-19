# wowqueuehelper
魔兽世界排队助手
魔兽怀旧服每天上午11点不到就开始排队，到了中午更是需要排队5小时以上，不得已写了这个程序。
<p>功能</p>
1、设置时间自动排队<br/>
2、掉线重新启动游戏（掉线15分钟内免排队）<br/>

![screenshot](https://github.com/hitechbeijing/wowqueuehelper/raw/master/cmd.jpg?raw=true)

## 依赖环境
python 3.6+
## 安装依赖：

```shell

pip3 install -r requirements.py

```

<p><b>强烈建议配置阿里巴巴开源镜像库：<b></p>
  
```shell
  
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

```
## 使用方法：<br/>
配置config.py<br/>
使用python3 main.py --queue启动自动排队<br/>
使用python3 main.py --reconnect自动重连<br/>
使用python3 main.py -R -A自动重连并且自动完成输入账号密码<br/>
<b>提示：为了提高图形识别准确率（可能受屏幕分辨率影响），最好自己截图替换account.jpg，password.jpg，login.jpg，button.jpg这四张图片</b><br/>
<b>后期考虑更换为文字识别的方式</b>

