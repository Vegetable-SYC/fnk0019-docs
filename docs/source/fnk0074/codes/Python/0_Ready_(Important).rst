##############################################################################
0. Chapter Ready (Important)
##############################################################################

Before starting building the projects, you need to make some preparation first, which is so crucial that you must not skip.

0.1 Installing Thonny (Important)
*********************************************

Thonny is a free, open-source software platform with compact size, simple interface, simple operation and rich functions, making it a Python IDE for beginners. In this tutorial, we use this IDE to develop ESP6266 during the whole process. 

Thonny supports various operating system, including Windows、Mac OS、Linux.

.. _Thonny:

Downloading Thonny
============================

Official website of Thonny: https://thonny.org 

Open-source code repositories of Thonny: https://github.com/thonny/thonny

Follow the instruction of official website to install Thonny or click the links below to download and install. (Select the appropriate one based on your operating system.)

+------------------+----------------------------------------------------------------------------+
| Operating System | Download links/methods                                                     |
+------------------+----------------------------------------------------------------------------+
| Windows          | https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe |
+------------------+----------------------------------------------------------------------------+
| Mac OS           | https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg |
+------------------+----------------------------------------------------------------------------+
|                  | **The latest version:**                                                    |
|                  |                                                                            |
|                  | **Binary bundle for PC (Thonny+Python):**                                  |
|                  |                                                                            |
|                  | bash <(wget -O - https://thonny.org/installer-for-linux)                   |
|                  |                                                                            |
|                  | **With pip:**                                                              |
|                  |                                                                            |
|                  | pip3 install thonny                                                        |
|                  |                                                                            |
| Linux            | **Distro packages (may not be the latest version):**                       |
|                  |                                                                            |
|                  | **Debian, Rasbian, Ubuntu, Mint and others:**                              |
|                  |                                                                            |
|                  | sudo apt install thonny                                                    |
|                  |                                                                            |
|                  | **Fedora:**                                                                |
|                  |                                                                            |
|                  | sudo dnf install thonny                                                    |
+------------------+----------------------------------------------------------------------------+

You can also open "Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Software", we have prepared it in advance.

.. image:: ../_static/imgs/0_LED/Chapter00_09.png
    :align: center

Installing on Windows
===================================

The icon of Thonny after downloading is as below. Double click "thonny-3.2.7.exe". 

.. image:: ../_static/imgs/0_LED/Chapter00_10.png
    :align: center

If you're not familiar with computer software installation, you can simply keep clicking "Next" until the installation completes.

.. image:: ../_static/imgs/0_LED/Chapter00_11.png
    :align: center

If you want to change Thonny's installation path, you can click "Browse" to modify it. After selecting installation path, click "OK".

If you do not want to change it, just click "Next".

.. image:: ../_static/imgs/0_LED/Chapter00_12.png
    :align: center

Check "Create desktop icon" and then it will generate a shortcut on your desktop to facilitate you to open Thonny later.

.. image:: ../_static/imgs/0_LED/Chapter00_13.png
    :align: center

Click "install" to install the software.

.. image:: ../_static/imgs/0_LED/Chapter00_14.png
    :align: center

During the installation process, you only need to wait for the installation to complete, and you msut not click "Cancel", otherwise Thonny will fail to be installed.

.. image:: ../_static/imgs/0_LED/Chapter00_15.png
    :align: center

Once you see the interface as below, Thonny has been installed successfully.

.. image:: ../_static/imgs/0_LED/Chapter00_16.png
    :align: center

If you've check "Create desktop icon" during the installation process, you can see the below icon on your desktop.

.. image:: ../_static/imgs/0_LED/Chapter00_17.png
    :align: center

0.2 Basic Configuration of Thonny
*****************************************

Click the desktop icon of Thonny and you can see the interface of it as follows:

.. image:: ../_static/imgs/0_LED/Chapter00_18.png
    :align: center

Select "View" -> "Files" and "Shell".

.. image:: ../_static/imgs/0_LED/Chapter00_19.png
    :align: center

.. image:: ../_static/imgs/0_LED/Chapter00_20.png
    :align: center

0.3 Installing CH340 (Important)
*******************************************

ESP8266 uses CH340 to download codes. So before using it, we need to install CH340 driver in our computers.

Windows
===============================

Check whether CH340 has been installed

1.	Connect your computer and ESP8266 with a USB cable.

.. image:: ../_static/imgs/0_LED/Chapter00_21.png
    :align: center

2.	Turn to the main interface of your computer, select "This PC" and right-click to select "Manage".

.. image:: ../_static/imgs/0_LED/Chapter00_22.png
    :align: center

3.	Click "Device Manager". If your computer has installed CH340, you can see"USB-SERIAL CH340 (COMx)". And you can click :ref:`here <Micropython>` to move to the next step.

.. image:: ../_static/imgs/0_LED/Chapter00_23.png
    :align: center

Installing CH340
----------------------------

1.	First, download CH340 driver, click http://www.wch-ic.com/search?q=CH340&t=downloads to download the appropriate one based on your operating system.

.. image:: ../_static/imgs/0_LED/Chapter00_24.png
    :align: center

You can also open " **Freenove_Ultimate_Starter_Kit_for_ESP8266/CH340** ", we have prepared the installation package.

.. image:: ../_static/imgs/0_LED/Chapter00_25.png
    :align: center

2.	Open the folder "Freenove_Ultimate_Starter_Kit_for_ESP8266/CH340/Windows/ch341ser"

.. image:: ../_static/imgs/0_LED/Chapter00_26.png
    :align: center

3.	Double click "CH341SER.EXE".

.. image:: ../_static/imgs/0_LED/Chapter00_27.png
    :align: center

4.	Click "INSTALL" and wait for the installation to complete.

.. image:: ../_static/imgs/0_LED/Chapter00_28.png
    :align: center

5.	Install successfully. Close all interfaces.

.. image:: ../_static/imgs/0_LED/Chapter00_29.png
    :align: center

6.	When ESP8266 is connected to computer, select "This PC", right-click to select "Manage" and click "Device Manager" in the newly pop-up dialog box, and you can see the following interface.

.. image:: ../_static/imgs/0_LED/Chapter00_30.png
    :align: center

7.	So far, CH340 has been installed successfully. Close all dialog boxes. 

MAC
======================================

First, download CH340 driver, click http://www.wch-ic.com/search?q=CH340&t=downloads to download the appropriate one based on your operating system.

.. image:: ../_static/imgs/0_LED/Chapter00_31.png
    :align: center

If you would not like to download the installation package, you can open "Freenove_Ultimate_Starter_Kit_for_ESP8266/CH340", we have prepared the installation package.

Second, open the folder " **Freenove_Ultimate_Starter_Kit_for_ESP8266/CH340/MAC/** "

.. image:: ../_static/imgs/0_LED/Chapter00_32.png
    :align: center

Third, click Continue.

.. image:: ../_static/imgs/0_LED/Chapter00_33.png
    :align: center

Fourth, click Install.

.. image:: ../_static/imgs/0_LED/Chapter00_34.png
    :align: center

Then, waiting Finsh.

.. image:: ../_static/imgs/0_LED/Chapter00_35.png
    :align: center

Finally, restart your PC.

.. image:: ../_static/imgs/0_LED/Chapter00_36.png
    :align: center

If you still haven't installed the CH340 by following the steps above, you can view readme.pdf to install it.

.. image:: ../_static/imgs/0_LED/Chapter00_37.png
    :align: center

.. _Micropython:

0.4 Burning Micropython Firmware (Important)
********************************************************

To run Python programs on ESP8266, we need to burn a firmware to ESP8266 first.

Downloading Micropython Firmware

Official website of microPython: http://micropython.org/

Webpage listing firmware of microPython for ESP8266: https://micropython.org/download/esp8266/

.. image:: ../_static/imgs/0_LED/Chapter00_38.png
    :align: center

Firmware used in this tutorial is **esp8266-20220117-v1.18.bin**

Click the following link to download directly:

https://micropython.org/resources/firmware/esp8266-20220117-v1.18.bin

This file is also provided in our data folder " **Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Firmware** ".

.. _loaded:

Burning a Micropython Firmware
=====================================

Connect your computer and ESP8266 with a USB cable.

.. image:: ../_static/imgs/0_LED/Chapter00_39.png
    :align: center

Make sure that the driver has been installed successfully and that it can recognize COM port correctly. Open device manager and expand "Ports".

.. image:: ../_static/imgs/0_LED/Chapter00_40.png
    :align: center

.. note::
    
    the port of different people may be different, which is a normal situation.

1.	Open Thonny, click "run" and select "Select interpreter...""

.. image:: ../_static/imgs/0_LED/Chapter00_41.png
    :align: center

2.	Select "Micropython (ESP8266)", select "USB-SERIAL CH340 (COM4)", and then click the long button under "Firmware".

.. image:: ../_static/imgs/0_LED/Chapter00_42.png
    :align: center

3.	The following dialog box pops up. Select "USB-SERIAL CH340 (COM4)" for "Port" and then click "Browse...". Select the previous prepared microPython firmware "esp8266-20220117-v1.18.bin". Check "Erase flash before installing" and click "install" to wait for the prompt of finishing installation.

Here we need to select Flash mode.On our ESP8266 development board, choose "DIO" mode or "DOUT" mode for better compatibility.If the ESP8266 module is abnormal, check whether the ESP8266 module works in the two modes.

Flash works in DOUT, DIO, QOUT, and QIO modes. 

1.DOUT: Address is input in 1-line mode and data is output in 2-line mode. 

2.DIO: Address is input in 2-line mode and data is output in 2-line mode. 

3.QOUT: Address is input in 1-line mode and data is output in 4-line mode. 

4.QIO: Address is input in 4-line mode and data is output in 4-line mode. 

If you need to use the QIO mode, ensure that the Flash supports the QIO mode.

.. image:: ../_static/imgs/0_LED/Chapter00_43.png
    :align: center

4.	Wait for the installation to be done.

.. image:: ../_static/imgs/0_LED/Chapter00_44.png
    :align: center

.. image:: ../_static/imgs/0_LED/Chapter00_45.png
    :align: center

After burning the Micropython firmware, "shell" will display some garbled characters, please do not worry, the garbled characters are displayed as follows:

.. image:: ../_static/imgs/0_LED/Chapter00_46.png
    :align: center

When the ESP8266 is powered on, the default baud rate is 74880. The default communication and serial port in the ESP8266 firmware is 115200. So if you set the serial port to 74880, this time can be displayed normally.

Here, we use The Arduino IDE serial port tool for output and display. The details are as follows: 

.. image:: ../_static/imgs/0_LED/Chapter00_47.png
    :align: center

5.	Close all dialog boxes, turn to main interface and click "STOP". As shown in the illustration below. Ignore the garbled part here.

.. image:: ../_static/imgs/0_LED/Chapter00_48.png
    :align: center

6.	So far, all the preparations have been made.

0.5 Testing codes (Important)
****************************************

Testing Shell Command
=================================

Enter "print('hello world')" in "Shell" and press Enter.

.. image:: ../_static/imgs/0_LED/Chapter00_49.png
    :align: center

.. _running_online:

Running Online
===============================

ESP8266 needs to be connected to a computer when it is run online. Users can use Thonny to writer and debug programs.

1.	Open Thonny and click "Open…".

.. image:: ../_static/imgs/0_LED/Chapter00_50.png
    :align: center

2.	On the newly pop-up window, click "This computer".

.. image:: ../_static/imgs/0_LED/Chapter00_51.png
    :align: center

In the new dialog box, select "HelloWorld.py" in 

" **Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes/00.0_HelloWorld** " folder.

.. image:: ../_static/imgs/0_LED/Chapter00_52.png
    :align: center

Click "Run current script" to execute the program and "Hello World" will be printed in "Shell". 

.. image:: ../_static/imgs/0_LED/Chapter00_53.png
    :align: center

.. note:: 
    
    When running online, if you press the reset key of ESP8266, user's code will not be executed again. If you wish to run the code automatically after resetting the code, please refer to the following :ref:`Running Offline <offline>`.

.. _offline:

Running Offline(Important)
=================================

After ESP8266 is reset, it runs the file boot.py in root directory first and then runs file main.py, and finally, it enters "Shell". Therefore, to make ESP8266 execute user's programs after resetting, we need to add a guiding program in boot.py to execute user's code.

1.	Move the program folder " **Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes** " 

to disk(D) in advance with the path of " **D:/Micropython_Codes** ". Open "Thonny".

.. image:: ../_static/imgs/0_LED/Chapter00_54.png
    :align: center

2.	Expand "00.1_Boot" in the "Micropython_Codes" in the directory of disk(D), and double-click boot.py, which is provided by us to enable programs in "MicroPython device" to run offline. 

.. image:: ../_static/imgs/0_LED/Chapter00_55.png
    :align: center

If you want your written programs to run offline, you need to upload boot.py we provided and all your codes to "MicroPython device" and press ESP8266's reset key. Here we use programs 00.0 and 00.1 as examples. Select "boot.py", right-click to select "Upload to /".

.. image:: ../_static/imgs/0_LED/Chapter00_56.png
    :align: center

Similarly, upload "HelloWorld.py" to "MicroPython device".

.. image:: ../_static/imgs/0_LED/Chapter00_57.png
    :align: center

3.	Press the reset key and in the box of the illustration below, you can see the code is executed.

.. image:: ../_static/imgs/0_LED/Chapter00_58.png
    :align: center

When you press the Reset key to run the offline code, the program will continue to execute while the ESP8266 is powered on.

.. image:: ../_static/imgs/0_LED/Chapter00_59.png
    :align: center

When you run offline code, you can exit the running program by pressing "CTRL" and "C" at the same time.   

Before pressing the keyboard, click "Shell" with the mouse, and then press the keyboard key.

.. image:: ../_static/imgs/0_LED/Chapter00_60.png
    :align: center

When your "Shell" is unresponsive or abnormal, you can exit the running program by pressing "CTRL" and "C" simultaneously. 

.. image:: ../_static/imgs/0_LED/Chapter00_61.png
    :align: center

If the ESP8266 does not work properly, you can press CTRL and C at the same time to observe whether the Shell responds.  If the ESP8266 still does not work properly, you can also rewrite the Micropython firmware and perform related operations again.

0.6 Thonny Common Operation
*************************************

Uploading Code to ESP8266
=================================

For convenience, we take the opertation on "boot.py" as an example here. We have added "boot.py" to every
code directory. Each time when ESP8266 restarts, if there is a "boot.py" in the root directory, it will execute this code first.

.. image:: ../_static/imgs/0_LED/Chapter00_62.png
    :align: center

Select "Blink.py" in "01.1_Blink", right-click your mouse and select "Upload to /" to upload code to ESP8266's root directory.

.. image:: ../_static/imgs/0_LED/Chapter00_63.png
    :align: center

Downloading Code to Computer
=================================

Select "boot.py" in "MicroPython device", right-click to select "Download to ..." to download the code to your computer.

.. image:: ../_static/imgs/0_LED/Chapter00_64.png
    :align: center

Deleting Files from ESP8266's Root Directory 
====================================================

Select "boot.py" in "MicroPython device", right-click it and select "Delete" to delete "boot.py" from ESP8266's root directory.

.. image:: ../_static/imgs/0_LED/Chapter00_65.png
    :align: center

Creating and Saving the code 
===================================

Click "File" -> "New" to create and write codes.

.. image:: ../_static/imgs/0_LED/Chapter00_66.png
    :align: center

Enter codes in the newly opened file. Here we use codes of "01.1_Blink.py" as an example.

.. image:: ../_static/imgs/0_LED/Chapter00_67.png
    :align: center

Click "Save" on the menu bar. You can save the codes either to your computer or to ESP8266.

.. image:: ../_static/imgs/0_LED/Chapter00_68.png
    :align: center

Select "MicroPython device", enter "main.py" in the newly pop-up window and click "OK".

.. image:: ../_static/imgs/0_LED/Chapter00_69.png
    :align: center

You can see that codes have been uploaded to ESP8266.

.. image:: ../_static/imgs/0_LED/Chapter00_70.png
    :align: center

.. image:: ../_static/imgs/0_LED/Chapter00_71.png
    :align: center

Disconnect and reconnect USB cable, and you can see that LED is ON for one second and then OFF for one second, which repeats in an endless loop.

.. image:: ../_static/imgs/0_LED/Chapter00_72.png
    :align: center