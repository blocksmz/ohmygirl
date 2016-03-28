import subprocess

def getTime():
    sda=subprocess.getoutput('date +%F-%H-%M')
    print('Sir,the current time is :'+sda)

if __name__=="__main__":
    getTime()