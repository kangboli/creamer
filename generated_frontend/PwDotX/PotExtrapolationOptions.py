from typing import Optional, List
from .Options import Options


class PotExtrapolationOptions(Options):
    """
    Others:
    ================
    
     Used to extrapolate the potential from preceding ionic steps. 
    
     Note: 'first_order' and 'second-order' extrapolation make sense 
     only for molecular dynamics calculations 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    first_order = 0
    """   
    extrapolate the potential with first-order 
    formula 

    """
    atomic = 1
    """   
    extrapolate the potential as if it was a sum of 
    atomic-like orbitals 

    """
    second_order = 2
    """   
    as above, with second order formula 

    """
    none = 3
    """   no extrapolation

    """
