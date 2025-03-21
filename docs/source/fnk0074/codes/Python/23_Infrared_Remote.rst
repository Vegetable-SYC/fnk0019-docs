##############################################################################
Chapter Infrared Remote
##############################################################################

In this chapter, we'll learn how to use an infrared remote control, and control a LED.

Project Infrared Remote Control
*****************************************************

First, we need to understand how infrared remote control works, then get the command sent from infrared remote control.

Component List
=======================================

+----------------------------------+---------------------------------------+
| ESP8266 x1                       |  USB cable                            |
|                                  |                                       |
| |Chapter01_00|                   |   |Chapter01_01|                      |
+----------------------------------+---------------------------------------+
| Breadboard x1                                                            |
|                                                                          |
| |Chapter01_02|                                                           |
+----------------------+-------------------------+-------------------------+
| Resistor 10kΩ x1     | Infrared Remote x1      | Jumper wire M/M x6      |
|                      |                         |                         |
| |Chapter23_02|       |  |Chapter23_01|         |     |Chapter23_00|      |
+----------------------+-------------------------+-------------------------+
| Infrared Remote x1                                                       |
|                                                                          |
| (May need CR2025 battery x1, please check the holder)                    |
|                                                                          |
| |Chapter23_03|                                                           |
+--------------------------------------------------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter01_02| image:: ../_static/imgs/1_LED/Chapter01_02.png
.. |Chapter23_00| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_00.png
.. |Chapter23_01| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_01.png
.. |Chapter23_02| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_02.png
.. |Chapter23_03| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_03.png

Component knowledge
============================

Infrared Remote
----------------------------

An infrared(IR) remote control is a device with a certain number of buttons. Pressing down different buttons will make the infrared emission tube, which is located in the front of the remote control, send infrared ray with different command. Infrared remote control technology is widely used in electronic products such as TV, air conditioning, etc. Thus making it possible for you to switch TV programs and adjust the temperature of the air conditioning when away from them. The remote control we use is shown below:

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_04.png
    :align: center

Infrared receiver
-----------------------------

An infrared(IR) receiver is a component which can receive the infrared light, so we can use it to detect the signal emitted by the infrared remote control. DATA pin here outputs the received infrared signal.

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_05.png
    :align: center

When you use the infrared remote control, the infrared remote control sends a key value to the receiving circuit according to the pressed keys. We can program the ESP8266 to do things like lighting, when a key value is received. 

The following is the key value that the receiving circuit will receive when each key of the infrared remote control is pressed.

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_06.png
    :align: center

Circuit
===============================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter23_19|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter23_20|

.. |Chapter23_19| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_19.png
.. |Chapter23_20| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_20.png

Code
===============================

Move the program folder "Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes" to disk(D) in advance with the path of "D:/Micropython_Codes".

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "19.1_Infrared_Remote". Select "irrecvdata.py", right click your mouse to select "Upload to /", wait for "irrecvdata.py" to be uploaded to ESP8266 and then double click "Infrared_Remote.py".

Infrared_Remote
---------------------------

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_21.png
    :align: center

Click "Run current script", press the key of the infrared remote and the key value will be printed in "Shell". As shown in the illustration below:

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_22.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/19.1_Infrared_Remote/Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 1-10
    :dedent:

Import the infrared decoder. 

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/19.1_Infrared_Remote/Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 1-1
    :dedent:

Associate the infrared decoder with Pin(5).

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/19.1_Infrared_Remote/Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 1-1
    :dedent:

Call ir_read() to read the value of the pressed key and assign it to IRValue.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/19.1_Infrared_Remote/Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 6-6
    :dedent:

When infrared key value is obtained, print it out in "Shell".

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/19.1_Infrared_Remote/Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 5-8
    :dedent:

Project Control LED through Infrared Remote
******************************************************

In this project, we will control the brightness of LED lights through an infrared remote control.

Component List
===============================

+----------------------------------+---------------------------------------+
| ESP8266 x1                       |          USB cable                    |
|                                  |                                       |
| |Chapter01_00|                   |          |Chapter01_01|               |
+----------------------------------+---------------------------------------+
| Breadboard x1                                                            |
|                                                                          |
| |Chapter01_02|                                                           |
+----------------------------------+---------------------------------------+
| Active buzzer x1                 | Jumper wire M/M                       |
|                                  |                                       |
| |Chapter23_10|                   |  |Chapter01_05|                       |
+----------------------+-----------+-------------+-------------------------+
| Resistor 10kΩ x2     | Resistor 1kΩ x1         | Resistor 220Ω x1        |
|                      |                         |                         |
| |Chapter16_02|       |  |Chapter16_03|         |  |Chapter16_04|         |
+----------------------+-------------------------+-------------------------+
| NPN transistor x1    | LED x1                  | Infrared receiver x1    |
|                      |                         |                         |
| (S8050)              |                         |                         |
|                      |                         |                         |
| |Chapter23_13|       |  |Chapter23_11|         |  |Chapter23_12|         |
+----------------------+-------------------------+-------------------------+
| Infrared Remote x1                                                       |
|                                                                          |
| (May need CR2025 battery x1, please check the holder)                    |
|                                                                          |
| |Chapter23_14|                                                           |
+--------------------------------------------------------------------------+

.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter16_02| image:: ../_static/imgs/16_Relay_&_Motor/Chapter16_02.png
.. |Chapter16_03| image:: ../_static/imgs/16_Relay_&_Motor/Chapter16_03.png
.. |Chapter16_04| image:: ../_static/imgs/16_Relay_&_Motor/Chapter16_04.png
.. |Chapter23_10| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_10.png
.. |Chapter23_11| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_11.png
.. |Chapter23_12| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_12.png
.. |Chapter23_13| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_13.png
.. |Chapter23_14| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_14.png

Circuit
===============================

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter23_15|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter23_16|

.. |Chapter23_15| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_15.png
.. |Chapter23_16| image:: ../_static/imgs/23_Infrared_Remote/Chapter23_16.png

Code
================================

The Code controls the brightness of the LED by determining the key value of the infrared received.

Move the program folder "Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes" to disk(D) in advance with the path of "D:/Micropython_Codes".

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "23.2_Control_LED_through_Infrared_Remote". Select "irrecvdata.py", right click your mouse to select "Upload to /", wait for "irrecvdata.py" to be uploaded to ESP8266 and then double click "Control_LED_through_Infrared_Remote.py". 

Control_LED_through_Infrared_Remote
------------------------------------------

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_23.png
    :align: center

Click "Run current script". When pressing "0", "1", "2", "3" of the infrared remote control, the buzzer will sound once, and the brightness of the LED light will change correspondingly.

Rendering

.. image:: ../_static/imgs/23_Infrared_Remote/Chapter23_24.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/23.2_Control_LED_through_Infrared_Remote/Control_LED_through_Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 1-35
    :dedent:

The handleControl() function is used to execute events corresponding to infrared code values. Every time when the function is called, the buzzer sounds once and determines the brightness of the LED based on the infrared key value. If the key value is not "0", "1", "2", "3", the buzzer sounds once, but the brightness of LED will not change.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/23.2_Control_LED_through_Infrared_Remote/Control_LED_through_Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 9-27
    :dedent:

Each time the key value of IR remote is received, function handleControl() will be called to process it.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/23.2_Control_LED_through_Infrared_Remote/Control_LED_through_Infrared_Remote.py
    :linenos: 
    :language: python
    :lines: 28-35
    :dedent: