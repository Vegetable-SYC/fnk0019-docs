################################################################
Chapter 74HC595 & LED Matrix
################################################################

.. include:: ../common/com.74HC595 & LED Matrix.rst

Code
================================================================

Two 74HC595 IC Chips are used in this project, one for controlling the LED Matrix's columns and the other for controlling the rows. According to the circuit connection, row data should be sent first, then column data. The following code will make the LED Matrix display a smiling face, and then display characters "0 to F" scrolling in a loop on the LED Matrix.

Python Code 19.1.1 LEDMatrix
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

.. hint:: 
    :red:`If you have any concerns, please contact us via:`  support@freenove.com

1.	Use ``cd`` command to enter 19.1.1_LEDMatrix directory of Python language.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/19.1.1_LEDMatrix
    
2.	Use Python command to execute Python code ``LEDMatrix.py``. 

.. code-block:: console

    $ python LEDMatrix.py

After the program is executed, the LED Matrix display a smiling face, and then display characters "0 to F" scrolling in a loop on the LED Matrix.

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/19.1.1_LEDMatrix/LEDMatrix.py
    :linenos: 
    :language: python

The first “for” loop in the “while” loop is used to display a static smile. Displaying column information from left to right, one column at a time with a total of 8 columns. This repeats 500 times to ensure sufficient display time.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/19.1.1_LEDMatrix/LEDMatrix.py
    :linenos: 
    :language: python
    :lines: 50-59

The second “for” loop is used to display scrolling characters "0 to F", for a total of 18 X 8 = 144 columns. Displaying the 0-8 column, then the 1-9 column, then the 2-10 column...... and so on…138-144 column in consecutively to achieve the scrolling effect. The display of each frame is repeated a certain number of times and the more repetitions, the longer the single frame display will be and the slower the scrolling movement.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/19.1.1_LEDMatrix/LEDMatrix.py
    :linenos: 
    :language: python
    :lines: 60-69
