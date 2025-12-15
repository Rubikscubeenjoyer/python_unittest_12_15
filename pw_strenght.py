import unittest

def calculate_password_strength(password: str) -> int:
    if len(password) == 0:
        return 0
    
    if "jelszo" in password.lower() or "123" in password:
        return 0
    
    strength = 1
    
    if len(password) >= 5:
        strength += 1
    if len(password) >= 8:
        strength += 2
    
    special_count = password.count('_') + password.count('-') + password.count('.')
    strength += special_count * 2
    
    return strength

if __name__ == "__main__":
    password = input("Kérem, adja meg a jelszót: ").strip()
    
    strength = calculate_password_strength(password)
    
    print(f"\nA jelszó erőssége: {strength}")
    
    if strength == 0:
        print("➤ Nagyon gyenge (tilos karakterlánc miatt vagy üres).")
    elif strength <= 2:
        print("➤ Gyenge")
    elif strength <= 4:
        print("➤ Közepes")
    elif strength <= 8:
        print("➤ Erős")
    else:
        print("➤ Nagyon erős")


class TestPasswordStrength(unittest.TestCase):
    
    def test_empty_password(self):
        self.assertEqual(calculate_password_strength(""), 0)
    
    def test_contains_jelszo_case_insensitive(self):
        self.assertEqual(calculate_password_strength("myJelszoPass"), 0)
        self.assertEqual(calculate_password_strength("JELSZO"), 0)
        self.assertEqual(calculate_password_strength("tajelszov"), 0)
    
    def test_contains_123(self):
        self.assertEqual(calculate_password_strength("pass123"), 0)
        self.assertEqual(calculate_password_strength("abc123def"), 0)
    
    def test_short_less_than_5(self):
        self.assertEqual(calculate_password_strength("abc"), 1)
        self.assertEqual(calculate_password_strength("abcd"), 1)
    
    def test_at_least_5_but_less_than_8(self):
        self.assertEqual(calculate_password_strength("abcde"), 2)
        self.assertEqual(calculate_password_strength("abcdefg"), 2)
    
    def test_at_least_8(self):
        self.assertEqual(calculate_password_strength("abcdefgh"), 4)
        self.assertEqual(calculate_password_strength("verylongpassword"), 4)
    
    def test_special_characters(self):
        self.assertEqual(calculate_password_strength("a-b.c_d"), 10)
        self.assertEqual(calculate_password_strength("pass--word..long"), 14)
    
    def test_forbidden_with_specials(self):
        self.assertEqual(calculate_password_strength("jelszo---...___"), 0)
        self.assertEqual(calculate_password_strength("abc123-._"), 0)
    
    def test_combined_good_password(self):
        self.assertEqual(calculate_password_strength("secure-password.long_enough"), 14)