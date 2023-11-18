# <summary>
#   src : https://open.kattis.com/problems/asciikassi
# </summary>

import unittest;

class myTests(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(generate_kassi(0),["++","++"])
        self.assertEqual(generate_kassi(1),["+-+","| |","+-+"])
        self.assertEqual(generate_kassi(2),["+--+","|  |","|  |","+--+"])
        pass

def generate_sandwiched_vertical(count):
    return str((" " * count)).center(count + 2, "|")

def generate_corner_horizontal(count):
    return str(("-" * count)).center(count + 2, "+")

def generate_kassi(count):
    array_list = []
    array_list.append(generate_corner_horizontal(count))
    for i in range(count):
        array_list.append(generate_sandwiched_vertical(count))
    array_list.append(generate_corner_horizontal(count))
    return array_list

def display_kassi(count):
    print(generate_corner_horizontal(count))
    for i in range(count):
        print(generate_sandwiched_vertical(count))
    print(generate_corner_horizontal(count))

if __name__ == "__main__":
    display_kassi(int(input().strip()))
