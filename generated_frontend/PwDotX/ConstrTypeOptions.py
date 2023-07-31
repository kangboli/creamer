from typing import Optional, List
from .Options import Options


class ConstrTypeOptions(Options):
    """
    Others:
    ================
    
     Type of constraint : 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    planar_angle = 0
    """   
    constraint on planar angle 
    (three atom indexes must be specified). 

    """
    atom_coord = 1
    """   
    constraint on local coordination-number, i.e. the 
    average number of atoms of type A surrounding a 
    specific atom. The coordination is defined by 
    using a Fermi-Dirac. 
    (four indexes must be specified). 

    """
    distance = 2
    """   
    constraint on interatomic distance 
    (two atom indexes must be specified). 

    """
    bennett_proj = 3
    """   
    constraint on the projection onto a given direction 
    of the vector defined by the position of one atom 
    minus the center of mass of the others. 
    G. Roma, J.P. Crocombette: J. Nucl. Mater. 403, 32 (2010), 
    doi:10.1016/j.jnucmat.2010.06.001 

    """
    torsional_angle = 4
    """   
    constraint on torsional angle 
    (four atom indexes must be specified). 

    """
    type_coord = 5
    """   
    constraint on global coordination-number, i.e. the 
    average number of atoms of type B surrounding the 
    atoms of type A. The coordination is defined by 
    using a Fermi-Dirac. 
    (four indexes must be specified). 

    """
