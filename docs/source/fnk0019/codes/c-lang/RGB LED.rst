##############################################################################
Chapter RGB LED
##############################################################################

.. include:: ../common/com.RGB LED.rst

Code
================================================================

We need to use the software to make the ordinary GPIO output PWM, since this project requires 3 PWM and in RPi only one GPIO has the hardware capability to output PWM,

C Code 5.1.1 Colorful LED
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 05.1.1_ColorfulLED directory of C code.

.. code-block:: console
    
    $ cd ~/Freenove_Kit/Code/C_Code/05.1.1_ColorfulLED
2.	Use following command to compile ``ColorfulLED.c`` and generate executable file ``ColorfulLED``.

.. note:: 
    in this project, the software PWM uses a multi-threading mechanism. So ``-lpthread`` option need to be add to the compiler.

.. code-block:: console    
    
    $ gcc ColorfulLED.c -o ColorfulLED -lwiringPi -lpthread

3.	And then run the generated file ``ColorfulLED``.

.. code-block:: console
    
    $ sudo ./ColorfulLED
After the program is executed, you will see that the RGB LED shows lights of different colors randomly.

The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/RGBLED/RGBLED.c
    :linenos: 
    :language: C

First, in subfunction of ledInit(), create the software PWM control pins used to control the R, G, B pin respectively.

.. literalinclude:: ../../../../fnk0066-codes/c-lang/RGBLED/RGBLED.c
    :linenos: 
    :language: C
    :lines: 10-15

Then create subfunction, and set the PWM of three pins.

.. literalinclude:: ../../../../fnk0066-codes/c-lang/RGBLED/RGBLED.c
    :linenos: 
    :language: C
    :lines: 17-22

Finally, in the “while” loop of main function, get three random numbers and specify them as the PWM duty cycle, which will be assigned to the corresponding pins. So RGB LED can switch the color randomly all the time.

.. literalinclude:: ../../../../fnk0066-codes/c-lang/RGBLED/RGBLED.c
    :linenos: 
    :language: C
    :lines: 33-42

The related function of PWM Software can be described as follows:

.. c:function:: long random();

This function will return a random number.

.. hint:: 
    For more details about Software PWM, please refer to: https://github.com/WiringPi/WiringPi
