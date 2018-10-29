import re


class User:
    """This class holds the methods for signing up and signing into the application"""
    def __init__(self, username, password, email_address, account_type):
        self.username = username
        self.password = password
        self.email_address = email_address
        self.account_type = account_type
        self.login_time_stamp = ""
        self.logout_time_stamp = ""

    @staticmethod
    def validate_email_address(email_address):
        """
        This checks for validity of the email address
        :param email_address:
        :return:
        """
        email = re.compile("(^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        match = email.match(email_address)
        if match:
            return True
        else:
            return False
