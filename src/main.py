'''!    @file       main.py
        @brief      Main script for execution of Lab 04.
        @details    This programs performs a step response on an RC circuit.
        @author     Juan Luna
        @date       2022-02-17 Original file
        @date       2022-12-30 Modified for portfolio update

'''
import pyb
import task_share
import utime

# Configure the ADC

## Pin object set as analog input for ADC reading
PinC0 = pyb.Pin (pyb.Pin.cpu.C0)
## Pin object set as output for step response
PinC1 = pyb.Pin (pyb.Pin.cpu.C1, pyb.Pin.OUT_PP)
## A/D converter object 
ADC   = pyb.ADC(PinC0)

## Timer object to create interrupts at 1-kHz frequency
Tim1  = pyb.Timer (1, freq = 1000)

## Queue object for data ADC reading data
Read_Queue = task_share.Queue('h', 1000, thread_protect = False, overwrite = False, name = "Read_Queue")

PinC1.low()

## A global variable for counting number of ADC readings 
gl_count = 0

def ADC_Read(Tim1):
    '''! @brief     Reads ADC values from input pin and puts it into a queue.
         @details   Uses an interrupt callback function so to guarantee a lower
                    lantency when running the code.
    '''
    global gl_count
    Read_Queue.put(ADC.read())
    gl_count += 1
    if gl_count == 1250:
        Tim1.callback(None)
    
if __name__ == '__main__':
    
    PinC1.low()
    utime.sleep(1)
    
    ## Counter for keeping track of number of items in queue.
    count = 0
    ## Boolean variable to signal the start/end of the step response.
    step_response = False
    
    while True:
        
        if step_response == True:
            # Read items from queue if there are indeed items
            if Read_Queue.any():
                count += 1
                print(count, ',' , Read_Queue.get())
                
                if Read_Queue.any() == False:
                    step_response = False
                    count = 0
                    
        elif step_response == False:
                        
            PinC1.low()
            gl_count = 0
            Tim1.callback(ADC_Read)
            PinC1.high()
            step_response = True