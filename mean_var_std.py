import numpy as np
# the error
# def error_validation(input_list):
# 	# defining an error to raise 
#     if len(input_list) != 9:
#             raise ValueError
#     try:
#         target_array = np.reshape(input_list, (3,3))
#     except ValueError:
#         print('List must contain nine numbers.')

#     return target_array
def calculate(input_list):
    # final output dictionary 
    final_output= {}
    
    # Making an exception for the list if it is less or more than 9 numbers raise a ValueError
    
    if len(input_list) == 9:
        # Reshaping the list into 3x3 array
        target_array = np.reshape(input_list, (3,3))
    
        
        # target_array = np.reshape(input_list, (3,3))
        # target_array = error_validation(input_list)
        
        # Calculating the mean for the target axis in the array 
        # Vertical axis mean
        v_mean = [float(np.mean(target_array[0:,0:1])), float(np.mean(target_array[0:,1:2])), float(np.mean(target_array[0:,2:3]))]
        # Horizontal axis mean
        h_mean = [float(np.mean(target_array[0])), float(np.mean(target_array[1])), float(np.mean(target_array[2]))]
        # The mean of all numbers in the array
        t_mean = float(np.mean(target_array))
        # adding the calculation of mean to the final dictionary
        final_output['mean'] = [v_mean, h_mean, t_mean]
        
        # Vertical axis variance
        v_var = [float(np.var(target_array[0:,0:1])), float(np.var(target_array[0:,1:2])), float(np.var(target_array[0:,2:3]))]
        # Horizontal axis variance
        h_var = [float(np.var(target_array[0])), float(np.var(target_array[1])), float(np.var(target_array[2]))]
        # The variance of all numbers in the array       
        t_var = float(np.var(target_array))
        # Adding the calculation of variance to the final dictionary
        final_output['variance'] = [v_var, h_var, t_var]
        
        # Vertical Standard Deviation
        v_std = [float(np.std(target_array[0:,0:1])), float(np.std(target_array[0:,1:2])), float(np.std(target_array[0:,2:3]))]
        # Horizontal Standard Deviation
        h_std = [float(np.std(target_array[0])), float(np.std(target_array[1])), float(np.std(target_array[2]))]
        # The standard deviation of all numbers in the array      
        t_std = float(np.std(target_array))
         # Adding the calculation of Standard Deviation to the final dictionary
        final_output['standard deviation'] = [v_std, h_std, t_std]    
        
        # Vertical axis max valus 
        v_max = [int(np.max(target_array[0:,0:1])), int(np.max(target_array[0:,1:2])), int(np.max(target_array[0:,2:3]))]
        # Horizontal axis max valus 
        h_max = [int(np.max(target_array[0])), int(np.max(target_array[1])), int(np.max(target_array[2]))]
        # The max value of all numbers in the array      
        t_max = int(np.max(target_array))
        # Adding the calculation of Max values to the final dictionary
        final_output['max'] = [v_max, h_max, t_max]
        
        # Vertical axis min value 
        v_min = [int(np.min(target_array[0:,0:1])), int(np.min(target_array[0:,1:2])), int(np.min(target_array[0:,2:3]))]
        # Horizontal axis min value 
        h_min = [int(np.min(target_array[0])), int(np.min(target_array[1])), int(np.min(target_array[2]))]
        # The min value of all numbers in the array  
        t_min = int(np.min(target_array))
        # Adding the calculation of Min values to the final dictionary
        final_output['min'] = [v_min, h_min, t_min]
        
        # vertical summation
        v_sum = [int(np.sum(target_array[0:,0:1])), int(np.sum(target_array[0:,1:2])), int(np.sum(target_array[0:,2:3]))]
        # horizontal summation
        h_sum = [int(np.sum(target_array[0])), int(np.sum(target_array[1])), int(np.sum(target_array[2]))]
        # The sum of all numbers in the array 
        t_sum = int(np.sum(target_array))
        # Adding the summition values to the final dictionary
        final_output['sum'] = [v_sum, h_sum, t_sum]
        
        # Calculation output  
        return final_output
    else:
        raise ValueError('List must contain nine numbers.')
    

    