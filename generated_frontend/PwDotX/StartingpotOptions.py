from typing import Optional, List
from .Options import Options


class StartingpotOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    file = 0
    """   
    start from existing "charge-density.xml" file in the 
    directory specified by variables ~prefix~ and ~outdir~ 
    For nscf and bands calculation this is the default 
    and the only sensible possibility. 

    """
    atomic = 1
    """   
    starting potential from atomic charge superposition 
    (default for scf, *relax, *md) 

    """
