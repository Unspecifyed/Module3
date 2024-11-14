import math
import sys

def vector_magnitude(vector):
    """
    Calculate the Pythagorean magnitude of a vector.
    
    Parameters:
        vector (list of float): A vector represented by its components.
    
    Returns:
        float: The magnitude of the vector.
    """
    return math.sqrt(sum(component ** 2 for component in vector))

def main():
    # Check if command line arguments are provided
    if len(sys.argv) > 1:
        try:
            # Convert command line arguments to floats (excluding the script name)
            vector = [float(arg) for arg in sys.argv[1:]]
            magnitude = vector_magnitude(vector)
            print(f"The magnitude of the vector {vector} is {magnitude}")
        except ValueError:
            print("All inputs must be numbers (int or float).")
            sys.exit(1)
    else:
        # Interactive loop for input until "exit" is typed
        while True:
            user_input = input("Enter vector components separated by spaces (or type 'exit' to quit): ")
            if user_input.lower() == "exit":
                print("Exiting the program.")
                break
            
            try:
                # Convert input to floats
                vector = [float(num) for num in user_input.split()]
                magnitude = vector_magnitude(vector)
                print(f"The magnitude of the vector {vector} is {magnitude}")
            except ValueError:
                print("All inputs must be numbers (int or float). Please try again.")

if __name__ == "__main__":
    main()
