class RecordMode:
    def __init__(self):
        self.__Recording=False
        self.__Playing=False
        self.__RecordMode=False
        self.__KeySet=[]
        self.track=[]

    def getRecording(self):
        return self.__Recording
    
    def getKeySet(self):
        return self.__KeySet

    def getPlaying(self):
        return self.__Playing
    
    def setRecording(self,Recording):
        self.__Recording=Recording
        return None
    def setRecordMode(self,RecordMode):
        self.__RecordMode=RecordMode
    def getRecordMode(self):
        return self.__RecordMode
    def setKeySet(self,keydata):
        self.__KeySet.append(keydata)

if __name__=="__main__":
    print("This is RecordControl module")