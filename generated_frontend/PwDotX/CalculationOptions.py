from typing import Optional, List
from .Options import Options


class CalculationOptions(Options):
    """
    Others:
    ================
    
     A string describing the task to be performed. Options are: 
    
     (vc = variable-cell). 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    vc__dash__relax = 0
    """   Undocumented 5

    """
    relax = 1
    """   Undocumented 3

    """
    scf = 2
    """   Undocumented 0

    """
    md = 3
    """   Undocumented 4

    """
    vc__dash__md = 4
    """   Undocumented 6

    """
    nscf = 5
    """   Undocumented 1

    """
    bands = 6
    """   Undocumented 2

    """
