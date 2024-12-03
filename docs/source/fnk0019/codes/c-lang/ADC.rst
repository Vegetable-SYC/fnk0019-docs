.. _ADC:

##############################################################################
(Important) Chapter ADC
##############################################################################

.. include:: ../common/com.ADC.rst

Code
================================================================

C Code 7.1.1 ADC
----------------------------------------------------------------

For C code for the ADC Device, a custom library needs to be installed.

1.	Use ``cd`` command to enter folder of the ADC Device library.

.. code-block:: console

    $ cd ~/Freenove_Kit/Libs/C-Libs/ADCDevice

2.	Execute command below to install the library.

.. code-block:: console

    $ sh ./build.sh

3. A successful installation, without error prompts, is shown below:

.. image:: ../_static/imgs/build.sh.png
        :width: 100%
        :align: center

Next, we will execute the code for this project.
First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 07.1.1_ADC directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/07.1.1_ADC
2.	Use following command to compile ``ADC.cpp`` and generate the executable file ``ADC``.

.. code-block:: console

    $ g++ ADC.cpp -o ADC -lwiringPi -lADCDevice
3.	Then run the generated file ``ADC``.

.. code-block:: console

    $ sudo ./ADC

After the program is executed, adjusting the potentiometer will produce a readout display of the potentiometer voltage values in the Terminal and the converted digital content. 

.. image:: ../_static/imgs/volatage-values.png
        :width: 100%
        :align: center

The following is the code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/07.1.1_ADC/ADC.cpp
    :linenos: 
    :language: C

In this code, a custom class library "ADCDevice" is used. It contains the method of utilizing the ADC Module in this project, through which the ADC Module can easily and quickly be used. In the code, you need to first create a class pointer adc, and then point to an instantiated object.

.. note:: 
    An instantiated object is given a name and created in memory or on disk using the structure described within a class declaration.

.. code-block:: c

    ADCDevice *adc;  // Define an ADC Device class object   
    ......
    adc = new ADCDevice();

Then use the member function detectIC(addr) in the class to detect the I2C module in the circuit. Different modules have different I2C addresses. Therefore, according to the different addresses, we can determine what the ADC module is in the circuit. When the correct module is detected, the pointer adc will point to the address of the object, and then the previously pointed content will be deleted to free memory. The default address of ADC module PCF8591 is 0x48, and that of ADC module ADS7830 is 0x4b.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/07.1.1_ADC/ADC.cpp
    :linenos: 
    :language: C
    :lines: 17-30

When you have a class object pointed to a specific device, you can get the ADC value of the specific channel by calling the member function analogRead (chn) in this class

.. code-block:: c

    int adcValue = adc->analogRead(0);  //read analog value of A0 pin

Then according to the formula, the voltage value is calculated and displayed on the Terminal.

.. code-block:: c

    float voltage = (float)adcValue / 255.0 * 3.3;  // Calculate voltage
    printf("ADC value : %d  ,\tVoltage : %.2fV\n",adcValue,voltage);

Reference:

.. c:function:: class ADCDevice

    This is a base class. All ADC module classes are its derived classes. It has a real function and a virtual function.

    .. c:function:: int detectI2C(int addr);

        This is a real function, which is used to detect whether the device with given I2C address exists. If it exists, return 1, otherwise return 0.

    .. c:function:: virtual int analogRead(int chn);

        This is a virtual function that reads the ADC value of the specified channel. It is implemented in a derived class.

.. c:function:: class PCF8591:public ADCDevice & class ADS7830:public ADCDevice  

    These two classes are derived from the ADCDevice class and mainly implement the function analogRead(chn).

    .. c:function:: int analogRead(int chn);

        This returns the value read on the supplied analog input pin.Parameter chn: For PCF8591, the range of chn is 0, 1, 2, 3. For ADS7830, the range of is 0, 1, 2, 3, 4, 5, 6, 7

You can find the source file of this library in the folder below: 

.. code-block:: console

    $ ~/Freenove_Kit/Libs/C-Libs/ADCDevice/
