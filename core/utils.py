import traceback
from typing import Union, List, Tuple
from decimal import Decimal


class DataManagement:
    """
    This class will contains a logic layer for handle the input data.

    The target is sanitize the input.
    """
    @staticmethod
    def sanitize_data(data: dict) -> Tuple[int, int]:
        try:
            left_range = data['l'] if 'l' in data else None
            right_range = data['r'] if 'r' in data else None

            if not left_range or not right_range:
                return 0, 0

            left_range = Decimal(left_range)
            right_range = Decimal(right_range)

            is_left_ok = left_range.is_finite() and left_range.is_signed() == False
            is_right_ok = right_range.is_finite() and right_range.is_signed() == False

            if is_left_ok and is_right_ok:
                return int(left_range), int(right_range)

            return 0, 0

        except Exception as err:
            traceback.print_exc()
            print(f'Error at DataManagement | sanitize_data: {str(err)}')
            return 0, 0


class Computation:
    """
    This class will handle the computation elements, applied for the input data.
    """

    @staticmethod
    def fibonacci_slow(n: int) -> int:
        if n in [0, 1]:
            return n
        return Computation.fibonacci_slow(n - 1) + Computation.fibonacci_slow(n - 2)

    @staticmethod
    def fibonacci_persistance_layer(n: int) -> int:
        data = {0: 0, 1: 1}

        def _intern_fibonacci(n: int) -> int:
            if n in data:  # Base case
                return data[n]
            # Compute and data the Fibonacci number
            data[n] = _intern_fibonacci(n - 1) + _intern_fibonacci(n - 2)  # Recursive case
            return data[n]

        return _intern_fibonacci(n)

    @staticmethod
    def fibonacci_in_range(l: int, r: int) -> Union[List[int], None]:
        """
        Execute a fibonacci in a range of elements integer.

        :param l int. Describe the "left" side from the range where the 
            Fibonacci will be computed.

        :param r int. Describe the "left" side from the range where the 
            Fibonacci will be computed.
        """
        try:
            # Use Fibonacci slow
            # out = [ Computation.fibonacci_slow(n) for n in range(l, r+1) ]
            # return out

            # Use Fibonacci with more speed
            out = [ Computation.fibonacci_persistance_layer(n) for n in range(l, r+1) ]
            return out

        except Exception as err:
            traceback.print_exc()
            print(f'Error: At Computation | Fibonacci {str(err)}')
            return None
