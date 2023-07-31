from typing import Optional, List
from .Namelist import Namelist
from .MixingModeOptions import MixingModeOptions
from .DiagonalizationOptions import DiagonalizationOptions
from .EfieldPhaseOptions import EfieldPhaseOptions
from .StartingpotOptions import StartingpotOptions
from .StartingwfcOptions import StartingwfcOptions


class Electrons(Namelist):
    """
    """

    def __init__(self,
                 electron_maxstep: Optional[int] = None,
                 scf_must_converge: Optional[bool] = None,
                 conv_thr: Optional[float] = None,
                 adaptive_thr: Optional[bool] = None,
                 conv_thr_init: Optional[float] = None,
                 conv_thr_multi: Optional[float] = None,
                 mixing_mode: Optional[MixingModeOptions] = None,
                 mixing_beta: Optional[float] = None,
                 mixing_ndim: Optional[int] = None,
                 mixing_fixed_ns: Optional[int] = None,
                 diagonalization: Optional[DiagonalizationOptions] = None,
                 diago_thr_init: Optional[float] = None,
                 diago_cg_maxiter: Optional[int] = None,
                 diago_david_ndim: Optional[int] = None,
                 diago_full_acc: Optional[bool] = None,
                 efield: Optional[float] = None,
                 efield_cart: Optional[List[float]] = None,
                 efield_phase: Optional[EfieldPhaseOptions] = None,
                 startingpot: Optional[StartingpotOptions] = None,
                 startingwfc: Optional[StartingwfcOptions] = None,
                 tqr: Optional[bool] = None,
                 real_space: Optional[bool] = None,
                 ):
        """
        Parameters
        ----------
        **electron_maxstep**: int
            *Default*:             100


            *Info*:             
             maximum number of iterations in a scf step 



        **scf_must_converge**: bool
            *Default*:             .TRUE.


            *Info*:             
             If .false. do not stop molecular dynamics or ionic relaxation 
             when electron_maxstep is reached. Use with care. 



        **conv_thr**: float
            *Default*:             1.D-6


            *Info*:             
             Convergence threshold for selfconsistency: 
             estimated energy error < conv_thr 
             (note that conv_thr is extensive, like the total energy). 
             
             For non-self-consistent calculations, conv_thr is used 
             to set the default value of the threshold (ethr) for 
             iterative diagonalizazion: see ~diago_thr_init~ 



        **adaptive_thr**: bool
            *Default*:             .FALSE


            *Info*:             
             If .TRUE. this turns on the use of an adaptive ~conv_thr~ for 
             the inner scf loops when using EXX. 



        **conv_thr_init**: float
            *Default*:             1.D-3


            *Info*:             
             When ~adaptive_thr~ = .TRUE. this is the convergence threshold 
             used for the first scf cycle. 



        **conv_thr_multi**: float
            *Default*:             1.D-1


            *Info*:             
             When ~adaptive_thr~ = .TRUE. the convergence threshold for 
             each scf cycle is given by: 
             max( ~conv_thr,~ ~conv_thr_multi~ * dexx ) 



        **mixing_mode**: MixingModeOptions
            *Default*:             'plain'



        **mixing_beta**: float
            *Default*:             0.7D0


            *Info*:             
             mixing factor for self-consistency 



        **mixing_ndim**: int
            *Default*:             8


            *Info*:             
             number of iterations used in mixing scheme. 
             If you are tight with memory, you may reduce it to 4 or so. 



        **mixing_fixed_ns**: int
            *Default*:             0


            *Info*:             
             For DFT+U : number of iterations with fixed ns ( ns is the 
             atomic density appearing in the Hubbard term ). 



        **diagonalization**: DiagonalizationOptions
            *Default*:             'david'



        **diago_thr_init**: float
            *Info*:             
             Convergence threshold (ethr) for iterative diagonalization 
             (the check is on eigenvalue convergence). 
             
             For scf calculations: default is 1.D-2 if starting from a 
             superposition of atomic orbitals; 1.D-5 if starting from a 
             charge density. During self consistency the threshold 
             is automatically reduced (but never below 1.D-13) when 
             approaching convergence. 
             
             For non-scf calculations: default is ( ~conv_thr/N~ elec)/10. 



        **diago_cg_maxiter**: int
            *Info*:             
             For conjugate gradient diagonalization: max number of iterations 



        **diago_david_ndim**: int
            *Default*:             2


            *Info*:             
             For Davidson diagonalization: dimension of workspace 
             (number of wavefunction packets, at least 2 needed). 
             A larger value may yield a smaller number of iterations in 
             the algorithm but uses more memory and more CPU time in 
             subspace diagonalization (cdiaghg/rdiaghg). You may try 
             ~diago_david_ndim=4~ if you are not tight on memory 
             and if the time spent in subspace diagonalization is small 
             compared to the time spent in h_psi 



        **diago_full_acc**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .TRUE. all the empty states are diagonalized at the same level 
             of accuracy of the occupied ones. Otherwise the empty states are 
             diagonalized using a larger threshold (this should not affect 
             total energy, forces, and other ground-state properties). 



        **efield**: float
            *Default*:             0.D0


            *Info*:             
             Amplitude of the finite electric field (in Ry a.u.; 
             1 a.u. = 36.3609*10^10 V/m). Used only if ~lelfield==.TRUE.~ 
             and if k-points ( ~K_POINTS~ card) are not automatic. 



        **efield_cart**: List[float]
            *Default*:             (0.D0, 0.D0, 0.D0)


            *Info*:             
             Finite electric field (in Ry a.u.=36.3609*10^10 V/m) in 
             cartesian axis. Used only if ~lelfield==.TRUE.~ and if 
             k-points ( ~K_POINTS~ card) are automatic. 


            *Others*:             Start - 1; End - 3



        **efield_phase**: EfieldPhaseOptions
            *Default*:             'none'



        **startingpot**: StartingpotOptions

        **startingwfc**: StartingwfcOptions
            *Default*:             'atomic+random'



        **tqr**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .true., use a real-space algorithm for augmentation 
             charges of ultrasoft pseudopotentials and PAWsets. 
             Faster but numerically less accurate than the default 
             G-space algorithm. Use with care and after testing! 



        **real_space**: bool
            *Default*:             .FALSE.


            *Info*:             
             If .true., exploit real-space localization to compute 
             matrix elements for nonlocal projectors. Faster and in 
             principle better scaling than the default G-space algorithm, 
             but numerically less accurate, may lead to some loss of 
             translational invariance. Use with care and after testing! 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._electron_maxstep: Optional[int] = electron_maxstep
        self._scf_must_converge: Optional[bool] = scf_must_converge
        self._conv_thr: Optional[float] = conv_thr
        self._adaptive_thr: Optional[bool] = adaptive_thr
        self._conv_thr_init: Optional[float] = conv_thr_init
        self._conv_thr_multi: Optional[float] = conv_thr_multi
        self._mixing_mode: Optional[MixingModeOptions] = mixing_mode
        self._mixing_beta: Optional[float] = mixing_beta
        self._mixing_ndim: Optional[int] = mixing_ndim
        self._mixing_fixed_ns: Optional[int] = mixing_fixed_ns
        self._diagonalization: Optional[DiagonalizationOptions] = diagonalization
        self._diago_thr_init: Optional[float] = diago_thr_init
        self._diago_cg_maxiter: Optional[int] = diago_cg_maxiter
        self._diago_david_ndim: Optional[int] = diago_david_ndim
        self._diago_full_acc: Optional[bool] = diago_full_acc
        self._efield: Optional[float] = efield
        self._efield_cart: Optional[List[float]] = efield_cart
        self._efield_phase: Optional[EfieldPhaseOptions] = efield_phase
        self._startingpot: Optional[StartingpotOptions] = startingpot
        self._startingwfc: Optional[StartingwfcOptions] = startingwfc
        self._tqr: Optional[bool] = tqr
        self._real_space: Optional[bool] = real_space

    @property
    def electron_maxstep(self) -> int:
        """
        Default:
        ================
        100


        Info:
        ================
        
         maximum number of iterations in a scf step 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._electron_maxstep

    @electron_maxstep.setter
    def electron_maxstep(self, value: int):
        self._electron_maxstep = value

    @property
    def scf_must_converge(self) -> bool:
        """
        Default:
        ================
        .TRUE.


        Info:
        ================
        
         If .false. do not stop molecular dynamics or ionic relaxation 
         when electron_maxstep is reached. Use with care. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._scf_must_converge

    @scf_must_converge.setter
    def scf_must_converge(self, value: bool):
        self._scf_must_converge = value

    @property
    def conv_thr(self) -> float:
        """
        Default:
        ================
        1.D-6


        Info:
        ================
        
         Convergence threshold for selfconsistency: 
         estimated energy error < conv_thr 
         (note that conv_thr is extensive, like the total energy). 
         
         For non-self-consistent calculations, conv_thr is used 
         to set the default value of the threshold (ethr) for 
         iterative diagonalizazion: see ~diago_thr_init~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._conv_thr

    @conv_thr.setter
    def conv_thr(self, value: float):
        self._conv_thr = value

    @property
    def adaptive_thr(self) -> bool:
        """
        Default:
        ================
        .FALSE


        Info:
        ================
        
         If .TRUE. this turns on the use of an adaptive ~conv_thr~ for 
         the inner scf loops when using EXX. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._adaptive_thr

    @adaptive_thr.setter
    def adaptive_thr(self, value: bool):
        self._adaptive_thr = value

    @property
    def conv_thr_init(self) -> float:
        """
        Default:
        ================
        1.D-3


        Info:
        ================
        
         When ~adaptive_thr~ = .TRUE. this is the convergence threshold 
         used for the first scf cycle. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._conv_thr_init

    @conv_thr_init.setter
    def conv_thr_init(self, value: float):
        self._conv_thr_init = value

    @property
    def conv_thr_multi(self) -> float:
        """
        Default:
        ================
        1.D-1


        Info:
        ================
        
         When ~adaptive_thr~ = .TRUE. the convergence threshold for 
         each scf cycle is given by: 
         max( ~conv_thr,~ ~conv_thr_multi~ * dexx ) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._conv_thr_multi

    @conv_thr_multi.setter
    def conv_thr_multi(self, value: float):
        self._conv_thr_multi = value

    @property
    def mixing_mode(self) -> MixingModeOptions:
        """
        Default:
        ================
        'plain'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._mixing_mode

    @mixing_mode.setter
    def mixing_mode(self, value: MixingModeOptions):
        self._mixing_mode = value

    @property
    def mixing_beta(self) -> float:
        """
        Default:
        ================
        0.7D0


        Info:
        ================
        
         mixing factor for self-consistency 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._mixing_beta

    @mixing_beta.setter
    def mixing_beta(self, value: float):
        self._mixing_beta = value

    @property
    def mixing_ndim(self) -> int:
        """
        Default:
        ================
        8


        Info:
        ================
        
         number of iterations used in mixing scheme. 
         If you are tight with memory, you may reduce it to 4 or so. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._mixing_ndim

    @mixing_ndim.setter
    def mixing_ndim(self, value: int):
        self._mixing_ndim = value

    @property
    def mixing_fixed_ns(self) -> int:
        """
        Default:
        ================
        0


        Info:
        ================
        
         For DFT+U : number of iterations with fixed ns ( ns is the 
         atomic density appearing in the Hubbard term ). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._mixing_fixed_ns

    @mixing_fixed_ns.setter
    def mixing_fixed_ns(self, value: int):
        self._mixing_fixed_ns = value

    @property
    def diagonalization(self) -> DiagonalizationOptions:
        """
        Default:
        ================
        'david'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._diagonalization

    @diagonalization.setter
    def diagonalization(self, value: DiagonalizationOptions):
        self._diagonalization = value

    @property
    def diago_thr_init(self) -> float:
        """
        Info:
        ================
        
         Convergence threshold (ethr) for iterative diagonalization 
         (the check is on eigenvalue convergence). 
         
         For scf calculations: default is 1.D-2 if starting from a 
         superposition of atomic orbitals; 1.D-5 if starting from a 
         charge density. During self consistency the threshold 
         is automatically reduced (but never below 1.D-13) when 
         approaching convergence. 
         
         For non-scf calculations: default is ( ~conv_thr/N~ elec)/10. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._diago_thr_init

    @diago_thr_init.setter
    def diago_thr_init(self, value: float):
        self._diago_thr_init = value

    @property
    def diago_cg_maxiter(self) -> int:
        """
        Info:
        ================
        
         For conjugate gradient diagonalization: max number of iterations 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._diago_cg_maxiter

    @diago_cg_maxiter.setter
    def diago_cg_maxiter(self, value: int):
        self._diago_cg_maxiter = value

    @property
    def diago_david_ndim(self) -> int:
        """
        Default:
        ================
        2


        Info:
        ================
        
         For Davidson diagonalization: dimension of workspace 
         (number of wavefunction packets, at least 2 needed). 
         A larger value may yield a smaller number of iterations in 
         the algorithm but uses more memory and more CPU time in 
         subspace diagonalization (cdiaghg/rdiaghg). You may try 
         ~diago_david_ndim=4~ if you are not tight on memory 
         and if the time spent in subspace diagonalization is small 
         compared to the time spent in h_psi 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._diago_david_ndim

    @diago_david_ndim.setter
    def diago_david_ndim(self, value: int):
        self._diago_david_ndim = value

    @property
    def diago_full_acc(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .TRUE. all the empty states are diagonalized at the same level 
         of accuracy of the occupied ones. Otherwise the empty states are 
         diagonalized using a larger threshold (this should not affect 
         total energy, forces, and other ground-state properties). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._diago_full_acc

    @diago_full_acc.setter
    def diago_full_acc(self, value: bool):
        self._diago_full_acc = value

    @property
    def efield(self) -> float:
        """
        Default:
        ================
        0.D0


        Info:
        ================
        
         Amplitude of the finite electric field (in Ry a.u.; 
         1 a.u. = 36.3609*10^10 V/m). Used only if ~lelfield==.TRUE.~ 
         and if k-points ( ~K_POINTS~ card) are not automatic. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._efield

    @efield.setter
    def efield(self, value: float):
        self._efield = value

    @property
    def efield_cart(self) -> List[float]:
        """
        Default:
        ================
        (0.D0, 0.D0, 0.D0)


        Info:
        ================
        
         Finite electric field (in Ry a.u.=36.3609*10^10 V/m) in 
         cartesian axis. Used only if ~lelfield==.TRUE.~ and if 
         k-points ( ~K_POINTS~ card) are automatic. 


        Others:
        ================
        Start - 1; End - 3

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._efield_cart

    @efield_cart.setter
    def efield_cart(self, value: List[float]):
        self._efield_cart = value

    @property
    def efield_phase(self) -> EfieldPhaseOptions:
        """
        Default:
        ================
        'none'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._efield_phase

    @efield_phase.setter
    def efield_phase(self, value: EfieldPhaseOptions):
        self._efield_phase = value

    @property
    def startingpot(self) -> StartingpotOptions:
        """
        """
        return self._startingpot

    @startingpot.setter
    def startingpot(self, value: StartingpotOptions):
        self._startingpot = value

    @property
    def startingwfc(self) -> StartingwfcOptions:
        """
        Default:
        ================
        'atomic+random'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._startingwfc

    @startingwfc.setter
    def startingwfc(self, value: StartingwfcOptions):
        self._startingwfc = value

    @property
    def tqr(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .true., use a real-space algorithm for augmentation 
         charges of ultrasoft pseudopotentials and PAWsets. 
         Faster but numerically less accurate than the default 
         G-space algorithm. Use with care and after testing! 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._tqr

    @tqr.setter
    def tqr(self, value: bool):
        self._tqr = value

    @property
    def real_space(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         If .true., exploit real-space localization to compute 
         matrix elements for nonlocal projectors. Faster and in 
         principle better scaling than the default G-space algorithm, 
         but numerically less accurate, may lead to some loss of 
         translational invariance. Use with care and after testing! 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._real_space

    @real_space.setter
    def real_space(self, value: bool):
        self._real_space = value

