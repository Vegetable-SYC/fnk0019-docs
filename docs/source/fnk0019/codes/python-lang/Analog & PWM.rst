################################################################
Chapter Analog & PWM
################################################################

.. include:: ../common/com.Analog & PWM.rst

Code
================================================================

This project uses the PWM output from the GPIO18 pin to make the pulse width gradually increase from 0% to 100% and then gradually decrease from 100% to 0% to make the LED glow brighter then dimmer. 

Python Code 4.1.1 BreathingLED
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 04.1.1_BreathingLED directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/04.1.1_BreathingLED

2.	Use the Python command to execute Python code “BreathingLED.py”.

.. code-block:: console

    $ python BreathingLED.py

After the program is executed, you will see that the LED gradually turns ON and then gradually turns OFF similar to “breathing”.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/04.1.1_BreathingLED/BreathingLED.py
    :linenos: 
    :language: python

Import the PWMLED class that controls leds from the gpiozero library.

.. code-block:: python

	from gpiozero import PWMLED

Create the PWMLED class for controlling the LED.

.. code-block:: python
    
    led = PWMLED(18 ,initial_value=0 ,frequency=1000)

PWMLED is connected to GPIO18, and its PWM frequency is set to 1000HZ, and the initial duty cycle to 0%.

.. code-block:: python

    led = PWMLED(18 ,initial_value=0 ,frequency=1000) # Set the PWM frequency to 1000Hz and the initial duty cycle to 0

There are two “for” loops used to control the breathing LED in the next endless “while” loop. The first loop outputs a power signal to the led PWM from 0% to 100% and the second loop outputs a power signal to the led PWM from 100% to 0%. 

led.value represents:The duty cycle of the PWM device. 0.0 is off, 1.0 is fully on. led.value in between may be specified for varying levels of power in the device. 

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/04.1.1_BreathingLED/BreathingLED.py
    :linenos: 
    :language: python
    :lines: 12-21

For more information about the methods used by the PWMLED class in the GPIO Zero library,please refer to:
https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmled

For more information about the methods used by the PWMOutputDevice class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_output.html#pwmoutputdevice


