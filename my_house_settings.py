# Settings for my Heating & Security Control

# CCTV variables
user = '' # In the string put your user name for your cctv system
passwd = '' # In the string put your password for you cctv system
camIP = '' # In the string put your local IP address for your cctv system
httpPort = '' # In the string enter your http port setup that is set in your cctv system
cam1 = '101' # Dependng on your cctv system for how many cameras or how the web request is required to view said camera
cam2 = '201' # Replace these values, I have left them in as these worked with my cctv system
cam3 = '301' # For my system the first digit refers to the camera and the 01 being the main stream 02 being substream
# Main stream is for best quality

# Google voice announcements
dialog = [] # Put links to a host for a recorded mp3, I used dropbox for mine

# Testing google home mini
kitchen_google = '' # In the string enter your local IP address for your google for sound from

# Default heating timer settings, these are defaults for when the GUI starts
morningTimer = '07:00:00' # Set them in here or when the GUI is running you can change them
bedtimeTimer = '23:00:00'

# ZONES
# ZONE DEFAULT OPTIONS: 0 = off, 1 = auto, 2 = on (This sets the GUI for how it works
z1BtnsList = ['z1_off_btn.png', 'z1_auto_btn.png', 'z1_on_btn.png']
z1Default = 1
z1Timer = 20
z1Trig = 'z1_trig_btn.png'

z2BtnsList = ['z2_off_btn.png', 'z2_auto_btn.png', 'z2_on_btn.png']
z2Default = 1
z2Timer = 15
z2Trig = 'z2_trig_btn.png'

z3BtnsList = ['z3_off_btn.png', 'z3_auto_btn.png', 'z3_on_btn.png']
z3Default = 1
z3Timer = 10
z3Trig = 'z3_trig_btn.png'

z4BtnsList = ['z4_off_btn.png', 'z4_auto_btn.png', 'z4_on_btn.png']
z4Default = 1
z4Timer = 5
z4Trig = 'z4_trig_btn.png'


# OPTIONS
# DEFAULT OPTIONS: 0 = off, 1 = on
# Ext voice buttons list
extVoiceBtnsList = ['ext_voice_off_btn.png', 'ext_voice_on_btn.png']
extVoiceDefault = 1

# Doors voice buttons list
doorsBtnsList = ['doors_voice_off_btn.png', 'doors_voice_on_btn.png']
doorsDefault = 1

# Modes buttons list
modesBtnsList = ['bbq_grey_btn.png', 'bbq_green_btn.png']
modesDefault = 0

# Decking buttons list
deckingBtnsList = ['decking_off_btn.png', 'decking_on_btn.png']
deckingDefault = 0


