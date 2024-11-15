import math
import sys

def vector_projection(vector_u, vector_v):
    """
    Calculate the vector projection of vector_u onto vector_v.
    
    Parameters:
        vector_u (list of float): The first vector.
        vector_v (list of float): The second vector.
    
    Returns:
        list of float: The vector projection of vector_u onto vector_v.
    """
    if len(vector_u) != len(vector_v):
        raise ValueError("Both vectors must have the same number of components.")

    # Calculate dot product of vector_u and vector_v
    dot_product = sum(u * v for u, v in zip(vector_u, vector_v))

    # Calculate the magnitude squared of vector_v
    magnitude_v_squared = sum(v ** 2 for v in vector_v)

    if magnitude_v_squared == 0:
        raise ValueError("The magnitude of vector_v is zero. Cannot project onto a zero vector.")

    # Calculate the scalar multiplier for the projection
    scalar_proj = dot_product / magnitude_v_squared

    # Calculate the vector projection
    projection = [scalar_proj * v for v in vector_v]

    return projection

def parse_vectors(input_str):
    """
    Parse the input into two vectors, with the first half of the numbers as vector_u and the rest as vector_v.
    
    Parameters:
        input_str (str): Input string with components separated by spaces.
    
    Returns:
        tuple of list of float: A tuple containing vector_u and vector_v.
    """
    components = input_str.split()
    half_length = len(components) // 2

    if len(components) % 2 != 0:
        raise ValueError("The input must contain an even number of components to form two equal vectors.")

    try:
        vector_u = [float(component) for component in components[:half_length]]
        vector_v = [float(component) for component in components[half_length:]]
    except ValueError:
        raise ValueError("All components must be numeric values.")

    return vector_u, vector_v

def get_input(args):
    """
    Get input string from command line arguments or prompt the user.
    
    Parameters:
        args (list of str): Command line arguments.
    
    Returns:
        str: The input string.
    """
    return " ".join(args[1:]) if len(args) > 1 else input("Enter the vector components separated by spaces (first half is vector_u, second half is vector_v):\n")

def main():
    input_str = get_input(sys.argv)
    try:
        vector_u, vector_v = parse_vectors(input_str)
        projection = vector_projection(vector_u, vector_v)
        print(f"The vector projection of vector_u onto vector_v is {projection}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
