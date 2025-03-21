##############################################################################
Chapter Motor & Driver
##############################################################################

In this chapter, we will learn about DC motors and DC motor drivers and how to control the speed and direction of a DC motor.

Project Control Motor with Potentiometer
***************************************************

Control the direction and speed of the motor with a potentiometer.

Component List
============================

+----------------------------------+---------------------------------------+
| ESP8266 x1                       | USB cable                             |
|                                  |                                       |
| |Chapter01_00|                   |  |Chapter01_01|                       |
+----------------------------------+---------------------------------------+
| Breadboard x1                    | Breadboard Power module x1            |
|                                  |                                       |
| |Chapter17_00|                   |  |Chapter17_01|                       |
+----------------------------------+---------------------------------------+
| Jumper wire M/M x12              | Rotary potentiometer x1               |
|                                  |                                       |
| |Chapter17_02|                   |  |Chapter17_04|                       |
+----------------------------------+---------------------------------------+
| Motor x1                         | L293D                                 |
|                                  |                                       |
| |Chapter17_05|                   |  |Chapter17_06|                       |
+----------------------------------+---------------------------------------+
| 9V battery (prepared by yourself) & battery line                         |
|                                                                          |
| |Chapter17_03|                                                           |
+--------------------------------------------------------------------------+

.. |Chapter01_00| image:: ../_static/imgs/1_LED/Chapter01_00.png
.. |Chapter01_01| image:: ../_static/imgs/1_LED/Chapter01_01.png
.. |Chapter17_00| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_00.png
.. |Chapter17_01| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_01.png
.. |Chapter17_02| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_02.png
.. |Chapter17_03| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_03.png
.. |Chapter17_04| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_04.png
.. |Chapter17_05| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_05.png
.. |Chapter17_06| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_06.png

Component knowledge
===========================

L293D
----------------------

L293D is an IC chip (Integrated Circuit Chip) with a 4-channel motor drive. You can drive a unidirectional DC motor with 4 ports or a bi-directional DC motor with 2 ports or a stepper motor (stepper motors are covered later in this Tutorial).

.. image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_07.png
    :align: center

Port description of L293D module is as follows:

+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| Pin name | Pin number   | Description                                                                                                   |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| In x     | 2, 7, 10, 15 | Channel x digital signal input pin                                                                            |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| Out x    | 3, 6, 11, 14 | Channel x output pin, input high or low level according to In x pin, get connected to +Vmotor or 0V           |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| Enable1  | 1            | Channel 1 and channel 2 enable pin, high level enable                                                         |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| Enable2  | 9            | Channel 3 and channel 4 enable pin, high level enable                                                         |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| 0V       | 4, 5, 12, 13 | Power cathode (GND)                                                                                           |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| +V       | 16           | Positive electrode (VCC) of power supply, supply voltage 3.0~36V                                              |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+
| +Vmotor  | 8            | Positive electrode of load power supply, provide power supply for the Out pin x, the supply voltage is +V~36V |
+----------+--------------+---------------------------------------------------------------------------------------------------------------+

For more detail, please refer to the datasheet for this IC Chip.

When using L293D to drive DC motor, there are usually two connection options.

The following connection option uses one channel of the L239D, which can control motor speed through the PWM, However the motor then can only rotate in one direction.

.. image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_08.png
    :align: center

The following connection uses two channels of the L239D: one channel outputs the PWM wave, and the other channel connects to GND, therefore you can control the speed of the motor. When these two channel signals are exchanged, not only controls the speed of motor, but also can control the steering of the motor.

.. image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_09.png
    :align: center

In practical use the motor is usually connected to channel 1 and 2 by outputting different levels to in1 and in2 to control the rotational direction of the motor, and output to the PWM wave to Enable1 port to control the motor's rotational speed. If the motor is connected to channel 3 and 4 by outputting different levels to in3 and in4 to control the motor's rotation direction, and output to the PWM wave to Enable2 pin to control the motor's rotational speed.

Circuit
=========================

Use caution when connecting this circuit because the DC Motor is a high-power component. :red:`Do not use the power provided by the ESP8266 to power the motor directly, as this may cause permanent damage to your RPi!` The logic circuit can be powered by the ESP8266's power or an external power supply, which should share a common ground with ESP8266.

.. list-table:: 
   :width: 100%
   :align: center

   * -  Schematic diagram
   * -  |Chapter17_10|
   * -  Hardware connection. 
    
        If you need any support, please feel free to contact us via: support@freenove.com
   
   * -  |Chapter17_11|

.. |Chapter17_10| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_10.png
.. |Chapter17_11| image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_11.png

Code
========================

Move the program folder "Freenove_Ultimate_Starter_Kit_for_ESP8266/Python/Python_Codes" to disk(D) in advance with the path of "D:/Micropython_Codes".

Open "Thonny", click "This computer" -> "D:" -> "Micropython_Codes" -> "15.1_Motor_And_Driver" and double click "Motor_And_Driver.py". 

Motor_And_Driver
------------------------

.. image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_15.png
    :align: center

Click "Run current script", rotate the potentiometer in one direction and the motor speeds up slowly in one direction. Rotate the potentiometer in the other direction and the motor will slow down to stop. And then rotate it in the original direction to accelerate the motor.

.. image:: ../_static/imgs/17_Motor_&_Driver/Chapter17_16.png
    :align: center

The following is the Code:

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/15.1_Motor_And_Driver/Motor_And_Driver.py
    :linenos: 
    :language: python
    :lines: 1-33
    :dedent:

The ADC of ESP8266 has a 10-bit accuracy, corresponding to a range from 0 to 1023. In this program, set the number 512 as the midpoint. If the value of ADC is less than 512, make the motor rotate in one direction. If the value of ADC is greater than 512, make the motor rotate in the other direction. Subtract 512 from the ADC value and take the absolute value, and then divide this result by 2 to be the speed of the motor.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/15.1_Motor_And_Driver/Motor_And_Driver.py
    :linenos: 
    :language: python
    :lines: 23-31
    :dedent:

Initialize pins of L293D chip.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/15.1_Motor_And_Driver/Motor_And_Driver.py
    :linenos: 
    :language: python
    :lines: 5-9
    :dedent:

Initialize ADC pins, set the range of voltage to 0-3.3V and the acquisition width of data to 0-1023.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/15.1_Motor_And_Driver/Motor_And_Driver.py
    :linenos: 
    :language: python
    :lines: 10-10
    :dedent:

Function driveMotor is used to control the rotation direction and speed of the motor. The dir represents direction while spd refers to speed.

.. literalinclude:: ../../../freenove_Kit/Python/Python_Codes/15.1_Motor_And_Driver/Motor_And_Driver.py
    :linenos: 
    :language: python
    :lines: 12-19
    :dedent: