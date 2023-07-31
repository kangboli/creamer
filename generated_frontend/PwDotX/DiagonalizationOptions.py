from typing import Optional, List
from .Options import Options


class DiagonalizationOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    ppcg = 0
    """   
    PPCG iterative diagonalization 

    """
    cg = 1
    """   
    Conjugate-gradient-like band-by-band diagonalization. 
    MUCH slower than 'david' but uses less memory and is 
    (a little bit) more robust. 

    """
    paro = 2
    """   
    ParO iterative diagonalization 

    """
    david = 3
    """   
    Davidson iterative diagonalization with overlap matrix 
    (default). Fast, may in some rare cases fail. 

    """
