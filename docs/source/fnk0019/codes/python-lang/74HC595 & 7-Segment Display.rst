################################################################
Chapter 74HC595 & 7-Segment Display
################################################################

.. include:: ../common/com.74HC595 & 7-Segment Display_1.rst

Code
================================================================

This code uses a 74HC595 IC Chip to control the 7-Segment Display. The use of the 74HC595 IC Chip is generally the same throughout this Tutorial. We need code to display the characters “0” to “F” one character at a time, and then output to display them with the 74HC595 IC Chip.

Python Code 18.1.1 SevenSegmentDisplay
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 18.1.1_SevenSegmentDisplay directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/18.1.1_SevenSegmentDisplay

2.	Use Python command to execute Python code “SevenSegmentDisplay.py”.

.. code-block:: console

    $ python SevenSegmentDisplay.py

After the program is executed, the 7-Segment Display starts to display the characters “0” to “F” in succession.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/17.1.1_SevenSegmentDisplay/SevenSegmentDisplay.py
    :linenos: 
    :language: python

First, we need to create encoding for characters “0” to “F” in the array.

.. code-block:: python

    num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]

In the “for” loop of loop() function, use the 74HC595 IC Chip to output contents of array “num” successively. SevenSegmentDisplay can then correctly display the corresponding characters. Pay attention to this in regard to shiftOut function, the transmission bit, flag bit amd highest bit will be transmitted preferentially.

.. code-block:: python
    for i in range(0,len(num)):
        latchPin.off()
        shiftOut(MSBFIRST,num[i]) #Output the figures and the highest level is transfered preferentially.
        latchPin.on()
        time.sleep(0.5)

If you want to display the decimal point, make the highest bit of each array “0”, which can be implemented easily by num[i]&0x7f.

.. code-block:: python
    shiftOut(MSBFIRST,num[i]&0x7f) # Use "&0x7f" to display the decimal point.

For more information about the methods used by the OutputDevice class in the GPIO Zero library,please refer to: https://gpiozero.readthedocs.io/en/stable/api_output.html#outputdevice

.. include:: ../common/com.74HC595 & 7-Segment Display_2.rst

Code
================================================================

In this code, we use the 74HC595 IC Chip to control the 4-Digit 7-Segment Display, and use the dynamic scanning method to show the changing number characters.

Python Code 18.2.1 StopWatch
----------------------------------------------------------------

This code uses the four step four pat mode to drive the Stepper Motor clockwise and reverse direction.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use cd command to enter 16.1.1_SteppingMotor directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch

2.	Use python command to execute code "StopWatch.py".

.. code-block:: console

    $ python StopWatch.py

After the program is executed, 4-Digit 7-segment start displaying a four-digit number dynamically, and the will plus 1 in each successive second.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch/StopWatch.py
    :linenos: 
    :language: python

First, define the pin of 74HC595 and 7-segment display common end, character encoding and a variable "counter" to be displayed counter.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch/StopWatch.py
    :linenos: 
    :language: python
    :lines: 15-21

Subfunction selectDigit (digit) function is used to open one of the 7-segment display and close the other 7-segment display, where the parameter digit value can be 1,2,4,8. Using "|" can open a number of 7-segment display.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch/StopWatch.py
    :linenos: 
    :language: python
    :lines: 38-42

Subfunction outData (data) is used to make the 74HC595 output an 8-bit data immediately.

.. code-block:: python

    def outData(data):      # function used to output data for 74HC595
        latchPin.off()
        shiftOut(MSBFIRST,data)
        latchPin.on()

Subfunction display (int dec) is used to make a 4-Digit 7-Segment Display a 4-bit integer. First open the common end of first 7-Segment Display Digit and turn OFF the other three Digits, now it can be used as 1-Digit 7-Segment Display. The first Digit is used for displaying single digits of "dec", the second Digit is for tens, the third for hundreds and fourth for thousands respectively. Each digit will be displayed for a period by using delay (). The time in this code is very brief, so you will a mess of Digits. If the time is set long enough, you will see that every digit is displayed independently.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch/StopWatch.py
    :linenos: 
    :language: python
    :lines: 44-60

Subfunction timer () is the timer callback function. When the time is up, this function will be executed. Accompanied by the execution, the variable counter will be added 1, and then reset the time of timer to 1s. 1s later, the function will be executed again.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/18.2.1_StopWatch/StopWatch.py
    :linenos: 
    :language: python
    :lines: 61-67

Subfunction setup(), configure all input output modes for the GPIO pin used. 

Finally, in loop function, make the digital tube display variable counter value in the while loop. The value will change in function timer (), so the content displayed by 7-segment display will change accordingly.

.. code-block:: python

    def loop():
        global t
        global counter
        t = threading.Timer(1.0,timer)      # set the timer
        t.start()                           #Start timing
        while True:
            display(counter)                #display the number counter

After the program is executed, press "Ctrl+C", then subfunction destroy() will be executed, and GPIO resources and timers will be released in this subfunction.

.. code-block:: python

    def destroy():  
        global t
        dataPin.close()
        latchPin.close()
        clockPin.close() 
        t.cancel()  
