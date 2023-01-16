import math

def addition(float_1, float_2):
    """Adds two float variables and returns their sum.

    Parameters
    ----------
    float_1 : float
        The first float to add. 
        
    float_2 : float
        The second float to add.


    Returns
    -------
    sum : float
        The sum of float_1 and float_2. 
    """    
    # Performing the calculation
    sum = float_1 + float_2

    # Returning the sum to the user.
    return sum
    
def greet_the_user(time_of_day, name):
    """Generates a string to greet the user based on the time of day, and the user's name

    Parameters
    ----------
    time_of_day : string
        The time of day. 
        Examples: "Morning", "Afternoon", "Evening"
        
    name : string
        The name of the user.


    Returns
    -------
    greeting : string
        The sum of float_1 and float_2. 
    """    
    # Cleaning input strings
    time_of_day = time_of_day.lower()
    name = name.lower()

    #Generating the greeting string. 
    greeting = "good " + time_of_day + ", " + name + "!!!"

    # Returning the sum to the user.
    return greeting
