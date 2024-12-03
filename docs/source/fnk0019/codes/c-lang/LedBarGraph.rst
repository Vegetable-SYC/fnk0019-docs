##############################################################################
Chapter LED Bar Graph
##############################################################################

.. include:: ../common/com.LedBarGraph.rst

Code
================================================================
This project is designed to make a flowing water lamp, which are these actions: First turn LED #1 ON, then turn it OFF. Then turn LED #2 ON, and then turn it OFF... and repeat the same to all 10 LEDs until the last LED is turns OFF. This process is repeated to achieve the “movements” of flowing water.

C Code 3.1.1 LightWater
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
        :red:`If you have any concerns, please contact us via:` support@freenove.com

1. Use ``cd`` command to enter ``03.1.1_LightWater`` directory of C code.

.. code-block:: console

       $ cd ~/Freenove_Kit/Code/C_Code/03.1.1_LightWater

2. Use the following command to compile ``LightWater.c`` and generate executable file ``LightWater``.

.. code-block:: console

       $ gcc LightWater.c -o LightWater -lwiringPi

3. Then run the generated file “LightWater”.

.. code-block:: console

       $ sudo ./LightWater

After the program is executed, you will see that Bar Graph LED starts with the flowing water pattern flashing from left to right and then back from right to left.
The following is the program code:

.. literalinclude:: ../../../../fnk0066-codes/c-lang/LightWater/LightWater_1.c
    :linenos: 
    :language: C

In the program, configure the GPIO0-GPIO9 to output mode. Then, in the endless “while” loop of main function, use two “for” loop to realize flowing water light from left to right and from right to left.

.. literalinclude:: ../../../../fnk0066-codes/c-lang/LightWater/LightWater_2.c
    :linenos: 
    :language: C
