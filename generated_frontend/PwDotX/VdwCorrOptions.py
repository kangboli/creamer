from typing import Optional, List
from .Options import Options


class VdwCorrOptions(Options):
    """
    Others:
    ================
    
     Type of Van der Waals correction. Allowed values: 
    Note that non-local functionals (eg vdw-DF) are NOT specified here but in ~input_dft~


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    xdm = 0
    """   
    Exchange-hole dipole-moment model. Optional variables: ~xdm_a1,~ ~xdm_a2~ 
    A. D. Becke et al., J. Chem. Phys. 127, 154108 (2007), doi:10.1063/1.2795701 
    A. Otero de la Roza et al., J. Chem. Phys. 136, 174109 (2012), 
    doi:10.1063/1.4705760 

    """
    dft__dash__d3 = 1
    """   
    Semiempirical Grimme's DFT-D3. Optional variables: 
    ~dftd3_version,~ ~dftd3_threebody~ 
    S. Grimme et al, J. Chem. Phys 132, 154104 (2010), doi:10.1002/jcc.20495 

    """
    grimme__dash__d2 = 2
    """   
    Semiempirical Grimme's DFT-D2. Optional variables: 
    ~london_s6,~ ~london_rcut,~ ~london_c6,~ ~london_rvdw~ 
    S. Grimme, J. Comp. Chem. 27, 1787 (2006), doi:10.1002/jcc.20495 
    V. Barone et al., J. Comp. Chem. 30, 934 (2009), doi:10.1002/jcc.21112 

    """
    grimme__dash__d3 = 3
    """   
    Semiempirical Grimme's DFT-D3. Optional variables: 
    ~dftd3_version,~ ~dftd3_threebody~ 
    S. Grimme et al, J. Chem. Phys 132, 154104 (2010), doi:10.1002/jcc.20495 

    """
    dft__dash__d = 4
    """   
    Semiempirical Grimme's DFT-D2. Optional variables: 
    ~london_s6,~ ~london_rcut,~ ~london_c6,~ ~london_rvdw~ 
    S. Grimme, J. Comp. Chem. 27, 1787 (2006), doi:10.1002/jcc.20495 
    V. Barone et al., J. Comp. Chem. 30, 934 (2009), doi:10.1002/jcc.21112 

    """
    ts__dash__vdw = 5
    """   
    Tkatchenko-Scheffler dispersion corrections with first-principle derived 
    C6 coefficients. 
    Optional variables: ~ts_vdw_econv_thr,~ ~ts_vdw_isolated~ 
    See A. Tkatchenko and M. Scheffler, PRL 102, 073005 (2009). 

    """
    tkatchenko__dash__scheffler = 6
    """   
    Tkatchenko-Scheffler dispersion corrections with first-principle derived 
    C6 coefficients. 
    Optional variables: ~ts_vdw_econv_thr,~ ~ts_vdw_isolated~ 
    See A. Tkatchenko and M. Scheffler, PRL 102, 073005 (2009). 

    """
    ts = 7
    """   
    Tkatchenko-Scheffler dispersion corrections with first-principle derived 
    C6 coefficients. 
    Optional variables: ~ts_vdw_econv_thr,~ ~ts_vdw_isolated~ 
    See A. Tkatchenko and M. Scheffler, PRL 102, 073005 (2009). 

    """
