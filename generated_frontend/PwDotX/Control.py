from typing import Optional, List
from .Namelist import Namelist
from .CalculationOptions import CalculationOptions
from .VerbosityOptions import VerbosityOptions
from .RestartModeOptions import RestartModeOptions
from .DiskIoOptions import DiskIoOptions


class Control(Namelist):
    """
    """

    def __init__(self,
                 calculation: Optional[CalculationOptions] = None,
                 title: Optional[str] = None,
                 verbosity: Optional[VerbosityOptions] = None,
                 restart_mode: Optional[RestartModeOptions] = None,
                 wf_collect: Optional[bool] = None,
                 nstep: Optional[int] = None,
                 iprint: Optional[int] = None,
                 tstress: Optional[bool] = None,
                 tprnfor: Optional[bool] = None,
                 dt: Optional[float] = None,
                 outdir: Optional[str] = None,
                 wfcdir: Optional[str] = None,
                 prefix: Optional[str] = None,
                 lkpoint_dir: Optional[bool] = None,
                 max_seconds: Optional[float] = None,
                 etot_conv_thr: Optional[float] = None,
                 forc_conv_thr: Optional[float] = None,
                 disk_io: Optional[DiskIoOptions] = None,
                 pseudo_dir: Optional[str] = None,
                 tefield: Optional[bool] = None,
                 dipfield: Optional[bool] = None,
                 lelfield: Optional[bool] = None,
                 nberrycyc: Optional[int] = None,
                 lorbm: Optional[bool] = None,
                 lberry: Optional[bool] = None,
                 gdir: Optional[int] = None,
                 nppstr: Optional[int] = None,
                 lfcpopt: Optional[bool] = None,
                 gate: Optional[bool] = None,
                 ):
        """
        Parameters
        ----------
        **calculation**: CalculationOptions
            *Default*:             'scf'



        **title**: str
            *Default*:             ' '


            *Info*:             
             reprinted on output. 



        **verbosity**: VerbosityOptions
            *Default*:             'low'



        **restart_mode**: RestartModeOptions
            *Default*:             'from_scratch'



        **wf_collect**: bool
            *Default*:             .TRUE.


            *Info*:             
             This flag controls the way wavefunctions are stored to disk : 
             
             .TRUE. collect wavefunctions from all processors, store them 
             into the output data directory "outdir"/"prefix".save 
             The resulting format is portable to a different number 
             of processor, or different kind of parallelization 
             
             .FALSE. OBSOLETE - NO LONGER IMPLEMENTED 
             do not collect wavefunctions, leave them in temporary 
             local files (one per processor). The resulting format 
             is readable only on the same number of processors and 
             with the same kind of parallelization used to write it. 
             
             Note that this flag has no effect on reading, only on writing. 



        **nstep**: int
            *Default*:             
             1 if ~calculation~ == 'scf', 'nscf', 'bands' ; 
             50 for the other cases 


            *Info*:             
             number of molecular-dynamics or structural optimization steps 
             performed in this run. If set to 0, the code performs a quick 
             "dry run", stopping just after initialization. This is useful 
             to check for input correctness and to have the summary printed. 



        **iprint**: int
            *Default*:             write only at convergence


            *Info*:             
             band energies are written every *iprint* iterations 



        **tstress**: bool
            *Default*:             .false.


            *Info*:             
             calculate stress. It is set to .TRUE. automatically if 
             ~calculation~ == 'vc-md' or 'vc-relax' 



        **tprnfor**: bool
            *Info*:             
             calculate forces. It is set to .TRUE. automatically if 
             ~calculation~ == 'relax','md','vc-md' 



        **dt**: float
            *Default*:             20.D0


            *Info*:             
             time step for molecular dynamics, in Rydberg atomic units 
             (1 a.u.=4.8378 * 10^-17 s : beware, the CP code uses 
             Hartree atomic units, half that much!!!) 



        **outdir**: str
            *Default*:             
             value of the ESPRESSO_TMPDIR environment variable if set; 
             current directory ('./') otherwise 


            *Info*:             
             input, temporary, output files are found in this directory, 
             see also ~wfcdir~ 



        **wfcdir**: str
            *Default*:             same as ~outdir~


            *Info*:             
             This directory specifies where to store files generated by 
             each processor (*.wfc {N} , *.igk {N} , etc.). Useful for 
             machines without a parallel file system: set ~wfcdir~ to 
             a local file system, while ~outdir~ should be a parallel 
             or network file system, visible to all processors. Beware: 
             in order to restart from interrupted runs, or to perform 
             further calculations using the produced data files, you 
             may need to copy files to ~outdir.~ Works only for pw.x. 



        **prefix**: str
            *Default*:             'pwscf'


            *Info*:             
             prepended to input/output filenames: 
             prefix.wfc, prefix.rho, etc. 



        **lkpoint_dir**: bool
            *Default*:             .true.


            *Info*:             
             If .false. a subdirectory for each k_point is not opened 
             in the "prefix".save directory; Kohn-Sham eigenvalues are 
             stored instead in a single file for all k-points. Currently 
             doesn't work together with ~wf_collect~ 



        **max_seconds**: float
            *Default*:             1.D+7, or 150 days, i.e. no time limit


            *Info*:             
             Jobs stops after ~max_seconds~ CPU time. Use this option 
             in conjunction with option ~restart_mode~ if you need to 
             split a job too long to complete into shorter jobs that 
             fit into your batch queues. 



        **etot_conv_thr**: float
            *Default*:             1.0D-4


            *Info*:             
             Convergence threshold on total energy (a.u) for ionic 
             minimization: the convergence criterion is satisfied 
             when the total energy changes less than ~etot_conv_thr~ 
             between two consecutive scf steps. Note that ~etot_conv_thr~ 
             is extensive, like the total energy. 
             See also ~forc_conv_thr~ - both criteria must be satisfied 



        **forc_conv_thr**: float
            *Default*:             1.0D-3


            *Info*:             
             Convergence threshold on forces (a.u) for ionic minimization: 
             the convergence criterion is satisfied when all components of 
             all forces are smaller than ~forc_conv_thr.~ 
             See also ~etot_conv_thr~ - both criteria must be satisfied 



        **disk_io**: DiskIoOptions
            *Default*:             see below



        **pseudo_dir**: str
            *Default*:             
             value of the $ESPRESSO_PSEUDO environment variable if set; 
             '$HOME/espresso/pseudo/' otherwise 


            *Info*:             
             directory containing pseudopotential files 



        **tefield**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. a saw-like potential simulating an electric field 
             is added to the bare ionic potential. See variables ~edir,~ 
             ~eamp,~ ~emaxpos,~ ~eopreg~ for the form and size of 
             the added potential. 
             



        **dipfield**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. and ~tefield==.TRUE.~ a dipole correction is also 
             added to the bare ionic potential - implements the recipe 
             of L. Bengtsson, PRB 59, 12301 (1999). See variables ~edir,~ 
             ~emaxpos,~ ~eopreg~ for the form of the correction. Must 
             be used ONLY in a slab geometry, for surface calculations, 
             with the discontinuity FALLING IN THE EMPTY SPACE. 



        **lelfield**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. a homogeneous finite electric field described 
             through the modern theory of the polarization is applied. 
             This is different from ~tefield~ == .true. ! 



        **nberrycyc**: int
            *Default*:             1


            *Info*:             
             In the case of a finite electric field ( ~lelfield~ == .TRUE. ) 
             it defines the number of iterations for converging the 
             wavefunctions in the electric field Hamiltonian, for each 
             external iteration on the charge density 



        **lorbm**: bool
            *Default*:             .FALSE.


            *Info*:             
             If **.TRUE.** perform orbital magnetization calculation. 
             If finite electric field is applied ( ~lelfield==.true.)~ only Kubo terms are computed 
             [for details see New J. Phys. 12, 053032 (2010), doi:10.1088/1367-2630/12/5/053032]. 
             
             The type of calculation is **'nscf'** and should be performed on an automatically 
             generated uniform grid of k points. 
             
             Works ONLY with norm-conserving pseudopotentials. 



        **lberry**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. perform a Berry phase calculation. 
             See the header of PW/src/bp_c_phase.f90 for documentation. 



        **gdir**: int
            *Info*:             
             For Berry phase calculation: direction of the k-point 
             strings in reciprocal space. Allowed values: 1, 2, 3 
             1=first, 2=second, 3=third reciprocal lattice vector 
             For calculations with finite electric fields 
             ( ~lelfield==.true.)~ "gdir" is the direction of the field. 



        **nppstr**: int
            *Info*:             
             For Berry phase calculation: number of k-points to be 
             calculated along each symmetry-reduced string. 
             The same for calculation with finite electric fields 
             ( ~lelfield==.true.).~ 



        **lfcpopt**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. perform a constant bias potential (constant-mu) calculation 
             for a static system with ESM method. See the header of PW/src/fcp.f90 
             for documentation. 
             
             NB: 
             - The total energy displayed in 'prefix.out' includes the potentiostat 
             contribution (-mu*N). 
             - ~calculation~ must be 'relax'. 
             - ~assume_isolated~ = 'esm' and ~esm_bc~ = 'bc2' or 'bc3' must be set 
             in ~SYSTEM~ namelist. 



        **gate**: bool
            *Default*:             .FALSE.


            *Info*:             
             In the case of charged cells ( ~tot_charge~ .ne. 0) setting gate = .TRUE. 
             represents the counter charge (i.e. -tot_charge) not by a homogeneous 
             background charge but with a charged plate, which is placed at ~zgate~ 
             (see below). Details of the gate potential can be found in 
             T. Brumme, M. Calandra, F. Mauri; PRB 89, 245406 (2014). 
             Note, that in systems which are not symmetric with respect to the plate, 
             one needs to enable the dipole correction! ( ~dipfield=.true.).~ 
             Currently, symmetry can be used with gate=.true. but carefully check 
             that no symmetry is included which maps *z* to - *z* even if in principle one 
             could still use them for symmetric systems (i.e. no dipole correction). 
             For ~nosym=.false.~ verbosity is set to 'high'. 
             Note: this option was called "monopole" in v6.0 and 6.1 of pw.x 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._calculation: Optional[CalculationOptions] = calculation
        self._title: Optional[str] = title
        self._verbosity: Optional[VerbosityOptions] = verbosity
        self._restart_mode: Optional[RestartModeOptions] = restart_mode
        self._wf_collect: Optional[bool] = wf_collect
        self._nstep: Optional[int] = nstep
        self._iprint: Optional[int] = iprint
        self._tstress: Optional[bool] = tstress
        self._tprnfor: Optional[bool] = tprnfor
        self._dt: Optional[float] = dt
        self._outdir: Optional[str] = outdir
        self._wfcdir: Optional[str] = wfcdir
        self._prefix: Optional[str] = prefix
        self._lkpoint_dir: Optional[bool] = lkpoint_dir
        self._max_seconds: Optional[float] = max_seconds
        self._etot_conv_thr: Optional[float] = etot_conv_thr
        self._forc_conv_thr: Optional[float] = forc_conv_thr
        self._disk_io: Optional[DiskIoOptions] = disk_io
        self._pseudo_dir: Optional[str] = pseudo_dir
        self._tefield: Optional[bool] = tefield
        self._dipfield: Optional[bool] = dipfield
        self._lelfield: Optional[bool] = lelfield
        self._nberrycyc: Optional[int] = nberrycyc
        self._lorbm: Optional[bool] = lorbm
        self._lberry: Optional[bool] = lberry
        self._gdir: Optional[int] = gdir
        self._nppstr: Optional[int] = nppstr
        self._lfcpopt: Optional[bool] = lfcpopt
        self._gate: Optional[bool] = gate

    @property
    def calculation(self) -> CalculationOptions:
        """
        Default:
        ================
        'scf'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._calculation

    @calculation.setter
    def calculation(self, value: CalculationOptions):
        self._calculation = value

    @property
    def title(self) -> str:
        """
        Default:
        ================
        ' '


        Info:
        ================
        
         reprinted on output. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def verbosity(self) -> VerbosityOptions:
        """
        Default:
        ================
        'low'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._verbosity

    @verbosity.setter
    def verbosity(self, value: VerbosityOptions):
        self._verbosity = value

    @property
    def restart_mode(self) -> RestartModeOptions:
        """
        Default:
        ================
        'from_scratch'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._restart_mode

    @restart_mode.setter
    def restart_mode(self, value: RestartModeOptions):
        self._restart_mode = value

    @property
    def wf_collect(self) -> bool:
        """
        Default:
        ================
        .TRUE.


        Info:
        ================
        
         This flag controls the way wavefunctions are stored to disk : 
         
         .TRUE. collect wavefunctions from all processors, store them 
         into the output data directory "outdir"/"prefix".save 
         The resulting format is portable to a different number 
         of processor, or different kind of parallelization 
         
         .FALSE. OBSOLETE - NO LONGER IMPLEMENTED 
         do not collect wavefunctions, leave them in temporary 
         local files (one per processor). The resulting format 
         is readable only on the same number of processors and 
         with the same kind of parallelization used to write it. 
         
         Note that this flag has no effect on reading, only on writing. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._wf_collect

    @wf_collect.setter
    def wf_collect(self, value: bool):
        self._wf_collect = value

    @property
    def nstep(self) -> int:
        """
        Default:
        ================
        
         1 if ~calculation~ == 'scf', 'nscf', 'bands' ; 
         50 for the other cases 


        Info:
        ================
        
         number of molecular-dynamics or structural optimization steps 
         performed in this run. If set to 0, the code performs a quick 
         "dry run", stopping just after initialization. This is useful 
         to check for input correctness and to have the summary printed. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nstep

    @nstep.setter
    def nstep(self, value: int):
        self._nstep = value

    @property
    def iprint(self) -> int:
        """
        Default:
        ================
        write only at convergence


        Info:
        ================
        
         band energies are written every *iprint* iterations 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._iprint

    @iprint.setter
    def iprint(self, value: int):
        self._iprint = value

    @property
    def tstress(self) -> bool:
        """
        Default:
        ================
        .false.


        Info:
        ================
        
         calculate stress. It is set to .TRUE. automatically if 
         ~calculation~ == 'vc-md' or 'vc-relax' 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tstress

    @tstress.setter
    def tstress(self, value: bool):
        self._tstress = value

    @property
    def tprnfor(self) -> bool:
        """
        Info:
        ================
        
         calculate forces. It is set to .TRUE. automatically if 
         ~calculation~ == 'relax','md','vc-md' 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tprnfor

    @tprnfor.setter
    def tprnfor(self, value: bool):
        self._tprnfor = value

    @property
    def dt(self) -> float:
        """
        Default:
        ================
        20.D0


        Info:
        ================
        
         time step for molecular dynamics, in Rydberg atomic units 
         (1 a.u.=4.8378 * 10^-17 s : beware, the CP code uses 
         Hartree atomic units, half that much!!!) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._dt

    @dt.setter
    def dt(self, value: float):
        self._dt = value

    @property
    def outdir(self) -> str:
        """
        Default:
        ================
        
         value of the ESPRESSO_TMPDIR environment variable if set; 
         current directory ('./') otherwise 


        Info:
        ================
        
         input, temporary, output files are found in this directory, 
         see also ~wfcdir~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._outdir

    @outdir.setter
    def outdir(self, value: str):
        self._outdir = value

    @property
    def wfcdir(self) -> str:
        """
        Default:
        ================
        same as ~outdir~


        Info:
        ================
        
         This directory specifies where to store files generated by 
         each processor (*.wfc {N} , *.igk {N} , etc.). Useful for 
         machines without a parallel file system: set ~wfcdir~ to 
         a local file system, while ~outdir~ should be a parallel 
         or network file system, visible to all processors. Beware: 
         in order to restart from interrupted runs, or to perform 
         further calculations using the produced data files, you 
         may need to copy files to ~outdir.~ Works only for pw.x. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._wfcdir

    @wfcdir.setter
    def wfcdir(self, value: str):
        self._wfcdir = value

    @property
    def prefix(self) -> str:
        """
        Default:
        ================
        'pwscf'


        Info:
        ================
        
         prepended to input/output filenames: 
         prefix.wfc, prefix.rho, etc. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, value: str):
        self._prefix = value

    @property
    def lkpoint_dir(self) -> bool:
        """
        Default:
        ================
        .true.


        Info:
        ================
        
         If .false. a subdirectory for each k_point is not opened 
         in the "prefix".save directory; Kohn-Sham eigenvalues are 
         stored instead in a single file for all k-points. Currently 
         doesn't work together with ~wf_collect~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lkpoint_dir

    @lkpoint_dir.setter
    def lkpoint_dir(self, value: bool):
        self._lkpoint_dir = value

    @property
    def max_seconds(self) -> float:
        """
        Default:
        ================
        1.D+7, or 150 days, i.e. no time limit


        Info:
        ================
        
         Jobs stops after ~max_seconds~ CPU time. Use this option 
         in conjunction with option ~restart_mode~ if you need to 
         split a job too long to complete into shorter jobs that 
         fit into your batch queues. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._max_seconds

    @max_seconds.setter
    def max_seconds(self, value: float):
        self._max_seconds = value

    @property
    def etot_conv_thr(self) -> float:
        """
        Default:
        ================
        1.0D-4


        Info:
        ================
        
         Convergence threshold on total energy (a.u) for ionic 
         minimization: the convergence criterion is satisfied 
         when the total energy changes less than ~etot_conv_thr~ 
         between two consecutive scf steps. Note that ~etot_conv_thr~ 
         is extensive, like the total energy. 
         See also ~forc_conv_thr~ - both criteria must be satisfied 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._etot_conv_thr

    @etot_conv_thr.setter
    def etot_conv_thr(self, value: float):
        self._etot_conv_thr = value

    @property
    def forc_conv_thr(self) -> float:
        """
        Default:
        ================
        1.0D-3


        Info:
        ================
        
         Convergence threshold on forces (a.u) for ionic minimization: 
         the convergence criterion is satisfied when all components of 
         all forces are smaller than ~forc_conv_thr.~ 
         See also ~etot_conv_thr~ - both criteria must be satisfied 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._forc_conv_thr

    @forc_conv_thr.setter
    def forc_conv_thr(self, value: float):
        self._forc_conv_thr = value

    @property
    def disk_io(self) -> DiskIoOptions:
        """
        Default:
        ================
        see below



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._disk_io

    @disk_io.setter
    def disk_io(self, value: DiskIoOptions):
        self._disk_io = value

    @property
    def pseudo_dir(self) -> str:
        """
        Default:
        ================
        
         value of the $ESPRESSO_PSEUDO environment variable if set; 
         '$HOME/espresso/pseudo/' otherwise 


        Info:
        ================
        
         directory containing pseudopotential files 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._pseudo_dir

    @pseudo_dir.setter
    def pseudo_dir(self, value: str):
        self._pseudo_dir = value

    @property
    def tefield(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. a saw-like potential simulating an electric field 
         is added to the bare ionic potential. See variables ~edir,~ 
         ~eamp,~ ~emaxpos,~ ~eopreg~ for the form and size of 
         the added potential. 
         



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tefield

    @tefield.setter
    def tefield(self, value: bool):
        self._tefield = value

    @property
    def dipfield(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. and ~tefield==.TRUE.~ a dipole correction is also 
         added to the bare ionic potential - implements the recipe 
         of L. Bengtsson, PRB 59, 12301 (1999). See variables ~edir,~ 
         ~emaxpos,~ ~eopreg~ for the form of the correction. Must 
         be used ONLY in a slab geometry, for surface calculations, 
         with the discontinuity FALLING IN THE EMPTY SPACE. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._dipfield

    @dipfield.setter
    def dipfield(self, value: bool):
        self._dipfield = value

    @property
    def lelfield(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. a homogeneous finite electric field described 
         through the modern theory of the polarization is applied. 
         This is different from ~tefield~ == .true. ! 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lelfield

    @lelfield.setter
    def lelfield(self, value: bool):
        self._lelfield = value

    @property
    def nberrycyc(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         In the case of a finite electric field ( ~lelfield~ == .TRUE. ) 
         it defines the number of iterations for converging the 
         wavefunctions in the electric field Hamiltonian, for each 
         external iteration on the charge density 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nberrycyc

    @nberrycyc.setter
    def nberrycyc(self, value: int):
        self._nberrycyc = value

    @property
    def lorbm(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If **.TRUE.** perform orbital magnetization calculation. 
         If finite electric field is applied ( ~lelfield==.true.)~ only Kubo terms are computed 
         [for details see New J. Phys. 12, 053032 (2010), doi:10.1088/1367-2630/12/5/053032]. 
         
         The type of calculation is **'nscf'** and should be performed on an automatically 
         generated uniform grid of k points. 
         
         Works ONLY with norm-conserving pseudopotentials. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lorbm

    @lorbm.setter
    def lorbm(self, value: bool):
        self._lorbm = value

    @property
    def lberry(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. perform a Berry phase calculation. 
         See the header of PW/src/bp_c_phase.f90 for documentation. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lberry

    @lberry.setter
    def lberry(self, value: bool):
        self._lberry = value

    @property
    def gdir(self) -> int:
        """
        Info:
        ================
        
         For Berry phase calculation: direction of the k-point 
         strings in reciprocal space. Allowed values: 1, 2, 3 
         1=first, 2=second, 3=third reciprocal lattice vector 
         For calculations with finite electric fields 
         ( ~lelfield==.true.)~ "gdir" is the direction of the field. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._gdir

    @gdir.setter
    def gdir(self, value: int):
        self._gdir = value

    @property
    def nppstr(self) -> int:
        """
        Info:
        ================
        
         For Berry phase calculation: number of k-points to be 
         calculated along each symmetry-reduced string. 
         The same for calculation with finite electric fields 
         ( ~lelfield==.true.).~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nppstr

    @nppstr.setter
    def nppstr(self, value: int):
        self._nppstr = value

    @property
    def lfcpopt(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. perform a constant bias potential (constant-mu) calculation 
         for a static system with ESM method. See the header of PW/src/fcp.f90 
         for documentation. 
         
         NB: 
         - The total energy displayed in 'prefix.out' includes the potentiostat 
         contribution (-mu*N). 
         - ~calculation~ must be 'relax'. 
         - ~assume_isolated~ = 'esm' and ~esm_bc~ = 'bc2' or 'bc3' must be set 
         in ~SYSTEM~ namelist. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lfcpopt

    @lfcpopt.setter
    def lfcpopt(self, value: bool):
        self._lfcpopt = value

    @property
    def gate(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         In the case of charged cells ( ~tot_charge~ .ne. 0) setting gate = .TRUE. 
         represents the counter charge (i.e. -tot_charge) not by a homogeneous 
         background charge but with a charged plate, which is placed at ~zgate~ 
         (see below). Details of the gate potential can be found in 
         T. Brumme, M. Calandra, F. Mauri; PRB 89, 245406 (2014). 
         Note, that in systems which are not symmetric with respect to the plate, 
         one needs to enable the dipole correction! ( ~dipfield=.true.).~ 
         Currently, symmetry can be used with gate=.true. but carefully check 
         that no symmetry is included which maps *z* to - *z* even if in principle one 
         could still use them for symmetric systems (i.e. no dipole correction). 
         For ~nosym=.false.~ verbosity is set to 'high'. 
         Note: this option was called "monopole" in v6.0 and 6.1 of pw.x 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._gate

    @gate.setter
    def gate(self, value: bool):
        self._gate = value

