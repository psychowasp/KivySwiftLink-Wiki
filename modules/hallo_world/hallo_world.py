from swift_types import *


@wrapper
class HalloWorld:

    def send_string(self, string: str):
        """
        Sends a str to swift.
        """
