from typing import Optional, List
from .Options import Options


class SmearingOptions(Options):
    """
    Others:
    ================
    
     Available options are: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    marzari__dash__vanderbilt = 0
    """   
    Marzari-Vanderbilt-DeVita-Payne cold smearing 
    (see PRL 82, 3296 (1999)) 

    """
    methfessel__dash__paxton = 1
    """   
    Methfessel-Paxton first-order spreading 
    (see PRB 40, 3616 (1989)). 

    """
    gauss = 2
    """   
    ordinary Gaussian spreading (Default) 

    """
    mp = 3
    """   
    Methfessel-Paxton first-order spreading 
    (see PRB 40, 3616 (1989)). 

    """
    m__dash__v = 4
    """   
    Marzari-Vanderbilt-DeVita-Payne cold smearing 
    (see PRL 82, 3296 (1999)) 

    """
    m__dash__p = 5
    """   
    Methfessel-Paxton first-order spreading 
    (see PRB 40, 3616 (1989)). 

    """
    fermi__dash__dirac = 6
    """   
    smearing with Fermi-Dirac function 

    """
    mv = 7
    """   
    Marzari-Vanderbilt-DeVita-Payne cold smearing 
    (see PRL 82, 3296 (1999)) 

    """
    cold = 8
    """   
    Marzari-Vanderbilt-DeVita-Payne cold smearing 
    (see PRL 82, 3296 (1999)) 

    """
    gaussian = 9
    """   
    ordinary Gaussian spreading (Default) 

    """
    f__dash__d = 10
    """   
    smearing with Fermi-Dirac function 

    """
    fd = 11
    """   
    smearing with Fermi-Dirac function 

    """
