from typing import Optional, List
from .Options import Options


class ExxdivTreatmentOptions(Options):
    """
    Others:
    ================
    
     Specific for EXX. It selects the kind of approach to be used 
     for treating the Coulomb potential divergencies at small q vectors. 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    vcut_ws = 0
    """   appropriate for strongly anisotropic supercells, see also ~ecutvcut.~

    """
    vcut_spherical = 1
    """   appropriate for cubic and quasi-cubic supercells

    """
    none = 2
    """   sets Coulomb potential at G,q=0 to 0.0 (required for GAU-PBE)

    """
    gygi__dash__baldereschi = 3
    """   appropriate for cubic and quasi-cubic supercells

    """
