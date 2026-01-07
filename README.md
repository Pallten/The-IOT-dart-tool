## Introduction
This project is a tool to assist during the play of darts. With the use of Raspberry Pi Pico WH, ultrasonic sensor HC-SR04 and a LDR photoresistor it measures how much light there is in a room and the distance to a wall. The data is then sent to Ubidots to be displayed. 

The time to complete this project if there are no errors in the WiFi connection is about 1 hour.


## Objective
This project is a very simple yet necessary reminder for myself.
It has two purposes.
1. Measure the distance to the dart board
2. Measure the amount of light

I play a lot of darts, and every so often I wonder why I'm getting a headache and the level of play has decreased. What I've found is that the light in the room has decreased periodically, which has resulted in me playing in a room that is way too dark.
Darts are also a social activity, usually played while drinking. This also adds to the necessity of reminding players of the quality of light.

Furthermore, there is always the question of which one of the players is being cheeky and standing too close to the board. Therefore, the function of measuring distance to the board was implemented to give an easy way to determine where the oche (throw line) should be.

That is why I have chosen to dedicate my IOT project to being an assistant, reminding me of my surroundings.


## Bill of materials
All material is bought at Elecrokit and the price is taken therefrom.
The price was taken June 2024.
If you click the price, you will be taken to the product page on Elecrokit.

| Item                                 | Specicication                                                              |                                 Price (sek)                                  |
|:------------------------------------ |:-------------------------------------------------------------------------- |:----------------------------------------------------------------------------:|
| Raspberry Pi Pico WH                 | Single-board micro controller equipped with Wi-Fi                          |          [109](https://www.electrokit.com/en/raspberry-pi-pico-wh)           |
| Solderless Breadboard 840 tie-points | Connection deck for solder-free connections,                               |      [69](https://www.electrokit.com/en/kopplingsdack-840-anslutningar)      |
| LED 5mm green diffuse 80mcd          | A small green LED light                                                    |         [5](https://www.electrokit.com/en/led-5mm-gron-diffus-80mcd)         |
| LED 5mm yellow diffuse 1500mcd       | A small yellow LED light                                                   |        [5](https://www.electrokit.com/en/led-5mm-gul-diffus-1500mcd)         |
| LED 5mm red diffuse 1500mcd          | A small red LED light                                                      |        [5](https://www.electrokit.com/en/led-5mm-rod-diffus-1500mcd)         |
| Distance sensor ultrasound HC-SR04   | Detects distance with the use of ultrasound. Efficient between 4-400cm     | [59](https://www.electrokit.com/en/avstandsmatare-ultraljud-hc-sr04-2-400cm) |
| Jumper wires 40-pin 30cm male/male   | 40-pin jumper wire with connectors in both ends for use with breadboards   |     [49](https://www.electrokit.com/en/labbsladd-40-pin-30cm-hane/hane)      |
| Resistor 330ohm                      | Resistor for the leds (3x is needed)                                       |    [10](https://www.electrokit.com/en/motstand-kolfilm-0.25w-330ohm-330r)    |
| Resistor 4.7kohm                     | Resistor for the Photo resistor                                            |           [10](https://www.electrokit.com/motstand-1w-54.7kohm-4k7)          |
| USB cable A-male - microB-male 1.8m  | Cable for connection between the microcontroller and computer              |  [39](https://www.electrokit.com/en/usb-kabel-a-hane-micro-b-5p-hane-1.8m)   |
| Photo resistor CdS 4-7 kohm          | Light dependent resistor (LDR). resistance decreases when light increases. |         [8](https://www.electrokit.com/en/fotomotstand-cds-4-7-kohm)         |
| **Total**                            |                                                                            |                                     368                                      |

Most parts were part of a start kit. As you will notice later, the breadboard is a bit large and can therefore be replaced with a smaller one. I do however recommend the one in the item list, as it helps to have extra space and will make future more advanced projects possible.

## Computer setup
I have used Thonny for the coding. ![Thonny_logo](https://hackmd.io/_uploads/HkMXcxOIR.png =x100)
Mainly, the set-up and installation process with Thonny was very simple.
I started using Visual Studio Code (VS Code) but ran into problems that I couldn't identify and therefore switched to Thonny.

VS Code, which is a more in-depth program, could be used as well, but there are more requirements for the setup and installation of additional software. This guide will not be going into that.

1. We will start with the installation of Thonny. You can follow [**THIS**](https://hackmd.io/@lnu-iot/SyTPrHwh_) guide provided by LNU
It covers installation for Windows, Mac and Linux.

2. Then we proceed with the update of the Raspberry. Which you can find [**HERE**](https://micropython.org/download/RPI_PICO_W/)

The reason for these links instead of describing the process myself is to keep the rapport as concise and easy to read as possible.

If you are sure that everything is working, we can proceed to the hardware!

## Putting everything together

Now we can start by connecting the hardware.

![image](https://hackmd.io/_uploads/HkYKmduIC.png)

This is a simple illustration of how I have chosen to place it.
In order to use as few jumpwires as possible, as they clutter up and take up space, I have connected the LEDs with the positive leg (the long one) directly to GND.
The other connection for the LEDs is done with the 330 ohm resistance cables to pins 15, 16 and 17, as can be seen in the illustration above.

Something that is important to remember is that the exact placement isn't that important.
If you choose to place the sensors differently on the breadboard, that won't be a problem as long as the connections are still going to the same pins on the microcontroller.
This too can be changed, but then adjustments to the code will need to be made as well.
![picow-pinout](https://hackmd.io/_uploads/BkNAwQdIA.svg)
Here is the map of the Raspberry Pi Pico WHs pinout.






## Platform
The platform used for displaying the data is Ubidots. Ubidots is a cloud-based IoT data visualization and analytics platform. It allows users to collect, visualize, and analyze data from connected devices.
They have a free plan with which you can achieve everything in this guide.
In the free plan the data is stored for one month. Storage for a longer period than a day is however unnecessary, as the function works to give direct feedback to the user.
**HOWEVER!**
There is a limit to the amount of data points you can send per day. This means that the choosing of Ubidots as the platform is not optimal.
The platform was chosen for its simplicity, and there was not enough time to switch to another.
A self-hosted solution would be optimal as it would allow for data to be sent for longer periods of time, as well as more freedom when designing the visualizations.

## How to install it from scratch

You will start by downloading the code from [**GITHUB**](https://github.com/Pallten/The-IOT-dart-tool.git). 

![image](https://hackmd.io/_uploads/H1uSwvtLA.png)
When following the link, you should arrive at this page

---

![image](https://hackmd.io/_uploads/H1VcOvFUC.png)
Download the zip!

---

![image](https://hackmd.io/_uploads/rJDuFvtUA.png)
Extract the files

---

![image](https://hackmd.io/_uploads/H1IdsDFU0.png)
Open Thonny and navigate to the files

---

![image](https://hackmd.io/_uploads/rJE_fhc8R.png)
Right-click and upload all five files

---

![image](https://hackmd.io/_uploads/SJP6G258R.png)
It should now look like this.

---

![image](https://hackmd.io/_uploads/HygxX2PYI0.png)
Open <keys.py> and enter your WiFi name and password.

---

Go to [**Ubidots**](https://ubidots.com/stem):  and register/log in

![image](https://hackmd.io/_uploads/HJbuZuFIC.png)
Go to devices to add a new one

---

![image](https://hackmd.io/_uploads/Bko2ZdKU0.png)
If there is already an existing test device, then delete it.
Then create a new one.

---

![image](https://hackmd.io/_uploads/r18wz_F8C.png)
Choose blank device

---

![image](https://hackmd.io/_uploads/ryJ4zutUA.png)
Choose the following name exactly:
**PicoWBoard**
This in order to not have to adjust the code!

---

![image](https://hackmd.io/_uploads/HyRCzdFUA.png)
Enter your new device, which will look like this.
Copy the **TOKEN** and replace the text in your <keys.py> file!

---

![image](https://hackmd.io/_uploads/SJmoX_FI0.png)
Create two new variables and name them **distance** and **light**

---

![image](https://hackmd.io/_uploads/S1uNVFt8A.png)

You can now test if it works by going to Thonny, open <main.py> and press play.

---

![image](https://hackmd.io/_uploads/SyA_4YYUC.png)
If done correctly, the shell should connect to WiFi, and start transmitting data to Ubidots.

---

![image](https://hackmd.io/_uploads/SJKzrttLC.png)
And in Ubidots you can see that the variables are receiving data.

---

### There you go!
You have now set it up and are transmitting data from the microcontroller to Ubidots!



This tutorial will not go into the details of how the visualizations were made, since it would make the rapport too in-depth and long.
If you need help with the visualizations, follow this [**LINK**](https://help.ubidots.com/en/articles/8183881-ubidots-basics-widgets)
In the end, I will show an example of how I have chosen to display the data, but you are free to make it however you please.


## The code itself
The code that makes all this work contains libraries for measuring distance and light, as well as the connection and transmission of data.
These libraries can be found here:
[Light](https://github.com/iot-lnu/pico-w/tree/main/sensor-examples/P23_LDR_Photo_Resistor)
[Distance](https://github.com/iot-lnu/pico-w/tree/main/sensor-examples/P27_Ultrasonic_Sensor_HC-SR04)
[WIFI and Ubidots](https://github.com/iot-lnu/pico-w/tree/main/network-examples/N3_WiFi_REST_API_Ubidots)


Something changed in the code that is worth taking note of is the following code:
[![image](https://hackmd.io/_uploads/BkR5g4280.png)](https://hackmd.io/_uploads/BkR5g4280.png)
*clickable image for larger size!



The transfer to Ubidots takes place approximately every 5th second
In order to send more reliable data and receive a rapid response to the distance the use of LEDs have been implemented.
The program runs the code in the distance file five times.
Then finds the median value and gives it to the function which sends it to Ubidots.
The LEDs respond to these values to indicate if the distance to the wall is correct.
This was implemented after observing that the ultrasounds were sometimes unreliable and produced faulty values far above or below the norm.
When five values are produced, it allows for there to be errors which will be disregarded.



## Transmitting the data / connectivity
The microcontroller is connected through WIFI, which for the purpose of using it at home, works well.



HTTP (Hypertext Transfer Protocol) is the protocol used for transferring data over the web. In this project, HTTP is the method used to send sensor data from the device to the Ubidots platform.

HTTP allows the device to communicate with Ubidots by sending data in a structured format called **JSON**, which stands for JavaScript Object Notation. The device uses HTTP POST requests to submit this data to a specific resource on the Ubidots server, referred to as an API endpoint. The URL of this endpoint is where the data is directed on the Ubidots server.

In the HTTP request, headers are included to provide additional information. One header contains an authentication token to verify the device and ensure it is authorized to send data. Another header specifies that the data being sent is formatted as JSON.


## Presenting the data
![image](https://hackmd.io/_uploads/BJAO4dWvA.png)
In this state the distance is not correct, and the light is not sufficient.

![image](https://hackmd.io/_uploads/r1AGHdZvC.png)
In this state the distance is correct, and the light is sufficient!

The "Light over time" graph is to get an overview of when the light is changing. Working as a soft warning before the real one.
The state of change for the indicator is whether the light value is above or below 40. The reason for choosing this value is through prototype testing. I've thrown dart while the sun is setting and checked the light value when it started to be too dark. 

![image](https://hackmd.io/_uploads/rkaZeu-wA.png)
The distance has this added color logic in order to react and respond to the change in distance.



## Finalizing the design
![Artboard 1](https://hackmd.io/_uploads/rkwTsuu80.png)
This is how the setup should be.

---

![image](https://hackmd.io/_uploads/rkJV1QhI0.png)
![image](https://hackmd.io/_uploads/SyCzymn8C.png)
![image](https://hackmd.io/_uploads/SJMS1mhLC.png)
Here are three images of how the project looks in real life.

---

In a perfect world the sensors would be placed by the board instead of by the oche. This is in order to give more reliable light measurements. This setup presumes that the light in the room is universal and equal in all places. This is due to the fact that it's way too unreliable to have the ultrasound bounce on a human instead of a solid wall. 
