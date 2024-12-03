################################################################
Chapter Buzzer
################################################################

.. include:: ../common/com.Buzzer.rst

Code
================================================================

In this project, a buzzer will be controlled by a push button switch. When the button switch is pressed, the buzzer sounds and when the button is released, the buzzer stops. It is analogous to our earlier project that controlled an LED ON and OFF.


Python Code 6.1.1 Doorbell
----------------------------------------------------------------

First, observe the project result, then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 06.1.1_Doorbell directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/06.1.1_Doorbell

2.	Use python command to execute python code “Doorbell.py”.

.. code-block:: console

    $ python Doorbell.py

After the program is executed, press the push button switch and the buzzer will sound. Release the push button switch and the buzzer will stop.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/06.1.1_Doorbell/Doorbell.py
    :linenos: 
    :language: python

The code is exactly the same as when we used a push button switch to control an LED. You can also try using the PNP transistor to achieve the same results.
Import the Buzzer class that controls Buzzer from the gpiozero library.

.. code-block:: python

    from gpiozero import Buzzer, Button

Create the Buzzer class for controlling the Buzzer.

.. code-block:: python

    buzzer = Buzzer(17)

In GPIO Zero, you assign the when_pressed and when_released properties to set up callbacks on those actions. 

Once it detects that the button is pressed, it executes the specified function onButtonPressed().  Once it detects that the button is released, it executes the specified function onButtonReleased()

.. code-block:: python
    
    def loop():
    button.when_pressed = onButtonPressed
    button.when_released = onButtonReleased

For more information about the methods used by the Buzzer class in the GPIO Zero library,please refer to:
https://gpiozero.readthedocs.io/en/stable/api_output.html#buzzer

Project 6.2 Alertor
****************************************************************

Next, we will use a passive buzzer to make an alarm. 

The list of components and the circuit is similar to the doorbell project. We only need to take the Doorbell circuit and replace the active buzzer with a passive buzzer.

Code
================================================================

In this project, our buzzer alarm is controlled by the push button switch. Press the push button switch and the buzzer will sound. Release the push button switch and the buzzer will stop.

As stated before, it is analogous to our earlier project that controlled an LED ON and OFF. To control a passive buzzer requires PWM of certain sound frequency.

Python Code 6.2.1 Alertor
----------------------------------------------------------------

First observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 06.2.1_Alertor directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/06.2.1_Alertor

2.	Use the python command to execute the Python code “Alertor.py”.

.. code-block:: console

    $ python Alertor.py

After the program is executed, press the push button switch and the buzzer will sound. Release the push button switch and the buzzer will stop.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/06.2.1_Alertor/Alertor.py
    :linenos: 
    :language: python


Define GPIO17 as the buzzer control pin, and GPIO18 as the button control pin to control the passive buzzer. It requires a certain frequency of PWM to control a passive buzzer, so the TonalBuzzer class is needed.

.. code-block:: python

    buzzer = TonalBuzzer(17)
    button = Button(18) # define Button pin according to BCM Numbering

In the while loop loop of the main function, when the push button switch is pressed the subfunction alertor() will be called and the alarm will issue a warning sound. The frequency curve of the alarm is based on a sine curve. We need to calculate the sine value from 0 to 360 degrees and multiplied by a certain value (here this value is 500) plus the resonant frequency of buzzer. We can set the PWM frequency through Tone(toneVal).

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/06.2.1_Alertor/Alertor.py
    :linenos: 
    :language: python
    :lines: 24-26

When the push button switch is released, the buzzer (in this case our Alarm) will stop.

.. code-block:: python

    def stopAlertor():
    buzzer.stop()

For more information about the methods used by the TonalBuzzer class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_output.html#tonalbuzzer

