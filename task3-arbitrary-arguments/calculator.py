def calculation(*args, **kwargs):
    """
    This function takes number of arguments and perform mathematical operations on them
    parameters:
    *args: numbers to be used in performing calculations
    **kwargs: operations to be performed on the numbers such as add, multiply, subtract, divide 
    Returns:
    The result of the specified operation(s) as a numeric value.

    Raises:
    ValueError: If an unsupported operation is provided or if the arguments are invalid.

    Example:
    calculation(1, 2, 3, add=True) returns 6
    calculation(10, 2, divide=True) returns 5.0
    """
    if not args:
        raise ValueError("At least one number is required for calculation.")
     # Check if arguments are numbers
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError(f"Invalid argument: {arg}. All arguments must be numbers.")
    
 # Initialize result
    result = args[0]

    # Apply operations
    if kwargs.get("add", False):  # Check if "add" is set to True
        result = sum(args)

    elif kwargs.get("multiply", False):  # Check if "multiply" is set to True
        result = 1 
        for num in args: 
           
            result *= num

    
    elif kwargs.get("subtract", False):
        for num in args[1:]:
            result -= num

    elif kwargs.get("divide", False):
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num

    else:
        raise ValueError("No valid operation specified. Use add, multiply, subtract, or divide.")
    return result
def main():

    try:
        # Get numbers from the user
        numbers = input("Enter numbers separated by spaces: ")
        args = [float(num) for num in numbers.split()]
        
        # Get the operation from the user
        operation = input("Enter the operation (add, multiply, subtract, divide): ").lower()
        
        # Map the operation to a keyword argument
        kwargs = {operation: True}
        
        # Call the calculation function
        result = calculation(*args, **kwargs)
        
        # Display the result
        print(f"The result of the {operation} operation is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


main() 