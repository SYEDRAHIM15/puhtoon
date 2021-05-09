#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To lovehacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020
"""
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
 """"""
####  RANDOM Clour ####
P  = '\033[1;97m'  #
M  = '\033[1;91m' #
H  = '\033[1;92m' #
K = '\033[1;93m' #
B  = '\033[1;94m' #
U  = '\033[1;95m' #
O = '\033[1;96m' #
 """"""
my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
def pkgs():""""""
        love("\033[1;91m«-----------------\033[1;96m𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴\033[1;91m-----------------»")
        love("\033[1;96m«-----------------Disclaimer---------------»")
        love("\033[1;91m     This Tool is for Educational Purpose")
        love("\033[1;93mThis presentation is for educational")
        love("\033[1;93mpurposes ONLY.How you use this information")
        love("\033[1;93mis your responsibility.I will not be")
        love("\033[1;93mheld accountable This Tool/Channel Doesn't")
        love("\033[1;93mSupport illegal activities.for any illegal")
        love("\033[1;93mActivitie This Tool is for Educational Purpose")
        love("\033[1;91m«---------------------------------»")
        love("\033[1;95mSYED 𝖱𝖠𝖧𝖨𝖬 2nd Tool Start ComingSoon New Update»")
        love("\033[1;96m «-----------------\033[1;92m𝖲𝖸𝖤𝖣 𝖱𝖠𝖧𝖨𝖬\033[1;96m--------------»")
        time.sleep(0.3)
        os.system("pip install lolcat")
try:
        import mechanize
except ImportError:
        os.system("pip2 install mechanize")
try:
        import requests
except ImportError:
        os.system("pip2 install requests")
        os.system("python2 Cloning.py")
from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
 
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
 
os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;96m|', '\033[1;92m/', '\033[1;95m-', '\033[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\033[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c )
        sys.stdout.flush()
        time.sleep(0.001)
t = threading.Thread(target=animate)
t.start()
 
time.sleep(5)
done = True
 
def keluar():
        print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
        os.sys.exit()
 
 
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
 
 
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')
 
 
def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.00001)
##### LOGO #####
logo = """"""
\033[1;96m𝖪𝖴𝖱𝖱𝖠𝖬 𝖧𝖠𝖢𝖪𝖤𝖱 ░░░\033[1;92m░░𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴╗░░WEBDEVELOPER╗░AND╗░░A\033[1;91mETICALHACKER╗
\033[1;96mYT╔═𝖪4(𝖪𝖴𝖱𝖱𝖠𝖬)║░\033[1;92m░░░░WEBHACKER╔══PAK╗ANONAYMOUS╔𝑭𝑨𝑪𝑬𝑩𝑶𝑶𝑲═╗𝑰𝑫 ║\033[1;91m░𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴╔╝
\033[1;96mPAKISTANI╦╝HACKERS\033[1;92m║░░░░░███████║██║░░╚═╝\033[1;91m█████═╝░
\033[1;96mWEBHACKER╔═𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴╗\033[1;92m██║░░░░░██╔══██║██║░░\033[1;91m██╗██╔═██╗░
\033[1;96mWHATSAPP\033[1;92m╦╝03168823296╗██║░░██║╚█\033[1;91m████╔╝██║░╚██╗
\033[1;96m╚═══\033[1;92m══╝░╚══════╝╚═╝░░╚═╝\033[1;91m░╚════╝░╚═╝░░╚═╝
\033[1;96mHACK\033[1;92mTHE╗░░░HACKERS╗░𝑲𝑼𝑹𝑹𝑨𝑴╗░HACKERS\033[1;91m████╗██╗░█████╗░
\033[1;96mWE\033[1;92mARE╗░LEGION║WE╔══NEVER╗\033[1;91mFORGIVE╔════╝SPEED█║LIMIT█╔══INCREASED█╗
\033[1;92mVISIT╔█OUR█╔𝑭𝑩║𝑨𝑪𝑪𝑶𝑼𝑵𝑻█\033[1;9║█𝑺𝒀𝑬𝑫█╗░░║𝑹𝑨𝑯𝑰𝑴██║
\033[1;92m██║╚██╔╝██║██╔\033[1;91m══██║██╔══╝░░██║██╔══██║
\033[1;92m██║░╚═╝░██║█\033[1;91m█║░░██║██║░░░░░██║██║░░██║
\033[1;92m╚═╝░░░░░╚═\033[1;91m╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
\033[1;47m\033[1;31m      PAKISTANI HACKER       \033[1;0m
\033[1;96m«-----------------\033[1;91m𝕊𝕐𝔼𝔻 ℝ𝔸ℍ𝕀𝕄\033[1;96m-----------------»
\033[1;91m  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈ 𝐊𝐔𝐑𝐑𝐀𝐌
\033[1;91m  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  HACKER
\033[1;91m  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈
\033[1;91m  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp
\033[1;91m  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈03168823296
\033[1;96m«-----------------\033[1;91m𝐒𝐘𝐄𝐃 𝐑𝐀𝐇𝐈𝐌\033[1;96m-----------------»"""
 
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
S = '\033[1;96m'
W = '\033[1;97m'
######Clear######
def clear():
    os.system('clear')
 
#### time sleep ####
def t():
    time.sleep(1)                             
def t1():                                         
    time.sleep(0.01)
#### print std #love###
def love(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                t1()
def menu():
    
    
    os.system('clear')
    print(logo)
    os.system('clear')
    os.system('echo  𝑆𝑌𝐸𝐷░░░░░░𝑅𝐴𝐻𝐼𝑀░░PAKISTANI░ETICAL░░HACKER | lolcat -a -F 0.1')
    os.system('echo  𝑆𝑌𝐸𝐷░░░░░𝑅𝐴𝐻𝐼𝑀██WEB██DEVELOPER░██ | lolcat -a -F 0.1')
    os.system('echo  WHATSAPP░░░░03168823296░░FOR THIS SCRIPT░ | lolcat -a -F 0.1')
    os.system('echo  CONTACT  ░░░░░ME ON WHATSAPP░░𝐾𝑈𝑅𝑅𝐴𝑀 CYBER HACKER░ | lolcat -a -F 0.1')
    os.system('echo  WE ARE ░░ANONAYMOUS░WE ARE LEGION WE NEVER GORFIVE | lolcat -a -F 0.1')
    os.system('echo  WE NEVER FORGET░ASPECT ░░ US ░KNOWLEDGE░IS░░FREE | lolcat -a -F 0.1')
    os.system('echo  HI, I AM 𝑆𝑌𝐸𝐷 𝑅𝐴𝐻𝐼𝑀  ETICAL HACKER | lolcat -a -F 0.1')
    os.system('echo  WE ARE ANONYMOUS WE ARE LEGION WE NEVER FORGIVE WE NEVER FORGET ASPECT US | lolcat -a -F 0.1')
    os.system('echo  SHABIR BALOCH WHATSAPP = 0316882329 | lolcat -a -F 0.1')
    os.system('echo  VISIT OUR 𝐹𝐴𝐶𝐸𝐵𝑂𝑂𝐾 𝑃𝑅𝑂𝐹𝐼𝐿𝐸  𝑆𝑌𝐸𝐷 𝑅𝐴𝐻𝐼𝑀 | lolcat -a -F 0.1')
    os.system('echo  PAKISTANI ETICAL HACKER AND A PROGRAMMER | lolcat -a -F 0.1')
    os.system('echo  LETS░░░░░ENJOY░░OUR░░░░░TOOL░░THANKS | lolcat -a -F 0.1')
    os.system('echo  ------ Your Mind is Your Best Weapon------&&date  | lolcat -a -F 0.1')
    os.system('echo ----------------𝙎𝙔𝙀𝘿 𝙍𝘼𝙃𝙄𝙈----------------| lolcat')
    os.system('echo  ┈┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈◢▇◣◢▇◣┈┈┈┈  𝙎𝙔𝙀𝘿 𝙍𝘼𝙃𝙄𝙈| lolcat --animate')
    os.system('echo  ┈┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈▇▇▇▇▇▇┈┈┈┈  𝙆𝙐𝙍𝙍𝘼𝙈 HACKER| lolcat --animate')
    os.system('echo  ┈┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈◥▇▇▇▇◤┈┈┈┈| lolcat')
    os.system('echo  ┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈◥▇▇◤┈┈┈┈┈   WhatsApp| lolcat --animate')
    os.system('echo  ┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈◥◤┈┈┈-̴̧̬͖͇̟̟̼̱͙̠͉̟̹̘̖̥͈͖͚̯͗͑͌̃̿͗̈̿̿̏͗̑̀̀͘┈┈┈03168823296| lolcat --animate')
    os.system('echo -----------------𝙎𝙔𝙀𝘿 𝙍𝘼𝙃𝙄𝙈----------------| lolcat --animate')
    os.system('echo    To return to this menu from any Tool| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo        Stop Process Press. CTRL + z| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo         Type python2 puhtoon.py| lolcat --animate')
    os.system('echo -----------------𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴 ---------------| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [A]  Install Random Mail Cloning--------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [B]  Install Email Cloning--------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [C]  Install Manual Password------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [D]  Install Group Cloning--------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [E]  Install With Out Fb Id-------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [F]  Install Facebook Target------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [G]  Install SpiderMan------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [H]  Install Kalilinux------------------------- Tool ----●  | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [I]  Install BlackHat-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [J]  Install RedMoonNew------------------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [K]  Install love3Hack3r----------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [L]  Install B4 BALOCH Clonnig----------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [M]  Install Web Admin Panel Finder------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [N]  Install Attacker-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [O]  Install Payload--------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [P]  Install CamHacker------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [Q]  Install Compiler-------------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [R]  Install Instagram Brut-------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [S]  Install Marsh Base------------------------ Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [T]  Install Gmail Target---------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [U]  Install Termux Logo----------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [V]  Install Termux TBomb---------------------- Tool ----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [W]  𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴  WhatsApp Group-------- Tool----● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [X]  BlackMafia Dragon404 New Update -----● | lolcat -a -F 0.01')
    time.sleep(0.0005)
    os.system('echo [Y]  Tool Update--------------------------● | lolcat --animate')
    time.sleep(0.0005)
    os.system('echo [Z]  EXIT | lolcat -a -F 0.1')
    time.sleep(0.0005)
    os.system('echo Slect Option A-Z➣➤| lolcat -a -F 0.1 ')
    mafia()
def mafia():
        black = raw_input('\033[1;91m┺\033[1;92m──\033[1;97m──\033[1;96m──\033[1;95m──\033[1;94m──\033[1;92m──\033[1;96m──━\033[1;93m➢\033[1;92m➣\033[1;91m➤')
        if black =="":
                print ("  𝑺𝒚𝒆𝒅𝑹𝒂𝒉𝒊𝒎!")
                mafia()
        elif black =="A" or black =="a":
                clear()
                print(logo)
                os.system("rm -rf $HOME/random")
                clear()
                os.system("cd $HOME && git clone https://github.com/lovehacker404/random")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/random && python2 lovehacker.py")
        elif black =="B" or black =="b":
                clear()
                print(logo)
                os.system("rm -rf $HOME/email")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/email")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/email && python2 lovehacker.py")
        elif black =="C" or black =="c":
                clear()
                print(logo)
                os.system("rm -rf $HOME/Password")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Password")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/Password && python2 lovehacker.py")
        elif black =="D" or black =="d":
                clear()
                print(logo)
                os.system("rm -rf $HOME/lovehack")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/lovehack")
                print (logo)
                time.sleep(5)
                os.system("cd $HOME/lovehack && python2 lovehacker.py")
        elif black =="E" or black =="e":
                clear()
                print(logo)
                os.system("rm -rf $HOME/402")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/402")
                print (logo)
                love("\033[1;93mTool User Name :\033[1;95m     Black ")
                love("\033[1;93mTool Password  :\033[1;95m     Mafia ")
                time.sleep(5)
                os.system("cd $HOME/402 && python2 Cloningx-2-1.py")
        elif black =="F" or black =="f":
                clear()
                print(logo)
                os.system("rm -rf $HOME/blackhole")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/blackhole")
                print (logo)
                love("\033[1;93mTool User Name :\033[1;95m     Black ")
                love("\033[1;93mTool Password  :\033[1;95m     Mafia ")
                love("\033[1;93m        :Target Attack  :     ")
                love("\033[1;93mPassword list  :\033[1;95mlovehacker-2.txt ")
                time.sleep(5)
                os.system("cd $HOME/blackhole && python2 AsifJaved.py")
        elif black =="G" or black =="g":
                clear()
                print(logo)
                os.system("rm -rf $HOME/Spider")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Spider")
                print (logo)
                love("\033[1;91mCongratulations Cobra Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name SpiderMan Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/Spider && python2 SpiderMan.py")
        elif black =="H" or black =="h":
                clear()
                print(logo)
                os.system("rm -rf $HOME/KaliIndia")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/KaliIndia")
                print (logo)
                love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name India Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/KaliIndia && python2 kalilinux.India.py")
        elif black =="I" or black =="i":
                clear()
                print(logo)
                os.system("rm -rf $HOME/BlackHat")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/BlackHat")
                print (logo)
                love("\033[1;96mCongratulations BlackHat Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name BlackHat Password lovehacker")
                time.sleep(5)
                os.system("cd $HOME/BlackHat && python2 BlackHat.py")
        elif black =="J" or black =="j":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/RedMoonNew")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/RedMoonNew")
                print (logo)
                love("\033[1;91mCongratulations RedMoonNew Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;93mTool User Name\033[1;92m RedMoonNew\033[1;93m Password \033[1;92mlovehacker")
                time.sleep(6)
                os.system("cd $HOME/RedMoonNew && python2 lovehacker")
        elif black =="K" or black =="k":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/lov3Hak3r")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/lov3Hak3r")
                print (logo)
                love("\033[1;96mCongratulations BlackMafia Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/lov3Hak3r && python2 lovehacker.py")
        elif black =="L" or black =="l":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/B4_BALOCH")
                os.system("cd $HOME && git clone https://github.com/shabirbaloch398/B4_BALOCH.git")
                print (logo)
                love("\033[1;93mCongratulations Cobra Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;95mTool Dont Have Username And Password Enjoy But Use 786786 Pass Or Username On My Tool Thanks")
                time.sleep(5)
                os.system("cd $HOME/Cobra && python2 Scorpion.py")
        elif black =="M" or black =="m":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/attack911")
                os.system("cd $HOME && git clone https://github.com/shabirbaloch398/attack911.git")
                print (logo)
                love("\033[1;91mCongratulations attack911 Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;96mAdmin Panel Finder")
                time.sleep(5)
                os.system("cd $HOME/attack911 && python2 attack911.py")
        elif black =="N" or black =="n":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/Attacker")
                os.system("cd $HOME && git clone https://github.com/shabirbaloch398/Attacker.git")
                print (logo)
                love("\033[1;96mCongratulations Attacker Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;92mBest Script")
                time.sleep(5)
                os.system("cd $HOME/Attacker && python2 B4.py")
        elif black =="O" or black =="o":
                clear()
                print(logo)
                print(logo)
                os.system("pkg install unstable-repo")
                os.system("pkg install metasploit")
                os.system("pkg install msfconsole")
                os.system("rm -rf $HOME/Black_Mafia")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Black_Mafia")
                print (logo)
                love("\033[1;93mCongratulations Black_Mafia Payload Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Black_Mafia && python3 Black_Mafia.py")
        elif black =="P" or black =="p":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/Pak")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Pak")
                print (logo)
                love("\033[1;96mCongratulations CamHacker Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("\033[1;92mEducational Perpose only")
                time.sleep(2)
                os.system("cd $HOME/Pak && python lovehacker.py")
        elif black =="Q" or black =="q":
                clear()
                print(logo)
                os.system("rm -rf $HOME/Compile")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Compile")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Compile && python2 lovehacker.py")
        elif black =="R" or black =="r":
                clear()
                print(logo)
                print(logo)
                os.system("pip2 install bs4")
                os.system("rm -rf $HOME/Insta")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Insta")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                love("Passwordlist No1 (wordlist.txt) No2 (BlackMafia.txt)")
                time.sleep(5)
                os.system("cd $HOME/Insta && python2 lovehacker.py")
        elif black =="S" or black =="s":
                clear()
                print(logo)
                os.system("rm -rf $HOME/TimePass")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/TimePass")
                print (logo)
                love("\033[1;93mCongratulations  Tool Has Been Update Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/TimePass && python2 lovehacker.py")
        elif black =="T" or black =="t":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/GmailAttack")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/GmailAttack")
                print (logo)
                love("\033[1;96mCongratulations GmailAttack Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                love("plz wi8 Password list name (lovehacker-1.txt) ")
                time.sleep(6)
                os.system("cd $HOME/GmailAttack && python2 lovehacker.py")
        elif black =="U" or black =="u":
                clear()
                print(logo)
                print(logo)
                os.system("rm -rf $HOME/Logo")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Logo")
                print (logo)
                love("\033[1;96mCongratulations BlackMafia Logo  Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/Logo && bash lovehacker.sh")
        elif black =="V" or black =="v":
                clear()
                print(logo)
                os.system("rm -rf $HOME/sms")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/sms")
                print (logo)
                love("\033[1;96mCongratulations BlackMafia TBomb Tool Has Been Installed Successfully")
                love("Now you can open this tool as usual")
                time.sleep(5)
                os.system("cd $HOME/sms && bash BlackMafia.sh")
        elif black =="W" or black =="w":
                clear()
                print(logo)
                
                time.sleep(5)
                
        elif black =="X" or black =="x":
                clear()
                print(logo)
                love("Welcome To 𝑺𝒀𝑬𝑫 𝑹𝑨𝑯𝑰𝑴 2nd Tool")
                love("BlackMafia 2nd Tool Start")
                love("Coming Soon New Update")
                time.sleep(5)
                os.system("rm -rf $HOME/Dragon404")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/Dragon404")
                print (logo)
                love("\033[1;96mCongratulations Dragon404 Tool Has Been Installed Successfully")
                love("Wellcom to Dragon404 tool")
                os.system("cd $HOME/Dragon404 && python2 lovehacker.py")
        elif black =="Y" or black =="y":
                clear()
                print(logo)
                os.system("rm -rf $HOME/World")
                os.system("pip install lolcat")
                os.system("cd $HOME && git clone https://github.com/lovehacker404/World")
                print (logo)
                love("\033[1;96mCongratulations BlackMafia Tool Has Been Update Successfully")
                time.sleep(5)
                os.system("cd $HOME/World && python2 Cloning.py")
        elif black =="Z" or black =="z":
            os.system("exit")
if __name__ == "__main__":
    menu()
 

                


