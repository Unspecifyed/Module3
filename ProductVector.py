import sys
from functools import reduce

def dot_product(vectors):
    """
    Calculate the cumulative dot product of multiple vectors.
    
    Parameters:
        vectors (list of list of float): A list of vectors (each vector is a list of floats).
    
    Returns:
        float: The cumulative dot product of all vectors.
    """
    # Check if all vectors have the same length
    if len(set(map(len, vectors))) != 1:
        raise ValueError("All vectors must have the same number of components.")

    # Calculate the cumulative dot product using reduce and zip
    return sum(reduce(lambda x, y: x * y, components) for components in zip(*vectors))

def parse_vectors(input_str):
    """
    Parse a semicolon-separated string of vectors.
    
    Parameters:
        input_str (str): Input string with vectors separated by semicolons and components by spaces.
    
    Returns:
        list of list of float: A list of vectors.
    """
    try:
        return [list(map(float, vector.strip().split())) for vector in input_str.split(";")]
    except ValueError:
        raise ValueError("All components must be numbers (int or float).")

def get_input(args):
    """
    Get input string from command line arguments or prompt the user.
    
    Parameters:
        args (list of str): Command line arguments.
    
    Returns:
        str: The input string.
    """
    return " ".join(args[1:]) if len(args) > 1 else input("Enter vectors separated by semicolons, with components separated by spaces:\n")

def main():
    input_str = get_input(sys.argv)
    try:
        vectors = parse_vectors(input_str)
        result = dot_product(vectors)
        print(f"The cumulative dot product of the vectors is {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
