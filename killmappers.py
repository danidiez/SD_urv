import os

os.system("kill -9 $(ps -a|grep python|cut -f2 -d"+"'"+" "+"')")
os.system("kill -9 $(ps -a|grep python|cut -f1 -d"+"'"+" "+"')")
