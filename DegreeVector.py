import math
import sys

def dot_product(vector1, vector2):
    """
    Calculate the dot product of two vectors.
    
    Parameters:
        vector1 (list of float): The first vector.
        vector2 (list of float): The second vector.
    
    Returns:
        float: The dot product of the two vectors.
    """
    return sum(a * b for a, b in zip(vector1, vector2))

def magnitude(vector):
    """
    Calculate the magnitude of a vector.
    
    Parameters:
        vector (list of float): The vector.
    
    Returns:
        float: The magnitude of the vector.
    """
    return math.sqrt(sum(component ** 2 for component in vector))

def angle_between_vectors(vector1, vector2):
    """
    Calculate the angle between two vectors in degrees.
    
    Parameters:
        vector1 (list of float): The first vector.
        vector2 (list of float): The second vector.
    
    Returns:
        float: The angle between the vectors in degrees.
    """
    dot_prod = dot_product(vector1, vector2)
    mag1 = magnitude(vector1)
    mag2 = magnitude(vector2)
    
    # To avoid division by zero, check if the magnitude is non-zero
    if mag1 == 0 or mag2 == 0:
        raise ValueError("Magnitude of one or both vectors is zero. Cannot calculate the angle.")

    # Calculate the cosine of the angle
    cos_theta = dot_prod / (mag1 * mag2)

    # Ensure cos_theta is within the valid range for acos (to avoid numerical issues)
    cos_theta = max(-1, min(1, cos_theta))

    # Calculate the angle in radians and convert to degrees
    theta_radians = math.acos(cos_theta)
    theta_degrees = math.degrees(theta_radians)
    return theta_degrees

def parse_vectors(input_str):
    """
    Parse a semicolon-separated string of two vectors.
    
    Parameters:
        input_str (str): Input string with two vectors separated by a semicolon and components by spaces.
    
    Returns:
        tuple of list of float: A tuple containing two vectors.
    """
    try:
        vectors = [list(map(float, vector.strip().split())) for vector in input_str.split(";")]
        if len(vectors) != 2:
            raise ValueError("Please provide exactly two vectors.")
        return vectors[0], vectors[1]
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
    return " ".join(args[1:]) if len(args) > 1 else input("Enter two vectors separated by a semicolon, with components separated by spaces:\n")

def main():
    input_str = get_input(sys.argv)
    try:
        vector1, vector2 = parse_vectors(input_str)
        angle = angle_between_vectors(vector1, vector2)
        print(f"The angle between the vectors {vector1} and {vector2} is {angle:.2f} degrees")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
