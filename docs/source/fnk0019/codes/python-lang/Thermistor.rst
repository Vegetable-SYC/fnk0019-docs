################################################################
Chapter Thermistor
################################################################

.. include:: ../common/com.Thermistor.rst

Code
================================================================

In this project code, the ADC value still needs to be read, but the difference here is that a specific formula is used to calculate the temperature value.

Python Code 11.1.1 Thermometer
----------------------------------------------------------------

If you did not configure I2C, please refer to :doc:`Chapter 7 ADC <ADC>`. If you did, please continue.

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 11.1.1_Thermometer directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/11.1.1_Thermometer

2.	Use python command to execute Python code “Thermometer.py”.

.. code-block:: console

    $ python Thermometer.py

After the program is executed, the Terminal window will display the current ADC value, voltage value and temperature value. Try to “pinch” the thermistor (without touching the leads) with your index finger and thumb for a brief time, you should see that the temperature value increases.

.. image:: ../_static/imgs/Thermistor_value.png
    :align: center

The following is the code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/11.1.1_Thermometer/Thermometer.py
    :linenos: 
    :language: python

In the code, the ADC value of ADC module A0 port is read, and then calculates the voltage and the resistance of Thermistor according to Ohms Law. Finally, it calculates the temperature sensed by the Thermistor, according to the formula. 
