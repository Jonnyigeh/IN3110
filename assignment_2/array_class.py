"""
Array class for assignment 2
"""
import numpy as np
class Array:
    """Generates an array with similar functionality as numpy or python arrays.

    Has functionality of element-wise adding, subtracting, multiplying etc.

    """
    def __init__(self, shape, *values):
        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid types

        if type(values[0]) == int:
            if all(isinstance(n, int) for n in values):
                pass
            else:
                raise ValueError(
                "Input elements must all be of the same datatype (int, float or bool)"
                )
        elif type(values[0]) == bool:
            if all(isinstance(n, bool) for n in values):
                pass
            else:
                raise ValueError(
                "Input elements must all be of the same datatype (int, float or bool)"
                )
        elif type(values[0]) == float:
            if all(isinstance(n, float) for n in values):
                pass
            else:
                raise ValueError(
                "Input elements must all be of the same datatype (int, float or bool)"
                )
        else:
            raise TypeError(
            "Input elements must be of type: int, float or boolean"
            )

        # Check that the amount of values corresponds to the shape
        if len(values) != shape[0]:
            raise ValueError(
            "Input array must be of same length as input shape"
            )
        # Set class-variables
        self.shape = shape[0]
        self.values = []
        for i in values:
            self.values.append(i)

    def __getitem__(self, index):
        """Extracts single element from self.values

        Returns:
            Int/Float/Bool: Element with index [index] in self.values

        """
        print(self.values[index])

    def __str__(self):
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.

        """
        return f"The Array has shape (1,{self.shape}) and elements {self.values}"

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        # if the array is a boolean you should return NotImplemented
        # check that the method supports the given arguments (check for data type and shape of array)
        new_array = [i for i in self.values]
        if isinstance(self.values[0],bool):
            return NotImplemented

        elif isinstance(other, Array):
            if isinstance(self.values[0],bool) or isinstance(other.values,bool):
                return NotImplemented
            elif len(self.values) != len(other.values):
                return NotImplemented
            else:
                for i in range(len(self.values)):
                    new_array[i] += other.values[i]
                return new_array

        elif isinstance(other,int) or isinstance(other,float):
            for i in range(len(self.values)):
                    new_array[i] += other
            return new_array
        else:
            return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """
        new_array = [i for i in self.values]
        if isinstance(other, Array):
            if self.values[0] == bool or other.values[0] == bool:
                return NotImplemented

            elif len(self.values) != len(other.values):
                return NotImplemented
            else:
                for i in range(len(self.values)):
                    new_array[i] -= other.values[i]
                return new_array

        elif type(other) == int or type(other) == float:
            for i in range(len(self.values)):
                    new_array[i] -= other
            return new_array
        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        new_array = [i for i in self.values]
        if isinstance(other, Array):
            if self.values[0] == bool or other.values == bool:
                return NotImplemented

            elif len(self.values) != len(other.values):
                return NotImplemented
            else:
                for i in range(len(self.values)):
                    new_array[i] *= other.values[i]
                return new_array

        elif type(other) == int or type(other) == float:
            for i in range(len(self.values)):
                    new_array[i] *= other
            return new_array

        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if isinstance(other, Array):
            if len(self.values) == len(other.values):
                return True
            else:
                return False
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.
            TypeError: if other is not an array or a number.
        """
        new_array = [i for i in self.values]
        if isinstance(other, Array):
            if len(self.values) != len(other.values):
                raise ValueError(
                "The length of the two arrays do not match!"
                )
            else:
                for i in range(len(self.values)):
                    new_array[i] = self.values[i] == other.values[i]
                return new_array

        elif type(other) == int or type(other) == float:
            for i in range(len(self.values)):
                new_array[i] = self.values[i] == other
            return new_array

        else:
            raise TypeError(
            "The second argument is not a valid quantity!"
            )

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        if self.values[0] == bool:
            return NotImplemented
        else:
            min_element = self.values[0]
            for element in self.values:
                if min_element > element:
                    min_element = element
                else:
                    pass

            return float(min_element)

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """
        if self.values[0] == bool:
            return NotImplemented

        mean = sum(element for element in self.values) / self.shape
        return mean



if __name__ == "__main__":
    inst = Array((3,),1,1,1)
    inst2 = Array((3,), 2,2,2)
    inst3 = Array((3,), 1,2,3)
    inst4 = Array((3,), True, False, False)
    i = 10
