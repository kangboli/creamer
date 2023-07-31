from typing import Optional, List
from .Options import Options


class AssumeIsolatedOptions(Options):
    """
    Others:
    ================
    
     Used to perform calculation assuming the system to be 
     isolated (a molecule or a cluster in a 3D supercell). 
     
     Currently available choices: 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    martyna__dash__tuckerman = 0
    """   
    Martyna-Tuckerman correction 
    to both total energy and scf potential. Adapted from: 
    G.J. Martyna, and M.E. Tuckerman, 
    "A reciprocal space based method for treating long 
    range interactions in ab-initio and force-field-based 
    calculation in clusters", J. Chem. Phys. 110, 2810 (1999), 
    doi:10.1063/1.477923. 

    """
    m__dash__t = 1
    """   
    Martyna-Tuckerman correction 
    to both total energy and scf potential. Adapted from: 
    G.J. Martyna, and M.E. Tuckerman, 
    "A reciprocal space based method for treating long 
    range interactions in ab-initio and force-field-based 
    calculation in clusters", J. Chem. Phys. 110, 2810 (1999), 
    doi:10.1063/1.477923. 

    """
    2d = 2
    """   
    Truncation of the Coulomb interaction in the z direction 
    for structures periodic in the x-y plane. Total energy, 
    forces and stresses are computed in a two-dimensional framework. 
    Linear-response calculations () done on top of a self-consistent 
    calculation with this flag will automatically be performed in 
    the 2D framework as well. Please refer to: 
    Sohier, T., Calandra, M., & Mauri, F. (2017), Density functional 
    perturbation theory for gated two-dimensional heterostructures: 
    Theoretical developments and application to flexural phonons in graphene. 
    Physical Review B, 96(7), 75448. https://doi.org/10.1103/PhysRevB.96.075448 
    
    NB: 
    - The length of the unit-cell along the z direction should 
    be larger than twice the thickness of the 2D material 
    (including electrons). A reasonable estimate for a 
    layer's thickness could be the interlayer distance in the 
    corresponding layered bulk material. Otherwise, 
    the atomic thickness + 10 bohr should be a safe estimate. 
    There is also a lower limit of 20 bohr imposed by the cutoff 
    radius used to read pseudopotentials (see read_pseudo.f90 in Modules). 
    
    - As for ESM above, only in-plane stresses make sense and one 
    should use cell_dofree='2Dxy' in a vc-relax calculation. 

    """
    mp = 3
    """   
    the Makov-Payne correction to the 
    total energy is computed. An estimate of the vacuum 
    level is also calculated so that eigenvalues can be 
    properly aligned. ONLY FOR CUBIC SYSTEMS ( ~ibrav=1,2,3).~ 
    Theory: G.Makov, and M.C.Payne, 
    "Periodic boundary conditions in ab initio 
    calculations" , PRB 51, 4014 (1995). 

    """
    m__dash__p = 4
    """   
    the Makov-Payne correction to the 
    total energy is computed. An estimate of the vacuum 
    level is also calculated so that eigenvalues can be 
    properly aligned. ONLY FOR CUBIC SYSTEMS ( ~ibrav=1,2,3).~ 
    Theory: G.Makov, and M.C.Payne, 
    "Periodic boundary conditions in ab initio 
    calculations" , PRB 51, 4014 (1995). 

    """
    mt = 5
    """   
    Martyna-Tuckerman correction 
    to both total energy and scf potential. Adapted from: 
    G.J. Martyna, and M.E. Tuckerman, 
    "A reciprocal space based method for treating long 
    range interactions in ab-initio and force-field-based 
    calculation in clusters", J. Chem. Phys. 110, 2810 (1999), 
    doi:10.1063/1.477923. 

    """
    none = 6
    """   
    (default): regular periodic calculation w/o any correction. 

    """
    makov__dash__payne = 7
    """   
    the Makov-Payne correction to the 
    total energy is computed. An estimate of the vacuum 
    level is also calculated so that eigenvalues can be 
    properly aligned. ONLY FOR CUBIC SYSTEMS ( ~ibrav=1,2,3).~ 
    Theory: G.Makov, and M.C.Payne, 
    "Periodic boundary conditions in ab initio 
    calculations" , PRB 51, 4014 (1995). 

    """
    esm = 8
    """   
    Effective Screening Medium Method. 
    For polarized or charged slab calculation, embeds 
    the simulation cell within an effective semi- 
    infinite medium in the perpendicular direction 
    (along z). Embedding regions can be vacuum or 
    semi-infinite metal electrodes (use ~esm_bc~ to 
    choose boundary conditions). If between two 
    electrodes, an optional electric field 
    ('esm_efield') may be applied. Method described in 
    M. Otani and O. Sugino, "First-principles calculations 
    of charged surfaces and interfaces: A plane-wave 
    nonrepeated slab approach", PRB 73, 115407 (2006). 
    
    NB: 
    - Two dimensional (xy plane) average charge density 
    and electrostatic potentials are printed out to 
    'prefix.esm1'. 
    
    - Requires cell with a_3 lattice vector along z, 
    normal to the xy plane, with the slab centered 
    around z=0. Also requires symmetry checking to be 
    disabled along z, either by setting ~nosym~ = .TRUE. 
    or by very slight displacement (i.e., 5e-4 a.u.) 
    of the slab along z. 
    
    - Components of the total stress; sigma_xy, sigma_yz, 
    sigma_zz, sigma_zy, and sigma_zx are meaningless 
    because ESM stress routines calculate only 
    components of stress; sigma_xx, sigma_xy, sigma_yx, 
    and sigma_yy. 
    
    - In case of calculation='vc-relax', use 
    cell_dofree='2Dxy' or other parameters so that 
    c-vector along z-axis should not be moved. 
    
    See ~esm_bc,~ ~esm_efield,~ ~esm_w,~ ~esm_nfit.~ 

    """
