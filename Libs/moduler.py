# library for mah framework #
import os
from Modules.torghost import torghost
from Modules.cupp import cupp
# gerekli kurulumları nasıl yapacaksan sh scripti yazarsın #
# modul list #
"""
"dirsearch" : "https://github.com/maurosoria/dirsearch"
"knockpy" : "https://pypi.org/project/knockpy/"
"Torghost" : "https://github.com/SusmithKrishnan/torghost.git"
"""
# git clone https://github.com/koraykutanoglu/ANONSURF # https://www.secops.com.tr/tr/defensive/anonsurf

# modul list #

class moduler:
    class dirsearch:
        def dirsearch(gir):
            try:
                os.system("dirsearch " + gir)
            except:
                print("Bir hata var!!!")
                
    class knockpy:
        def knockpy(gir):
            try:
                os.system("knockpy " + gir)
            except:
                print("bir hata var!!!")
                
    class torghost:
        def banner():
            torghost.torghost.banner()
            
        def help():
            torghost.torghost.help()
            
        def start():
            torghost.torghost.start()
            
        def stop():
            torghost.torghost.stop()
            
        def switch():
            torghost.torghost.switch()
            
        def update():
            torghost.torghost.update()
            
    class cupp:
        def launch():
            cupp.cupp.start()