# Lab 04: We Interrupt This Program...
 This repository contains the source code and documentation for Lab 4 of ME 405 (Mechatronics) course at California Polytechnic State University.
 
 In this laboratory exercise, we integrated the code developed in the previous week, a user interface and data prinitng function, into a main file which recorded the voltage output through an ADC plot. 
 
 First, we created an output pin object, and a ADC pin object. The step response plot of the voltage output through the RC circuit is shown below (**Figure 1**).
 
 ![Step response with Kp = 0.3, period = 10 ms](https://github.com/jdlu97/Lab-4/blob/main/src/step_response.png?raw=true)
 
 **Figure 1:** Voltage step response of RC circuit with values **R = 100 ohms** and **C = 3.35x10^6 nano-ferrads** with data collection of **800 ms**.
 
 
 As we can see from the plot, the voltage response reaches 63% of steady state value (2,580 ADC in this case), at a little above **300 ms**. 
 This 63% value corresponds with the time constant value of the first-order RC circuit. This compares well to our caculated time constant value
 from the equation: **t=RC**, where **t = 100 ohms x 3.35x10^-3 ferrads = 0.335 seconds**. 
 The observed time constant of 350 ms is 5% greater than the calculated 335 ms value, which is very reasonable compared to the errors of up to 
 25% that can be observed with electronics. Our observed time constant value is taken with low resolution, however even with a much more conservative
 value estimate of 400 ms, it is still only has a 19% error and is within reason. 