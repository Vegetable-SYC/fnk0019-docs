################################################################
Chapter Button and leds
################################################################

.. include:: ../common/com.ButtonAndLEDs.rst

Code
================================================================

This project is designed for learning how to use Push Button Switch to control an LED. We first need to read the state of switch, and then determine whether to turn the LED ON in accordance to the state of the switch.

Python Code 2.1.1 ButtonLED
----------------------------------------------------------------

First, observe the project result, then learn about the code in detail. Remember in code “button” = switch function

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 02.1.1_ButtonLED directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/02.1.1_ButtonLED

2.	Use Python command to execute btnLED.py.

.. code-block:: console

    $ python ButtonLED.py

Then the Terminal window continues to show the characters “led off…”, press the switch button and the LED turns ON and then Terminal window shows "led on…". Release the button, then LED turns OFF and then the terminal window text "led off…" appears. You can press "Ctrl+C" at any time to terminate the program. 

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/02.1.1_ButtonLED/ButtonLED.py
    :linenos: 
    :language: python

Import the Button class that controls Button from the gpiozero library.

.. code-block:: python

    from gpiozero import LED, Button

Define GPIO17 as the LED control pin and GPIO18 as the button control pin. The button is set to the input mode with a pull-up resistor by default.

.. code-block:: python

    led = LED(17)       # define LED pin according to BCM Numbering
    button = Button(18) # define Button pin according to BCM Numbering

The loop continuously determines whether the key is pressed. When the button is pressed, the variable button.is_pressed has a value of 1 and the LED lights up. Otherwise, the LED will be off.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/02.1.1_ButtonLED/ButtonLED.py
    :linenos: 
    :language: python
    :lines: 13-20

For more information about GPIOZero, please refer to the link below:

https://gpiozero.readthedocs.io/en/stable/

For more information about the methods used by the Button class in the GPIO Zero library,please refer to:

https://gpiozero.readthedocs.io/en/stable/api_input.html#button


.. include:: ../common/com.ButtonAndLEDs_2.rst

Code
================================================================

In this project, we still detect the state of Push Button Switch to control an LED. Here we need to define a variable to define the state of LED. When the button switch is pressed once, the state of LED will be changed once. This will allow the circuit to act as a virtual table lamp.

Python Code 2.2.1 Tablelamp
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 02.2.1_Tablelamp directory of Python code

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/02.2.1_Tablelamp

2.	Use python command to execute python code “Tablelamp.py”.

.. code-block:: console

    $ python Tablelamp.py

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/02.2.1_Tablelamp/Tablelamp.py
    :linenos: 
    :language: python

In GPIO Zero, you assign the when_pressed and when_released properties to set up callbacks on those actions. 

Once it detects that the button is pressed, it executes the specified function onButtonPressed().In the onButtonPressed function, the led. toggle () function reverses the state of the LED device.If it's on, turn it off; If it's off, turn it on.Each time the key is pressed, the state of the LED will change once.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/02.2.1_Tablelamp/Tablelamp.py
    :linenos: 
    :language: python
    :lines: 14-24

To explicitly close a connection to a pin, you can manually call the close() method on a device object:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/02.2.1_Tablelamp/Tablelamp.py
    :linenos: 
    :language: python
    :lines: 25-34

For more information about the methods used by the Button class in the GPIO Zero library,please refer to:
https://gpiozero.readthedocs.io/en/stable/api_input.html#button
