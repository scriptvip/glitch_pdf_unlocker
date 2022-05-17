import os
try:
    import pikepdf
except ModuleNotFoundError:
    pip3 install pikepdf
    pip install pikepdf
from os.path import isfile, join
from os import listdir
#folder_path=On_Red+" Not Selected [!]  "


# Regular Colors
Black="\033[0;30m" # Black 
Red="\033[0;31m" # Red 
Green="\033[0;32m" # Green 
Yellow="\033[0;33m" # Yellow 
Blue="\033[0;34m" # Blue 
Purple="\033[0;35m" # Purple 
Cyan="\033[0;36m" # Cyan
White="\033[0;37m" # White



# Background
On_Black="\033[40m" # Black 
On_Red="\033[41m" # Red 
On_Green="\033[42m" # Green
On_Yellow="\033[43m" # Yellow 
On_Blue="\033[44m" # Blue 
On_Purple="\033[45m" # Purple 
On_Cyan="\033[46m" # Cyan 
On_White="\033[47m" # White

folder_path=On_Red+" Not Selected [!]  "
#f=input(" ==> ")
def main():
#    print(files_path)
    files = [f for f in os.listdir(files_path) if os.path.isfile(join(files_path, f))]
    for f in files:
#        print(f)
        if f.endswith(".pdf"):
            try:
                print(Yellow+"     [🔒] "+f+Green+"  decrypted [✅] ")
                print("  ")
                pdf = pikepdf.open(f,allow_overwriting_input=True)
                pdf.save(f)
                continue
            except FileNotFoundError:
                continue
        else:
            pass


def banner():
    os.system('clear')
    print (Blue +"      _    _                                         ")
    print (Green+"   ,-(|)--(|)-.                                      ")
    print (Blue +"   \_   ..   _/"+Cyan+" .--. .-.   _  .-.      .-.           ")
    print (Green+"     \______/  "+Cyan+": .--': :  :_;.' `.     : :           ")
    print (Red + "       V  V    "+Cyan+": : _ : :  .-.`. .'.--. : `-. "+Blue+"   ___  ")
    print (Green+"       `.^^`.  "+Cyan+": :; :: :_ : : : :'  ..': .. :"+Green+" /^,--' ")
    print (Blue +"         \^^^\ "+Cyan+"`.__.'`.__;:_; :_;`.__.':_;:_;"+Blue +"(^^\    ")
    print (Green+"         |^^^|                  _,-._        \^^\    ")
    print (Blue +"        (^^^^\      __      _,-'^^^^^`.    _,'^^)    ")
    print (Green+"         \^^^^`._,-'^^`-._.'^^^^__^^^^ `--'^^^_/     ")
    print (Blue +"          \^^^^^ ^^^_^^^^^^^_,-'  `.^^^^^^^^_/       ")
    print (Green+"           `.____,-' `-.__.'        `-.___.'         ")
    print (Green+"               coded by Abdo Sleem (*__^)            ")
    print (Purple+"   |------------------------------------------------|")
    print (Black +"    "+On_Yellow+"   Folder ==> "+folder_path+On_Black)
    print (Purple+"   |------------------------------------------------|")
    print ("   ")
try:
    banner()
    folder=input(Yellow+"   Do You Want To Use Current Folder ["+Green+"y"+Yellow+"/"+Green+"n"+Yellow+"]:"+Green)
    if folder == "y":
        folder_path=On_Green+" "+os.getcwd()+"  "
        banner()
        files_path=os.getcwd()
        main()

#else:
 #   _else_()

    else:
        banner()
        folder2=input(Yellow+"   Type PDF Files Folder Path : "+Green)
        print(" ")
        path=os.path.exists(folder2)
        while path == False:
            print(Red+"   Path Not Exists [!] ")
            print("  ")
            folder2=input(Yellow+"   Type PDF Files Folder Path : "+Green)
            path=os.path.exists(folder2)
            print(" ")
        else:
            folder_path=On_Green+" "+folder2+"  "
            banner()
            files_path=str(folder2)
            main()

except KeyboardInterrupt:
    print("  ")
    print(Yellow+"   Thanks For Useing !!!")
    print("   ")
#if folder == "y":
  #  folder_path=On_Green+" "+os.getcwd()+"  "
 #   banner()
   # files_path=os.getcwd()
    #print (files_path)
    #main()

#else:
 #   _else_()
