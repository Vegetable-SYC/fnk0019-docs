##############################################################################
0. Chapter LED
##############################################################################

This chapter is the Start Point in the journey to build and explore ESP8266 electronic projects. We will start with simple "Blink" project.

0.1. Project Blink
**********************************

In this project, we will use ESP8266 to control blinking a common LED.

Component List
==============================

.. list-table:: 
   :width: 100%
   :align: center

   * -  ESP8266 x1
     -  USB cable
   
   * -  |Chapter00_00|
     -  |Chapter00_01| 

.. |Chapter00_00| image:: ../_static/imgs/0_LED/Chapter00_00.png
.. |Chapter00_01| image:: ../_static/imgs/0_LED/Chapter00_01.png

Power
-------------------------

ESP8266 needs 5v power supply. In this tutorial, we need connect ESP8266 development board to computer via USB cable to power it and program it. We can also use other 5v power source to power it.

.. image:: ../_static/imgs/0_LED/Chapter00_02.png
    :align: center

In the following projects, we only use USB cable to power ESP8266 development board by default.

Sketch
============================

According to the circuit, when the GPIO2 of ESP8266 output level is high, the LED turns ON. Conversely, when the GPIO2 ESP8266 output level is low, the LED turns OFF. Therefore, we can let GPIO2 circularly output high and low level to make the LED blink.

Upload the following Sketch: 

Freenove_Ultimate_Starter_Kit_for_ESP8266\\C\\Sketches\\Sketch_01.1_Blink

Before uploading the code, click "Tools", "Board" and select " NodeMCU 1.0(ESP-12E Module)".

.. image:: ../_static/imgs/0_LED/Chapter00_03.png
    :align: center

Select the serial port.

.. image:: ../_static/imgs/0_LED/Chapter00_04.png
    :align: center

.. note::
    
    For macOS users, if the uploading fails, please set the baud rate to 115200 before clicking "Upload Using Programmer".

.. image:: ../_static/imgs/0_LED/Chapter00_05.png
    :align: center

Sketch_01.1_Blink
------------------------------

.. image:: ../_static/imgs/0_LED/Chapter00_06.png
    :align: center

Click "Upload", Download the code to ESP8266 and your LED in the circuit starts Blink.

.. image:: ../_static/imgs/0_LED/Chapter00_07.png
    :align: center

:red:`If you have any concerns, please contact us via:` support@freenove.com

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 1-20
    :dedent:

The Arduino IDE code usually contains two basic functions: void setup() and void loop(). 

After the board is reset, the setup() function will be executed firstly, and then the loop() function.

setup() function is generally used to write code to initialize the hardware. And loop() function is used to write code to achieve certain functions. loop() function is executed repeatedly. When the execution reaches the end of loop(), it will jump to the beginning of loop() to run again.

.. image:: ../_static/imgs/0_LED/Chapter00_08.png
    :align: center

.. py:function:: Reset

    Reset operation will lead the code to be executed from the beginning. Switching on the power, finishing uploading the code and pressing the reset button will trigger reset operation.

    In the circuit, ESP8266's GPIO2 is connected to the LED, so the LED pin is defined as 2.

In the circuit, ESP8266's GPIO2 is connected to the LED, so the LED pin is defined as 2.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 7-7
    :dedent:

This means that after this line of code, all PIN_LED will be treated as 2.

In the setup () function, first, we set the PIN_LED as output mode, which can make the port output high level or low level.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 10-11
    :dedent:

Then, in the loop () function, set the PIN_LED to output high level to make LED light up.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 16-16
    :dedent:

Wait for 1000ms, that is 1s. Delay () function is used to make control board wait for a moment before executing the next statement. The parameter indicates the number of milliseconds to wait for.

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 17-17
    :dedent:

Then set the PIN_LED to output low level, and LED light off. One second later, the execution of loop () function will be completed. 

.. literalinclude:: ../../../freenove_Kit/C/Sketches/Sketch_01.1_Blink/Sketch_01.1_Blink.ino
    :linenos: 
    :language: c
    :lines: 18-19
    :dedent:

The loop() function is constantly being executed, so LED will keep blinking.

Reference
--------------------------

.. py:function:: void pinMode(int pin, int mode);	
    
    Configures the specified pin to behave either as an input or an output. 
    
    **Parameters**
    
    pin: the pin number to set the mode of.
    
    mode: INPUT, OUTPUT, INPUT_PULLDOWM, or INPUT_PULLUP.
    
.. py:function:: void digitalWrite (int pin, int value);	
    
    Writes the value HIGH or LOW (1 or 0) to the given pin which must have been previously set as an output.
    
For more related functions, please refer to https://www.arduino.cc/reference/en/