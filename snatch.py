import instaloader, time, os, sys, requests
from colorama import Fore , Back

time.sleep(1)
os.system("clear")
time.sleep(2)
print(Fore.GREEN , "")

def typewriter_animation(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def InstaSnatch():
    Insnatch = '''

	   ____             __          ____              __         __
	  /  _/  ___   ___ / /_ ___ _  / __/  ___  ___ _ / /_ ____  / /
	 _/ /   / _ \ (_-</ __// _ `/ _\ \   / _ \/ _ `// __// __/ / _ |
	/___/  /_//_//___/\__/ \_,_/ /___/  /_//_/\_,_/ \__/ \__/ /_//_/
	__________________
	𝙶𝚒𝚝𝙷𝚞𝚋 : 𝚃𝚗𝚈𝚝𝙲𝚘𝚍𝚎𝚛
	𝙲𝚘𝚍𝚎𝚍 𝙱𝚢 𝙼𝚎 </𝟹
	𝙶𝚒𝚝𝙷𝚞𝚋 : https://tinyurl.com/2qtjl3tb
	<----------------------------------->

    '''
    typewriter_animation(Insnatch)

InstaSnatch()

time.sleep(1)
print(Fore.RED , "")
print("")
time.sleep(1)

print("Attempting Login...")

with open('credentials.txt', 'r') as f:
        contents = f.read()
        lines = contents.splitlines()
        username = lines[0]
        password = lines[1]

SnatchSuccessful = '''


[+]	Snatch Successfull !!
'''

def download_profile():

    L = instaloader.Instaloader()

    try:
        L.login(username, password)
        print(Fore.GREEN ,"Login Successful !!")
    except:
        print(Fore.RED , "Login Failed !!")
        sys.exit()

    print(Fore.LIGHTBLUE_EX , "")
    print("")
    time.sleep(2)

    target_username = input("[+]	Enter Target Username -->  ")

    print("")
    print("")

    try:

        L.download_profile(target_username, profile_pic_only=False)
        time.sleep(2)
        typewriter_animation(SnatchSuccessful)
    except Exception as e:
        print("[+]	Snatch Failure !!	Error :", str(e))

download_profile()

time.sleep(2)
message = "[+]	Thank You For Using !!!"
print("")
print("")
typewriter_animation(message)
time.sleep(2)
