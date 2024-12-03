##############################################################################
Chapter Analog & PWM
##############################################################################

.. include:: ../common/com.Analog & PWM.rst

Code
================================================================

This project uses the PWM output from the GPIO18 pin to make the pulse width gradually increase from 0% to 100% and then gradually decrease from 100% to 0% to make the LED glow brighter then dimmer. 

BreathingLED
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
        :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 04.1.1_BreathingLED directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/04.1.1_BreathingLED

2.	Use following command to compile ``BreathingLED.c`` and generate executable file ``BreathingLED``.

.. code-block:: console

    $ gcc BreathingLED.c -o BreathingLED -lwiringPi

3.	Then run the generated file ``BreathingLED``

.. code-block:: console

    $ sudo ./BreathingLED

After the program is executed, you'll see that LED is turned from on to off and then from off to on gradually like breathing.
The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/BreathingLED/BreathingLED.c
    :linenos: 
    :language: C

First, create a software PWM pin.

.. code-block:: c

    softPwmCreate(ledPin,  0, 100);//Creat SoftPWM pin

There are two “for” loops in the next endless “while” loop. The first loop outputs a power signal to the ledPin PWM from 0% to 100% and the second loop outputs a power signal to the ledPin PWM from 100% to 0%. 

.. literalinclude:: ../../../../fnk0066-codes/c-lang/BreathingLED/BreathingLED.c
    :linenos: 
    :language: C
    :lines: 15-26

You can also adjust the rate of the state change of LED by changing the parameter of the delay() function in the “for” loop.

.. c:function:: int softPwmCreate (int pin, int initialValue, int pwmRange) ;

This creates a software controlled PWM pin.

.. c:function:: int softPwmCreate (int pin, int initialValue, int pwmRange) ;

This updates the PWM value on the given pin.

.. hint:: 
    For more details, please refer https://github.com/WiringPi/WiringPi