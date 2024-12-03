##############################################################################
Chapter Potentiometer & LED
##############################################################################

.. include:: ../common/com.Potentiometer & LED.rst

Code
================================================================

C Code 8.1.1 Softlight
----------------------------------------------------------------

If you did not configure I2C, please refer to :doc:`Chapter 7 ADC <ADC>` . If you did, please move on.
First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 08.1.1_Softlight directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/08.1.1_Softlight
2.	Use following command to compile “Softlight.cpp” and generate executable file ``Softlight``.

.. code-block:: console

    $ g++ Softlight.cpp -o Softlight -lwiringPi -lADCDevice
3.	Then run the generated file ``Softlight``.

.. code-block:: console

    $ sudo ./Softlight

After the program is executed, adjusting the potentiometer will display the voltage values of the potentiometer in the Terminal window and the converted digital quantity. As a consequence, the brightness of LED will be changed.

The following is the code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/08.1.1_Softlight/Softlight.cpp
    :linenos: 
    :language: C

In the code, read the ADC value of potentiometer and map it to the duty cycle of PWM to control LED brightness.

.. code-block:: c

    int adcValue = adc->analogRead(0);    //read analog value of A0 pin
    softPwmWrite(ledPin,adcValue*100/255);    // Mapping to PWM duty cycle
