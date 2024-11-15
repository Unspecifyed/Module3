import sys

def cross_product(vector_u, vector_v):
    """
    Calculate the cross product of vector_u and vector_v using the given formula.
    
    Parameters:
        vector_u (list of float): The first vector.
        vector_v (list of float): The second vector.
    
    Returns:
        list of float: The cross product of vector_u and vector_v using the specified formula.
    """
    if len(vector_u) != 3 or len(vector_v) != 3:
        raise ValueError("Both vectors must have exactly 3 components.")

    # Calculate the cross product using the given formula
    cross_prod = [
        vector_u[1] * vector_v[2] - vector_v[1] * vector_u[2],
        vector_u[2] * vector_v[0] - vector_v[2] * vector_u[0],
        vector_u[0] * vector_v[1] - vector_u[0] * vector_u[1]
    ]

    return cross_prod

def parse_vectors(input_str):
    """
    Parse the input into two 3D vectors.
    
    Parameters:
        input_str (str): Input string with components separated by spaces.
    
    Returns:
        tuple of list of float: A tuple containing vector_u and vector_v.
    """
    components = input_str.split()

    if len(components) != 6:
        raise ValueError("The input must contain exactly 6 components to form two 3D vectors.")

    try:
        vector_u = [float(component) for component in components[:3]]
        vector_v = [float(component) for component in components[3:]]
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
    return " ".join(args[1:]) if len(args) > 1 else input("Enter the vector components separated by spaces (first 3 components are vector_u, next 3 components are vector_v):\n")

def main():
    input_str = get_input(sys.argv)
    try:
        vector_u, vector_v = parse_vectors(input_str)
        cross_prod = cross_product(vector_u, vector_v)
        print(f"The cross product of vector_u and vector_v is {cross_prod}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
