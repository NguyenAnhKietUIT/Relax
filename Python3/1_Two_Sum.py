from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the array that add up to the target.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list of two indices corresponding to the numbers that add up to the target.
        """
        # Create a dictionary to store the number and its index
        temp = {}

        # Iterate through the array
        for index, value in enumerate(nums):
            # Calculate the difference needed to achieve the target
            j = target - value
            # Check if the difference exists in the dictionary
            if j in temp:
                # If found, return the indices of the two numbers
                return [temp[j], index]
            # Otherwise, store the current number and its index in the dictionary
            temp[value] = index
