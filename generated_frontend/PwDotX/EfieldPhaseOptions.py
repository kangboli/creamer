from typing import Optional, List
from .Options import Options


class EfieldPhaseOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    read = 0
    """   
    set the zero of the electronic polarization (with ~lelfield==.true..)~ 
    to the result of a previous calculation 

    """
    none = 1
    """   
    none of the above points 

    """
    write = 2
    """   
    write on disk data on electronic polarization to be read in another 
    calculation 

    """
