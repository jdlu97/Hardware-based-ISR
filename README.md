# Hardware-Based Interrupt Service Routine
 
 In this project, we wrote and tested interrupt-based code using the STM32 Nucleo microcontroller and an RC circuit connected to it. We wrote an interrupt callback function to read ADC values on an analog pin and additional code that would save the data on a queue. Likewise, we adapted our previously-developed user interface to send user input (a simple "press enter" prompt) to the main program that initiated a step response and receive data from a queue using serial communication. The user interface also included printing and plotting functionality to visually show the step response (in the form of ADC reading as a function of time).
 
 On the electrical aspect of the project, we had an RC circuit made from a 100-ohm resistor and a 3.35e+6 nano-farads capacitor.
 
 The step response plot of one of our test runs is shown below (**Figure 1**) for a 1000-ms data collection.

 <p align="center">
    <img src="https://github.com/jdlu97/Hardware-based-ISR/blob/main/img/step_response.jpg?raw=true" alt="Step response of RC circuit"/>
 </p>
 
 <p align="center">Step response for the RC-circuit with a time-constant of about <b>360 ms</b>.</p><br/>
 
 As we can see from the plot, the ADC readings reach 63% of the steady state value, 2,580 ADC in this case, at around **360 ms**. 
 This 63% of the final value number corresponds with the time constant value of the first-order RC circuit. This value closely matches with the calculated time constant from theory, using the equation: $t=RC$, where $t = 100$ &Omega; x $3.35\cdot10^{-3} F = 0.335$ seconds.
 
 The observed time constant of 360 ms is 7.2% greater than the calculated 335 ms value. This is a reasonable number considering the errors of up to 25% that can be observed with electronics. Our observed time constant value is taken with low resolution. However , even with a much more conservative value estimate of 400 ms, it is still only has a 19% error and is within reason. 
 
 ## Known Issues
 
 In the user interface code `user_interface.py`, we were only able to run our program when a print statement in line 53 is present. Simply removing this would cause the code to execute but never run the step response. While this issue could have been resolved by reviewing the structure of the code and spending time debugging, our team prioritized functionality so we accepted this bug for now and continued working on the exercise until completion. A future version of the code will look into this issue.