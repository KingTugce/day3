# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers 
# inside the list. The function should then return a list.
# Bonus: Use a list comprehension to find your solution
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]   



def find_even(a_list):
    even_numbers = []
    for nums in a_list: 
        if nums %2 == 0:
            even_numbers.append(nums)
    print(find_even[2, 7, 10, 11, 12])