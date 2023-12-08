# your code goes here!
class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):

        addresses = re.split(r'[,\s]+', self.email_addresses)

        valid_addresses = list(
            filter(lambda address: address != '', addresses))

        return valid_addresses
