from system import pexp
from system import time
from system import speedtest_cli
import re
import os
import subprocess
from entertain import joke
import sys
sys.path.append("/home/blocks/softinst/liclipse/ohmygirl/src/entertain/alice")
import importlib
importlib.reload(sys)
from entertain.alice import mygirl

print("Hello sir, I'm your girl. Anything I can help?")

while(True):
    try:
        command=input("")
        
        if re.search(r'.*(could)?.*(what.*s|tell){1,}.*time.*|.{,5}time\??',command):
            time.getTime()
            print('\n')
        
        elif command.startswith('!'):
            realC=command[1:]
            res=subprocess.getoutput(realC)
            print('Sir, here is the result:\n'+res+'\n')
            
        elif re.search(r'(tell.*a|could.*tell|a).*joke.*(please)?',command):
            joke.output()
            print('\n')
            
        elif re.search(r'remote access',command):
            pexp.main()
            
        elif re.search('netspeed',command):
            speedtest_cli.main()
            
        elif re.search(r'.*chat.*',command):
            os.chdir('entertain/alice')
            mygirl.bot()
            
        elif re.match(r'^(q|b).*',command,flags=re.IGNORECASE):
            break
        
        else:
            print('Sorry Sir, I cannot understand that\n')
    
    except Exception as e:
        print(e)
        pass



    