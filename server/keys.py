from path import *
def purgekeys():
    from glob import glob
    from os import remove, chdir
    try:
        chdir(keypath)
    except:
        pass
    for file in glob("*.key"):
        remove(file)
    return "Keys purged"

def newuserkey():
    import os
    from random import randint
    from secrets import token_hex
    from glob import glob
    from pathlib import Path
    usedkeys = []
    try:
        os.chdir(keypath)
    except:
        pass
    for file in glob("*.key"):
        with open(file, "r") as f:
            usedkeys.append(f.read())
    while True:
        key = str(token_hex(8))
        if key in usedkeys:
            pass
        else:
            break
    while True:
        keyfile = Path(str(randint(1000000, 9999999)) + str(".key"))
        if keyfile.is_file():
            pass
        else:
            break
    with open(keyfile, "w") as f:
        f.write(key)
    return "Key: " + key
    
def usekey(key):
    import os
    from glob import glob
    try:
        os.chdir(keypath)
    except:
        pass
    for file in glob("*.key"):
        with open(file, "r") as f:
            if f.read() == key:
                with open(file, "w") as z:
                    z.write("")
                return True
            else:
                pass

def addusrfromkey(username, password):
    import db
    try:
        db.USERCREDS[username]
        return False
    except:
        pass
    import os
    try:
        os.chdir(serverpath)
    except:
        pass
    #shit should  happen here idk how to do it tho :(
    with open("db.py", "r") as f:
        lines = f.readlines()
    lines[1] = lines[1] + '    "' + username + '" ' + ":" + ' "' + password + '"' + "," + "\n"
    with open("db.py", "w") as f:
        f.writelines(lines)