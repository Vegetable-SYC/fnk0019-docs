################################################################
Chapter Potentiometer & LED
################################################################

.. include:: ../common/com.Potentiometer & LED.rst

Code
================================================================

Python Code 8.1.1 Softlight
----------------------------------------------------------------

If you did not configure I2C, please refer to :doc:`Chapter 7 ADC <ADC>`. If you did, please continue.

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use cd command to enter 08.1.1_Softlight directory of Python code

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/08.1.1_Softlight

2.	Use the python command to execute the Python code “Softlight.py”.

.. code-block:: console

    $ python Softlight.py

After the program is executed, adjusting the potentiometer will display the voltage values of the potentiometer in the Terminal window and the converted digital quantity. As a consequence, the brightness of LED will be changed.

The following is the code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/08.1.1_Softlight/Softlight.py
    :linenos: 
    :language: python

In the code, read ADC value of potentiometers and map it to the duty cycle of the PWM to control LED brightness.

.. code-block:: python

    value = adc.analogRead(0)      # read the ADC value of channel 0
    led.value = value / 255.0      # Mapping to PWM duty cycle


