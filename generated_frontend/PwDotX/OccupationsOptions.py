from typing import Optional, List
from .Options import Options


class OccupationsOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    tetrahedra = 0
    """   
    Tetrahedron method, Bloechl's version: 
    P.E. Bloechl, PRB 49, 16223 (1994) 
    Requires uniform grid of k-points, to be 
    automatically generated (see card ~K_POINTS).~ 
    Well suited for calculation of DOS, 
    less so (because not variational) for 
    force/optimization/dynamics calculations. 

    """
    tetrahedra_opt = 1
    """   
    Optimized tetrahedron method: 
    see M. Kawamura, PRB 89, 094515 (2014). 
    Can be used for phonon calculations as well. 

    """
    smearing = 2
    """   
    gaussian smearing for metals; 
    see variables ~smearing~ and ~degauss~ 

    """
    from_input = 3
    """   
    The occupation are read from input file, 
    card ~OCCUPATIONS.~ Option valid only for a 
    single k-point, requires ~nbnd~ to be set 
    in input. Occupations should be consistent 
    with the value of ~tot_charge.~ 

    """
    fixed = 4
    """   
    for insulators with a gap 

    """
    tetrahedra_lin = 5
    """   
    Original linear tetrahedron method. 
    To be used only as a reference; 
    the optimized tetrahedron method is more efficient. 

    """
