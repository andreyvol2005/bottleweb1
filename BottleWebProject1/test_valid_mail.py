import unittest
from myform_mail import validate_email

class TestValidEmails(unittest.TestCase):
    
    def test_valid_email_formats(self):
        valid_emails = [
            "simple@example.com",
            "john.doe@example.com",
            "jane_doe123@example.com",  
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(
                    validate_email(email),
                    f"Email '{email}' it should be valid, but it was rejected"
                )

if __name__ == '__main__':
    unittest.main()
