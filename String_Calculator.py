#simple string calculators
import unittest

def add(numbers: str) -> int:

    #handle custom deliminitor "//"
    if numbers.startswith("//"):
        substring=numbers[2:]  #remove "//" and extract delimiter as first two characters are deliminitors
        delimiter, numbers = substring.split("\n", 1) #split the string in 2 parts, first - delimiter and second in numbers
        numbers = numbers.replace(delimiter, ",")  #replace delimiter with comma

    numbers = numbers.replace("\n", ",")  #if string not starts with "//" then replace all "\n" to comma
    #print("numbers",numbers)

    if numbers:
        num_list = numbers.split(",") #create a number list
    else:
        num_list = []
    #print("num list",num_list)

    #check for negative numbers
    negatives = []
    for num in num_list:
        if num:
            num_int = int(num)
            if num_int < 0:
                negatives.append(num_int)

    if negatives:
        negative_strings = [str(num) for num in negatives]

        # join all the negative string
        negative_message = ", ".join(negative_strings)

        # create the error mesage
        error_message = f"Negative numbers not allowed: {negative_message}"

        # raise the error with message
        raise ValueError(error_message)
        
    #if all the above conditons are statisfy then find and return total.    
    total = 0
    for num in num_list:
        if num:
            total += int(num)
    return total

class TestAddFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0) #test case for empty string, expected : 0

    def test_single_number(self):
        self.assertEqual(add("1"), 1) #test case for single number input, expected : 1

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6) #test case for two number input, expected : 6

    def test_newline_as_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6) #test case for new line, expected : 6

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3) #test case for //, expected 3

    def test_another_custom_delimiter(self):
        self.assertEqual(add("//|\n1|2|3"), 6) #test case for delimiter, expected 6

    def test_negative_numbers(self):  #test case for negative numbers
        with self.assertRaises(ValueError) as context: 
            add("1,-2,3")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2")

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("//;\n1;-2;3;-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")

#accept user input
user_input = input("Enter numbers: ").replace("\\n", "\n")

try:
    result = add(user_input)
    print("Result:", result)
except ValueError as e:
    print("Error:", e)

# run unit test
unittest.main(exit=False)
