import itchat
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    #发送"午安"给文件助手
    iRoom = itchat.search_chatrooms(name='闲置')
    if len(iRoom)==0:
        itchat.send("没找到群。", toUserName="filehelper")
        print('No group found')
        
    else:
        for room in iRoom:
                gn = room['UserName']
                break
        itchat.send_image('/home/moyuge/code/screen.jpg', toUserName=gn)
        itchat.send("320出24寸曲面屏，可刀。", toUserName=gn)
        print('Message has been sent to',room['NickName'])
    
sched = BlockingScheduler()

# 任务会在每天中午12：00触发
sched.add_job(job_function,'cron',hour='8-23/3',jitter=600)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    print('login_passed')
    itchat.send("开工了。", toUserName="filehelper")
    sched.start()
    itchat.run()
