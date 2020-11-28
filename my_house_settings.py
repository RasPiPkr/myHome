# Settings for my Heating & Security Control

# GPIO pins used on Raspberry Pi
relayPins = [18, 23, 24, 22, 6, 13, 19, 26]
pirPins = [21, 20, 16, 12]

# CCTV variables
user = '' # In the string put your user name for your cctv system
passwd = '' # In the string put your password for you cctv system
camIP = '' # In the string put your local IP address for your cctv system
httpPort = '' # In the string enter your http port setup that is set in your cctv system
# Your system might not need these:
cam1 = '101' # Dependng on your cctv system for how many cameras or how the web request is required to view said camera
cam2 = '201' # Replace these values, I have left them in as these worked with my cctv system
cam3 = '301' # For my system the first digit refers to the camera and the 01 being the main stream 02 being substream
# Main stream is for best quality

# Google voice announcements
dialog = [] # Put links to a host for a recorded mp3, I used dropbox for mine

# Testing google home mini
voice_google = '' # In the string enter your local IP address for your google for sound from

# Default heating timer settings, these are defaults for when the GUI starts
morningTimer = '07:00:00' # Set them in here or when the GUI is running you can change them then
morningTimerTemp = '20.0'
bedtimeTimer = '23:00:00'
bedtimeTimerTemp = '19.0'
defaultTemp = '20.0'

# External lights on time
sunset = '16:00:00'
sunrise = '07:00:00'

# ZONES
# ZONE DEFAULT OPTIONS: 0 = off, 1 = auto, 2 = on (This sets the GUI for how it works)
z1BtnsList = ['z1_off_btn.png', 'z1_auto_btn.png', 'z1_on_btn.png']
z1Default = 1
z1Timer = 120 # Seconds
z1Trig = 'z1_trig_btn.png'

z2BtnsList = ['z2_off_btn.png', 'z2_auto_btn.png', 'z2_on_btn.png']
z2Default = 1
z2Timer = 120 # Seconds
z2Trig = 'z2_trig_btn.png'

z3BtnsList = ['z3_off_btn.png', 'z3_auto_btn.png', 'z3_on_btn.png']
z3Default = 1
z3Timer = 120 # Seconds
z3Trig = 'z3_trig_btn.png'

z4BtnsList = ['z4_off_btn.png', 'z4_auto_btn.png', 'z4_on_btn.png']
z4Default = 1
z4Timer = 120 # Seconds
z4Trig = 'z4_trig_btn.png'


# OPTIONS
# DEFAULT OPTIONS: 0 = off, 1 = on
# Ext voice buttons list
extVoiceBtnsList = ['ext_voice_off_btn.png', 'ext_voice_on_btn.png']
extVoiceDefault = 0

# Doors voice buttons list
doorsBtnsList = ['doors_voice_off_btn.png', 'doors_voice_on_btn.png']
doorsDefault = 0

# CCTV buttons list
cctvBtnsList = ['cctv_off_btn.png', 'cctv_on_btn.png']
cctvDefault = 0

# Decking buttons list
deckingBtnsList = ['decking_off_btn.png', 'decking_on_btn.png']
deckingDefault = 0


