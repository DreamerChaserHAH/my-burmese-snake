# <summary>
#   src : https://open.kattis.com/problems/anewalphabet
# </summary>

import unittest

class MyTests(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(generate_new_string("All your base are belong to us."), "@11 `/0|_||Z 8@$3 @|Z3 8310[]\[]6 ']['0 |_|$.")
        pass
    def test_case_2(self):
        self.assertEqual(generate_new_string("What's the Frequency, Kenneth?"), "\/\/[-]@'][''$ ']['[-]3 #|Z3(,)|_|3[]\[](`/, |<3[]\[][]\[]3']['[-]?")
        pass
    def test_case_3(self):
        self.assertEqual(generate_new_string("A new alphabet!"), "@ []\[]3\/\/ @1|D[-]@83']['!")
        pass

alphabet_replacement_table = {
    'a':'@',
    'b':'8',
    'c':'(',
    'd':'|)',
    'e':'3',
    'f':'#',
    'g':'6',
    'h':'[-]',
    'i':'|',
    'j':'_|',
    'k':'|<',
    'l':'1',
    'm':'[]\/[]',
    'n':'[]\[]',
    'o':'0',
    'p':'|D',
    'q':'(,)',
    'r':'|Z',
    's':'$',
    't':"']['",
    'u':'|_|',
    'v':'\\/',
    'w':'\\/\\/',
    'x':'}{',
    'y':'`/',
    'z':'2'
}

def generate_new_character(original_character):
    try:
        return alphabet_replacement_table[str(original_character).lower()]
    except KeyError:
        return original_character

def generate_new_string(original_string):
    return ''.join(list(map(lambda x: generate_new_character(x) , [*original_string])))

if __name__ == '__main__':
    print(generate_new_string(input()))
    