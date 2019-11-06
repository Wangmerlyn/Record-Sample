from pynput.keyboard import Listener
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import threading
import pyaudio 
import wave

import RecordControl as rc  #记录按键，控制状态
import Recorder as recorder #录音器


def writetofile(key):
    keydata =str(key)
    print(keydata)
    if keydata=="Key.enter":
        Listener.stop()
    elif not Mode.getRecordMode():
        if keydata=="'r'":
            Mode.setRecordMode(True) #进入录音模式
            print("Recording mode ON\nSelect your Key")
        else:
            pass
    elif Mode.getRecordMode():  #如果处于录音模式
        if not Mode.getRecording():
            Mode.setRecording(True)
            a=recorder.Recorder()
            Mode.setKeySet(keydata) #没有开始录音
            Mode.track.append(a)    #开始录音，添加音轨
            a.start()   #录音开始
        elif Mode.getRecording() and keydata==Mode.getKeySet()[-1]:
            print("Recording mode On\nrecording stopped")
            Mode.setRecording(False)
            Mode.track[-1].stop()
            Mode.track[-1].save("track"+str(len(Mode.getKeySet())))
    with open("log.txt",'a') as f:
        f.write(str(time.clock())+":"+keydata+'\n')


if __name__=="__main__":
    plt.close('add')
    print (sd.query_devices())
    with Listener(on_press=writetofile) as Listener:
        print('a')
        Mode=rc.RecordMode()
        Listener.join()
    i=0
    print(i)