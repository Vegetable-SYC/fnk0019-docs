################################################################
Chapter RGB LED
################################################################

.. include:: ../common/com.RGB LED.rst

Code
================================================================

We need to use RGBLED class to control RGBLED. The parameters for setting the RGBLED as common cathode or common anode are provided in the RGBLED class. You can set it according to the type of your RGB LED, and the default setting in our example code is based on common anode.

Python Code 5.1.1 ColorfulLED
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 05.1.1_ColorfulLED directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/05.1.1_ColorfulLED

2.	Use python command to execute python code “ColorfulLED.py”.

.. code-block:: console

    $ python ColorfulLED.py

After the program is executed, you will see that the RGB LED randomly lights up different colors.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/05.1.1_ColorfulLED/ColorfulLED.py
    :linenos: 
    :language: python

Import the RGBLED class that controls RGBLED from the gpiozero library.

.. code-block:: python
    
    from gpiozero import RGBLED

Create the RGBLED class for controlling the RGBLED.

.. code-block:: python
    
    led = RGBLED(red=17, green=18, blue=27, active_high=False) # define the pins for R:GPIO17,G:GPIO18,B:GPIO2

In the previous chapter, we learned how to make a pin output PWM using the Python language. In this project, we output to three pins via PWM. In the "while" loop of the "loop" function, we first generate three random numbers and then assign these three random numbers to the PWM values of the three pins, which will make the RGB LED randomly produce multiple colors.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/05.1.1_ColorfulLED/ColorfulLED.py
    :linenos: 
    :language: python
    :lines: 21-28

For more information about the methods used by the RGBLED class in the GPIO Zero library,please refer to:
https://gpiozero.readthedocs.io/en/stable/api_output.html#rgbled
