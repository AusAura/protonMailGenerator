#! python3
#Michi4
from PIL import Image
import pyautogui
import sys
import time
import random
import string
import webbrowser
import ctypes
import re

freeze_time_rate = 3

## for clipboard
CF_TEXT = 1
kernel32 = ctypes.windll.kernel32
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
user32 = ctypes.windll.user32
user32.GetClipboardData.restype = ctypes.c_void_p


def getClip6digit():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            print(data, data_locked)
            print(text, value)
            return re.search(r'(\d{6})', (str(value)))
    finally:
        user32.CloseClipboard()


def getMail():
    user32.OpenClipboard(0)
    try:
        if user32.IsClipboardFormatAvailable(CF_TEXT):
            data = user32.GetClipboardData(CF_TEXT)
            data_locked = kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            kernel32.GlobalUnlock(data_locked)
            if "@yomail.info" in str(value)  or "@10mail.org"  in str(value)  or "@emlpro.com" in str(value) or "@emltmp.com" in str(value): # 
                match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(value))
                return str(match.group(0))
            return False
    finally:
        user32.CloseClipboard()


def randomize(
                _option_,
                _length_
            ):
    """
    Random passwords and mails generator
    """

    if _length_ > 0 :

        # Options:
        #       -p      for letters, numbers and symbols
        #       -s      for letters and numbers
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-s':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        elif _option_ == '-l':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_='1234567890'
        elif _option_ == '-m':
            string._characters_='JFMASOND'

        if _option_ == '-d':
            _generated_info_=random.randint(1,28)
        elif _option_ == '-y':
            _generated_info_=random.randint(1950,2000)
        else:
            _generated_info_=''
            for _counter_ in range(0,_length_) :
                _generated_info_= _generated_info_ + random.choice(string._characters_)

        return _generated_info_
    else:
        return 'error'


if __name__ == '__main__':

    webbrowser.open('https://google.com') ## start browser
    time.sleep(2 * freeze_time_rate)

    # pyautogui.keyDown('ctrlleft') 
    # pyautogui.keyDown('shift') 
    # pyautogui.typewrite('p') 
    # pyautogui.keyUp('ctrlleft') 
    # pyautogui.keyUp('shift') # ctrl + shift + P for private

    pyautogui.keyDown('ctrlleft') 
    pyautogui.typewrite('n') 
    pyautogui.keyUp('ctrlleft') # ctrl + N for new tab

    pyautogui.typewrite('https://account.proton.me/signup?plan=free\n') ## type, go to Proton
    time.sleep(5 * freeze_time_rate)

    # Making Username
    _username_=randomize('-s',5)+randomize('-s',5)+randomize('-s',5)
    pyautogui.typewrite(_username_ + '\t\t\t')
    print("Username:" + _username_)

    # Making Password
    _password_=randomize('-p',16)
    pyautogui.typewrite(_password_+'\t'+_password_+'\t')
    print("Password:" + _password_)

    pyautogui.typewrite('\n') ## enter
    time.sleep(2 * freeze_time_rate)
    pyautogui.typewrite('\t\t\t\n') # switch to email confirmation

    pyautogui.keyDown('ctrlleft')  
    pyautogui.typewrite('t') 
    pyautogui.keyUp('ctrlleft') ## new tab

    time.sleep(1 * freeze_time_rate)
    pyautogui.typewrite('https://dropmail.me/en/\n') ## type, go to dropmail


    pyautogui.keyDown('shift')
    pyautogui.keyDown('down') 
    pyautogui.keyUp('down') 
    pyautogui.keyUp('shift') ## select the page instead of address bar
    time.sleep(1 * freeze_time_rate)

    newMail = True
    while True:
        if not newMail:
            pyautogui.keyDown('ctrlleft')
            pyautogui.typewrite('r')
            pyautogui.keyUp('ctrlleft') ## refresh the page if mail is not there
            time.sleep(1 * freeze_time_rate)

        pyautogui.typewrite('\t' * 28)  ## select the email address element

        pyautogui.keyDown('ctrlleft')
        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.press('down')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.keyUp('ctrlleft') ## select only the email address string


        pyautogui.keyDown('ctrlleft') 
        pyautogui.typewrite('c') 
        pyautogui.keyUp('ctrlleft') ## copy

        ## get the email from the clipboard to the script. Sometimes generated email domain is disabled in Proton
        newMail = getMail() 

        if newMail:
            print("10 min mail: " + newMail)
            break ## if success

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('\t') ## switch back to proton tab
    pyautogui.keyUp('ctrlleft')
    time.sleep(1 * freeze_time_rate)

    pyautogui.keyDown('ctrlleft');  
    pyautogui.typewrite('v'); ## paste the email from the clipboard
    pyautogui.keyUp('ctrlleft')
    pyautogui.press('backspace') ## delete one additional space in the end
    pyautogui.typewrite('\n') ## submit

    time.sleep(10 * freeze_time_rate)

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('\t')
    pyautogui.keyUp('ctrlleft') ## switch to email confirmation
    time.sleep(1 * freeze_time_rate)

    pyautogui.typewrite("\t" * 14 + "\n") ## select the 'HTML-design'

    pyautogui.keyDown('shiftleft')
    pyautogui.typewrite('\t\t'); ## select the code window 
    pyautogui.keyUp('shiftleft')

    pyautogui.keyDown('ctrlleft'); 
    pyautogui.typewrite('a'); ## select the text
    pyautogui.keyUp('ctrlleft')

    pyautogui.keyDown('ctrlleft'); 
    pyautogui.typewrite('c'); ## copy
    pyautogui.keyUp('ctrlleft')

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('\t') ## to proton tab
    pyautogui.keyUp('ctrlleft')

    time.sleep(1 * freeze_time_rate)

    ver_code = getClip6digit().group()
    print(ver_code)
    pyautogui.typewrite(ver_code + '\n') ## extracts and types the code from the clipboard

    time.sleep(5 * freeze_time_rate)
    pyautogui.typewrite('\n') ## enter, selects the displayed username

    time.sleep(5 * freeze_time_rate)
    pyautogui.typewrite('\t\t\t\n') ## skip the phone number assignation

    time.sleep(1 * freeze_time_rate)
    pyautogui.typewrite('\t\n') ## confirm

    logfile = open("accountLog.txt", "a") ## saving details to the file
    logfile.write(_username_ + "@proton.me:" + _password_ + "\n")
    logfile.close()