from nessrest import ness6rest

class ScannerConnector:

    def __init__(self, url, login, pwd, no_ssl):
        self.nessus_url=url
        self.nessus_login=login
        self.nessus_pwd=pwd
        self.nessus_secure=no_ssl


    def connect(self):
        self.connector=ness6rest.Scanner(url=self.nessus_url, login=self.nessus_login,
                                         password=self.nessus_pwd, insecure=self.nessus_secure)
        return self.connector






