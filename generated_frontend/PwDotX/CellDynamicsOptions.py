from typing import Optional, List
from .Options import Options


class CellDynamicsOptions(Options):
    """
    Others:
    ================
    
     Specify the type of dynamics for the cell. 
     For different type of calculation different possibilities 
     are allowed and different default values apply: 
     
     **CASE** ( ~calculation~ == 'vc-relax' ) 
    
     **CASE** ( ~calculation~ == 'vc-md' ) 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    damp__dash__pr = 0
    """   
    damped (Beeman) dynamics of the Parrinello-Rahman extended lagrangian 

    """
    sd = 1
    """   steepest descent ( not implemented )

    """
    pr = 2
    """   
    (Beeman) molecular dynamics of the Parrinello-Rahman extended lagrangian 

    """
    w = 3
    """   
    (Beeman) molecular dynamics of the new Wentzcovitch extended lagrangian 

    """
    damp__dash__w = 4
    """   
    damped (Beeman) dynamics of the new Wentzcovitch extended lagrangian 

    """
    none = 5
    """   no dynamics

    """
    bfgs = 6
    """   
    BFGS quasi-newton algorithm **(default)** 
    ~ion_dynamics~ must be **'bfgs'** too 

    """
