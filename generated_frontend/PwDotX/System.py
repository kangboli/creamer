from typing import Optional, List
from .Namelist import Namelist
from .Group0 import Group0
from .OccupationsOptions import OccupationsOptions
from .SmearingOptions import SmearingOptions
from .ExxdivTreatmentOptions import ExxdivTreatmentOptions
from .UProjectionTypeOptions import UProjectionTypeOptions
from .HubbardParametersOptions import HubbardParametersOptions
from .ConstrainedMagnetizationOptions import ConstrainedMagnetizationOptions
from .AssumeIsolatedOptions import AssumeIsolatedOptions
from .EsmBcOptions import EsmBcOptions
from .VdwCorrOptions import VdwCorrOptions
from .Dftd3VersionOptions import Dftd3VersionOptions
from .Group1 import Group1


class System(Namelist):
    """
    """

    def __init__(self,
                 ibrav: Optional[int] = None,
                 nat: Optional[int] = None,
                 ntyp: Optional[int] = None,
                 nbnd: Optional[int] = None,
                 tot_charge: Optional[float] = None,
                 starting_charge: Optional[List[float]] = None,
                 tot_magnetization: Optional[float] = None,
                 starting_magnetization: Optional[List[float]] = None,
                 ecutwfc: Optional[float] = None,
                 ecutrho: Optional[float] = None,
                 ecutfock: Optional[float] = None,
                 nr1: Optional[int] = None,
                 nr2: Optional[int] = None,
                 nr3: Optional[int] = None,
                 nr1s: Optional[int] = None,
                 nr2s: Optional[int] = None,
                 nr3s: Optional[int] = None,
                 nosym: Optional[bool] = None,
                 nosym_evc: Optional[bool] = None,
                 noinv: Optional[bool] = None,
                 no_t_rev: Optional[bool] = None,
                 force_symmorphic: Optional[bool] = None,
                 use_all_frac: Optional[bool] = None,
                 occupations: Optional[OccupationsOptions] = None,
                 one_atom_occupations: Optional[bool] = None,
                 starting_spin_angle: Optional[bool] = None,
                 degauss: Optional[float] = None,
                 smearing: Optional[SmearingOptions] = None,
                 nspin: Optional[int] = None,
                 noncolin: Optional[bool] = None,
                 ecfixed: Optional[float] = None,
                 qcutz: Optional[float] = None,
                 q2sigma: Optional[float] = None,
                 input_dft: Optional[str] = None,
                 ace: Optional[bool] = None,
                 exx_fraction: Optional[float] = None,
                 screening_parameter: Optional[float] = None,
                 exxdiv_treatment: Optional[ExxdivTreatmentOptions] = None,
                 x_gamma_extrapolation: Optional[bool] = None,
                 ecutvcut: Optional[float] = None,
                 nqx1: Optional[int] = None,
                 nqx2: Optional[int] = None,
                 nqx3: Optional[int] = None,
                 localization_thr: Optional[float] = None,
                 lda_plus_u: Optional[bool] = None,
                 lda_plus_u_kind: Optional[int] = None,
                 hubbard_u: Optional[List[float]] = None,
                 hubbard_j0: Optional[List[float]] = None,
                 hubbard_v: Optional[List[float]] = None,
                 hubbard_alpha: Optional[List[float]] = None,
                 hubbard_beta: Optional[List[float]] = None,
                 hubbard_j: Optional[List[float]] = None,
                 starting_ns_eigenvalue: Optional[List[float]] = None,
                 U_projection_type: Optional[UProjectionTypeOptions] = None,
                 Hubbard_parameters: Optional[HubbardParametersOptions] = None,
                 ensemble_energies: Optional[bool] = None,
                 edir: Optional[int] = None,
                 emaxpos: Optional[float] = None,
                 eopreg: Optional[float] = None,
                 eamp: Optional[float] = None,
                 angle1: Optional[List[float]] = None,
                 angle2: Optional[List[float]] = None,
                 lforcet: Optional[bool] = None,
                 constrained_magnetization: Optional[ConstrainedMagnetizationOptions] = None,
                 fixed_magnetization: Optional[List[float]] = None,
                 lambda_is_a_python_keyword: Optional[float] = None,
                 report: Optional[int] = None,
                 lspinorb: Optional[bool] = None,
                 assume_isolated: Optional[AssumeIsolatedOptions] = None,
                 esm_bc: Optional[EsmBcOptions] = None,
                 esm_w: Optional[float] = None,
                 esm_efield: Optional[float] = None,
                 esm_nfit: Optional[int] = None,
                 fcp_mu: Optional[float] = None,
                 vdw_corr: Optional[VdwCorrOptions] = None,
                 london: Optional[bool] = None,
                 london_s6: Optional[float] = None,
                 london_c6: Optional[List[float]] = None,
                 london_rvdw: Optional[List[float]] = None,
                 london_rcut: Optional[float] = None,
                 dftd3_version: Optional[Dftd3VersionOptions] = None,
                 dftd3_threebody: Optional[bool] = None,
                 ts_vdw_econv_thr: Optional[float] = None,
                 ts_vdw_isolated: Optional[bool] = None,
                 xdm: Optional[bool] = None,
                 xdm_a1: Optional[float] = None,
                 xdm_a2: Optional[float] = None,
                 space_group: Optional[int] = None,
                 uniqueb: Optional[bool] = None,
                 origin_choice: Optional[int] = None,
                 rhombohedral: Optional[bool] = None,
                 ):
        """
        Parameters
        ----------
        **ibrav**: int
            *Info*:             
             Bravais-lattice index. Optional only if space_group is set. 
             If ibrav /= 0, specify EITHER [ ~celldm(1)-~ ~celldm(6)~ ] 
             OR [ ~A,~ ~B,~ ~C,~ ~cosAB,~ ~cosAC,~ ~cosBC~ ] 
             but NOT both. The lattice parameter "alat" is set to 
             alat = celldm(1) (in a.u.) or alat = A (in Angstrom); 
             see below for the other parameters. 
             For ibrav=0 specify the lattice vectors in ~CELL_PARAMETERS,~ 
             optionally the lattice parameter alat = celldm(1) (in a.u.) 
             or = A (in Angstrom). If not specified, the lattice parameter is 
             taken from ~CELL_PARAMETERS~ 
             IMPORTANT NOTICE 1: 
             with ibrav=0 lattice vectors must be given with a sufficiently large 
             number of digits and with the correct symmetry, or else symmetry 
             detection may fail and strange problems may arise in symmetrization. 
             IMPORTANT NOTICE 2: 
             do not use celldm(1) or A as a.u. to Ang conversion factor, 
             use the true lattice parameters or nothing, 
             specify units in ~CELL_PARAMETERS~ and ~ATOMIC_POSITIONS~ 
             
             ibrav structure celldm(2)-celldm(6) 
             or: b,c,cosbc,cosac,cosab 
             0 free 
             crystal axis provided in input: see card ~CELL_PARAMETERS~ 
             
             1 cubic P (sc) 
             v1 = a(1,0,0), v2 = a(0,1,0), v3 = a(0,0,1) 
             
             2 cubic F (fcc) 
             v1 = (a/2)(-1,0,1), v2 = (a/2)(0,1,1), v3 = (a/2)(-1,1,0) 
             
             3 cubic I (bcc) 
             v1 = (a/2)(1,1,1), v2 = (a/2)(-1,1,1), v3 = (a/2)(-1,-1,1) 
             -3 cubic I (bcc), more symmetric axis: 
             v1 = (a/2)(-1,1,1), v2 = (a/2)(1,-1,1), v3 = (a/2)(1,1,-1) 
             
             4 Hexagonal and Trigonal P celldm(3)=c/a 
             v1 = a(1,0,0), v2 = a(-1/2,sqrt(3)/2,0), v3 = a(0,0,c/a) 
             
             5 Trigonal R, 3fold axis c celldm(4)=cos(gamma) 
             The crystallographic vectors form a three-fold star around 
             the z-axis, the primitive cell is a simple rhombohedron: 
             v1 = a(tx,-ty,tz), v2 = a(0,2ty,tz), v3 = a(-tx,-ty,tz) 
             where c=cos(gamma) is the cosine of the angle gamma between 
             any pair of crystallographic vectors, tx, ty, tz are: 
             tx=sqrt((1-c)/2), ty=sqrt((1-c)/6), tz=sqrt((1+2c)/3) 
             -5 Trigonal R, 3fold axis <111> celldm(4)=cos(gamma) 
             The crystallographic vectors form a three-fold star around 
             <111>. Defining a' = a/sqrt(3) : 
             v1 = a' (u,v,v), v2 = a' (v,u,v), v3 = a' (v,v,u) 
             where u and v are defined as 
             u = tz - 2*sqrt(2)*ty, v = tz + sqrt(2)*ty 
             and tx, ty, tz as for case ibrav=5 
             Note: if you prefer x,y,z as axis in the cubic limit, 
             set u = tz + 2*sqrt(2)*ty, v = tz - sqrt(2)*ty 
             See also the note in Modules/latgen.f90 
             
             6 Tetragonal P (st) celldm(3)=c/a 
             v1 = a(1,0,0), v2 = a(0,1,0), v3 = a(0,0,c/a) 
             
             7 Tetragonal I (bct) celldm(3)=c/a 
             v1=(a/2)(1,-1,c/a), v2=(a/2)(1,1,c/a), v3=(a/2)(-1,-1,c/a) 
             
             8 Orthorhombic P celldm(2)=b/a 
             celldm(3)=c/a 
             v1 = (a,0,0), v2 = (0,b,0), v3 = (0,0,c) 
             
             9 Orthorhombic base-centered(bco) celldm(2)=b/a 
             celldm(3)=c/a 
             v1 = (a/2, b/2,0), v2 = (-a/2,b/2,0), v3 = (0,0,c) 
             -9 as 9, alternate description 
             v1 = (a/2,-b/2,0), v2 = (a/2, b/2,0), v3 = (0,0,c) 
             91 Orthorhombic one-face base-centered A-type 
             celldm(2)=b/a 
             celldm(3)=c/a 
             v1 = (a, 0, 0), v2 = (0,b/2,-c/2), v3 = (0,b/2,c/2) 
             
             10 Orthorhombic face-centered celldm(2)=b/a 
             celldm(3)=c/a 
             v1 = (a/2,0,c/2), v2 = (a/2,b/2,0), v3 = (0,b/2,c/2) 
             
             11 Orthorhombic body-centered celldm(2)=b/a 
             celldm(3)=c/a 
             v1=(a/2,b/2,c/2), v2=(-a/2,b/2,c/2), v3=(-a/2,-b/2,c/2) 
             
             12 Monoclinic P, unique axis c celldm(2)=b/a 
             celldm(3)=c/a, 
             celldm(4)=cos(ab) 
             v1=(a,0,0), v2=(b*cos(gamma),b*sin(gamma),0), v3 = (0,0,c) 
             where gamma is the angle between axis a and b. 
             -12 Monoclinic P, unique axis b celldm(2)=b/a 
             celldm(3)=c/a, 
             celldm(5)=cos(ac) 
             v1 = (a,0,0), v2 = (0,b,0), v3 = (c*cos(beta),0,c*sin(beta)) 
             where beta is the angle between axis a and c 
             
             13 Monoclinic base-centered celldm(2)=b/a 
             (unique axis c) celldm(3)=c/a, 
             celldm(4)=cos(gamma) 
             v1 = ( a/2, 0, -c/2), 
             v2 = (b*cos(gamma), b*sin(gamma), 0 ), 
             v3 = ( a/2, 0, c/2), 
             where gamma=angle between axis a and b projected on xy plane 
             
             -13 Monoclinic base-centered celldm(2)=b/a 
             (unique axis b) celldm(3)=c/a, 
             celldm(5)=cos(beta) 
             v1 = ( a/2, b/2, 0), 
             v2 = ( -a/2, b/2, 0), 
             v3 = (c*cos(beta), 0, c*sin(beta)), 
             where beta=angle between axis a and c projected on xz plane 
             IMPORTANT NOTICE: until QE v.6.4.1, axis for ibrav=-13 had a 
             different definition: v1(old) =-v2(now), v2(old) = v1(now) 
             
             14 Triclinic celldm(2)= b/a, 
             celldm(3)= c/a, 
             celldm(4)= cos(bc), 
             celldm(5)= cos(ac), 
             celldm(6)= cos(ab) 
             v1 = (a, 0, 0), 
             v2 = (b*cos(gamma), b*sin(gamma), 0) 
             v3 = (c*cos(beta), c*(cos(alpha)-cos(beta)cos(gamma))/sin(gamma), 
             c*sqrt( 1 + 2*cos(alpha)cos(beta)cos(gamma) 
             - cos(alpha)^2-cos(beta)^2-cos(gamma)^2 )/sin(gamma) ) 
             where alpha is the angle between axis b and c 
             beta is the angle between axis a and c 
             gamma is the angle between axis a and b 



        **nat**: int
            *Info*:             
             number of atoms in the unit cell (ALL atoms, except if 
             space_group is set, in which case, INEQUIVALENT atoms) 



        **ntyp**: int
            *Info*:             
             number of types of atoms in the unit cell 



        **nbnd**: int
            *Default*:             
             for an insulator, ~nbnd~ = number of valence bands 
             ( ~nbnd~ = # of electrons /2); 
             **r** for a metal, 20% more (minimum 4 more) 


            *Info*:             
             Number of electronic states (bands) to be calculated. 
             Note that in spin-polarized calculations the number of 
             k-point, not the number of bands per k-point, is doubled 



        **tot_charge**: float
            *Default*:             0.0


            *Info*:             
             Total charge of the system. Useful for simulations with charged cells. 
             By default the unit cell is assumed to be neutral (tot_charge=0). 
             tot_charge=+1 means one electron missing from the system, 
             tot_charge=-1 means one additional electron, and so on. 
             
             In a periodic calculation a compensating jellium background is 
             inserted to remove divergences if the cell is not neutral. 



        **starting_charge**: List[float]
            *Default*:             0.0


            *Info*:             
             starting charge on atomic type 'i', 
             to create starting potential with ~startingpot~ = 'atomic'. 


            *Others*:             Start - 1; End - ntyp



        **tot_magnetization**: float
            *Default*:             -1 [unspecified]


            *Info*:             
             Total majority spin charge - minority spin charge. 
             Used to impose a specific total electronic magnetization. 
             If unspecified then tot_magnetization variable is ignored and 
             the amount of electronic magnetization is determined during 
             the self-consistent cycle. 



        **starting_magnetization**: List[float]
            *Info*:             
             Starting spin polarization on atomic type 'i' in a spin 
                            polarized calculation. Values range between -1 (all spins
                            down for the valence electrons of atom type 'i' ) to 1 
             (all spins up). Breaks the symmetry and provides a starting 
             point for self-consistency. The default value is zero, BUT a 
             value MUST be specified for AT LEAST one atomic type in spin 
             polarized calculations, unless you constrain the magnetization 
             (see ~tot_magnetization~ and ~constrained_magnetization).~ 
             Note that if you start from zero initial magnetization, you 
             will invariably end up in a nonmagnetic (zero magnetization) 
             state. If you want to start from an antiferromagnetic state, 
             you may need to define two different atomic species 
             corresponding to sublattices of the same atomic type. 
             starting_magnetization is ignored if you are performing a 
             non-scf calculation, if you are restarting from a previous 
             run, or restarting from an interrupted run. 
             If you fix the magnetization with ~tot_magnetization,~ 
             you should not specify starting_magnetization. 
             In the spin-orbit case starting with zero 
             starting_magnetization on all atoms imposes time reversal 
             symmetry. The magnetization is never calculated and 
             kept zero (the internal variable domag is .FALSE.). 


            *Others*:             Start - 1; End - ntyp



        **ecutwfc**: float
            *Info*:             
             kinetic energy cutoff (Ry) for wavefunctions 



        **ecutrho**: float
            *Default*:             4 * ~ecutwfc~


            *Info*:             
             Kinetic energy cutoff (Ry) for charge density and potential 
             For norm-conserving pseudopotential you should stick to the 
             default value, you can reduce it by a little but it will 
             introduce noise especially on forces and stress. 
             If there are ultrasoft PP, a larger value than the default is 
             often desirable (ecutrho = 8 to 12 times ~ecutwfc,~ typically). 
             PAW datasets can often be used at 4* ~ecutwfc,~ but it depends 
             on the shape of augmentation charge: testing is mandatory. 
             The use of gradient-corrected functional, especially in cells 
             with vacuum, or for pseudopotential without non-linear core 
             correction, usually requires an higher values of ecutrho 
             to be accurately converged. 



        **ecutfock**: float
            *Default*:             ecutrho


            *Info*:             
             Kinetic energy cutoff (Ry) for the exact exchange operator in 
             EXX type calculations. By default this is the same as ~ecutrho~ 
             but in some EXX calculations, a significant speed-up can be obtained 
             by reducing ecutfock, at the expense of some loss in accuracy. 
             Must be .gt. ~ecutwfc.~ Not implemented for stress calculation 
             and for US-PP and PAW pseudopotentials. 
             Use with care, especially in metals where it may give raise 
             to instabilities. 



        **nr1**: int
            *Info*:             
             Three-dimensional FFT mesh (hard grid) for charge 
             density (and scf potential). If not specified 
             the grid is calculated based on the cutoff for 
             charge density (see also ~ecutrho)~ 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nr2**: int
            *Info*:             
             Three-dimensional FFT mesh (hard grid) for charge 
             density (and scf potential). If not specified 
             the grid is calculated based on the cutoff for 
             charge density (see also ~ecutrho)~ 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nr3**: int
            *Info*:             
             Three-dimensional FFT mesh (hard grid) for charge 
             density (and scf potential). If not specified 
             the grid is calculated based on the cutoff for 
             charge density (see also ~ecutrho)~ 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nr1s**: int
            *Info*:             
             Three-dimensional mesh for wavefunction FFT and for the smooth 
             part of charge density ( smooth grid ). 
             Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nr2s**: int
            *Info*:             
             Three-dimensional mesh for wavefunction FFT and for the smooth 
             part of charge density ( smooth grid ). 
             Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nr3s**: int
            *Info*:             
             Three-dimensional mesh for wavefunction FFT and for the smooth 
             part of charge density ( smooth grid ). 
             Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
             Note: you must specify all three dimensions for this setting to 
             be used. 



        **nosym**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.TRUE.) symmetry is not used. Consequences: 
             
             - if a list of k points is provided in input, it is used 
             "as is": symmetry-inequivalent k-points are not generated, 
             and the charge density is not symmetrized; 
             
             - if a uniform (Monkhorst-Pack) k-point grid is provided in 
             input, it is expanded to cover the entire Brillouin Zone, 
             irrespective of the crystal symmetry. 
             Time reversal symmetry is assumed so k and -k are considered 
             as equivalent unless ~noinv=.true.~ is specified. 
             
             Do not use this option unless you know exactly what you want 
             and what you get. May be useful in the following cases: 
             - in low-symmetry large cells, if you cannot afford a k-point 
             grid with the correct symmetry 
             - in MD simulations 
             - in calculations for isolated atoms 



        **nosym_evc**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.TRUE.) symmetry is not used, and k points are 
             forced to have the symmetry of the Bravais lattice; 
             an automatically generated Monkhorst-Pack grid will contain 
             all points of the grid over the entire Brillouin Zone, 
             plus the points rotated by the symmetries of the Bravais 
             lattice which were not in the original grid. The same 
             applies if a k-point list is provided in input instead 
             of a Monkhorst-Pack grid. Time reversal symmetry is assumed 
             so k and -k are equivalent unless ~noinv=.true.~ is specified. 
             This option differs from ~nosym~ because it forces k-points 
             in all cases to have the full symmetry of the Bravais lattice 
             (not all uniform grids have such property!) 



        **noinv**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.TRUE.) disable the usage of k => -k symmetry 
             (time reversal) in k-point generation 



        **no_t_rev**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.TRUE.) disable the usage of magnetic symmetry operations 
             that consist in a rotation + time reversal. 



        **force_symmorphic**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.TRUE.) force the symmetry group to be symmorphic by disabling 
             symmetry operations having an associated fractionary translation 



        **use_all_frac**: bool
            *Default*:             .FALSE.


            *Info*:             
             if (.FALSE.) force real-space FFT grids to be commensurate with 
             fractionary translations of non-symmorphic symmetry operations, 
             if present (e.g.: if a fractional translation (0,0,c/4) exists, 
             the FFT dimension along the c axis must be multiple of 4). 
             if (.TRUE.) do not impose any constraints to FFT grids, even in 
             the presence of non-symmorphic symmetry operations. 
             BEWARE: use_all_frac=.TRUE. may lead to wrong results for 
             hybrid functionals and phonon calculations. Both cases use 
             symmetrization in real space that works for non-symmorphic 
             operations only if the real-space FFT grids are commensurate. 



        **occupations**: OccupationsOptions

        **one_atom_occupations**: bool
            *Default*:             .FALSE.


            *Info*:             
             This flag is used for isolated atoms ( ~nat=1)~ together with 
             ~occupations='from_input'.~ If it is .TRUE., the wavefunctions 
             are ordered as the atomic starting wavefunctions, independently 
             from their eigenvalue. The occupations indicate which atomic 
             states are filled. 
             
             The order of the states is written inside the UPF pseudopotential file. 
             In the scalar relativistic case: 
             S -> l=0, m=0 
             P -> l=1, z, x, y 
             D -> l=2, r^2-3z^2, xz, yz, xy, x^2-y^2 
             
             In the noncollinear magnetic case (with or without spin-orbit), 
             each group of states is doubled. For instance: 
             P -> l=1, z, x, y for spin up, l=1, z, x, y for spin down. 
             Up and down is relative to the direction of the starting 
             magnetization. 
             
             In the case with spin-orbit and time-reversal 
             ( ~starting_magnetization=0.0)~ the atomic wavefunctions are 
             radial functions multiplied by spin-angle functions. 
             For instance: 
             P -> l=1, j=1/2, m_j=-1/2,1/2. l=1, j=3/2, 
             m_j=-3/2, -1/2, 1/2, 3/2. 
             
             In the magnetic case with spin-orbit the atomic wavefunctions 
             can be forced to be spin-angle functions by setting 
             ~starting_spin_angle~ to .TRUE.. 



        **starting_spin_angle**: bool
            *Default*:             .FALSE.


            *Info*:             
             In the spin-orbit case when ~domag=.TRUE.,~ by default, 
             the starting wavefunctions are initialized as in scalar 
             relativistic noncollinear case without spin-orbit. 
             
             By setting ~starting_spin_angle=.TRUE.~ this behaviour can 
             be changed and the initial wavefunctions are radial 
             functions multiplied by spin-angle functions. 
             
             When ~domag=.FALSE.~ the initial wavefunctions are always 
             radial functions multiplied by spin-angle functions 
             independently from this flag. 
             
             When ~lspinorb~ is .FALSE. this flag is not used. 



        **degauss**: float
            *Default*:             0.D0 Ry


            *Info*:             
             value of the gaussian spreading (Ry) for brillouin-zone 
             integration in metals. 



        **smearing**: SmearingOptions
            *Default*:             'gaussian'



        **nspin**: int
            *Default*:             1


            *Info*:             
             nspin = 1 : non-polarized calculation (default) 
             
             nspin = 2 : spin-polarized calculation, LSDA 
             (magnetization along z axis) 
             
             nspin = 4 : spin-polarized calculation, noncollinear 
             (magnetization in generic direction) 
             DO NOT specify ~nspin~ in this case; 
             specify ~noncolin=.TRUE.~ instead 



        **noncolin**: bool
            *Default*:             .false.


            *Info*:             
             if .true. the program will perform a noncollinear calculation. 



        **ecfixed**: float
            *Default*:             0.0



        **qcutz**: float
            *Default*:             0.0



        **q2sigma**: float
            *Default*:             0.1


            *Info*:             
             ecfixed, qcutz, q2sigma: parameters for modified functional to be 
             used in variable-cell molecular dynamics (or in stress calculation). 
             "ecfixed" is the value (in Rydberg) of the constant-cutoff; 
             "qcutz" and "q2sigma" are the height and the width (in Rydberg) 
             of the energy step for reciprocal vectors whose square modulus 
             is greater than "ecfixed". In the kinetic energy, G^2 is 
             replaced by G^2 + qcutz * (1 + erf ( (G^2 - ecfixed)/q2sigma) ) 
             See: M. Bernasconi et al, J. Phys. Chem. Solids 56, 501 (1995), 
             doi:10.1016/0022-3697(94)00228-2 



        **input_dft**: str
            *Default*:             read from pseudopotential files


            *Info*:             
             Exchange-correlation functional: eg 'PBE', 'BLYP' etc 
             See Modules/funct.f90 for allowed values. 
             Overrides the value read from pseudopotential files. 
             Use with care and if you know what you are doing! 



        **ace**: bool
            *Default*:             true


            *Info*:             
             Use Adaptively Compressed Exchange operator as in 
             Lin Lin, J. Chem. Theory Comput. 2016, 12, 2242--2249, doi:10.1021/acs.jctc.6b00092 
             
             Set to false to use standard Exchange (much slower) 



        **exx_fraction**: float
            *Default*:             it depends on the specified functional


            *Info*:             
             Fraction of EXX for hybrid functional calculations. In the case of 
             ~input_dft='PBE0',~ the default value is 0.25, while for ~input_dft='B3LYP'~ 
             the ~exx_fraction~ default value is 0.20. 



        **screening_parameter**: float
            *Default*:             0.106


            *Info*:             
             screening_parameter for HSE like hybrid functionals. 
             For more information, see: 
             J. Chem. Phys. 118, 8207 (2003), doi:10.1063/1.1564060 
             J. Chem. Phys. 124, 219906 (2006), doi:10.1063/1.2204597 



        **exxdiv_treatment**: ExxdivTreatmentOptions
            *Default*:             'gygi-baldereschi'



        **x_gamma_extrapolation**: bool
            *Default*:             .true.


            *Info*:             
             Specific for EXX. If .true., extrapolate the G=0 term of the 
             potential (see README in examples/EXX_example for more) 
             Set this to .false. for GAU-PBE. 



        **ecutvcut**: float
            *Default*:             0.0 Ry


            *Info*:             
             Reciprocal space cutoff for correcting Coulomb potential 
             divergencies at small q vectors. 



        **nqx1**: int
            *Info*:             
             Three-dimensional mesh for q (k1-k2) sampling of 
             the Fock operator (EXX). Can be smaller than 
             the number of k-points. 
             
             Currently this defaults to the size of the k-point mesh used. 
             In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        **nqx2**: int
            *Info*:             
             Three-dimensional mesh for q (k1-k2) sampling of 
             the Fock operator (EXX). Can be smaller than 
             the number of k-points. 
             
             Currently this defaults to the size of the k-point mesh used. 
             In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        **nqx3**: int
            *Info*:             
             Three-dimensional mesh for q (k1-k2) sampling of 
             the Fock operator (EXX). Can be smaller than 
             the number of k-points. 
             
             Currently this defaults to the size of the k-point mesh used. 
             In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        **localization_thr**: float
            *Default*:             0.0


            *Info*:             
             Overlap threshold over which the exchange integral over a pair of localized orbitals 
             is included in the evaluation of EXX operator. Any value greater than 0.0 triggers 
             the SCDM localization and the evaluation on EXX using the localized orbitals. 
             Very small value of the threshold should yield the same result as the default EXX 
             evaluation



        **lda_plus_u**: bool
            *Default*:             .FALSE.


            *Info*:             
             Specify ~lda_plus_u~ = .TRUE. to enable DFT+U calculations 
             See: Anisimov, Zaanen, and Andersen, PRB 44, 943 (1991); 
             Anisimov et al., PRB 48, 16929 (1993); 
             Liechtenstein, Anisimov, and Zaanen, PRB 52, R5467 (1994). 
             You must specify, for each species with a U term, the value of 
             U and (optionally) alpha, J of the Hubbard model (all in eV): 
             see ~lda_plus_u_kind,~ ~Hubbard_U,~ ~Hubbard_alpha,~ ~Hubbard_J~ 



        **lda_plus_u_kind**: int
            *Default*:             0


            *Info*:             
             Specifies the type of calculation: 
             
             0 DFT+U simplified version of Cococcioni and de Gironcoli, 
             PRB 71, 035105 (2005), using ~Hubbard_U~ 
             
             1 DFT+U rotationally invariant scheme of Liechtenstein et al., 
             using ~Hubbard_U~ and ~Hubbard_J~ 
             
             2 DFT+U+V simplified version of Campo Jr and Cococcioni, 
             J. Phys.: Condens. Matter 22, 055602 (2010), using ~Hubbard_V~ 



        **hubbard_u**: List[float]
            *Default*:             0.D0 for all species


            *Info*:             
             Hubbard_U(i): U parameter (eV) for species i, DFT+U calculation 


            *Others*:             Start - 1; End - ntyp



        **hubbard_j0**: List[float]
            *Default*:             0.D0 for all species


            *Info*:             
             Hubbard_J0(i): J0 parameter (eV) for species i, DFT+U+J calculation, 
             see PRB 84, 115108 (2011) for details. 


            *Others*:             Start - 1; End - ntype



        **hubbard_v**: List[float]
            *Default*:             0.D0 for all elements


            *Info*:             
             Hubbard_V(na,nb,k): V parameters (eV) between atoms na and nb, 
             used in DFT+U+V calculations (only for ~lda_plus_u_kind=2).~ 
             The atomic indices na and nb correspond to the atomic positions 
             in the ~ATOMIC_POSITIONS~ card (this is not the same as Hubbard_U 
             which is specified for ~ATOMIC_SPECIES).~ 
             Wnen na=nb, then Hubbard_V(na,na,k) is the on-site Hubbard_U 
             for the atom na. 
             natx=50 (if needed it can be changed in /Modules/parameters.f90) 
             The index k controls the "interaction type" (k=1 is used for the 
             simplest DFT+U+V calculation): 
             k=1 - interaction between standard orbitals (both on na and nb); 
             k=2 - interaction between standard (on na) and background (on nb) orbitals; 
             k=3 - interaction between background orbitlas (both on na and nb); 
             k=4 - interaction between background (on na) and standard (on nb) orbitals. 
             Standard orbitals correspond to the main Hubbard channel (e.g. d electrons 
             in transition metals) and background orbitals correspond to the secondary 
             Hubbard channel (e.g. p electrons in transition metals). 


            *Others*:             Start - 1,1,1; End - natx,27*natx,4



        **hubbard_alpha**: List[float]
            *Default*:             0.D0 for all species


            *Info*:             
             Hubbard_alpha(i) is the perturbation (on atom i, in eV) 
             used to compute U with the linear-response method of 
             Cococcioni and de Gironcoli, PRB 71, 035105 (2005) 
             (only for ~lda_plus_u_kind=0)~ 


            *Others*:             Start - 1; End - ntyp



        **hubbard_beta**: List[float]
            *Default*:             0.D0 for all species


            *Info*:             
             Hubbard_beta(i) is the perturbation (on atom i, in eV) 
             used to compute J0 with the linear-response method of 
             Cococcioni and de Gironcoli, PRB 71, 035105 (2005) 
             (only for ~lda_plus_u_kind=0).~ See also 
             PRB 84, 115108 (2011). 


            *Others*:             Start - 1; End - ntyp



        **hubbard_j**: List[float]
            *Default*:             0.D0 for all species


            *Info*:             
             Hubbard_J(i,ityp): J parameters (eV) for species ityp, 
             used in DFT+U calculations (only for ~lda_plus_u_kind=1)~ 
             For p orbitals: J = Hubbard_J(1,ityp); 
             For d orbitals: J = Hubbard_J(1,ityp), B = Hubbard_J(2,ityp); 
             For f orbitals: J = Hubbard_J(1,ityp), E2 = Hubbard_J(2,ityp), 
             E3= Hubbard_J(3,ityp). 
             If B or E2 or E3 are not specified or set to 0 they will be 
             calculated from J using atomic ratios. 


            *Others*:             Start - 1,1; End - 3,ntyp



        **starting_ns_eigenvalue**: List[float]
            *Default*:             -1.d0 that means NOT SET


            *Info*:             
             In the first iteration of an DFT+U run it overwrites 
             the m-th eigenvalue of the ns occupation matrix for the 
             ispin component of atomic species ityp. 
             For the noncolin case the ispin index runs up to npol. 
             The value lmax is given by the maximum angular momentum 
             number to which the Hubbard U is applied. 
             Leave unchanged eigenvalues that are not set. 
             This is useful to suggest the desired orbital occupations 
             when the default choice takes another path. 


            *Others*:             Start - 1,1,1; End - 2*lmax+1,nspin\ or\ npol,ntyp



        **U_projection_type**: UProjectionTypeOptions
            *Default*:             'atomic'



        **Hubbard_parameters**: HubbardParametersOptions
            *Default*:             'input'



        **ensemble_energies**: bool
            *Default*:             .false.


            *Info*:             
             If ensemble_energies = .true., an ensemble of xc energies 
             is calculated non-selfconsistently for perturbed 
             exchange-enhancement factors and LDA vs. PBE correlation 
             ratios after each converged electronic ground state 
             calculation. 
             
             Ensemble energies can be analyzed with the 'bee' utility
                            included with libbeef.
            
                            Requires linking against libbeef.
                            input_dft must be set to a BEEF-type functional
                            (e.g. input_dft = 'BEEF-vdW' ) 



        **edir**: int
            *Info*:             
             The direction of the electric field or dipole correction is 
             parallel to the bg(:,edir) reciprocal lattice vector, so the 
             potential is constant in planes defined by FFT grid points; 
             ~edir~ = 1, 2 or 3. Used only if ~tefield~ is .TRUE. 



        **emaxpos**: float
            *Default*:             0.5D0


            *Info*:             
             Position of the maximum of the saw-like potential along crystal 
             axis ~edir,~ within the unit cell (see below), 0 < emaxpos < 1 
             Used only if ~tefield~ is .TRUE. 



        **eopreg**: float
            *Default*:             0.1D0


            *Info*:             
             Zone in the unit cell where the saw-like potential decreases. 
             ( see below, 0 < eopreg < 1 ). Used only if ~tefield~ is .TRUE. 



        **eamp**: float
            *Default*:             0.001 a.u.


            *Info*:             
             Amplitude of the electric field, in ***Hartree*** a.u.; 
             1 a.u. = 51.4220632*10^10 V/m. Used only if ~tefield==.TRUE.~ 
             The saw-like potential increases with slope ~eamp~ in the 
             region from ( ~emaxpos+~ ~eopreg-1)~ to ( ~emaxpos),~ then decreases 
             to 0 until ( ~emaxpos+~ ~eopreg),~ in units of the crystal 
             vector ~edir.~ Important: the change of slope of this 
             potential must be located in the empty region, or else 
             unphysical forces will result. 



        **angle1**: List[float]
            *Info*:             
             The angle expressed in degrees between the initial 
             magnetization and the z-axis. For noncollinear calculations 
             only; index i runs over the atom types. 


            *Others*:             Start - 1; End - ntyp



        **angle2**: List[float]
            *Info*:             
             The angle expressed in degrees between the projection 
             of the initial magnetization on x-y plane and the x-axis. 
             For noncollinear calculations only. 


            *Others*:             Start - 1; End - ntyp



        **lforcet**: bool
            *Info*:             
             When starting a non collinear calculation using an existing density 
             file from a collinear lsda calculation assumes previous density points in 
             *z* direction and rotates it in the direction described by ~angle1~ and 
             ~angle2~ variables for atomic type 1 



        **constrained_magnetization**: ConstrainedMagnetizationOptions
            *Default*:             'none'



        **fixed_magnetization**: List[float]
            *Default*:             0.d0


            *Info*:             
             total magnetization vector (x,y,z components) to be kept 
             fixed when ~constrained_magnetization=='total'~ 


            *Others*:             Start - 1; End - 3



        **lambda_is_a_python_keyword**: float
            *Default*:             1.d0


            *Info*:             
             parameter used for constrained_magnetization calculations 
             N.B.: if the scf calculation does not converge, try to reduce lambda 
             to obtain convergence, then restart the run with a larger lambda 



        **report**: int
            *Default*:             -1


            *Info*:             
             determines when atomic magnetic moments are printed on output: 
             report = 0 never 
             report =-1 at the beginning of the scf and at convergence 
             report = N: as -1, plus every N scf iterations 



        **lspinorb**: bool
            *Info*:             
             if .TRUE. the noncollinear code can use a pseudopotential with 
             spin-orbit. 



        **assume_isolated**: AssumeIsolatedOptions
            *Default*:             'none'



        **esm_bc**: EsmBcOptions
            *Default*:             'pbc'



        **esm_w**: float
            *Default*:             0.d0


            *Info*:             
             If ~assume_isolated~ = 'esm', determines the position offset 
             [in a.u.] of the start of the effective screening region, 
             measured relative to the cell edge. (ESM region begins at 
             z = +/- [L_z/2 + esm_w] ). 



        **esm_efield**: float
            *Default*:             0.d0


            *Info*:             
             If ~assume_isolated~ = 'esm' and ~esm_bc~ = 'bc2', gives the 
             magnitude of the electric field [Ry/a.u.] to be applied 
             between semi-infinite ESM electrodes. 



        **esm_nfit**: int
            *Default*:             4


            *Info*:             
             If ~assume_isolated~ = 'esm', gives the number of z-grid points 
             for the polynomial fit along the cell edge. 



        **fcp_mu**: float
            *Default*:             0.d0


            *Info*:             
             If ~lfcpopt~ = .TRUE., gives the target Fermi energy [Ry]. One can start 
             with appropriate total charge of the system by giving 'tot_charge'. 



        **vdw_corr**: VdwCorrOptions
            *Default*:             'none'



        **london**: bool
            *Default*:             .FALSE.



        **london_s6**: float
            *Default*:             0.75


            *Info*:             
             global scaling parameter for DFT-D. Default is good for PBE. 



        **london_c6**: List[float]
            *Default*:             standard Grimme-D2 values


            *Info*:             
             atomic C6 coefficient of each atom type 
             
             ( if not specified default values from S. Grimme, J. Comp. Chem. 27, 1787 (2006), 
             doi:10.1002/jcc.20495 are used; see file Modules/mm_dispersion.f90 ) 


            *Others*:             Start - 1; End - ntyp



        **london_rvdw**: List[float]
            *Default*:             standard Grimme-D2 values


            *Info*:             
             atomic vdw radii of each atom type 
             
             ( if not specified default values from S. Grimme, J. Comp. Chem. 27, 1787 (2006), 
             doi:10.1002/jcc.20495 are used; see file Modules/mm_dispersion.f90 ) 


            *Others*:             Start - 1; End - ntyp



        **london_rcut**: float
            *Default*:             200


            *Info*:             
             cutoff radius (a.u.) for dispersion interactions 



        **dftd3_version**: Dftd3VersionOptions
            *Default*:             3



        **dftd3_threebody**: bool
            *Default*:             TRUE


            *Info*:             
             Turn three-body terms in Grimme-D3 on. If .false. two-body contributions 
             only are computed, using two-body parameters of Grimme-D3. 
             If dftd3_version=2, three-body contribution is always disabled. 



        **ts_vdw_econv_thr**: float
            *Default*:             1.D-6


            *Info*:             
             Optional: controls the convergence of the vdW energy (and forces). The default value 
             is a safe choice, likely too safe, but you do not gain much in increasing it 



        **ts_vdw_isolated**: bool
            *Default*:             .FALSE.


            *Info*:             
             Optional: set it to .TRUE. when computing the Tkatchenko-Scheffler vdW energy 
             for an isolated (non-periodic) system. 



        **xdm**: bool
            *Default*:             .FALSE.



        **xdm_a1**: float
            *Default*:             0.6836


            *Info*:             
             Damping function parameter a1 (adimensional). It is NOT necessary to give 
             a value if the functional is one of B86bPBE, PW86PBE, PBE, BLYP. For functionals 
             in this list, the coefficients are given in: 
             http://schooner.chem.dal.ca/wiki/XDM 
             A. Otero de la Roza, E. R. Johnson, J. Chem. Phys. 138, 204109 (2013), 
             doi:10.1063/1.4705760 



        **xdm_a2**: float
            *Default*:             1.5045


            *Info*:             
             Damping function parameter a2 (angstrom). It is NOT necessary to give 
             a value if the functional is one of B86bPBE, PW86PBE, PBE, BLYP. For functionals 
             in this list, the coefficients are given in: 
             http://schooner.chem.dal.ca/wiki/XDM 
             A. Otero de la Roza, E. R. Johnson, J. Chem. Phys. 138, 204109 (2013), 
             doi:10.1063/1.4705760 



        **space_group**: int
            *Default*:             0


            *Info*:             
             The number of the space group of the crystal, as given 
             in the International Tables of Crystallography A (ITA). 
             This allows to give in input only the inequivalent atomic 
             positions. The positions of all the symmetry equivalent atoms 
             are calculated by the code. Used only when the atomic positions 
             are of type crystal_sg. See also ~uniqueb,~ 
             ~origin_choice,~ ~rhombohedral~ 



        **uniqueb**: bool
            *Default*:             .FALSE.


            *Info*:             
             Used only for monoclinic lattices. If .TRUE. the b 
             unique ibrav (-12 or -13) are used, and symmetry 
             equivalent positions are chosen assuming that the 
             two fold axis or the mirror normal is parallel to the 
             b axis. If .FALSE. it is parallel to the c axis. 



        **origin_choice**: int
            *Default*:             1


            *Info*:             
             Used only for space groups that in the ITA allow 
             the use of two different origins. origin_choice=1, 
             means the first origin, while origin_choice=2 is the 
             second origin. 



        **rhombohedral**: bool
            *Default*:             .TRUE.


            *Info*:             
             Used only for rhombohedral space groups. 
             When .TRUE. the coordinates of the inequivalent atoms are 
             given with respect to the rhombohedral axes, when .FALSE. 
             the coordinates of the inequivalent atoms are given with 
             respect to the hexagonal axes. They are converted internally 
             to the rhombohedral axes and ~ibrav=5~ is used in both cases. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._ibrav: Optional[int] = ibrav
        self._nat: Optional[int] = nat
        self._ntyp: Optional[int] = ntyp
        self._nbnd: Optional[int] = nbnd
        self._tot_charge: Optional[float] = tot_charge
        self._starting_charge: Optional[List[float]] = starting_charge
        self._tot_magnetization: Optional[float] = tot_magnetization
        self._starting_magnetization: Optional[List[float]] = starting_magnetization
        self._ecutwfc: Optional[float] = ecutwfc
        self._ecutrho: Optional[float] = ecutrho
        self._ecutfock: Optional[float] = ecutfock
        self._nr1: Optional[int] = nr1
        self._nr2: Optional[int] = nr2
        self._nr3: Optional[int] = nr3
        self._nr1s: Optional[int] = nr1s
        self._nr2s: Optional[int] = nr2s
        self._nr3s: Optional[int] = nr3s
        self._nosym: Optional[bool] = nosym
        self._nosym_evc: Optional[bool] = nosym_evc
        self._noinv: Optional[bool] = noinv
        self._no_t_rev: Optional[bool] = no_t_rev
        self._force_symmorphic: Optional[bool] = force_symmorphic
        self._use_all_frac: Optional[bool] = use_all_frac
        self._occupations: Optional[OccupationsOptions] = occupations
        self._one_atom_occupations: Optional[bool] = one_atom_occupations
        self._starting_spin_angle: Optional[bool] = starting_spin_angle
        self._degauss: Optional[float] = degauss
        self._smearing: Optional[SmearingOptions] = smearing
        self._nspin: Optional[int] = nspin
        self._noncolin: Optional[bool] = noncolin
        self._ecfixed: Optional[float] = ecfixed
        self._qcutz: Optional[float] = qcutz
        self._q2sigma: Optional[float] = q2sigma
        self._input_dft: Optional[str] = input_dft
        self._ace: Optional[bool] = ace
        self._exx_fraction: Optional[float] = exx_fraction
        self._screening_parameter: Optional[float] = screening_parameter
        self._exxdiv_treatment: Optional[ExxdivTreatmentOptions] = exxdiv_treatment
        self._x_gamma_extrapolation: Optional[bool] = x_gamma_extrapolation
        self._ecutvcut: Optional[float] = ecutvcut
        self._nqx1: Optional[int] = nqx1
        self._nqx2: Optional[int] = nqx2
        self._nqx3: Optional[int] = nqx3
        self._localization_thr: Optional[float] = localization_thr
        self._lda_plus_u: Optional[bool] = lda_plus_u
        self._lda_plus_u_kind: Optional[int] = lda_plus_u_kind
        self._hubbard_u: Optional[List[float]] = hubbard_u
        self._hubbard_j0: Optional[List[float]] = hubbard_j0
        self._hubbard_v: Optional[List[float]] = hubbard_v
        self._hubbard_alpha: Optional[List[float]] = hubbard_alpha
        self._hubbard_beta: Optional[List[float]] = hubbard_beta
        self._hubbard_j: Optional[List[float]] = hubbard_j
        self._starting_ns_eigenvalue: Optional[List[float]] = starting_ns_eigenvalue
        self._U_projection_type: Optional[UProjectionTypeOptions] = U_projection_type
        self._Hubbard_parameters: Optional[HubbardParametersOptions] = Hubbard_parameters
        self._ensemble_energies: Optional[bool] = ensemble_energies
        self._edir: Optional[int] = edir
        self._emaxpos: Optional[float] = emaxpos
        self._eopreg: Optional[float] = eopreg
        self._eamp: Optional[float] = eamp
        self._angle1: Optional[List[float]] = angle1
        self._angle2: Optional[List[float]] = angle2
        self._lforcet: Optional[bool] = lforcet
        self._constrained_magnetization: Optional[ConstrainedMagnetizationOptions] = constrained_magnetization
        self._fixed_magnetization: Optional[List[float]] = fixed_magnetization
        self._lambda_is_a_python_keyword: Optional[float] = lambda_is_a_python_keyword
        self._report: Optional[int] = report
        self._lspinorb: Optional[bool] = lspinorb
        self._assume_isolated: Optional[AssumeIsolatedOptions] = assume_isolated
        self._esm_bc: Optional[EsmBcOptions] = esm_bc
        self._esm_w: Optional[float] = esm_w
        self._esm_efield: Optional[float] = esm_efield
        self._esm_nfit: Optional[int] = esm_nfit
        self._fcp_mu: Optional[float] = fcp_mu
        self._vdw_corr: Optional[VdwCorrOptions] = vdw_corr
        self._london: Optional[bool] = london
        self._london_s6: Optional[float] = london_s6
        self._london_c6: Optional[List[float]] = london_c6
        self._london_rvdw: Optional[List[float]] = london_rvdw
        self._london_rcut: Optional[float] = london_rcut
        self._dftd3_version: Optional[Dftd3VersionOptions] = dftd3_version
        self._dftd3_threebody: Optional[bool] = dftd3_threebody
        self._ts_vdw_econv_thr: Optional[float] = ts_vdw_econv_thr
        self._ts_vdw_isolated: Optional[bool] = ts_vdw_isolated
        self._xdm: Optional[bool] = xdm
        self._xdm_a1: Optional[float] = xdm_a1
        self._xdm_a2: Optional[float] = xdm_a2
        self._space_group: Optional[int] = space_group
        self._uniqueb: Optional[bool] = uniqueb
        self._origin_choice: Optional[int] = origin_choice
        self._rhombohedral: Optional[bool] = rhombohedral

    @property
    def ibrav(self) -> int:
        """
        Info:
        ================
        
         Bravais-lattice index. Optional only if space_group is set. 
         If ibrav /= 0, specify EITHER [ ~celldm(1)-~ ~celldm(6)~ ] 
         OR [ ~A,~ ~B,~ ~C,~ ~cosAB,~ ~cosAC,~ ~cosBC~ ] 
         but NOT both. The lattice parameter "alat" is set to 
         alat = celldm(1) (in a.u.) or alat = A (in Angstrom); 
         see below for the other parameters. 
         For ibrav=0 specify the lattice vectors in ~CELL_PARAMETERS,~ 
         optionally the lattice parameter alat = celldm(1) (in a.u.) 
         or = A (in Angstrom). If not specified, the lattice parameter is 
         taken from ~CELL_PARAMETERS~ 
         IMPORTANT NOTICE 1: 
         with ibrav=0 lattice vectors must be given with a sufficiently large 
         number of digits and with the correct symmetry, or else symmetry 
         detection may fail and strange problems may arise in symmetrization. 
         IMPORTANT NOTICE 2: 
         do not use celldm(1) or A as a.u. to Ang conversion factor, 
         use the true lattice parameters or nothing, 
         specify units in ~CELL_PARAMETERS~ and ~ATOMIC_POSITIONS~ 
         
         ibrav structure celldm(2)-celldm(6) 
         or: b,c,cosbc,cosac,cosab 
         0 free 
         crystal axis provided in input: see card ~CELL_PARAMETERS~ 
         
         1 cubic P (sc) 
         v1 = a(1,0,0), v2 = a(0,1,0), v3 = a(0,0,1) 
         
         2 cubic F (fcc) 
         v1 = (a/2)(-1,0,1), v2 = (a/2)(0,1,1), v3 = (a/2)(-1,1,0) 
         
         3 cubic I (bcc) 
         v1 = (a/2)(1,1,1), v2 = (a/2)(-1,1,1), v3 = (a/2)(-1,-1,1) 
         -3 cubic I (bcc), more symmetric axis: 
         v1 = (a/2)(-1,1,1), v2 = (a/2)(1,-1,1), v3 = (a/2)(1,1,-1) 
         
         4 Hexagonal and Trigonal P celldm(3)=c/a 
         v1 = a(1,0,0), v2 = a(-1/2,sqrt(3)/2,0), v3 = a(0,0,c/a) 
         
         5 Trigonal R, 3fold axis c celldm(4)=cos(gamma) 
         The crystallographic vectors form a three-fold star around 
         the z-axis, the primitive cell is a simple rhombohedron: 
         v1 = a(tx,-ty,tz), v2 = a(0,2ty,tz), v3 = a(-tx,-ty,tz) 
         where c=cos(gamma) is the cosine of the angle gamma between 
         any pair of crystallographic vectors, tx, ty, tz are: 
         tx=sqrt((1-c)/2), ty=sqrt((1-c)/6), tz=sqrt((1+2c)/3) 
         -5 Trigonal R, 3fold axis <111> celldm(4)=cos(gamma) 
         The crystallographic vectors form a three-fold star around 
         <111>. Defining a' = a/sqrt(3) : 
         v1 = a' (u,v,v), v2 = a' (v,u,v), v3 = a' (v,v,u) 
         where u and v are defined as 
         u = tz - 2*sqrt(2)*ty, v = tz + sqrt(2)*ty 
         and tx, ty, tz as for case ibrav=5 
         Note: if you prefer x,y,z as axis in the cubic limit, 
         set u = tz + 2*sqrt(2)*ty, v = tz - sqrt(2)*ty 
         See also the note in Modules/latgen.f90 
         
         6 Tetragonal P (st) celldm(3)=c/a 
         v1 = a(1,0,0), v2 = a(0,1,0), v3 = a(0,0,c/a) 
         
         7 Tetragonal I (bct) celldm(3)=c/a 
         v1=(a/2)(1,-1,c/a), v2=(a/2)(1,1,c/a), v3=(a/2)(-1,-1,c/a) 
         
         8 Orthorhombic P celldm(2)=b/a 
         celldm(3)=c/a 
         v1 = (a,0,0), v2 = (0,b,0), v3 = (0,0,c) 
         
         9 Orthorhombic base-centered(bco) celldm(2)=b/a 
         celldm(3)=c/a 
         v1 = (a/2, b/2,0), v2 = (-a/2,b/2,0), v3 = (0,0,c) 
         -9 as 9, alternate description 
         v1 = (a/2,-b/2,0), v2 = (a/2, b/2,0), v3 = (0,0,c) 
         91 Orthorhombic one-face base-centered A-type 
         celldm(2)=b/a 
         celldm(3)=c/a 
         v1 = (a, 0, 0), v2 = (0,b/2,-c/2), v3 = (0,b/2,c/2) 
         
         10 Orthorhombic face-centered celldm(2)=b/a 
         celldm(3)=c/a 
         v1 = (a/2,0,c/2), v2 = (a/2,b/2,0), v3 = (0,b/2,c/2) 
         
         11 Orthorhombic body-centered celldm(2)=b/a 
         celldm(3)=c/a 
         v1=(a/2,b/2,c/2), v2=(-a/2,b/2,c/2), v3=(-a/2,-b/2,c/2) 
         
         12 Monoclinic P, unique axis c celldm(2)=b/a 
         celldm(3)=c/a, 
         celldm(4)=cos(ab) 
         v1=(a,0,0), v2=(b*cos(gamma),b*sin(gamma),0), v3 = (0,0,c) 
         where gamma is the angle between axis a and b. 
         -12 Monoclinic P, unique axis b celldm(2)=b/a 
         celldm(3)=c/a, 
         celldm(5)=cos(ac) 
         v1 = (a,0,0), v2 = (0,b,0), v3 = (c*cos(beta),0,c*sin(beta)) 
         where beta is the angle between axis a and c 
         
         13 Monoclinic base-centered celldm(2)=b/a 
         (unique axis c) celldm(3)=c/a, 
         celldm(4)=cos(gamma) 
         v1 = ( a/2, 0, -c/2), 
         v2 = (b*cos(gamma), b*sin(gamma), 0 ), 
         v3 = ( a/2, 0, c/2), 
         where gamma=angle between axis a and b projected on xy plane 
         
         -13 Monoclinic base-centered celldm(2)=b/a 
         (unique axis b) celldm(3)=c/a, 
         celldm(5)=cos(beta) 
         v1 = ( a/2, b/2, 0), 
         v2 = ( -a/2, b/2, 0), 
         v3 = (c*cos(beta), 0, c*sin(beta)), 
         where beta=angle between axis a and c projected on xz plane 
         IMPORTANT NOTICE: until QE v.6.4.1, axis for ibrav=-13 had a 
         different definition: v1(old) =-v2(now), v2(old) = v1(now) 
         
         14 Triclinic celldm(2)= b/a, 
         celldm(3)= c/a, 
         celldm(4)= cos(bc), 
         celldm(5)= cos(ac), 
         celldm(6)= cos(ab) 
         v1 = (a, 0, 0), 
         v2 = (b*cos(gamma), b*sin(gamma), 0) 
         v3 = (c*cos(beta), c*(cos(alpha)-cos(beta)cos(gamma))/sin(gamma), 
         c*sqrt( 1 + 2*cos(alpha)cos(beta)cos(gamma) 
         - cos(alpha)^2-cos(beta)^2-cos(gamma)^2 )/sin(gamma) ) 
         where alpha is the angle between axis b and c 
         beta is the angle between axis a and c 
         gamma is the angle between axis a and b 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ibrav

    @ibrav.setter
    def ibrav(self, value: int):
        self._ibrav = value

    @property
    def nat(self) -> int:
        """
        Info:
        ================
        
         number of atoms in the unit cell (ALL atoms, except if 
         space_group is set, in which case, INEQUIVALENT atoms) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nat

    @nat.setter
    def nat(self, value: int):
        self._nat = value

    @property
    def ntyp(self) -> int:
        """
        Info:
        ================
        
         number of types of atoms in the unit cell 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ntyp

    @ntyp.setter
    def ntyp(self, value: int):
        self._ntyp = value

    @property
    def nbnd(self) -> int:
        """
        Default:
        ================
        
         for an insulator, ~nbnd~ = number of valence bands 
         ( ~nbnd~ = # of electrons /2); 
         **r** for a metal, 20% more (minimum 4 more) 


        Info:
        ================
        
         Number of electronic states (bands) to be calculated. 
         Note that in spin-polarized calculations the number of 
         k-point, not the number of bands per k-point, is doubled 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nbnd

    @nbnd.setter
    def nbnd(self, value: int):
        self._nbnd = value

    @property
    def tot_charge(self) -> float:
        """
        Default:
        ================
        0.0


        Info:
        ================
        
         Total charge of the system. Useful for simulations with charged cells. 
         By default the unit cell is assumed to be neutral (tot_charge=0). 
         tot_charge=+1 means one electron missing from the system, 
         tot_charge=-1 means one additional electron, and so on. 
         
         In a periodic calculation a compensating jellium background is 
         inserted to remove divergences if the cell is not neutral. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tot_charge

    @tot_charge.setter
    def tot_charge(self, value: float):
        self._tot_charge = value

    @property
    def starting_charge(self) -> List[float]:
        """
        Default:
        ================
        0.0


        Info:
        ================
        
         starting charge on atomic type 'i', 
         to create starting potential with ~startingpot~ = 'atomic'. 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._starting_charge

    @starting_charge.setter
    def starting_charge(self, value: List[float]):
        self._starting_charge = value

    @property
    def tot_magnetization(self) -> float:
        """
        Default:
        ================
        -1 [unspecified]


        Info:
        ================
        
         Total majority spin charge - minority spin charge. 
         Used to impose a specific total electronic magnetization. 
         If unspecified then tot_magnetization variable is ignored and 
         the amount of electronic magnetization is determined during 
         the self-consistent cycle. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tot_magnetization

    @tot_magnetization.setter
    def tot_magnetization(self, value: float):
        self._tot_magnetization = value

    @property
    def starting_magnetization(self) -> List[float]:
        """
        Info:
        ================
        
         Starting spin polarization on atomic type 'i' in a spin 
                        polarized calculation. Values range between -1 (all spins
                        down for the valence electrons of atom type 'i' ) to 1 
         (all spins up). Breaks the symmetry and provides a starting 
         point for self-consistency. The default value is zero, BUT a 
         value MUST be specified for AT LEAST one atomic type in spin 
         polarized calculations, unless you constrain the magnetization 
         (see ~tot_magnetization~ and ~constrained_magnetization).~ 
         Note that if you start from zero initial magnetization, you 
         will invariably end up in a nonmagnetic (zero magnetization) 
         state. If you want to start from an antiferromagnetic state, 
         you may need to define two different atomic species 
         corresponding to sublattices of the same atomic type. 
         starting_magnetization is ignored if you are performing a 
         non-scf calculation, if you are restarting from a previous 
         run, or restarting from an interrupted run. 
         If you fix the magnetization with ~tot_magnetization,~ 
         you should not specify starting_magnetization. 
         In the spin-orbit case starting with zero 
         starting_magnetization on all atoms imposes time reversal 
         symmetry. The magnetization is never calculated and 
         kept zero (the internal variable domag is .FALSE.). 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._starting_magnetization

    @starting_magnetization.setter
    def starting_magnetization(self, value: List[float]):
        self._starting_magnetization = value

    @property
    def ecutwfc(self) -> float:
        """
        Info:
        ================
        
         kinetic energy cutoff (Ry) for wavefunctions 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ecutwfc

    @ecutwfc.setter
    def ecutwfc(self, value: float):
        self._ecutwfc = value

    @property
    def ecutrho(self) -> float:
        """
        Default:
        ================
        4 * ~ecutwfc~


        Info:
        ================
        
         Kinetic energy cutoff (Ry) for charge density and potential 
         For norm-conserving pseudopotential you should stick to the 
         default value, you can reduce it by a little but it will 
         introduce noise especially on forces and stress. 
         If there are ultrasoft PP, a larger value than the default is 
         often desirable (ecutrho = 8 to 12 times ~ecutwfc,~ typically). 
         PAW datasets can often be used at 4* ~ecutwfc,~ but it depends 
         on the shape of augmentation charge: testing is mandatory. 
         The use of gradient-corrected functional, especially in cells 
         with vacuum, or for pseudopotential without non-linear core 
         correction, usually requires an higher values of ecutrho 
         to be accurately converged. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ecutrho

    @ecutrho.setter
    def ecutrho(self, value: float):
        self._ecutrho = value

    @property
    def ecutfock(self) -> float:
        """
        Default:
        ================
        ecutrho


        Info:
        ================
        
         Kinetic energy cutoff (Ry) for the exact exchange operator in 
         EXX type calculations. By default this is the same as ~ecutrho~ 
         but in some EXX calculations, a significant speed-up can be obtained 
         by reducing ecutfock, at the expense of some loss in accuracy. 
         Must be .gt. ~ecutwfc.~ Not implemented for stress calculation 
         and for US-PP and PAW pseudopotentials. 
         Use with care, especially in metals where it may give raise 
         to instabilities. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ecutfock

    @ecutfock.setter
    def ecutfock(self, value: float):
        self._ecutfock = value

    @property
    def nr1(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional FFT mesh (hard grid) for charge 
         density (and scf potential). If not specified 
         the grid is calculated based on the cutoff for 
         charge density (see also ~ecutrho)~ 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr1

    @nr1.setter
    def nr1(self, value: int):
        self._nr1 = value

    @property
    def nr2(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional FFT mesh (hard grid) for charge 
         density (and scf potential). If not specified 
         the grid is calculated based on the cutoff for 
         charge density (see also ~ecutrho)~ 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr2

    @nr2.setter
    def nr2(self, value: int):
        self._nr2 = value

    @property
    def nr3(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional FFT mesh (hard grid) for charge 
         density (and scf potential). If not specified 
         the grid is calculated based on the cutoff for 
         charge density (see also ~ecutrho)~ 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr3

    @nr3.setter
    def nr3(self, value: int):
        self._nr3 = value

    @property
    def nr1s(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for wavefunction FFT and for the smooth 
         part of charge density ( smooth grid ). 
         Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr1s

    @nr1s.setter
    def nr1s(self, value: int):
        self._nr1s = value

    @property
    def nr2s(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for wavefunction FFT and for the smooth 
         part of charge density ( smooth grid ). 
         Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr2s

    @nr2s.setter
    def nr2s(self, value: int):
        self._nr2s = value

    @property
    def nr3s(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for wavefunction FFT and for the smooth 
         part of charge density ( smooth grid ). 
         Coincides with ~nr1,~ ~nr2,~ ~nr3~ if ~ecutrho~ = 4 * ecutwfc ( default ) 
         Note: you must specify all three dimensions for this setting to 
         be used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nr3s

    @nr3s.setter
    def nr3s(self, value: int):
        self._nr3s = value

    @property
    def nosym(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.TRUE.) symmetry is not used. Consequences: 
         
         - if a list of k points is provided in input, it is used 
         "as is": symmetry-inequivalent k-points are not generated, 
         and the charge density is not symmetrized; 
         
         - if a uniform (Monkhorst-Pack) k-point grid is provided in 
         input, it is expanded to cover the entire Brillouin Zone, 
         irrespective of the crystal symmetry. 
         Time reversal symmetry is assumed so k and -k are considered 
         as equivalent unless ~noinv=.true.~ is specified. 
         
         Do not use this option unless you know exactly what you want 
         and what you get. May be useful in the following cases: 
         - in low-symmetry large cells, if you cannot afford a k-point 
         grid with the correct symmetry 
         - in MD simulations 
         - in calculations for isolated atoms 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nosym

    @nosym.setter
    def nosym(self, value: bool):
        self._nosym = value

    @property
    def nosym_evc(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.TRUE.) symmetry is not used, and k points are 
         forced to have the symmetry of the Bravais lattice; 
         an automatically generated Monkhorst-Pack grid will contain 
         all points of the grid over the entire Brillouin Zone, 
         plus the points rotated by the symmetries of the Bravais 
         lattice which were not in the original grid. The same 
         applies if a k-point list is provided in input instead 
         of a Monkhorst-Pack grid. Time reversal symmetry is assumed 
         so k and -k are equivalent unless ~noinv=.true.~ is specified. 
         This option differs from ~nosym~ because it forces k-points 
         in all cases to have the full symmetry of the Bravais lattice 
         (not all uniform grids have such property!) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nosym_evc

    @nosym_evc.setter
    def nosym_evc(self, value: bool):
        self._nosym_evc = value

    @property
    def noinv(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.TRUE.) disable the usage of k => -k symmetry 
         (time reversal) in k-point generation 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._noinv

    @noinv.setter
    def noinv(self, value: bool):
        self._noinv = value

    @property
    def no_t_rev(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.TRUE.) disable the usage of magnetic symmetry operations 
         that consist in a rotation + time reversal. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._no_t_rev

    @no_t_rev.setter
    def no_t_rev(self, value: bool):
        self._no_t_rev = value

    @property
    def force_symmorphic(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.TRUE.) force the symmetry group to be symmorphic by disabling 
         symmetry operations having an associated fractionary translation 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._force_symmorphic

    @force_symmorphic.setter
    def force_symmorphic(self, value: bool):
        self._force_symmorphic = value

    @property
    def use_all_frac(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         if (.FALSE.) force real-space FFT grids to be commensurate with 
         fractionary translations of non-symmorphic symmetry operations, 
         if present (e.g.: if a fractional translation (0,0,c/4) exists, 
         the FFT dimension along the c axis must be multiple of 4). 
         if (.TRUE.) do not impose any constraints to FFT grids, even in 
         the presence of non-symmorphic symmetry operations. 
         BEWARE: use_all_frac=.TRUE. may lead to wrong results for 
         hybrid functionals and phonon calculations. Both cases use 
         symmetrization in real space that works for non-symmorphic 
         operations only if the real-space FFT grids are commensurate. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._use_all_frac

    @use_all_frac.setter
    def use_all_frac(self, value: bool):
        self._use_all_frac = value

    @property
    def occupations(self) -> OccupationsOptions:
        """
        """
        return self._occupations

    @occupations.setter
    def occupations(self, value: OccupationsOptions):
        self._occupations = value

    @property
    def one_atom_occupations(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         This flag is used for isolated atoms ( ~nat=1)~ together with 
         ~occupations='from_input'.~ If it is .TRUE., the wavefunctions 
         are ordered as the atomic starting wavefunctions, independently 
         from their eigenvalue. The occupations indicate which atomic 
         states are filled. 
         
         The order of the states is written inside the UPF pseudopotential file. 
         In the scalar relativistic case: 
         S -> l=0, m=0 
         P -> l=1, z, x, y 
         D -> l=2, r^2-3z^2, xz, yz, xy, x^2-y^2 
         
         In the noncollinear magnetic case (with or without spin-orbit), 
         each group of states is doubled. For instance: 
         P -> l=1, z, x, y for spin up, l=1, z, x, y for spin down. 
         Up and down is relative to the direction of the starting 
         magnetization. 
         
         In the case with spin-orbit and time-reversal 
         ( ~starting_magnetization=0.0)~ the atomic wavefunctions are 
         radial functions multiplied by spin-angle functions. 
         For instance: 
         P -> l=1, j=1/2, m_j=-1/2,1/2. l=1, j=3/2, 
         m_j=-3/2, -1/2, 1/2, 3/2. 
         
         In the magnetic case with spin-orbit the atomic wavefunctions 
         can be forced to be spin-angle functions by setting 
         ~starting_spin_angle~ to .TRUE.. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._one_atom_occupations

    @one_atom_occupations.setter
    def one_atom_occupations(self, value: bool):
        self._one_atom_occupations = value

    @property
    def starting_spin_angle(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         In the spin-orbit case when ~domag=.TRUE.,~ by default, 
         the starting wavefunctions are initialized as in scalar 
         relativistic noncollinear case without spin-orbit. 
         
         By setting ~starting_spin_angle=.TRUE.~ this behaviour can 
         be changed and the initial wavefunctions are radial 
         functions multiplied by spin-angle functions. 
         
         When ~domag=.FALSE.~ the initial wavefunctions are always 
         radial functions multiplied by spin-angle functions 
         independently from this flag. 
         
         When ~lspinorb~ is .FALSE. this flag is not used. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._starting_spin_angle

    @starting_spin_angle.setter
    def starting_spin_angle(self, value: bool):
        self._starting_spin_angle = value

    @property
    def degauss(self) -> float:
        """
        Default:
        ================
        0.D0 Ry


        Info:
        ================
        
         value of the gaussian spreading (Ry) for brillouin-zone 
         integration in metals. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._degauss

    @degauss.setter
    def degauss(self, value: float):
        self._degauss = value

    @property
    def smearing(self) -> SmearingOptions:
        """
        Default:
        ================
        'gaussian'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._smearing

    @smearing.setter
    def smearing(self, value: SmearingOptions):
        self._smearing = value

    @property
    def nspin(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         nspin = 1 : non-polarized calculation (default) 
         
         nspin = 2 : spin-polarized calculation, LSDA 
         (magnetization along z axis) 
         
         nspin = 4 : spin-polarized calculation, noncollinear 
         (magnetization in generic direction) 
         DO NOT specify ~nspin~ in this case; 
         specify ~noncolin=.TRUE.~ instead 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nspin

    @nspin.setter
    def nspin(self, value: int):
        self._nspin = value

    @property
    def noncolin(self) -> bool:
        """
        Default:
        ================
        .false.


        Info:
        ================
        
         if .true. the program will perform a noncollinear calculation. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._noncolin

    @noncolin.setter
    def noncolin(self, value: bool):
        self._noncolin = value

    @property
    def ecfixed(self) -> float:
        """
        Default:
        ================
        0.0



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ecfixed

    @ecfixed.setter
    def ecfixed(self, value: float):
        self._ecfixed = value

    @property
    def qcutz(self) -> float:
        """
        Default:
        ================
        0.0



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._qcutz

    @qcutz.setter
    def qcutz(self, value: float):
        self._qcutz = value

    @property
    def q2sigma(self) -> float:
        """
        Default:
        ================
        0.1


        Info:
        ================
        
         ecfixed, qcutz, q2sigma: parameters for modified functional to be 
         used in variable-cell molecular dynamics (or in stress calculation). 
         "ecfixed" is the value (in Rydberg) of the constant-cutoff; 
         "qcutz" and "q2sigma" are the height and the width (in Rydberg) 
         of the energy step for reciprocal vectors whose square modulus 
         is greater than "ecfixed". In the kinetic energy, G^2 is 
         replaced by G^2 + qcutz * (1 + erf ( (G^2 - ecfixed)/q2sigma) ) 
         See: M. Bernasconi et al, J. Phys. Chem. Solids 56, 501 (1995), 
         doi:10.1016/0022-3697(94)00228-2 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._q2sigma

    @q2sigma.setter
    def q2sigma(self, value: float):
        self._q2sigma = value

    @property
    def input_dft(self) -> str:
        """
        Default:
        ================
        read from pseudopotential files


        Info:
        ================
        
         Exchange-correlation functional: eg 'PBE', 'BLYP' etc 
         See Modules/funct.f90 for allowed values. 
         Overrides the value read from pseudopotential files. 
         Use with care and if you know what you are doing! 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._input_dft

    @input_dft.setter
    def input_dft(self, value: str):
        self._input_dft = value

    @property
    def ace(self) -> bool:
        """
        Default:
        ================
        true


        Info:
        ================
        
         Use Adaptively Compressed Exchange operator as in 
         Lin Lin, J. Chem. Theory Comput. 2016, 12, 2242--2249, doi:10.1021/acs.jctc.6b00092 
         
         Set to false to use standard Exchange (much slower) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ace

    @ace.setter
    def ace(self, value: bool):
        self._ace = value

    @property
    def exx_fraction(self) -> float:
        """
        Default:
        ================
        it depends on the specified functional


        Info:
        ================
        
         Fraction of EXX for hybrid functional calculations. In the case of 
         ~input_dft='PBE0',~ the default value is 0.25, while for ~input_dft='B3LYP'~ 
         the ~exx_fraction~ default value is 0.20. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._exx_fraction

    @exx_fraction.setter
    def exx_fraction(self, value: float):
        self._exx_fraction = value

    @property
    def screening_parameter(self) -> float:
        """
        Default:
        ================
        0.106


        Info:
        ================
        
         screening_parameter for HSE like hybrid functionals. 
         For more information, see: 
         J. Chem. Phys. 118, 8207 (2003), doi:10.1063/1.1564060 
         J. Chem. Phys. 124, 219906 (2006), doi:10.1063/1.2204597 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._screening_parameter

    @screening_parameter.setter
    def screening_parameter(self, value: float):
        self._screening_parameter = value

    @property
    def exxdiv_treatment(self) -> ExxdivTreatmentOptions:
        """
        Default:
        ================
        'gygi-baldereschi'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._exxdiv_treatment

    @exxdiv_treatment.setter
    def exxdiv_treatment(self, value: ExxdivTreatmentOptions):
        self._exxdiv_treatment = value

    @property
    def x_gamma_extrapolation(self) -> bool:
        """
        Default:
        ================
        .true.


        Info:
        ================
        
         Specific for EXX. If .true., extrapolate the G=0 term of the 
         potential (see README in examples/EXX_example for more) 
         Set this to .false. for GAU-PBE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._x_gamma_extrapolation

    @x_gamma_extrapolation.setter
    def x_gamma_extrapolation(self, value: bool):
        self._x_gamma_extrapolation = value

    @property
    def ecutvcut(self) -> float:
        """
        Default:
        ================
        0.0 Ry


        Info:
        ================
        
         Reciprocal space cutoff for correcting Coulomb potential 
         divergencies at small q vectors. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ecutvcut

    @ecutvcut.setter
    def ecutvcut(self, value: float):
        self._ecutvcut = value

    @property
    def nqx1(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for q (k1-k2) sampling of 
         the Fock operator (EXX). Can be smaller than 
         the number of k-points. 
         
         Currently this defaults to the size of the k-point mesh used. 
         In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nqx1

    @nqx1.setter
    def nqx1(self, value: int):
        self._nqx1 = value

    @property
    def nqx2(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for q (k1-k2) sampling of 
         the Fock operator (EXX). Can be smaller than 
         the number of k-points. 
         
         Currently this defaults to the size of the k-point mesh used. 
         In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nqx2

    @nqx2.setter
    def nqx2(self, value: int):
        self._nqx2 = value

    @property
    def nqx3(self) -> int:
        """
        Info:
        ================
        
         Three-dimensional mesh for q (k1-k2) sampling of 
         the Fock operator (EXX). Can be smaller than 
         the number of k-points. 
         
         Currently this defaults to the size of the k-point mesh used. 
         In QE =< 5.0.2 it defaulted to nqx1=nqx2=nqx3=1. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nqx3

    @nqx3.setter
    def nqx3(self, value: int):
        self._nqx3 = value

    @property
    def localization_thr(self) -> float:
        """
        Default:
        ================
        0.0


        Info:
        ================
        
         Overlap threshold over which the exchange integral over a pair of localized orbitals 
         is included in the evaluation of EXX operator. Any value greater than 0.0 triggers 
         the SCDM localization and the evaluation on EXX using the localized orbitals. 
         Very small value of the threshold should yield the same result as the default EXX 
         evaluation



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._localization_thr

    @localization_thr.setter
    def localization_thr(self, value: float):
        self._localization_thr = value

    @property
    def lda_plus_u(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         Specify ~lda_plus_u~ = .TRUE. to enable DFT+U calculations 
         See: Anisimov, Zaanen, and Andersen, PRB 44, 943 (1991); 
         Anisimov et al., PRB 48, 16929 (1993); 
         Liechtenstein, Anisimov, and Zaanen, PRB 52, R5467 (1994). 
         You must specify, for each species with a U term, the value of 
         U and (optionally) alpha, J of the Hubbard model (all in eV): 
         see ~lda_plus_u_kind,~ ~Hubbard_U,~ ~Hubbard_alpha,~ ~Hubbard_J~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lda_plus_u

    @lda_plus_u.setter
    def lda_plus_u(self, value: bool):
        self._lda_plus_u = value

    @property
    def lda_plus_u_kind(self) -> int:
        """
        Default:
        ================
        0


        Info:
        ================
        
         Specifies the type of calculation: 
         
         0 DFT+U simplified version of Cococcioni and de Gironcoli, 
         PRB 71, 035105 (2005), using ~Hubbard_U~ 
         
         1 DFT+U rotationally invariant scheme of Liechtenstein et al., 
         using ~Hubbard_U~ and ~Hubbard_J~ 
         
         2 DFT+U+V simplified version of Campo Jr and Cococcioni, 
         J. Phys.: Condens. Matter 22, 055602 (2010), using ~Hubbard_V~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lda_plus_u_kind

    @lda_plus_u_kind.setter
    def lda_plus_u_kind(self, value: int):
        self._lda_plus_u_kind = value

    @property
    def hubbard_u(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all species


        Info:
        ================
        
         Hubbard_U(i): U parameter (eV) for species i, DFT+U calculation 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_u

    @hubbard_u.setter
    def hubbard_u(self, value: List[float]):
        self._hubbard_u = value

    @property
    def hubbard_j0(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all species


        Info:
        ================
        
         Hubbard_J0(i): J0 parameter (eV) for species i, DFT+U+J calculation, 
         see PRB 84, 115108 (2011) for details. 


        Others:
        ================
        Start - 1; End - ntype

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_j0

    @hubbard_j0.setter
    def hubbard_j0(self, value: List[float]):
        self._hubbard_j0 = value

    @property
    def hubbard_v(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all elements


        Info:
        ================
        
         Hubbard_V(na,nb,k): V parameters (eV) between atoms na and nb, 
         used in DFT+U+V calculations (only for ~lda_plus_u_kind=2).~ 
         The atomic indices na and nb correspond to the atomic positions 
         in the ~ATOMIC_POSITIONS~ card (this is not the same as Hubbard_U 
         which is specified for ~ATOMIC_SPECIES).~ 
         Wnen na=nb, then Hubbard_V(na,na,k) is the on-site Hubbard_U 
         for the atom na. 
         natx=50 (if needed it can be changed in /Modules/parameters.f90) 
         The index k controls the "interaction type" (k=1 is used for the 
         simplest DFT+U+V calculation): 
         k=1 - interaction between standard orbitals (both on na and nb); 
         k=2 - interaction between standard (on na) and background (on nb) orbitals; 
         k=3 - interaction between background orbitlas (both on na and nb); 
         k=4 - interaction between background (on na) and standard (on nb) orbitals. 
         Standard orbitals correspond to the main Hubbard channel (e.g. d electrons 
         in transition metals) and background orbitals correspond to the secondary 
         Hubbard channel (e.g. p electrons in transition metals). 


        Others:
        ================
        Start - 1,1,1; End - natx,27*natx,4

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_v

    @hubbard_v.setter
    def hubbard_v(self, value: List[float]):
        self._hubbard_v = value

    @property
    def hubbard_alpha(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all species


        Info:
        ================
        
         Hubbard_alpha(i) is the perturbation (on atom i, in eV) 
         used to compute U with the linear-response method of 
         Cococcioni and de Gironcoli, PRB 71, 035105 (2005) 
         (only for ~lda_plus_u_kind=0)~ 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_alpha

    @hubbard_alpha.setter
    def hubbard_alpha(self, value: List[float]):
        self._hubbard_alpha = value

    @property
    def hubbard_beta(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all species


        Info:
        ================
        
         Hubbard_beta(i) is the perturbation (on atom i, in eV) 
         used to compute J0 with the linear-response method of 
         Cococcioni and de Gironcoli, PRB 71, 035105 (2005) 
         (only for ~lda_plus_u_kind=0).~ See also 
         PRB 84, 115108 (2011). 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_beta

    @hubbard_beta.setter
    def hubbard_beta(self, value: List[float]):
        self._hubbard_beta = value

    @property
    def hubbard_j(self) -> List[float]:
        """
        Default:
        ================
        0.D0 for all species


        Info:
        ================
        
         Hubbard_J(i,ityp): J parameters (eV) for species ityp, 
         used in DFT+U calculations (only for ~lda_plus_u_kind=1)~ 
         For p orbitals: J = Hubbard_J(1,ityp); 
         For d orbitals: J = Hubbard_J(1,ityp), B = Hubbard_J(2,ityp); 
         For f orbitals: J = Hubbard_J(1,ityp), E2 = Hubbard_J(2,ityp), 
         E3= Hubbard_J(3,ityp). 
         If B or E2 or E3 are not specified or set to 0 they will be 
         calculated from J using atomic ratios. 


        Others:
        ================
        Start - 1,1; End - 3,ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._hubbard_j

    @hubbard_j.setter
    def hubbard_j(self, value: List[float]):
        self._hubbard_j = value

    @property
    def starting_ns_eigenvalue(self) -> List[float]:
        """
        Default:
        ================
        -1.d0 that means NOT SET


        Info:
        ================
        
         In the first iteration of an DFT+U run it overwrites 
         the m-th eigenvalue of the ns occupation matrix for the 
         ispin component of atomic species ityp. 
         For the noncolin case the ispin index runs up to npol. 
         The value lmax is given by the maximum angular momentum 
         number to which the Hubbard U is applied. 
         Leave unchanged eigenvalues that are not set. 
         This is useful to suggest the desired orbital occupations 
         when the default choice takes another path. 


        Others:
        ================
        Start - 1,1,1; End - 2*lmax+1,nspin\ or\ npol,ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._starting_ns_eigenvalue

    @starting_ns_eigenvalue.setter
    def starting_ns_eigenvalue(self, value: List[float]):
        self._starting_ns_eigenvalue = value

    @property
    def U_projection_type(self) -> UProjectionTypeOptions:
        """
        Default:
        ================
        'atomic'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._U_projection_type

    @U_projection_type.setter
    def U_projection_type(self, value: UProjectionTypeOptions):
        self._U_projection_type = value

    @property
    def Hubbard_parameters(self) -> HubbardParametersOptions:
        """
        Default:
        ================
        'input'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._Hubbard_parameters

    @Hubbard_parameters.setter
    def Hubbard_parameters(self, value: HubbardParametersOptions):
        self._Hubbard_parameters = value

    @property
    def ensemble_energies(self) -> bool:
        """
        Default:
        ================
        .false.


        Info:
        ================
        
         If ensemble_energies = .true., an ensemble of xc energies 
         is calculated non-selfconsistently for perturbed 
         exchange-enhancement factors and LDA vs. PBE correlation 
         ratios after each converged electronic ground state 
         calculation. 
         
         Ensemble energies can be analyzed with the 'bee' utility
                        included with libbeef.
        
                        Requires linking against libbeef.
                        input_dft must be set to a BEEF-type functional
                        (e.g. input_dft = 'BEEF-vdW' ) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ensemble_energies

    @ensemble_energies.setter
    def ensemble_energies(self, value: bool):
        self._ensemble_energies = value

    @property
    def edir(self) -> int:
        """
        Info:
        ================
        
         The direction of the electric field or dipole correction is 
         parallel to the bg(:,edir) reciprocal lattice vector, so the 
         potential is constant in planes defined by FFT grid points; 
         ~edir~ = 1, 2 or 3. Used only if ~tefield~ is .TRUE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._edir

    @edir.setter
    def edir(self, value: int):
        self._edir = value

    @property
    def emaxpos(self) -> float:
        """
        Default:
        ================
        0.5D0


        Info:
        ================
        
         Position of the maximum of the saw-like potential along crystal 
         axis ~edir,~ within the unit cell (see below), 0 < emaxpos < 1 
         Used only if ~tefield~ is .TRUE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._emaxpos

    @emaxpos.setter
    def emaxpos(self, value: float):
        self._emaxpos = value

    @property
    def eopreg(self) -> float:
        """
        Default:
        ================
        0.1D0


        Info:
        ================
        
         Zone in the unit cell where the saw-like potential decreases. 
         ( see below, 0 < eopreg < 1 ). Used only if ~tefield~ is .TRUE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._eopreg

    @eopreg.setter
    def eopreg(self, value: float):
        self._eopreg = value

    @property
    def eamp(self) -> float:
        """
        Default:
        ================
        0.001 a.u.


        Info:
        ================
        
         Amplitude of the electric field, in ***Hartree*** a.u.; 
         1 a.u. = 51.4220632*10^10 V/m. Used only if ~tefield==.TRUE.~ 
         The saw-like potential increases with slope ~eamp~ in the 
         region from ( ~emaxpos+~ ~eopreg-1)~ to ( ~emaxpos),~ then decreases 
         to 0 until ( ~emaxpos+~ ~eopreg),~ in units of the crystal 
         vector ~edir.~ Important: the change of slope of this 
         potential must be located in the empty region, or else 
         unphysical forces will result. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._eamp

    @eamp.setter
    def eamp(self, value: float):
        self._eamp = value

    @property
    def angle1(self) -> List[float]:
        """
        Info:
        ================
        
         The angle expressed in degrees between the initial 
         magnetization and the z-axis. For noncollinear calculations 
         only; index i runs over the atom types. 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._angle1

    @angle1.setter
    def angle1(self, value: List[float]):
        self._angle1 = value

    @property
    def angle2(self) -> List[float]:
        """
        Info:
        ================
        
         The angle expressed in degrees between the projection 
         of the initial magnetization on x-y plane and the x-axis. 
         For noncollinear calculations only. 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._angle2

    @angle2.setter
    def angle2(self, value: List[float]):
        self._angle2 = value

    @property
    def lforcet(self) -> bool:
        """
        Info:
        ================
        
         When starting a non collinear calculation using an existing density 
         file from a collinear lsda calculation assumes previous density points in 
         *z* direction and rotates it in the direction described by ~angle1~ and 
         ~angle2~ variables for atomic type 1 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lforcet

    @lforcet.setter
    def lforcet(self, value: bool):
        self._lforcet = value

    @property
    def constrained_magnetization(self) -> ConstrainedMagnetizationOptions:
        """
        Default:
        ================
        'none'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._constrained_magnetization

    @constrained_magnetization.setter
    def constrained_magnetization(self, value: ConstrainedMagnetizationOptions):
        self._constrained_magnetization = value

    @property
    def fixed_magnetization(self) -> List[float]:
        """
        Default:
        ================
        0.d0


        Info:
        ================
        
         total magnetization vector (x,y,z components) to be kept 
         fixed when ~constrained_magnetization=='total'~ 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fixed_magnetization

    @fixed_magnetization.setter
    def fixed_magnetization(self, value: List[float]):
        self._fixed_magnetization = value

    @property
    def lambda_is_a_python_keyword(self) -> float:
        """
        Default:
        ================
        1.d0


        Info:
        ================
        
         parameter used for constrained_magnetization calculations 
         N.B.: if the scf calculation does not converge, try to reduce lambda 
         to obtain convergence, then restart the run with a larger lambda 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lambda_is_a_python_keyword

    @lambda_is_a_python_keyword.setter
    def lambda_is_a_python_keyword(self, value: float):
        self._lambda_is_a_python_keyword = value

    @property
    def report(self) -> int:
        """
        Default:
        ================
        -1


        Info:
        ================
        
         determines when atomic magnetic moments are printed on output: 
         report = 0 never 
         report =-1 at the beginning of the scf and at convergence 
         report = N: as -1, plus every N scf iterations 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._report

    @report.setter
    def report(self, value: int):
        self._report = value

    @property
    def lspinorb(self) -> bool:
        """
        Info:
        ================
        
         if .TRUE. the noncollinear code can use a pseudopotential with 
         spin-orbit. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lspinorb

    @lspinorb.setter
    def lspinorb(self, value: bool):
        self._lspinorb = value

    @property
    def assume_isolated(self) -> AssumeIsolatedOptions:
        """
        Default:
        ================
        'none'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._assume_isolated

    @assume_isolated.setter
    def assume_isolated(self, value: AssumeIsolatedOptions):
        self._assume_isolated = value

    @property
    def esm_bc(self) -> EsmBcOptions:
        """
        Default:
        ================
        'pbc'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._esm_bc

    @esm_bc.setter
    def esm_bc(self, value: EsmBcOptions):
        self._esm_bc = value

    @property
    def esm_w(self) -> float:
        """
        Default:
        ================
        0.d0


        Info:
        ================
        
         If ~assume_isolated~ = 'esm', determines the position offset 
         [in a.u.] of the start of the effective screening region, 
         measured relative to the cell edge. (ESM region begins at 
         z = +/- [L_z/2 + esm_w] ). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._esm_w

    @esm_w.setter
    def esm_w(self, value: float):
        self._esm_w = value

    @property
    def esm_efield(self) -> float:
        """
        Default:
        ================
        0.d0


        Info:
        ================
        
         If ~assume_isolated~ = 'esm' and ~esm_bc~ = 'bc2', gives the 
         magnitude of the electric field [Ry/a.u.] to be applied 
         between semi-infinite ESM electrodes. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._esm_efield

    @esm_efield.setter
    def esm_efield(self, value: float):
        self._esm_efield = value

    @property
    def esm_nfit(self) -> int:
        """
        Default:
        ================
        4


        Info:
        ================
        
         If ~assume_isolated~ = 'esm', gives the number of z-grid points 
         for the polynomial fit along the cell edge. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._esm_nfit

    @esm_nfit.setter
    def esm_nfit(self, value: int):
        self._esm_nfit = value

    @property
    def fcp_mu(self) -> float:
        """
        Default:
        ================
        0.d0


        Info:
        ================
        
         If ~lfcpopt~ = .TRUE., gives the target Fermi energy [Ry]. One can start 
         with appropriate total charge of the system by giving 'tot_charge'. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fcp_mu

    @fcp_mu.setter
    def fcp_mu(self, value: float):
        self._fcp_mu = value

    @property
    def vdw_corr(self) -> VdwCorrOptions:
        """
        Default:
        ================
        'none'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._vdw_corr

    @vdw_corr.setter
    def vdw_corr(self, value: VdwCorrOptions):
        self._vdw_corr = value

    @property
    def london(self) -> bool:
        """
        Default:
        ================
        .FALSE.



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._london

    @london.setter
    def london(self, value: bool):
        self._london = value

    @property
    def london_s6(self) -> float:
        """
        Default:
        ================
        0.75


        Info:
        ================
        
         global scaling parameter for DFT-D. Default is good for PBE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._london_s6

    @london_s6.setter
    def london_s6(self, value: float):
        self._london_s6 = value

    @property
    def london_c6(self) -> List[float]:
        """
        Default:
        ================
        standard Grimme-D2 values


        Info:
        ================
        
         atomic C6 coefficient of each atom type 
         
         ( if not specified default values from S. Grimme, J. Comp. Chem. 27, 1787 (2006), 
         doi:10.1002/jcc.20495 are used; see file Modules/mm_dispersion.f90 ) 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._london_c6

    @london_c6.setter
    def london_c6(self, value: List[float]):
        self._london_c6 = value

    @property
    def london_rvdw(self) -> List[float]:
        """
        Default:
        ================
        standard Grimme-D2 values


        Info:
        ================
        
         atomic vdw radii of each atom type 
         
         ( if not specified default values from S. Grimme, J. Comp. Chem. 27, 1787 (2006), 
         doi:10.1002/jcc.20495 are used; see file Modules/mm_dispersion.f90 ) 


        Others:
        ================
        Start - 1; End - ntyp

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._london_rvdw

    @london_rvdw.setter
    def london_rvdw(self, value: List[float]):
        self._london_rvdw = value

    @property
    def london_rcut(self) -> float:
        """
        Default:
        ================
        200


        Info:
        ================
        
         cutoff radius (a.u.) for dispersion interactions 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._london_rcut

    @london_rcut.setter
    def london_rcut(self, value: float):
        self._london_rcut = value

    @property
    def dftd3_version(self) -> Dftd3VersionOptions:
        """
        Default:
        ================
        3



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._dftd3_version

    @dftd3_version.setter
    def dftd3_version(self, value: Dftd3VersionOptions):
        self._dftd3_version = value

    @property
    def dftd3_threebody(self) -> bool:
        """
        Default:
        ================
        TRUE


        Info:
        ================
        
         Turn three-body terms in Grimme-D3 on. If .false. two-body contributions 
         only are computed, using two-body parameters of Grimme-D3. 
         If dftd3_version=2, three-body contribution is always disabled. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._dftd3_threebody

    @dftd3_threebody.setter
    def dftd3_threebody(self, value: bool):
        self._dftd3_threebody = value

    @property
    def ts_vdw_econv_thr(self) -> float:
        """
        Default:
        ================
        1.D-6


        Info:
        ================
        
         Optional: controls the convergence of the vdW energy (and forces). The default value 
         is a safe choice, likely too safe, but you do not gain much in increasing it 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ts_vdw_econv_thr

    @ts_vdw_econv_thr.setter
    def ts_vdw_econv_thr(self, value: float):
        self._ts_vdw_econv_thr = value

    @property
    def ts_vdw_isolated(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         Optional: set it to .TRUE. when computing the Tkatchenko-Scheffler vdW energy 
         for an isolated (non-periodic) system. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._ts_vdw_isolated

    @ts_vdw_isolated.setter
    def ts_vdw_isolated(self, value: bool):
        self._ts_vdw_isolated = value

    @property
    def xdm(self) -> bool:
        """
        Default:
        ================
        .FALSE.



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xdm

    @xdm.setter
    def xdm(self, value: bool):
        self._xdm = value

    @property
    def xdm_a1(self) -> float:
        """
        Default:
        ================
        0.6836


        Info:
        ================
        
         Damping function parameter a1 (adimensional). It is NOT necessary to give 
         a value if the functional is one of B86bPBE, PW86PBE, PBE, BLYP. For functionals 
         in this list, the coefficients are given in: 
         http://schooner.chem.dal.ca/wiki/XDM 
         A. Otero de la Roza, E. R. Johnson, J. Chem. Phys. 138, 204109 (2013), 
         doi:10.1063/1.4705760 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xdm_a1

    @xdm_a1.setter
    def xdm_a1(self, value: float):
        self._xdm_a1 = value

    @property
    def xdm_a2(self) -> float:
        """
        Default:
        ================
        1.5045


        Info:
        ================
        
         Damping function parameter a2 (angstrom). It is NOT necessary to give 
         a value if the functional is one of B86bPBE, PW86PBE, PBE, BLYP. For functionals 
         in this list, the coefficients are given in: 
         http://schooner.chem.dal.ca/wiki/XDM 
         A. Otero de la Roza, E. R. Johnson, J. Chem. Phys. 138, 204109 (2013), 
         doi:10.1063/1.4705760 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xdm_a2

    @xdm_a2.setter
    def xdm_a2(self, value: float):
        self._xdm_a2 = value

    @property
    def space_group(self) -> int:
        """
        Default:
        ================
        0


        Info:
        ================
        
         The number of the space group of the crystal, as given 
         in the International Tables of Crystallography A (ITA). 
         This allows to give in input only the inequivalent atomic 
         positions. The positions of all the symmetry equivalent atoms 
         are calculated by the code. Used only when the atomic positions 
         are of type crystal_sg. See also ~uniqueb,~ 
         ~origin_choice,~ ~rhombohedral~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._space_group

    @space_group.setter
    def space_group(self, value: int):
        self._space_group = value

    @property
    def uniqueb(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         Used only for monoclinic lattices. If .TRUE. the b 
         unique ibrav (-12 or -13) are used, and symmetry 
         equivalent positions are chosen assuming that the 
         two fold axis or the mirror normal is parallel to the 
         b axis. If .FALSE. it is parallel to the c axis. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._uniqueb

    @uniqueb.setter
    def uniqueb(self, value: bool):
        self._uniqueb = value

    @property
    def origin_choice(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         Used only for space groups that in the ITA allow 
         the use of two different origins. origin_choice=1, 
         means the first origin, while origin_choice=2 is the 
         second origin. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._origin_choice

    @origin_choice.setter
    def origin_choice(self, value: int):
        self._origin_choice = value

    @property
    def rhombohedral(self) -> bool:
        """
        Default:
        ================
        .TRUE.


        Info:
        ================
        
         Used only for rhombohedral space groups. 
         When .TRUE. the coordinates of the inequivalent atoms are 
         given with respect to the rhombohedral axes, when .FALSE. 
         the coordinates of the inequivalent atoms are given with 
         respect to the hexagonal axes. They are converted internally 
         to the rhombohedral axes and ~ibrav=5~ is used in both cases. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._rhombohedral

    @rhombohedral.setter
    def rhombohedral(self, value: bool):
        self._rhombohedral = value

