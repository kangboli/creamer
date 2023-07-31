from typing import Optional, List
from .Options import Options


class IonVelocitiesOptions(Options):
    """
    Others:
    ================
    
     Initial ionic velocities. Available options are: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    default = 0
    """   
    start a new simulation from random thermalized 
    distribution of velocities if ~tempw~ is set, 
    with zero velocities otherwise; restart from 
    atomic velocities read from the restart file 

    """
    from_input = 1
    """   
    start or continue the simulation with atomic 
    velocities read from standard input - see card 
    ~ATOMIC_VELOCITIES~ 

    """
