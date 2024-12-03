##############################################################################
Chapter Photoresistor & LED
##############################################################################

.. include:: ../common/com.Photoresistor & LED.rst

Code
================================================================

The code used in this project is identical with what was used in the last chapter.

C Code 10.1.1 Nightlamp
----------------------------------------------------------------

If you did not configure I2C, please refer to :doc:`Chapter 7 ADC <ADC>`. If you did, please continue.
First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 10.1.1_Nightlamp directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/10.1.1_Nightlamp

2.	Use following command to compile ``Nightlamp.cpp`` and generate executable file ``Nightlamp``.

.. code-block:: console

    $ g++ Nightlamp.cpp -o Nightlamp -lwiringPi -lADCDevice

3.	Then run the generated file ``Nightlamp``.

.. code-block:: console

    $ sudo ./Nightlamp

After the program is executed, if you cover the Photoresistor or increase the light shining on it, the brightness of the LED changes accordingly. As in previous projects the Terminal window will display the current input voltage value of ADC module A0 pin and the converted digital quantity.
The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/10.1.1_Nightlamp/Nightlamp.cpp
    :linenos: 
    :language: C

