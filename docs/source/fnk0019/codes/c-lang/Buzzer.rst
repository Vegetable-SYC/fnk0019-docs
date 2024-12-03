##############################################################################
Chapter Buzzer
##############################################################################

.. include:: ../common/com.Buzzer.rst

Code
================================================================

In this project, a buzzer will be controlled by a push button switch. When the button switch is pressed, the buzzer sounds and when the button is released, the buzzer stops. It is analogous to our earlier project that controlled an LED ON and OFF.

Doorbell
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 06.1.1_Doorbell directory of C code.

.. code-block:: console    
    
    $ cd ~/Freenove_Kit/Code/C_Code/06.1.1_Doorbell

2.	Use following command to compile “Doorbell.c” and generate executable file ``Doorbell.c``.

.. code-block:: console    
    
    $ gcc Doorbell.c -o Doorbell -lwiringPi

3.	Then run the generated file ``Doorbell``.

.. code-block:: console    
    
    $ sudo ./Doorbell

After the program is executed, press the push button switch and the will buzzer sound. Release the push button switch and the buzzer will stop.
The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/Buzzer/Doorbell.c
    :linenos: 
    :language: C

.. note:: 
    The code is exactly the same as when we used a push button switch to control an LED. You can also try using the PNP transistor to achieve the same results.

Project Alertor
****************************************************************

Next, we will use a passive buzzer to make an alarm. 
The list of components and the circuit is similar to the doorbell project. We only need to take the Doorbell circuit and replace the active buzzer with a passive buzzer.

Code
================================================================

In this project, our buzzer alarm is controlled by the push button switch. Press the push button switch and the buzzer will sound. Release the push button switch and the buzzer will stop.
As stated before, it is analogous to our earlier project that controlled an LED ON and OFF.
To control a passive buzzer requires PWM of certain sound frequency.

Alertor
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 06.2.1_Alertor directory of C code.

.. code-block:: console    

    $ cd ~/Freenove_Kit/Code/C_Code/06.2.1_Alertor
2.	Use following command to compile ``Alertor.c`` and generate executable file ``Alertor``. ``-lm`` and ``-lpthread`` compiler options need to added here.

.. code-block:: console    

    $ gcc Alertor.c -o Alertor -lwiringPi -lm -lpthread

3.	Then run the generated file ``Alertor``.

.. code-block:: console    

    $ sudo ./Alertor

After the program is executed, press the push button switch and the buzzer will sound. Release the push button switch and the buzzer will stop.
The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/Buzzer/Alertor.c
    :linenos: 
    :language: C

The code is the same to the active buzzer but the method is different. A passive buzzer requires PWM of a certain frequency, so you need to create a software PWM pin though softToneCreate (buzzeRPin). Here softTone is designed to generate square waves with variable frequency and a duty cycle fixed to 50%, which is a better choice for controlling the buzzer.

.. code-block:: c

    softToneCreate(buzzeRPin);

In the while loop of the main function, when the push button switch is pressed the subfunction alertor() will be called and the alarm will issue a warning sound. The frequency curve of the alarm is based on a sine curve. We need to calculate the sine value from 0 to 360 degrees and multiplied by a certain value (here this value is 500) plus the resonant frequency of buzzer. We can set the PWM frequency through softToneWrite (pin, toneVal).

.. literalinclude:: ../../../../fnk0066-codes/c-lang/Buzzer/Alertor.c
    :linenos: 
    :language: C
    :lines: 9-18

.. code-block:: c

    void stopAlertor(int pin){
        softToneWrite(pin,0);
    }

The related functions of softTone are described as follows: 

.. c:function:: int softToneCreate (int pin) ;

This creates a software controlled tone pin.

.. c:function:: void softToneWrite (int pin, int freq) ;

This updates the tone frequency value on the given pin.

.. hint:: 
    For more details about softTone, please refer to : https://github.com/WiringPi/WiringPi
