from Characters import Characters
from configs import *

class Hunter(Characters):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            Skins.ELMER
        )

