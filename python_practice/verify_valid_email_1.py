import re


class VerifyEmail:
    '''Verifies if an email is valid'''
    user_input = input(f"Type email you want to verify and press enter\n")

    def __init__(self, search_pattern, user_input) -> str:
        self.search_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
        
    def valid_format(self):
        '''Verifies if an email is in the correct format'''
        print(self.user_input)
        # print(f"{self.search_pattern}")


# class IsValidEmail:
#     "verifies if an email has a valid format"
#     user_input = input(f"Type email you want to verify and press enter\n")

#     def __init__(self) -> str:
#         self.search_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"


#     def validate_mail(self) -> str:
#         # self.valid = f"{IsValidEmail.user_input} is a valid email"
#         # self.invalid = 
#         if(re.search(self.search_pattern, IsValidEmail.user_input)):
#             print("valid")
#         else:
#             print("invalid")


email = VerifyEmail.valid_format("alex@gmail.com")
print(type(email))
print(email)

# if __name__ == '__main__':
#     IsValidEmail.validate_mail(IsValidEmail.user_input)
