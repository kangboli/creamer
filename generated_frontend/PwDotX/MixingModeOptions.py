from typing import Optional, List
from .Options import Options


class MixingModeOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    local__dash__tf = 0
    """   
    as above, with local-density-dependent TF screening 
    (for highly inhomogeneous systems) 

    """
    tf = 1
    """   
    as above, with simple Thomas-Fermi screening 
    (for highly homogeneous systems) 

    """
    plain = 2
    """   charge density Broyden mixing

    """
