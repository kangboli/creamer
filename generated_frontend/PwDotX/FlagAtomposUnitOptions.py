from typing import Optional, List
from .Options import Options


class FlagAtomposUnitOptions(Options):
    """
    Others:
    ================
    
     Units for ATOMIC_POSITIONS: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    alat = 0
    """   
    atomic positions are in cartesian coordinates, in 
    units of the lattice parameter (either celldm(1) 
    or A). If no option is specified, 'alat' is assumed; 
    not specifying units is DEPRECATED and will no 
    longer be allowed in the future 

    """
    crystal = 1
    """   
    atomic positions are in crystal coordinates, i.e. 
    in relative coordinates of the primitive lattice 
    vectors as defined either in card ~CELL_PARAMETERS~ 
    or via the ibrav + celldm / a,b,c... variables 

    """
    angstrom = 2
    """   
    atomic positions are in cartesian coordinates, in Angstrom 

    """
    bohr = 3
    """   
    atomic positions are in cartesian coordinate, 
    in atomic units (i.e. Bohr radii) 

    """
    crystal_sg = 4
    """   
    atomic positions are in crystal coordinates, i.e. 
    in relative coordinates of the primitive lattice. 
    This option differs from the previous one because 
    in this case only the symmetry inequivalent atoms 
    are given. The variable ~space_group~ must indicate 
    the space group number used to find the symmetry 
    equivalent atoms. The other variables that control 
    this option are uniqueb, origin_choice, and 
    rhombohedral. 

    """
