##############################################################################
Chapter 74HC595 & 7-Segment Display
##############################################################################

.. include:: ../common/com.74HC595 & 7-Segment Display_1.rst
  
Code
================================================================

This code uses a 74HC595 IC Chip to control the 7-Segment Display. The use of the 74HC595 IC Chip is generally the same throughout this Tutorial. We need code to display the characters “0” to “F” one character at a time, and then output to display them with the 74HC595 IC Chip.

C Code 18.1.1 SevenSegmentDisplay
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter 18.1.1_SevenSegmentDisplay directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/18.1.1_SevenSegmentDisplay

2.	Use following command to compile ``SevenSegmentDisplay.c`` and generate executable file ``SevenSegmentDisplay``.

.. code-block:: console

    $ gcc SevenSegmentDisplay.c -o SevenSegmentDisplay -lwiringPi

3.	Then run the generated file ``SevenSegmentDisplay``.

.. code-block:: console

    $ sudo ./SevenSegmentDisplay

After the program is executed, the 7-Segment Display starts to display the characters “0” to “F” in succession.
The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.1.1_SevenSegmentDisplay/SevenSegmentDisplay.c
    :linenos: 
    :language: C

First, we need to create encoding for characters “0” to “F” in the array.

.. code-block:: c

    unsigned char num[]={0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e};

In the “for” loop of loop() function, use the 74HC595 IC Chip to output contents of array “num” successively. SevenSegmentDisplay can then correctly display the corresponding characters. Pay attention to this in regard to shiftOut function, the transmission bit, flag bit and highest bit will be transmitted preferentially.

.. code-block:: c

    for(i=0;i<sizeof(num);i++){
        digitalWrite(latchPin,LOW);
        _shiftOut(dataPin,clockPin,MSBFIRST,num[i]);//Output the figures and the highest level is transfered preferentially.
        digitalWrite(latchPin,HIGH);
        delay(500);
    }

If you want to display the decimal point, make the highest bit of each array “0”, which can be implemented easily by num[i]&0x7f.

.. code-block:: c

    _shiftOut(dataPin,clockPin,MSBFIRST,num[i] & 0x7f);

.. include:: ../common/com.74HC595 & 7-Segment Display_2.rst

Code
================================================================

In this code, we use the 74HC595 IC Chip to control the 4-Digit 7-Segment Display, and use the dynamic scanning method to show the changing number characters.

C Code 18.2.1 StopWatch
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.\

.. hint:: 
    :red:`If you have any concerns, please contact us via:` support@freenove.com

1.	Use ``cd`` command to enter directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/18.2.1_StopWatch

2.	Use following command to compile ``StopWatch.c`` and generate executable file ``StopWatch``. 

.. code-block:: console

    $ gcc StopWatch.c -o StopWatch -lwiringPi

3.	Run the generated file ``SteppingMotor``.

.. code-block:: console

    $ sudo ./StopWatch

After the program is executed, the 4-Digit 7-Segment Display starts displaying a four-digit number dynamically, and the numeric value of this number will increase by plus 1 each second thereafter.
The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C

First, we define the pin of the 74HC595 IC Chip and the 7-Segment Display Common Anode, use character encoding and a variable "counter" to enable the counter to be visible on the 7-Segment Display.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 12-18

Subfunction selectDigit (int digit) function is used to open one of the 7-Segment Displays while closing the other 7-Segment Displays, where the parameter digit value can be 1,2,4,8. Using "|" can open a number of a 7-Segment Display.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 20-25

Subfunction outData (int8_t data) is used to make the 74HC595 IC Chip output an 8-bit data immediately.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 42-46

Subfunction display (int dec) is used to make a 4-Digit 7-Segment Display a 4-bit integer. First open the common end of first 7-Segment Display Digit and turn OFF the other three Digits, now it can be used as 1-Digit 7-Segment Display. The first Digit is used for displaying single digits of "dec", the second Digit is for tens, the third for hundreds and fourth for thousands respectively. Each digit will be displayed for a period by using delay (). The time in this code is very brief, so you will see digits all together. If the time is set long enough, you will see that every digit is displayed independently.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 47-68

Subfunction timer (int sig) is the timer function, which will set an alarm to signal. This function will be executed once at set time intervals. Accompanied by the execution, “1” will be added as the variable counter and then reset the time of timer to 1s.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 69-75

Finally, in the main function, configure the GPIO, and set the timer function.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 84-93

In the while loop, make the digital display variable counter value “1”. The value will change in function timer (), so the content displayed by the 7-Segment Display will change accordingly.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/18.2.1_StopWatch/StopWatch.c
    :linenos: 
    :language: C
    :lines: 94-96
