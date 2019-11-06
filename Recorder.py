import pyaudio
import threading
import wave


class Recorder():
    def __init__(self,chunk=1024,channels=1,rate=64000):
        self.CHUNK=chunk
        self.CHANNELS=channels
        self.FORMAT=pyaudio.paInt16
        self.RATE=rate
        self.__running =True
        self.__FRAMES=[]

    def start(self):
        print("recording")
        threading._start_new_thread(self.__recording,())

    def __recording(self):
        self._running=True
        self._FRAMES=[]
        p=pyaudio.PyAudio()
        stream=p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        while(self._running):
            data=stream.read(self.CHUNK)
            self._FRAMES.append(data)
        stream.stop_stream()
        stream.close
        p.terminate

    def stop(self):
        print("stop")
        self._running=False
    
    def save(self,filename):
        p =pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename+=".wav"
        wf=wave.open(filename,'wb')
        
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._FRAMES))
        wf.close()
        print("saved "+filename)
    
    def isRecording(self):
        return self._running

if __name__=="__main__":
    print("This is RecorderModule")