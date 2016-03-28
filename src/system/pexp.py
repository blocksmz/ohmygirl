import pexpect

def girlssh():
    
    your_sship='139.59.246.196'
    your_sshport='10001'
    your_sshUserName='blocks'
    qus=input('Use default configuration? (yes|no)')
    if qus=='yes':
        pass
    else:
        your_sship=input('Input your ip address:')
        your_sshport=input('Input your target port:')
        your_sshUserName=input('Input your ssh username:')
        
        
    command='ssh '+'-p '+your_sshport+' '+your_sshUserName+'@'+your_sship
    
    res=pexpect.spawnu(command)
    ret=res.expect([your_sshUserName+'.*'+'password','continue connecting (yes/no)?',pexpect.EOF,pexpect.TIMEOUT])
    if ret==0:
        res.setecho(False)
        your_password=input('Input your ssh password:')
        res.sendline(your_password)
    elif ret==1:
        res.sendline('yes\n')
        res.setecho(False)
        your_password=input('Input your ssh password:')
        res.sendline(your_password)
    elif ret==2:
        print('EOF hitted!\n')
    elif ret==3:
        print('Timeout!\n')
    print(res.before)
    
    index=res.expect([your_sshUserName,pexpect.EOF,pexpect.TIMEOUT])
    print(res.before)
    if index==0:
        print('Success!')
    elif index==1:
        print('Hit the EOF')
    elif index==2:
        print('Timeout occured!')
    quire=input('Into interactive mode(yes|no)?')
    if quire=='yes':
        res.interact()
    else: 
        while(True):
            sshcommand=input('Input your next instructioon:')
            if sshcommand=='quit':
                break
            res.sendline(sshcommand)
            res.expect(your_sshUserName)
            print(res.before)
            print(res.after)

    res.close()
    
def girlsftp():
    your_sftpip='139.59.246.196'
    your_sftpport='10001'
    your_sftpUserName='blocks'
    qus=input('Use default configuration?(yes|no)')
    if qus=='yes':
        pass
    else:
        your_sftpip=input('Input your ip address:')
        your_sftpport=input('Input your target port:')
        your_sftpUserName=input('Input your ssh username:')
    
    command='sftp '+'-P '+your_sftpport+' '+your_sftpUserName+'@'+your_sftpip
    
    res=pexpect.spawnu(command)
    res.expect(your_sftpUserName+'.*'+'password')
    print(res.before)
    res.setecho(False)
    your_password=input('Input your sftp password:')
    res.sendline(your_password)
    print(res.before)
    index=res.expect(['sftp>',pexpect.EOF,pexpect.TIMEOUT])
    if index==0:
        print('Success!')
    elif index==1:
        print('Hit EOF')
    elif index==2:
        print('Timeout!')
    quire=input('Enter interactive mode?(yes|no)')
    if quire=='yes':
        res.interact()
    else:
        while(True):
            sftpcommand=input('Input your next instructioon:')
            if sftpcommand=='quit':
                break
            res.sendline(sftpcommand)
            res.expect('sftp>')
            print(res.before)
            print(res.after)
    res.close()

def main():
    choice=input('1,ssh\n2,sftp\n')
    choice=int(choice)
    if choice==1:
        try:
            girlssh()
        except pexpect.EOF:
            print('quit succed!\n')
        except Exception as e:
            print(e)
    elif choice==2:
        try:
            girlsftp()
        except pexpect.EOF:
            print('quit succeed!')
        except Exception as e:
            print(e)
    else:
        print('You have the wrong choice!!\n')