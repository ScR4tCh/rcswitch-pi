'''
Created on Sep 29, 2014

@author: scratch
'''
class DummySwitch():
    def __init__(self):
        pass
    
    def enableTransmit(self, *args):
        pass
    
    def disableTransmit(self):
        pass
    
    def enableLEDNotify(self, *args):
        pass
    
    def switchOn(self, syscode,devcode):
        print("DUMMY : "+str(syscode)+"."+str(devcode)+"  ON")
    
    def switchOff(self,syscode,devcode):
        print("DUMMY : "+str(syscode)+"."+str(devcode)+"  OFF")

    def send(self,data,dlength):
        print("DUMMY : "+str(data)+" length="+str(dlength))

