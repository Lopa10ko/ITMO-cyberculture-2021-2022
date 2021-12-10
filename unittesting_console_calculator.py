import unittest
from console_calculator import main

class Testing(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_calculator(self):
        self.assertEqual(main(('45 + 4 - 242442 + 32342'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), -210051)
        self.assertEqual(main(('56-757+5888-583+784+8858+1+1'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 14248)
        self.assertEqual(main(('1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 45)
        self.assertEqual(main(('58838 -544 + 85858 - 29296 + 5930 - 5903 -4444'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 110439)
        self.assertEqual(main(('5773+5885 -4 + 584828 -588 + 58 - 58588'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 537364)
        self.assertEqual(main(('884882 - 4848848 + 2 - 3484'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), -3967448)
        self.assertEqual(main(('453--43+4433-43343 +44'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), -38370)
        self.assertEqual(main(('437774  + 848484848-         488'.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 848922134)
        self.assertEqual(main(('8 88 8 8 8 8 8 -  7 7 77 7 7 '.replace(' ', '').replace('--', '+').replace('-', '+-').split('+'))), 8811111)
        pass

if __name__ == '__main__':
    unittest.main()
