import unittest
from myform_mail import validate_email

class TestInvalidEmails(unittest.TestCase):
    
    def test_invalid_email_formats(self):
        invalid_emails = [
            "", # empty string
            "plainaddress", # no @ and domain
            "@missingusername.com ", # there is no username
            "username@.com ", # there is no domain before the dot
            ".username@domain.com ", # dot at the beginning of the name
            "username@domain..com ", # two points in the domain
            "username@domain.com .", # dot at the end
            "username@domain_com", # invalid character _
            "username@domain.c ", # the domain is too short
            "user@name@domain.com ", # two characters @
            "username@domain.com -", # invalid character -
            "user name@domain.com ", # a space in the name
            "user..name@domain.com ", # two dots in the name
            "username@domain", # no top-level domain
            "username@domain..com ", # two dots in a row
            "username@-domain.com ", # hyphen at the beginning of the domain
            "username@domain.c0m ", # digit in the top-level domain
            "username@domain.c_m ", # invalid character in the domain
            "username@domain.123 ", # numbers instead of letters in the domain
            "username@domain.c ", # domain is too short (1 character)
            "username@domain.con ", # typo in the domain
            "username@.domain.com ", # missing domain before the dot
            "user@domain..com ", # two dots in a row
            "user@.com ", # just the dot after @
            "user@domain..com ", # two points in the domain
            "user@-domain.com ", # hyphen at the beginning of the domain
            "user@domain.-com ", # a hyphen before a dot
            "user@domain_com", # underscore in the domain
            "user@domain.c0m ", # the number in the TLD
            "user@domain.c *m", # special character in the domain
            "user@domain.1com " # the number at the beginning of the TLD
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(
                    validate_email(email),
                    f"The email '{email}' was expected to be invalid"
                )

if __name__ == '__main__':
    unittest.main()
