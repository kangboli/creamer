from typing import Optional, List
from .Options import Options


class Dftd3VersionOptions(Options):
    """
    Others:
    ================
    
     Version of Grimme implementation of Grimme-D3: 
    
     NOTE: not all functionals are parametrized. 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    dftd3_version__ws____is____ws__6 = 0
    """   
    Grimme-D3M (BJ damping) 

    """
    dftd3_version__ws____is____ws__4 = 1
    """   
    Grimme-D3 (BJ damping) 

    """
    dftd3_version__ws____is____ws__5 = 2
    """   
    Grimme-D3M (zero damping) 

    """
    dftd3_version__ws____is____ws__2 = 3
    """   
    Original Grimme-D2 parametrization 

    """
    dftd3_version__ws____is____ws__3 = 4
    """   
    Grimme-D3 (zero damping) 

    """
