from typing import Optional, List
from .Options import Options


class WfcExtrapolationOptions(Options):
    """
    Others:
    ================
    
     Used to extrapolate the wavefunctions from preceding ionic steps. 
    
     Note: **'first_order'** and **'second-order'** extrapolation make sense 
     only for molecular dynamics calculations 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    first_order = 0
    """   
    extrapolate the wave-functions with first-order formula. 

    """
    second_order = 1
    """   
    as above, with second order formula. 

    """
    none = 2
    """   no extrapolation

    """
