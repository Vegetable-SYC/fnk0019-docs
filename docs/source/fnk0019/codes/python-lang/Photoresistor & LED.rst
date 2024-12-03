################################################################
Chapter Photoresistor & LED
################################################################

.. include:: ../common/com.Photoresistor & LED.rst

Code
================================================================

The code used in this project is identical with what was used in the last chapter.

Python Code 10.1.1 Nightlamp
----------------------------------------------------------------

If you did not configure I2C, please refer to :doc:`Chapter 7 ADC <ADC>`. If you did, please continue.

First, observe the project result, and then learn about the code in detail. 

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use cd command to enter 10.1_Nightlamp directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/10.1.1_Nightlamp

2.	Use the python command to execute the Python code “Nightlamp.py”.

.. code-block:: console

    $ python Nightlamp.py

After the program is executed, if you cover the Photoresistor or increase the light shining on it, the brightness of the LED changes accordingly. As in previous projects the Terminal window will display the current input voltage value of ADC module A0 pin and the converted digital quantity.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/10.1.1_Nightlamp/Nightlamp.py
    :linenos: 
    :language: python

