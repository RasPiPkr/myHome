from my_house_settings import *
import RPi.GPIO as GPIO
from PIL import Image
import tkinter as tk
import pychromecast
import threading
import requests
import time
import glob
import io


############################################ Put GPIO pins used into the settings
relayPins = [18, 23, 24, 22, 6, 13, 19, 26]
pirPins = [21, 20, 16, 12]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for i in range(len(relayPins)):
    GPIO.setup(relayPins[i], GPIO.OUT, initial=GPIO.HIGH)
    time.sleep(0.2)
for i in range(len(pirPins)):
    GPIO.setup(pirPins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    time.sleep(0.2)

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')
root = tk.Tk()
root.geometry('800x480')
root.attributes('-fullscreen', True)
root.config(bg='black', cursor='none')
timeFont = ('digits', 165)
setFont = ('digits', 192)
digitFont = ('digits', 60)
sensorFont = ('Verdana', 20)
textFont = ('Verdana', 12)
cpuFont = ('Verdana', 16)
currTime = tk.StringVar()
currDate = tk.StringVar()
temp1Sensor = tk.StringVar()
temp2Sensor = tk.StringVar()
############################# Sort so it gets from the settings.py
setTempVar = tk.StringVar() # Use the value=
setTempVar.set('20.0')
mHrsVar = tk.StringVar()
mDefaultHrs = '07'
mMinsVar = tk.StringVar()
mDefaultMins = '00'
mTempVar = tk.StringVar()
mDefaultTemp = '20.0'
bHrsVar = tk.StringVar()
bDefaultHrs = '23'
bMinsVar = tk.StringVar()
bDefaultMins = '00'
bTempVar = tk.StringVar()
bDefaultTemp = '19.0'
#############################
pHrs = [str(i).zfill(2) for i in range(24)]
pMins = [str(i).zfill(2) for i in range(60)]
t = [str('{:.1f}'.format(i)) for i in range(16, 23)]
pTemp = []
for i in t:
    pTemp.append(i)
    pTemp.append(i[:-1] + '5')


def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def test1Run(device_file):
    global heatingDelay
    heatingDelay = int(time.time())
    while True:
        try:
            getTemp = read_temp(device_file)
            temp1Sensor.set('{:.1f}C'.format(getTemp[0]))
            if int(timerSecs - heatingDelay) >= 30:
                if temp1Sensor.get() <= setTempVar.get() and temp2Sensor.get() <= setTempVar.get():
                    GPIO.output(18, GPIO.LOW)
                else:
                    GPIO.output(18, GPIO.HIGH)
            time.sleep(30)
        except:
            temp1Sensor.set('N/A')

def test2Run(device_file):
    while True:
        try:
            getTemp = read_temp(device_file)
            temp2Sensor.set('{:.1f}C'.format(getTemp[0]))
            time.sleep(30)
        except:
            temp2Sensor.set('N/A')

def voice():
    device = pychromecast.Chromecast(voice_google)
    device.wait()
    media = device.media_controller
    global voiceList
    voiceList = []
    while True:
        if len(voiceList) != 0:
            media.play_media(voiceList[0], 'audio/mp3')
            time.sleep(3)
            voiceList.pop(0)
        time.sleep(0.5)

def pir1Thread():
    global z1PreTrig, extVoiceDefault,voiceList
    while True:
        z1PreTrig = False
        time.sleep(0.2)
        if z1Default == 1:
            if GPIO.input(21) == False:
                grabImg(cam1)
                if extVoiceDefault == 1:
                    voiceList.append(dialog[2])
                dispImg()
                if secMenu:
                    z1PreTrig = True
                    z1Img = tk.PhotoImage(file=z1Trig)
                    z1Btn.config(image=z1Img)
                    GPIO.output(6, GPIO.LOW)
                    time.sleep(z1Timer)
                    try:
                        z1Img = tk.PhotoImage(file=z1BtnsList[z1Default])
                        z1Btn.config(image=z1Img)
                    except:
                        pass
                else:
                    z1PreTrig = True
                    GPIO.output(6, GPIO.LOW)
                    time.sleep(z1Timer)
                    try:
                        z1Img = tk.PhotoImage(file=z1BtnsList[z1Default])
                        z1Btn.config(image=z1Img)
                    except:
                        pass
            else:
                GPIO.output(6, GPIO.HIGH)
                

def pir2Thread():
    global z2PreTrig, extVoiceDefault, voiceList
    while True:
        z2PreTrig = False
        time.sleep(0.2)
        if z2Default == 1:
            if GPIO.input(20) == False:
                grabImg(cam2)
                if extVoiceDefault == 1:
                    voiceList.append(dialog[3])
                dispImg()
                if secMenu:
                    z2PreTrig = True
                    z2Img = tk.PhotoImage(file=z2Trig)
                    z2Btn.config(image=z2Img)
                    GPIO.output(13, GPIO.LOW)
                    time.sleep(z2Timer)
                    try:
                        z2Img = tk.PhotoImage(file=z2BtnsList[z2Default])
                        z2Btn.config(image=z2Img)
                    except:
                        pass
                else:
                    z2PreTrig = True
                    GPIO.output(13, GPIO.LOW)
                    time.sleep(z2Timer)
                    try:
                        z2Img = tk.PhotoImage(file=z2BtnsList[z2Default])
                        z2Btn.config(image=z2Img)
                    except:
                        pass
            else:
                GPIO.output(13, GPIO.HIGH)

def pir3Thread():
    global z3PreTrig, extVoiceDefault, voiceList
    while True:
        z3PreTrig = False
        time.sleep(0.2)
        if z3Default == 1:
            if GPIO.input(16) == False:
                grabImg(cam3)
                if extVoiceDefault == 1:
                    voiceList.append(dialog[4])
                dispImg()
                if secMenu:
                    z3PreTrig = True
                    z3Img = tk.PhotoImage(file=z3Trig)
                    z3Btn.config(image=z3Img)
                    GPIO.output(19, GPIO.LOW)
                    time.sleep(z3Timer)
                    try:
                        z3Img = tk.PhotoImage(file=z3BtnsList[z3Default])
                        z3Btn.config(image=z3Img)
                    except:
                        pass
                else:
                    z3PreTrig = True
                    GPIO.output(19, GPIO.LOW)
                    time.sleep(z3Timer)
                    try:
                        z3Img = tk.PhotoImage(file=z3BtnsList[z3Default])
                        z3Btn.config(image=z3Img)
                    except:
                        pass
            else:
                GPIO.output(19, GPIO.HIGH)

def pir4Thread():
    global z4PreTrig
    while True:
        z4PreTrig = False
        time.sleep(0.2)
        if z4Default == 1:
            if GPIO.input(12) == False:
                if secMenu:
                    z4PreTrig = True
                    z4Img = tk.PhotoImage(file=z4Trig)
                    z4Btn.config(image=z4Img)
                    GPIO.output(26, GPIO.LOW)
                    time.sleep(z4Timer)
                    try:
                        z4Img = tk.PhotoImage(file=z4BtnsList[z4Default])
                        z4Btn.config(image=z4Img)
                    except:
                        pass
                else:
                    z4PreTrig = True
                    GPIO.output(26, GPIO.LOW)
                    time.sleep(z4Timer)
                    try:
                        z4Img = tk.PhotoImage(file=z4BtnsList[z4Default])
                        z4Btn.config(image=z4Img)
                    except:
                        pass
            else:
                GPIO.output(26, GPIO.HIGH)

def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def showTime():
    global timerSecs, getTemp, timeNow, lastTouch, menuScreen, morningTimer, bedtimeTimer
    timerSecs = int(time.time())
    getCurrTimeDate = time.ctime().split()
    todaysDate = getCurrTimeDate[0] + ' ' + getCurrTimeDate[1] + ' ' + getCurrTimeDate[2] + ' ' + getCurrTimeDate[4]
    timeNow = getCurrTimeDate[3]
    currTime.set(timeNow)
    currDate.set(todaysDate)
    if menuScreen == True and (timerSecs - lastTouch) >= 30:
        screenSaver()
    if timeNow == morningTimer:
        setTempVar.set('20.0')
    elif timeNow == bedtimeTimer:
        setTempVar.set('19.0')
    root.after(1000, showTime)

def screenSaver():
    global dispFrame, menuScreen, secMenu
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack()
    root.event_generate('<Motion>', warp=True, x=799, y=479)
    menuScreen = False
    secMenu = False
    bigBtn = tk.Button(dispFrame, textvariable=currTime, font=timeFont, bd=0, highlightthickness=0, 
                       relief='flat', bg='black', fg='gray', activebackground='grey', command=mainMenu)
    bigBtn.pack(ipadx=10, ipady=150)

def heating_menu():
    global dispFrame, menuScreen, lastTouch, secMenu
    global backImg, plusHourImg, progImg, plusTempImg, minusTempImg
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack(expand=True, fill='both')
    menuScreen = True
    lastTouch = int(time.time())
    secMenu = False

    backImg = tk.PhotoImage(file='back_btn.png')
    backBtn = tk.Button(dispFrame, image=backImg, bg='black', bd=0, highlightthickness=0,
                        activebackground='black', command=mainMenu)
    backBtn.grid(row=0, column=0, padx=10, pady=5)

    plusHourImg = tk.PhotoImage(file='plus_hour_btn.png')
    plusHourBtn = tk.Button(dispFrame, image=plusHourImg, bg='black', bd=0, highlightthickness=0, activebackground='black')
    plusHourBtn.grid(row=1, column=0, padx=10)

    progImg = tk.PhotoImage(file='prog_btn.png')
    progBtn = tk.Button(dispFrame, image=progImg, bg='black', bd=0, highlightthickness=0, activebackground='black',
                        command=prog_menu)
    progBtn.grid(row=2, column=0, padx=10, pady=5)
    
    upTemp = tk.Label(dispFrame, textvariable=temp1Sensor, fg='grey', bg='black', font=digitFont)
    upTemp.grid(row=0, column=1, columnspan=3)
    
    setTemp = tk.Label(dispFrame, textvariable=setTempVar, fg='grey', bg='black', font=setFont)
    setTemp.grid(row=0, column=1, rowspan=3, columnspan=3)
    
    dnTemp = tk.Label(dispFrame, textvariable=temp2Sensor, fg='grey', bg='black', font=digitFont)
    dnTemp.grid(row=2, column=1, columnspan=3)

    plusTempImg = tk.PhotoImage(file='plus_temp_btn.png')
    plusTempBtn = tk.Button(dispFrame, image=plusTempImg, bg='black', bd=0, highlightthickness=0,
                            activebackground='black', command=setTempUp)
    plusTempBtn.grid(row=0, column=4, rowspan=2, padx=10, pady=5, sticky='n')

    minusTempImg = tk.PhotoImage(file='minus_temp_btn.png')
    minusTempBtn = tk.Button(dispFrame, image=minusTempImg, bg='black', bd=0, highlightthickness=0,
                             activebackground='black', command=setTempDown)
    minusTempBtn.grid(row=1, column=4, rowspan=2, padx=10, pady=5, sticky='s')

def setTempUp():
    global lastTouch, heatingDelay
    lastTouch = int(time.time())
    heatingDelay = int(time.time())
    currVar = float(setTempVar.get())
    currVar = currVar + float(0.5)
    setTempVar.set(currVar)

def setTempDown():
    global lastTouch, heatingDelay
    lastTouch = int(time.time())
    heatingDelay = int(time.time())
    currVar = float(setTempVar.get())
    currVar = currVar - float(0.5)
    setTempVar.set(currVar)

def security_menu():
    global dispFrame, menuScreen, lastTouch, secMenu
    global z1Img, z1Btn, z2Img, z2Btn, z3Img, z3Btn, z4Img, z4Btn, backImg
    global eVoiceImg, eVoiceBtn, dVoiceImg, dVoiceBtn, modesImg, modesBtn, deckImg, deckBtn
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack(expand=True, fill='both')
    menuScreen = True
    lastTouch = int(time.time())
    secMenu = True

    backImg = tk.PhotoImage(file='round_back_btn.png')
    backBtn = tk.Button(dispFrame, image=backImg, bg='black', bd=0, highlightthickness=0,
                        activebackground='black', command=mainMenu)
    backBtn.grid(row=0, column=0, sticky='n', padx=6, pady=5)

    eVoiceImg = tk.PhotoImage(file=extVoiceBtnsList[extVoiceDefault])
    eVoiceBtn = tk.Button(dispFrame, image=eVoiceImg, bg='black', bd=0, highlightthickness=0,
                          activebackground='black', command=eVoiceChange)
    eVoiceBtn.grid(row=0, column=0, rowspan=2)

    dVoiceImg = tk.PhotoImage(file=doorsBtnsList[doorsDefault])
    dVoiceBtn = tk.Button(dispFrame, image=dVoiceImg, bg='black', bd=0, highlightthickness=0,
                          activebackground='black', command=dVoiceChange)
    dVoiceBtn.grid(row=1, column=0, sticky='s')

    modesImg = tk.PhotoImage(file='cctv_on_btn.png')#modesBtnsList[modesDefault]) Sort so gets img from settings
    modesBtn = tk.Button(dispFrame, image=modesImg, bg='black', bd=0, highlightthickness=0,
                         activebackground='black')#, command=lambda: grabImg('301')) Sort to change the button img not grabImg
    modesBtn.grid(row=0, column=1, padx=6, sticky='s')

    deckImg = tk.PhotoImage(file=deckingBtnsList[deckingDefault])
    deckBtn = tk.Button(dispFrame, image=deckImg, bg='black', bd=0, highlightthickness=0,
                        activebackground='black', command=deckChange)
    deckBtn.grid(row=1, column=1, padx=6, sticky='n')

    if z1Default == 1 and z1PreTrig == True:
        z1Img = tk.PhotoImage(file=z1Trig)
    elif z1Default == 1 and z1PreTrig == False:
        z1Img = tk.PhotoImage(file=z1BtnsList[z1Default])
    else:
        z1Img = tk.PhotoImage(file=z1BtnsList[z1Default])
    z1Btn = tk.Button(dispFrame, image=z1Img, bg='black', bd=0, highlightthickness=0,
                      activebackground='black', command=z1Change)
    z1Btn.grid(row=0, column=2, padx=6, pady=5)

    if z3Default == 1 and z3PreTrig == True:
        z3Img = tk.PhotoImage(file=z3Trig)
    elif z3Default == 1 and z3PreTrig == False:
        z3Img = tk.PhotoImage(file=z3BtnsList[z3Default])
    else:
        z3Img = tk.PhotoImage(file=z3BtnsList[z3Default])
    z3Btn = tk.Button(dispFrame, image=z3Img, bg='black', bd=0, highlightthickness=0,
                      activebackground='black', command=z3Change)
    z3Btn.grid(row=1, column=2, padx=6)

    if z2Default == 1 and z2PreTrig == True:
        z2Img = tk.PhotoImage(file=z2Trig)
    elif z2Default == 1 and z2PreTrig == False:
        z2Img = tk.PhotoImage(file=z2BtnsList[z2Default])
    else:
        z2Img = tk.PhotoImage(file=z2BtnsList[z2Default])
    z2Btn = tk.Button(dispFrame, image=z2Img, bg='black', bd=0, highlightthickness=0,
                      activebackground='black', command=z2Change)
    z2Btn.grid(row=0, column=3, pady=5)

    if z4Default == 1 and z4PreTrig == True:
        z4Img = tk.PhotoImage(file=z4Trig)
    elif z4Default == 1 and z4PreTrig == False:
        z4Img = tk.PhotoImage(file=z4BtnsList[z4Default])
    else:
        z4Img = tk.PhotoImage(file=z4BtnsList[z4Default])
    z4Btn = tk.Button(dispFrame, image=z4Img, bg='black', bd=0, highlightthickness=0,
                      activebackground='black', command=z4Change)
    z4Btn.grid(row=1, column=3)

def z1Change():
    global z1Default, z1Img, z1Btn
    global lastTouch
    lastTouch = int(time.time())
    z1Default += 1
    if z1Default == len(z1BtnsList):
        z1Default = 0
    z1Img = tk.PhotoImage(file=z1BtnsList[z1Default])
    z1Btn.config(image=z1Img)
    if z1Default == 0:
        GPIO.output(6, GPIO.HIGH)
    elif z1Default == 1:
        pass
    else:
        GPIO.output(6, GPIO.LOW)

def z2Change():
    global z2Default, z2Img, z2Btn
    global lastTouch
    lastTouch = int(time.time())
    z2Default += 1
    if z2Default == len(z2BtnsList):
        z2Default = 0
    z2Img = tk.PhotoImage(file=z2BtnsList[z2Default])
    z2Btn.config(image=z2Img)
    if z2Default == 0:
        GPIO.output(13, GPIO.HIGH)
    elif z2Default == 1:
        pass
    else:
        GPIO.output(13, GPIO.LOW)

def z3Change():
    global z3Default, z3Img, z3Btn
    global lastTouch
    lastTouch = int(time.time())
    z3Default += 1
    if z3Default == len(z3BtnsList):
        z3Default = 0
    z3Img = tk.PhotoImage(file=z3BtnsList[z3Default])
    z3Btn.config(image=z3Img)
    if z3Default == 0:
        GPIO.output(19, GPIO.HIGH)
    elif z3Default == 1:
        pass
    else:
        GPIO.output(19, GPIO.LOW)

def z4Change():
    global z4Default, z4Img, z4Btn
    global lastTouch
    lastTouch = int(time.time())
    z4Default += 1
    if z4Default == len(z4BtnsList):
        z4Default = 0
    z4Img = tk.PhotoImage(file=z4BtnsList[z4Default])
    z4Btn.config(image=z4Img)
    if z4Default == 0:
        GPIO.output(26, GPIO.HIGH)
    elif z4Default == 1:
        pass
    else:
        GPIO.output(26, GPIO.LOW)

def eVoiceChange():
    global extVoiceDefault, eVoiceImg, eVoiceBtn
    global lastTouch
    lastTouch = int(time.time())
    extVoiceDefault += 1
    if extVoiceDefault == len(extVoiceBtnsList):
        extVoiceDefault = 0
    eVoiceImg = tk.PhotoImage(file=extVoiceBtnsList[extVoiceDefault])
    eVoiceBtn.config(image=eVoiceImg)

def dVoiceChange():
    global doorsDefault, dVoiceImg, dVoiceBtn
    global lastTouch
    lastTouch = int(time.time())
    doorsDefault += 1
    if doorsDefault == len(doorsBtnsList):
        doorsDefault = 0
    dVoiceImg = tk.PhotoImage(file=doorsBtnsList[doorsDefault])
    dVoiceBtn.config(image=dVoiceImg)

def modesChange():
    global modesDefault, modesImg, modesBtn
    global lastTouch
    lastTouch = int(time.time())
    modesDefault += 1
    if modesDefault == len(modesBtnsList):
        modesDefault = 0
    modesImg = tk.PhotoImage(file=modesBtnsList[modesDefault])
    modesBtn.config(image=modesImg)

def deckChange():
    global deckingDefault, deckImg, deckBtn
    global lastTouch
    lastTouch = int(time.time())
    deckingDefault += 1
    if deckingDefault == len(deckingBtnsList):
        deckingDefault = 0
    deckImg = tk.PhotoImage(file=deckingBtnsList[deckingDefault])
    deckBtn.config(image=deckImg)
    if deckingDefault == 0:
        GPIO.output(23, GPIO.HIGH)
    else:
        GPIO.output(23, GPIO.LOW)

def mainMenu():    
    global dispFrame, menuScreen, lastTouch, htgImg, secImg
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack()
    menuScreen = True
    lastTouch = int(time.time())
    spare = tk.Label(dispFrame, bg='black', width=1)
    spare.grid(row=0, column=0)

    htgImg = tk.PhotoImage(file='heating_btn.png')
    htgBtn = tk.Button(dispFrame, image=htgImg, bg='black', bd=0, highlightthickness=0,
                       activebackground='black', command=heating_menu)
    htgBtn.grid(row=0, column=1, padx=15, pady=60)

    secImg = tk.PhotoImage(file='security_btn.png')
    secBtn = tk.Button(dispFrame, image=secImg, bg='black', bd=0, highlightthickness=0,
                       activebackground='black', command=security_menu)
    secBtn.grid(row=0, column=2, padx=15, pady=60)

def get_prog_timer():
    global morningTimer, morningTemp, bedtimeTimer, bedtimeTemp
    global mDefaultHrs, mDefaultMins, mDefaultTemp, bDefaultHrs, bDefaultMins, bDefaultTemp
    morningTimer = '{}:{}:00'.format(str(mHrsVar.get()), str(mMinsVar.get()))
    mDefaultHrs = str(mHrsVar.get())
    mDefaultMins = str(mMinsVar.get())
    bedtimeTimer = '{}:{}:00'.format(str(bHrsVar.get()), str(bMinsVar.get()))
    bDefaultHrs = str(bHrsVar.get())
    bDefaultMins = str(bMinsVar.get())
    mDefaultTemp = str(mTempVar.get())
    bDefaultTemp = str(bTempVar.get())
    heating_menu()

def prog_menu():
    global dispFrame, menuScreen, lastTouch, secMenu
    global backImg, morningImg, bedtimeImg
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack(expand=True, fill='both')
    menuScreen = True
    lastTouch = int(time.time())
    secMenu = False
    
    backImg = tk.PhotoImage(file='back_btn.png')
    backBtn = tk.Button(dispFrame, image=backImg, bg='black', bd=0, highlightthickness=0,
                        activebackground='black', command=get_prog_timer)
    backBtn.grid(row=0, column=0, padx=10, pady=5)

    tk.Label(dispFrame, text='', bg='black', width=4).grid(row=0, column=1)

    morningImg = tk.PhotoImage(file='morning.png')
    morningLabel = tk.Label(dispFrame, image=morningImg, bg='black')
    morningLabel.grid(row=0, column=2)

    tk.Label(dispFrame, text='', bg='black', width=18).grid(row=0, column=3)
    tk.Label(dispFrame, text='', bg='black', width=2).grid(row=0, column=4)

    mFrame = tk.Frame(dispFrame, bg='black')
    mFrame.grid(row=1, column=0, columnspan=5)

    mHrsBox = tk.Spinbox(mFrame, textvariable=mHrsVar, values=pHrs, font=digitFont, width=2)
    mHrsBox.pack(side='left')
    mHrsVar.set(mDefaultHrs)
    tk.Label(mFrame, text=':', font=digitFont).pack(side='left')
    mMinsBox = tk.Spinbox(mFrame, textvariable=mMinsVar, values=pMins, font=digitFont, width=2)
    mMinsBox.pack(side='left')
    mMinsVar.set(mDefaultMins)
    tk.Label(mFrame, text='', bg='black', width=20).pack(side='left')
    mTempBox = tk.Spinbox(mFrame, textvariable=mTempVar, values=pTemp, font=digitFont, width=4)
    mTempBox.pack(side='left')
    mTempVar.set(mDefaultTemp)

    bedtimeImg = tk.PhotoImage(file='bedtime.png')
    bedtimeLabel = tk.Label(dispFrame, image=bedtimeImg, bg='black')
    bedtimeLabel.grid(row=2, column=2, pady=25)

    tk.Label(dispFrame, text='', bg='black', width=18).grid(row=0, column=3)
    tk.Label(dispFrame, text='', bg='black', width=2).grid(row=0, column=4)

    bFrame = tk.Frame(dispFrame, bg='black')
    bFrame.grid(row=3, column=0, columnspan=5)

    bHrsBox = tk.Spinbox(bFrame, textvariable=bHrsVar, values=pHrs, font=digitFont, width=2)
    bHrsBox.pack(side='left')
    bHrsVar.set(bDefaultHrs)
    tk.Label(bFrame, text=':', font=digitFont).pack(side='left')
    bMinsBox = tk.Spinbox(bFrame, textvariable=bMinsVar, values=pMins, font=digitFont, width=2)
    bMinsBox.pack(side='left')
    bMinsVar.set(bDefaultMins)
    tk.Label(bFrame, text='', bg='black', width=20).pack(side='left')
    bTempBox = tk.Spinbox(bFrame, textvariable=bTempVar, values=pTemp, font=digitFont, width=4)
    bTempBox.pack(side='left')
    bTempVar.set(bDefaultTemp)
    
def grabImg(cam):
    capture = requests.get('http://{}:{}@{}:{}/ISAPI/Streaming/channels/{}/picture?videoResolutionWidth=1920&videoResolutionHeight=1080'.format(user, passwd, camIP, httpPort, cam))
    img = Image.open(io.BytesIO(capture.content))
    newImg = img.resize((800, 450))
    newImg.save('cctv.png')

    
def dispImg():
    global dispFrame, menuScreen, lastTouch, secMenu, cameraImg
    dispFrame.destroy()
    dispFrame = tk.Frame(root, bg='black')
    dispFrame.pack(expand=True, fill='both')
    menuScreen = True
    lastTouch = int(time.time() + 90)
    secMenu = False
    cameraImg = tk.PhotoImage(file='cctv.png')
    cameraLabel = tk.Label(dispFrame, image=cameraImg)
    cameraLabel.pack(pady=15)

u = threading.Thread(target=test1Run, args=(device_folder[0] + '/w1_slave',))
u.start()
d = threading.Thread(target=test2Run, args=(device_folder[0] + '/w1_slave',))
d.start()
pir1 = threading.Thread(target=pir1Thread)
pir1.start()
pir2 = threading.Thread(target=pir2Thread)
pir2.start()
pir3 = threading.Thread(target=pir3Thread)
pir3.start()
pir4 = threading.Thread(target=pir4Thread)
pir4.start()
v = threading.Thread(target=voice)
v.start()
menuScreen = False
global dispFrame
dispFrame = tk.Frame(root)
dispFrame.pack()
screenSaver()
showTime()

root.mainloop()

