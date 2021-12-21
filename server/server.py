import socket
from config import HOST, HOST_PORT
import keys as bk
import mb
import os
from db import *

close = False

def restart():
    conn.close()
    s.close()
    os.system("python " + str(os.getcwd() + "/server.py"))    
    exit()

while True:
    wrongpass = 0
    if close == False:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                s.bind((HOST, HOST_PORT))
                s.listen(1)
                conn, addr = s.accept()
            except Exception as E: 
                print("Failed setup", E) 
                close = True

            print("Connected to by: ", addr)

            def newacc():
                conn.send("It seems you are using an invite key!".encode())
                conn.send("Please enter your username: ".encode())
                username = conn.recv(1024).decode()
                conn.send("Please enter your password: ".encode())
                password = conn.recv(1024).decode()
                try:
                    bk.addusrfromkey(username, password)
                    conn.send("Account created!".encode())
                    conn.send("Please reconnect with your credentials!".encode())
                    restart()
                except:
                    conn.send("Account creation failed!".encode())
                    conn.close()

            def login_backend(username, password):
                global wrongpass
                username = username.lower()
                try:
                    if USERCREDS[username] == password:
                        wrongpass = 0
                        return True
                    else:
                        wrongpass = wrongpass + 1
                        return False
                except:
                    wrongpass = wrongpass + 1
                    return False

            def login_frontend():
                global username
                while True:    
                    conn.send("Username: ".encode())
                    username = conn.recv(1024).decode()
                    if bk.usekey(username):
                        newacc()
                        break
                    else:
                        pass
                    conn.send("Password: ".encode())
                    password = conn.recv(512).decode()
                    if wrongpass == 5:
                        conn.close()
                    else:
                        pass
                    if login_backend(username, password):
                        conn.send("clear".encode())
                        conn.send("Login Successful\n".encode())
                        break
                    else:
                        conn.send("Login Failed\n".encode())

            login_frontend()

            def readmbstart():
                conn.send((mb.readmb(username).replace("[", "").replace("]", "").replace(("." + username), "")).encode())

            def sendstart():
                conn.send("Username?: ".encode())
                recipusername = conn.recv(1024).decode().lower()
                try:
                    USERCREDS[recipusername]
                except:
                    conn.send("Username not found\n".encode())
                    return
                conn.send("Subject?: ".encode())
                subject = conn.recv(1024).decode().replace(" ", "_")
                conn.send("Message?: ".encode())
                message = conn.recv(1024).decode()
                try:
                    mb.send(recipusername, message, subject, username)
                    conn.send("Mail Sent!".encode())
                except:
                    conn.send(("Exception while sending :(\n").encode())

            def ping():
                conn.send("pong".encode())

            while True:
                data = conn.recv(512)
                if not data:
                    break

                print('Received: "' + data.decode() + '"')

                if data.decode() == "help":
                    conn.send("help:Shows this\nping:Gives a response\nexit:Disconnected you from the server\nread:Reads mail\nsend:Sends mail\npurgemail:Deletes all your mail\naddusr:If you are an admin generate a userkey\npurgekeys: Deletes all keys".encode())

                elif data.decode() == "ping":
                    ping()

                elif data.decode() == "read":
                    readmbstart()

                elif data.decode() == "send":
                    sendstart()

                elif data.decode() == "purgemail":
                    mb.delmb(username)
                    conn.send("Mailbox Purged!".encode())

                elif data.decode() == "addusr":
                    if username in ADMINS:
                        conn.send(bk.newuserkey().encode())
                    else:
                        conn.send("You are not an admin\n".encode())
                
                elif data.decode() == "purgekeys":
                    if username in ADMINS:
                        try:
                            conn.send(bk.purgekeys().encode())
                        except:
                            conn.send("Error while purging keys\n".encode())
                    else:
                        conn.send("You are not an admin\n".encode())

                elif data.decode() == "exit":
                    conn.close()
                    break

                else:
                    pass

            conn.close()
            s.close()
            print("Connection closed\n")
        except:
            print("Connection closed\n")
    else:
        break
