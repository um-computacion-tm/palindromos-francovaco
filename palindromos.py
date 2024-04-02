import unittest

def is_palindrome(mystring):
    print(mystring)
    for indice in range (0, len(mystring)):
        print(mystring[indice]+ " -> " + mystring[-(indice +1)])
        if mystring[indice] != mystring[-(indice +1)]:
            print("mepa que no es")
            return False
    return True

class TestPalindrome(unittest.TestCase):
    def test_a(self):
        resultado = is_palindrome('a')
        self.assertEqual(resultado, True)
    def test_b(self):
        resultado = is_palindrome('hipopótamo')
        self.assertEqual(resultado, False)
    def test_c(self):
        resultado = is_palindrome('neuquen')
        self.assertEqual(resultado, True)

unittest.main()