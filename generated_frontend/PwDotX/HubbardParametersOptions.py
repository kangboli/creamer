from typing import Optional, List
from .Options import Options


class HubbardParametersOptions(Options):
    """
    Others:
    ================
    
     Available choices: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    input = 0
    """   
    read the ~Hubbard_U~ (or ~Hubbard_V)~ parameters from 
    the PW input file 

    """
    file = 1
    """   
    read the ~Hubbard_V~ parameters from the file "parameters.in" 
    which can be generated after the linear-response calculation 
    (using the HP code). This option has a higher priority over 
    the ~Hubbard_V~ if they are specified in the input. This option 
    can be used only when ~lda_plus_u_kind~ = 2. 

    """
