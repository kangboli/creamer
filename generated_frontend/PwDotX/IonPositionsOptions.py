from typing import Optional, List
from .Options import Options


class IonPositionsOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    default = 0
    """   
    if restarting, use atomic positions read from the 
    restart file; in all other cases, use atomic 
    positions from standard input. 

    """
    from_input = 1
    """   
    read atomic positions from standard input, even if restarting. 

    """
