class TaxiGameError(Exception):
    """Eccezione base per il Taxi Game"""
    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

class ActionError(TaxiGameError):
    """Action not valid"""
    pass