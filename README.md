# Home Heating & Security Control

---
### Requirements:
This project uses mainly standard libraries but some other libraries are required for some features so on the command line enter:<br>

```pip3 install pychromecast``` <-- Used for voice announcement on Google Home.<br>
```pip3 install beautifulsoup4``` <-- Used for web scraping for sunrise and sunset times.<br>
```pip3 install pillow``` <-- Used for resizing CCTV camera image to fit touchscreen but might be installed on some versions of Raspbian or Raspberry Pi OS.<br>

---
This project controls my heating via a temperature sensor through a Raspberry Pi 3B+ GPIO (General Purpose Input Output) and if the set temperature in my Python GUI (Graphical User Interface) then triggers a relay module which is connected to my Central Heating Boiler replacing the old thermostat.<br>I also have 4x external PIR's (Passive Infra-Red Sensors) which are connected to GPIO's individually and LED Security lighting which are individually connected to a relay modules.<br>Each PIR is linked through the python code to a Security Light due to the position around my house. In the Security menu there are settings for voice announcement through our Google Home Mini's.<br>A recent feature I added was that when an external PIR is triggered that the Raspberry Pi would grab a CCTV picture for the corresponding camera from my networked CCTV system and display on the touch screen for 2 minutes.<br><br>Below are some pictures of my custom made frame from off cuts of Oak for the 5" LCD Touchscreen and menus.<br>
!['Screen Saver Mode'](time.png)!['Raspberry Pi 3B+ and PSU'](case.png)!['Security Menu'](security.png)!['Heating Menu'](heating.png)!['Main Menu'](main.png)!['Timer Menu'](timer.png)<br>
The main reason for this project was that our existing GJD Security Lighting Controller touch pad was showing signs of age and our thermostat used AAA batteries and can go through them annually.
