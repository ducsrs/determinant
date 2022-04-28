# determinant
Simple recursive script for calculating the determinant of a square numerical matrix.

Returns an integer if the matrix contains only integers or a float otherwise.

The actual determinant calculator is simply the function ```det```; the functions ```to_row``` and ```safe_input``` are used to turn command-line input into a list of lists of numbers. If you don't need that functionality, you can use ```from det import det``` instead of the entire module.
