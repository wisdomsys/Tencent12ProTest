import unittest


def get_suit():
    suite = unittest.defaultTestLoader.discover('', '*test.py')
    return suite


def run_case(suite):
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    suite = get_suit()
    run_case(suite)
