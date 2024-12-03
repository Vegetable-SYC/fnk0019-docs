################################################################
Chapter Button and leds
################################################################

.. include:: ../common/com.ButtonAndLEDs.rst

Code
================================================================

This project is designed for learning how to use Push Button Switch to control an LED. We first need to read the state of switch, and then determine whether to turn the LED ON in accordance to the state of the switch.

C language codes 
----------------------------------------------------------------
First, observe the project result, then learn about the code in detail.

.. hint:: 
    If you need any support, please feel free to contact us via: support@freenove.com

1. Use ``cd`` command to enter ``ButtonLED`` directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/ButtonLED

2. Use the following command to compile the code ``ButtonLED.c`` and generate executable file ``ButtonLED``.

.. code-block:: console

    $ gcc ButtonLED.c -o ButtonLED -lwiringPi

3. Then run the generated file ``blink``.

.. code-block:: console

    $ sudo ./ButtonLED

Later, the terminal window continues to print out the characters “led off…”. Press the button, then LED is turned on and then terminal window prints out the "led on…". 
Release the button, then LED is turned off and then terminal window prints out the "led off…". You can press ``Ctrl+C`` to terminate the program.

The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/ButtonLED/ButtonLED.c
    :linenos: 
    :language: C

In the circuit connection, LED and Button are connected with GPIO17 and GPIO18 respectively, which correspond to 0 and 1 respectively in wiringPI. So define ledPin and buttonPin as 0 and 1 respectively.

.. code-block:: c

    #define ledPin    0     //define the ledPin
    #define buttonPin 1     //define the buttonPin

In the while loop of main function, use digitalRead(buttonPin) to determine the state of Button. When the button is pressed, the function returns low level, the result of “if” is true, and then turn on LED. Or, turn off LED

.. literalinclude:: ../../../../fnk0066-codes/c-lang/ButtonLED/ButtonLED.c
    :linenos: 
    :language: C
    :lines: 24-31

.. c:function:: int digitalRead (int pin);

    This function returns the value read at the given pin. It will be “HIGH” or “LOW”(1 or 0) depending on the logic level at the pin.


