from path import *
def send(recipusername, msg, subject, sendrusername):
    from datetime import datetime
    from pathlib import Path
    #import os
    mailfile = mbpath + subject + "." + recipusername
    frozenmailfile = mailfile
    numbercount = 1
    while True:
        if Path(frozenmailfile).is_file():
            mailfile = mbpath + subject + "_" + numbercount + "." + recipusername
            frozenmailfile = mailfile
            numbercount += 1
        else:
            break
    senddate = str(datetime.now().strftime(r"%d/%m/%Y %H:%M:%S"))
    from os import system
    system("echo x > " + mailfile)
    finalstr = "Send date: " + senddate + ("\n") + "Message Content: " + msg + ("\n") + "From: " + sendrusername
    with open(mailfile, 'w') as f:
        f.write(finalstr)
    return "Mail sent"

def readmb(username):
    from glob import glob 
    import os
    text = []
    try:
        os.chdir(mbpath)
    except:
        #return "Error: Could not find mailbox"
        pass
    for file in glob("*." + username):
        with open(file, "r") as f:
            text.append((file, " - ", f.read().replace("\n", " - ").replace(",", "")))
    if text == []:
        return "No mail"
    else:
        return str(text)

def delmb(username):
    from glob import glob
    import os
    try:
        os.chdir(mbpath)
    except:
        #return "Error: Could not find mailbox"
        pass
    for file in glob("*." + username):
        os.remove(file)
