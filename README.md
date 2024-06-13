# Control Remote Server Using Telebot:
Hey, there linux **CLI** lovers don't have pc to install **LINUX** distroes but want to learn basic Linux CLI commands this module is for you. This has follwoing features:
- You can use any server or local computer to build remote access to.
- You just need telegram bot.
- All the CLI commands are as same as that of LINUX but with them you can control CLI of any machine like windows and mac not only LINUX distroes.
- Installation and set up is super easy.

# Installation procedure:
## Windows:
- First clone the repository by using CLI of downloading zip file.
- The nevigate to the directory where zip file is installed.
- Then extrac the zip file.
- Nevigate to the **HackTheSystem-main** directory.
- Shift+RightClick of mouse to open termianl in the current directory. Run the building dependency file as follows:
```
python buildingDependency.py
```
- You will find three new .bat files are generated- installreq.bat, copyfile.bat, backgroundrun.bat
- First edit main.py file. Open in note pad or in any of your favourite code editor and enter bot API and ChatIDs of your friends and yours for further info to gather about usage of bot. Like bot will let the given chat IDs know who starts the bot.
- After editing and saving main.py run installreq.bat by double clicking it. It will install all required modules used in the main.py
- After that run copyfile.bat by double clicking it. It will creat a main.pyw file. Now, you are all done.
- Just cut the backgroundrun.bat file to startup folder to monitor the system.

## Linux and Mac:
In these systems as CLI is bit more flexible hence installation is bit more easy.

- open terminal in any desired directory.
```
git clone https://github.com/atrajit-sarkar/HackTheSystem.git
```
This will clone HackTheSystem-main directory in your desired directory.
- Edit the main.py file as above in case of windows installation.
- Now, run main.py in background as follows:
```
nohup python3 main.py &
```
- You can also make the main.pyw file using the follwoing command:
```
cp ./main.py ./main.pyw
```
- Then again you will get a main.pyw file in your directory. Then make a shell script run.sh with the following command:
```
#! /bin/bash
python3 main.py
```
- Cut the file into the startup folder. And here you go.