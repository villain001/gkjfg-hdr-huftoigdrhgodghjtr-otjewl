import os
from keep_alive import keep_alive
try:
    import colorama
except ModuleNotFoundError:
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    import pyfiglet
from colorama import init, Fore, Back, Style
print("\n\n\33[48;5;5m\33[38;5;234m ❮ WALL WELCOME BOT ❯ \33[0m\33[48;5;235m\33[38;5;5m \33[0m")
init()
print(Fore.GREEN + Style.BRIGHT)
print(pyfiglet.figlet_format("qiqi", font="cybermedium"))
import aminofix
import time
keep_alive()
nm=open("client.txt","r")
para = nm.readlines()
fm=open("message.txt","r")
msg=(fm.read())
email=para[0].strip()
password=para[1].strip()
device=para[3].strip()
client = aminofix.Client(device)
link=para[2].strip()
xd=client.get_from_code(link)
cd=xd.objectId
cid=xd.path[1:xd.path.index("/")]
print(cid)
client.login(email=email, password=password)
subclient = aminofix.SubClient(comId=cid, profile=client.profile)
oldComments = []
users = subclient.get_all_users()
for nickname, id in zip(users.profile.nickname, users.profile.userId):
    wallComments = subclient.get_wall_comments(str(id), sorting='top').content

    if msg not in wallComments:
        oldComments.append(str(id))
        try:
        	subclient.comment(msg, userId=str(id))
        	print("Welcomed ", nickname, str(id))
        except Exception:
        	pass

    time.sleep(5.0)
