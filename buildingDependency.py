import os

dir=os.getcwd()

#installreq.bat
with open(f"{dir}/installreq.bat","w") as f:
    f.write('''@echo off
pip install -r requirements.txt''')

#copyfile.bat   
with open(f"{dir}/copyfile.bat","w") as f:
    f.write(fr'''@echo off
xcopy {dir}\main.py {dir}\main.pyw''')

#backgroundrun.bat    
with open(fr"{dir}\backgroundrun.bat","w") as f:
    f.write(fr'''@echo off
pyw.exe {dir}\main.pyw''')