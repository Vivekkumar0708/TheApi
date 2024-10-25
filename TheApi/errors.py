class InvalidAmountError(Exception):
    def __init__(self, amount):
        super().__init__(
            f"Invalid amount of {method} requested: jokes. Maximum allowed is 10 Minimum allowed is 1."
        )
class RequestError(Exception):
    def __init__(self, err):
        super().__init__(err)