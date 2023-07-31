from typing import Optional, List
from .Options import Options


class UProjectionTypeOptions(Options):
    """
    Others:
    ================
    
     Only active when ~lda_plus_U~ is .true., specifies the type 
     of projector on localized orbital to be used in the DFT+U 
     scheme. 
     
     Currently available choices: 
    
     NB: forces and stress currently implemented only for the 
     'atomic' and 'pseudo' choice. 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    ortho__dash__atomic = 0
    """   use Lowdin orthogonalized atomic wfc's

    """
    norm__dash__atomic = 1
    """   
    Lowdin normalization of atomic wfc. Keep in mind: 
    atomic wfc are not orthogonalized in this case. 
    This is a "quick and dirty" trick to be used when 
    atomic wfc from the pseudopotential are not 
    normalized (and thus produce occupation whose 
    value exceeds unity). If orthogonalized wfc are 
    not needed always try **'atomic'** first. 

    """
    file = 2
    """   
    use the information from file "prefix".atwfc that must 
    have been generated previously, for instance by pmw.x 
    (see PP/src/poormanwannier.f90 for details). 

    """
    atomic = 3
    """   use atomic wfc's (as they are) to build the projector

    """
    pseudo = 4
    """   
    use the pseudopotential projectors. The charge density 
    outside the atomic core radii is excluded. 
    N.B.: for atoms with +U, a pseudopotential with the 
    all-electron atomic wavefunctions is required (i.e., 
    as generated by ld1.x with lsave_wfc flag). 

    """