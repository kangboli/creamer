from typing import Optional, List
from .Options import Options


class FlagKpointTypeOptions(Options):
    """
    Others:
    ================
    
     K_POINTS options are: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    crystal_b = 0
    """   
    As tpiba_b, but k-points are in crystal coordinates. 
    See Doc/brillouin_zones.pdf for usage of BZ labels. 

    """
    crystal = 1
    """   
    read k-points in crystal coordinates, i.e. in relative 
    coordinates of the reciprocal lattice vectors 

    """
    crystal_c = 2
    """   
    As tpiba_c, but k-points are in crystal coordinates. 

    """
    tpiba_c = 3
    """   
    Used for band-structure contour plots. 
    k-points are in units of 2 *pi/a.* nks must be 3. 
    3 k-points k_0, k_1, and k_2 specify a rectangle 
    in reciprocal space of vertices k_0, k_1, k_2, 
    k_1 + k_2 - k_0: k_0 + \alpha (k_1-k_0)+ 
    \beta (k_2-k_0) with 0 <\alpha,\beta < 1. 
    The code produces a uniform mesh n1 x n2 
    k points in this rectangle. n1 and n2 are 
    the weights of k_1 and k_2. The weight of k_0 
    is not used. 

    """
    tpiba_b = 4
    """   
    Used for band-structure plots. 
    See Doc/brillouin_zones.pdf for usage of BZ labels; 
    otherwise, k-points are in units of 2 pi/a. 
    nks points specify nks-1 lines in reciprocal space. 
    Every couple of points identifies the initial and 
    final point of a line. pw.x generates N intermediate 
    points of the line where N is the weight of the first point. 

    """
    automatic = 5
    """   
    automatically generated uniform grid of k-points, i.e, 
    generates ( nk1, nk2, nk3 ) grid with ( sk1, sk2, sk3 ) offset. 
    nk1, nk2, nk3 as in Monkhorst-Pack grids 
    k1, k2, k3 must be 0 ( no offset ) or 1 ( grid displaced 
    by half a grid step in the corresponding direction ) 
    BEWARE: only grids having the full symmetry of the crystal 
    work with tetrahedra. Some grids with offset may not work. 

    """
    tpiba = 6
    """   
    read k-points in cartesian coordinates, 
    in units of 2 pi/a (default) 

    """
    gamma = 7
    """   
    use k = 0 (no need to list k-point specifications after card) 
    In this case wavefunctions can be chosen as real, 
    and specialized subroutines optimized for calculations 
    at the gamma point are used (memory and cpu requirements 
    are reduced by approximately one half). 

    """
