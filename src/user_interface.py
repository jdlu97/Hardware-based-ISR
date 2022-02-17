'''! @file    user_interface.py
     @brief   Implements a user interface for Lab 04.
     @details 
     @author  Cade Liberty
     @author  Juan Luna
     @author  Marcus Monroe
     @date    February 10, 2022 
'''
import serial
import matplotlib.pyplot as plt
import time

## Communication port number for task user
COM_num = "COM6"       
        
def send(command):
    '''!    @brief  Sends the proportional gain value over serial.
    '''
    port.write((command+"\r\n").encode('utf-8'))
        
def read():
    '''!    @brief  Reads data from the serial port sent by the Nucleo.
            @param  data    Variable representing data from serial port
    '''
    data = port.readline().decode('utf-8')
             
if __name__ == '__main__':
    
    ## Boolean variable for triggering plotting of the data.
    print_flag = False
    ## Boolean variable that tells program whether Kp is already sent over serial.
    input_flag = False

    ## List of time stamps for each encoder reading value.
    time_list = []
    ## List of encoder position values in step response.
    position = []

    with serial.Serial(str(COM_num), 115200) as port:
    
        while True:
            if print_flag == False:
                if input_flag == False:
                    print('Please, press enter to start step response: ')
                    send(input())
                    print("Recording...")
                    input_flag = True
                    ## @brief   Timing variable keeping track of starting time.
                    start_time = time.time()
                
                else:
                    try:
                        print("Running...")
                        ## Data from serial port
                        data = port.readline().decode('utf-8')
                        ## @brief   Current data from serial port
                        current_data = [idx for idx in data.replace('r\n', '').split(',')]
                        
                        time_list.append(float(current_data[0]))
                        position.append(float(current_data[1]))
                        
                    except:
                        pass
                    
                    if (time.time() - start_time) > 4:
                        print_flag = True
                           
            elif print_flag == True:
                print('Printing a plot...')
                print("t" , len(time_list))
                print("x", len(position))

                ## @brief   fig     Figure on which plot will be shown.
                fig, ax = plt.subplots()

                # Scatter plot of time and position data.
                ax.scatter(time_list, position)

                # Plot labels: title, x-label, and y-label
                ax.set_title("Response Plot")
                ax.set_xlabel("Time, ms")
                ax.set_ylabel("ADC reading")
                    
                # Display the figure
                plt.show()

                print_flag = False
                input_flag = False
                
                ## List of time stamps for each encoder reading value.
                time_list = []
                ## List of encoder position values in step response.
                position = []