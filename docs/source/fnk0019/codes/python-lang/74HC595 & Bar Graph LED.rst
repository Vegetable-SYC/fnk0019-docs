################################################################
Chapter 74HC595 & Bar Graph LED
################################################################

.. include:: ../common/com.74HC595 & Bar Graph LED.rst

Code
================================================================

In this project we will make a flowing water light with a 74HC595 chip to learn about its functions.

Python Code 17.1.1 LightWater02 
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 17.1.1_LightWater02 directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/17.1.1_LightWater02

2.	Use python command to execute Python code “LightWater02.py”. 

.. code-block:: console

    $ python LightWater02.py

After the program is executed, you will see that Bar Graph LED starts with the flowing water pattern flashing from left to right and then back from right to left.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/17.1.1_LightWater02/LightWater02.py
    :linenos: 
    :language: python

Import the OutputDevice class that controls the 74HC595 chip from the gpiozero library.

.. code-block:: python

    from gpiozero import OutputDevice

Create the OutputDevice class for controlling the 74HC595 chip.

.. code-block:: python

    dataPin   = OutputDevice(17)      # DS Pin of 74HC595(Pin14)
    latchPin  = OutputDevice(27)      # ST_CP Pin of 74HC595(Pin12)
    clockPin  = OutputDevice(22)      # CH_CP Pin of 74HC595(Pin11)

In the code, we define a shiftOut() function, which is used to output values with bits in order, where the dPin for the data pin, cPin for the clock and order for the priority bit flag (high or low). This function conforms to the operational modes of the 74HC595. LSBFIRST and MSBFIRST are two different flow directions.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/17.1.1_LightWater02/LightWater02.py
    :linenos: 
    :language: python
    :lines: 19-26

In the loop() function, we use two cycles to achieve the action goal. First, define a variable x=0x01, binary 00000001. When it is transferred to the output port of 74HC595, the low bit outputs high level, then an LED turns ON. Next, x is shifted one bit, when x is transferred to the output port of 74HC595 once again, the LED that turns ON will be shifted. Repeat the operation, over and over and the effect of a flowing water light will be visible. If the direction of the shift operation for x is different, the flowing direction is different.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/17.1.1_LightWater02/LightWater02.py
    :linenos: 
    :language: python
    :lines: 28-43

For more information about the methods used by the OutputDevice class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

