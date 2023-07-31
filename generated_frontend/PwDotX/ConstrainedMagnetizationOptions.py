from typing import Optional, List
from .Options import Options


class ConstrainedMagnetizationOptions(Options):
    """
    Others:
    ================
    
     Used to perform constrained calculations in magnetic systems. 
     Currently available choices: 
    
     N.B.: symmetrization may prevent to reach the desired orientation 
     of the magnetization. Try not to start with very highly symmetric 
     configurations or use the nosym flag (only as a last remedy) 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    total = 0
    """   
    total magnetization is constrained by 
    adding a penalty functional to the total energy: 
    
    LAMBDA * SUM_ {i} ( magnetization(i) - fixed_magnetization(i) )**2 
    
    where the sum over i runs over the three components of 
    the magnetization. Lambda is a real number (see below). 
    Noncolinear case only. Use ~tot_magnetization~ for LSDA 

    """
    atomic__ws__direction = 1
    """   
    not all the components of the atomic 
    magnetic moment are constrained but only the cosine 
    of angle1, and the penalty functional is: 
    
    LAMBDA * SUM_ {itype} ( mag_mom(3,itype)/mag_mom_tot - cos(angle1(ityp)) )**2 

    """
    atomic = 2
    """   
    atomic magnetization are constrained to the defined 
    starting magnetization adding a penalty: 
    
    LAMBDA * SUM_ {i,itype} ( magnetic_moment(i,itype) - mcons(i,itype) )**2 
    
    where i runs over the cartesian components (or just z 
    in the collinear case) and itype over the types (1-ntype). 
    mcons(:,:) array is defined from starting_magnetization, 
    (and angle1, angle2 in the non-collinear case). lambda is 
    a real number 

    """
    total__ws__direction = 3
    """   
    the angle theta of the total magnetization 
    with the z axis (theta = fixed_magnetization(3)) 
    is constrained: 
    
    LAMBDA * ( arccos(magnetization(3)/mag_tot) - theta )**2 
    
    where mag_tot is the modulus of the total magnetization. 

    """
    none = 4
    """   
    no constraint 

    """
