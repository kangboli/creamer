from typing import Optional, List
from .Options import Options


class EsmBcOptions(Options):
    """
    Others:
    ================
    
     If ~assume_isolated~ = 'esm', determines the boundary 
     conditions used for either side of the slab. 
     
     Currently available choices: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    pbc = 0
    """   (default): regular periodic calculation (no ESM).

    """
    bc2 = 1
    """   
    Metal-slab-metal (dual electrode configuration). 
    See also ~esm_efield.~ 

    """
    bc1 = 2
    """   Vacuum-slab-vacuum (open boundary conditions).

    """
    bc3 = 3
    """   Vacuum-slab-metal

    """
