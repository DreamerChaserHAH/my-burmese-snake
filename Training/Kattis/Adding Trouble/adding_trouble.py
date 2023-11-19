# <summary>
#   https://open.kattis.com/problems/addingtrouble
# </summary>

import unittest

class myTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(check_answer("2 3 5"), True)
        self.assertEqual(check_answer("1 1 3"), False)
        self.assertEqual(check_answer("-1 1 0"), True)
        pass;

def check_answer(statement):
    numbers = process_input(statement)
    return numbers[0] + numbers[1] == numbers[2]

def process_input(input_string):
    return list(map(lambda value: int(value), str(input_string).strip().split(' ')))
    
if __name__ == "__main__":
    print("correct!" if check_answer(input()) else "wrong!")