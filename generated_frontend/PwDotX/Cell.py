from typing import Optional, List
from .Namelist import Namelist
from .CellDynamicsOptions import CellDynamicsOptions
from .CellDofreeOptions import CellDofreeOptions


class Cell(Namelist):
    """
    Label:
    ================
    
     input this namelist only if ~calculation~ == 'vc-relax' or 'vc-md' 


    """

    def __init__(self,
                 cell_dynamics: Optional[CellDynamicsOptions] = None,
                 press: Optional[float] = None,
                 wmass: Optional[float] = None,
                 cell_factor: Optional[float] = None,
                 press_conv_thr: Optional[float] = None,
                 cell_dofree: Optional[CellDofreeOptions] = None,
                 ):
        """
        Parameters
        ----------
        **cell_dynamics**: CellDynamicsOptions

        **press**: float
            *Default*:             0.D0


            *Info*:             
             Target pressure [KBar] in a variable-cell md or relaxation run. 



        **wmass**: float
            *Default*:             
             0.75*Tot_Mass/pi**2 for Parrinello-Rahman MD; 
             0.75*Tot_Mass/pi**2/Omega**(2/3) for Wentzcovitch MD 


            *Info*:             
             Fictitious cell mass [amu] for variable-cell simulations 
             (both 'vc-md' and 'vc-relax' ) 



        **cell_factor**: float
            *Default*:             2.0 for variable-cell calculations, 1.0 otherwise


            *Info*:             
             Used in the construction of the pseudopotential tables. 
             It should exceed the maximum linear contraction of the 
             cell during a simulation. 



        **press_conv_thr**: float
            *Default*:             0.5D0 Kbar


            *Info*:             
             Convergence threshold on the pressure for variable cell 
             relaxation ('vc-relax' : note that the other convergence 
             thresholds for ionic relaxation apply as well). 



        **cell_dofree**: CellDofreeOptions
            *Default*:             'all'



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._cell_dynamics: Optional[CellDynamicsOptions] = cell_dynamics
        self._press: Optional[float] = press
        self._wmass: Optional[float] = wmass
        self._cell_factor: Optional[float] = cell_factor
        self._press_conv_thr: Optional[float] = press_conv_thr
        self._cell_dofree: Optional[CellDofreeOptions] = cell_dofree

    @property
    def cell_dynamics(self) -> CellDynamicsOptions:
        """
        """
        return self._cell_dynamics

    @cell_dynamics.setter
    def cell_dynamics(self, value: CellDynamicsOptions):
        self._cell_dynamics = value

    @property
    def press(self) -> float:
        """
        Default:
        ================
        0.D0


        Info:
        ================
        
         Target pressure [KBar] in a variable-cell md or relaxation run. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._press

    @press.setter
    def press(self, value: float):
        self._press = value

    @property
    def wmass(self) -> float:
        """
        Default:
        ================
        
         0.75*Tot_Mass/pi**2 for Parrinello-Rahman MD; 
         0.75*Tot_Mass/pi**2/Omega**(2/3) for Wentzcovitch MD 


        Info:
        ================
        
         Fictitious cell mass [amu] for variable-cell simulations 
         (both 'vc-md' and 'vc-relax' ) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._wmass

    @wmass.setter
    def wmass(self, value: float):
        self._wmass = value

    @property
    def cell_factor(self) -> float:
        """
        Default:
        ================
        2.0 for variable-cell calculations, 1.0 otherwise


        Info:
        ================
        
         Used in the construction of the pseudopotential tables. 
         It should exceed the maximum linear contraction of the 
         cell during a simulation. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._cell_factor

    @cell_factor.setter
    def cell_factor(self, value: float):
        self._cell_factor = value

    @property
    def press_conv_thr(self) -> float:
        """
        Default:
        ================
        0.5D0 Kbar


        Info:
        ================
        
         Convergence threshold on the pressure for variable cell 
         relaxation ('vc-relax' : note that the other convergence 
         thresholds for ionic relaxation apply as well). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._press_conv_thr

    @press_conv_thr.setter
    def press_conv_thr(self, value: float):
        self._press_conv_thr = value

    @property
    def cell_dofree(self) -> CellDofreeOptions:
        """
        Default:
        ================
        'all'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._cell_dofree

    @cell_dofree.setter
    def cell_dofree(self, value: CellDofreeOptions):
        self._cell_dofree = value

