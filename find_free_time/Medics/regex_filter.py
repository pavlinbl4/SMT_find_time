"""To write a function in Python that uses regex to retrieve the required information from the input string
and return it in the form of a dictionary with the corresponding key-value pairs, the following code can be used"""

import re


def regex_string_to_dict(input_string):
    regex_pattern = r'<option value="(\d+)">(.+)</option>'
    regex_matches = re.search(regex_pattern, input_string)
    result_dict = {}
    if regex_matches:
        result_dict[regex_matches.group(1)] = regex_matches.group(2)
    return result_dict


if __name__ == '__main__':
    print(regex_string_to_dict('<option value="6108">Гинекология</option>'))

"""In the above code, the re module is imported to use the regex pattern matching functionality. 
The input string is provided as the argument to the function. 
A regex pattern to match the required pattern in the input string is defined using the r'' syntax. 
The search() method is used to find the first occurrence of the pattern in the input string. 
If a match is found, a"""
