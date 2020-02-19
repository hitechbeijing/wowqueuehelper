from queue import wow_queue
from reconnect import wow_reconnect
import argparse

def main():
   parser = argparse.ArgumentParser(description='魔兽世界排队助手')
   parser.add_argument('-Q','--queue',
                    help='自动登陆排队', action='store_true')
   parser.add_argument('-R','--reconnect',
                    help='掉线重新登陆',action='store_true')
   parser.add_argument('-A','--autologin',
                    help='自动填充账号密码登陆（即直接通过游戏主程序登陆）',action='store_true') 
   args = parser.parse_args()
   if args.queue==False and args.reconnect==False:
       parser.print_help()
   else:
       return args

if __name__ == '__main__':
    args=main()
    if args is not None and args.queue==True and args.reconnect==False:
        wow_queue=wow_queue()
        wow_queue.config_queue()
    if args is not None and args.reconnect==True and args.queue==False:
        wow_reconnect=wow_reconnect()
        if (args.autologin==True):
            wow_reconnect.check_state(login=True)
        else:
            wow_reconnect.check_state()

