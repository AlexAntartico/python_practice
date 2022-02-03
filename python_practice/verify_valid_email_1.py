import re


class VerifyEmail:
    '''Verifies if an email provided by user is valid'''

    def __init__(self, email) -> str:
        """
        Initialize attributes. Defines the search pattern using regular
        expressions. email parameter will be taken by input at the moment
        of creating class intance.
        """
        self.email = email
        self.search_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
        # regex pattern is simplified here for educational purposes

    def valid_format(self):
        '''Verifies if an email is in the correct format'''
        if (re.search(self.search_pattern, self.email)):
            print("valid email format")
        else:
            print("invalid email format")
        print(f"Verified email is: {self.email}")


user_email = VerifyEmail(input("what is the email you want to verify?\n"))
user_email.valid_format()
