import os
import signal
import subprocess
import shlex
from time import sleep


def test_video():
    cmd = shlex.split('scrcpy --record tmp.mp4')
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # stdout = subprocess.PIPE 正确输出
    # stderr = subprocess.STDOUT 错误输出
    # scrcpy --record tmp.mp4
    '''
    SIGINT    终止进程     中断进程  (control+c)
    SIGTERM   终止进程     软件终止信号
    SIGKILL   终止进程     杀死进程
    SIGALRM   闹钟信号
    '''
    print(p)
    sleep(10)
    os.kill(p.pid, signal.SIGTERM)
