from typing import Optional, List
from .Options import Options


class CellDofreeOptions(Options):
    """
    Others:
    ================
    
     Select which of the cell parameters should be moved: 
    
     BEWARE: if axis are not orthogonal, some of these options do not 
     work (symmetry is broken). If you are not happy with them, 
     edit subroutine init_dofree in file Modules/cell_base.f90 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    epitaxial_ac = 0
    """   fix axis 1 and 3 while allowing axis 2 to move

    """
    all = 1
    """   all axis and angles are moved

    """
    xy = 2
    """   only v1_x and v2_y are moved

    """
    yz = 3
    """   only v2_y and v3_z are moved

    """
    xz = 4
    """   only v1_x and v3_z are moved

    """
    epitaxial_ab = 5
    """   fix axis 1 and 2 while allowing axis 3 to move

    """
    epitaxial_bc = 6
    """   fix axis 2 and 3 while allowing axis 1 to move

    """
    shape = 7
    """   all axis and angles, keeping the volume fixed

    """
    2dxy = 8
    """   only x and y components are allowed to change

    """
    2dshape = 9
    """   as above, keeping the area in xy plane fixed

    """
    volume = 10
    """   the volume changes, keeping all angles fixed (i.e. only celldm(1) changes)

    """
    xyz = 11
    """   only v1_x, v2_y, v3_z are moved

    """
    x = 12
    """   only the x component of axis 1 (v1_x) is moved

    """
    y = 13
    """   only the y component of axis 2 (v2_y) is moved

    """
    z = 14
    """   only the z component of axis 3 (v3_z) is moved

    """
    ibrav = 15
    """   all axis and angles are moved, but the lattice remains consistent with the initial ibrav choice

    """
