from typing import Optional, List
from .Group import Group


class Group1(Group):
    """
    Label:
    ================
    variables used only if ~gate~ = .TRUE.


    """

    def __init__(self,
                 zgate: Optional[float] = None,
                 relaxz: Optional[bool] = None,
                 block: Optional[bool] = None,
                 block_1: Optional[float] = None,
                 block_2: Optional[float] = None,
                 block_height: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **zgate**: float
            *Default*:             0.5


            *Info*:             
             used only if ~gate~ = .TRUE. 
             Specifies the position of the charged plate which represents 
             the counter charge in doped systems ( ~tot_charge~ .ne. 0). 
             In units of the unit cell length in *z* direction, ~zgate~ in ]0,1[ 
             Details of the gate potential can be found in 
             T. Brumme, M. Calandra, F. Mauri; PRB 89, 245406 (2014). 



        **relaxz**: bool
            *Default*:             .FALSE.


            *Info*:             
             used only if ~gate~ = .TRUE. 
             Allows the relaxation of the system towards the charged plate. 
             Use carefully and utilize either a layer of fixed atoms or a 
             potential barrier ( ~block=.TRUE.)~ to avoid the atoms moving to 
             the position of the plate or the dipole of the dipole 
             correction ( ~dipfield=.TRUE.).~ 



        **block**: bool
            *Default*:             .FALSE.


            *Info*:             
             used only if ~gate~ = .TRUE. 
             Adds a potential barrier to the total potential seen by the 
             electrons to mimic a dielectric in field effect configuration 
             and/or to avoid electrons spilling into the vacuum region for 
             electron doping. Potential barrier is from ~block_1~ to ~block_2~ and 
             has a height of block_height. 
             If ~dipfield~ = .TRUE. then ~eopreg~ is used for a smooth increase and 
             decrease of the potential barrier. 



        **block_1**: float
            *Default*:             0.45


            *Info*:             
             used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
             lower beginning of the potential barrier, in units of the 
             unit cell size along *z,* ~block_1~ in ]0,1[ 



        **block_2**: float
            *Default*:             0.55


            *Info*:             
             used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
             upper beginning of the potential barrier, in units of the 
             unit cell size along *z,* ~block_2~ in ]0,1[ 



        **block_height**: float
            *Default*:             0.1


            *Info*:             
             used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
             Height of the potential barrier in Rydberg. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._zgate: Optional[float] = zgate
        self._relaxz: Optional[bool] = relaxz
        self._block: Optional[bool] = block
        self._block_1: Optional[float] = block_1
        self._block_2: Optional[float] = block_2
        self._block_height: Optional[float] = block_height

    @property
    def zgate(self) -> float:
        """
        Default:
        ================
        0.5


        Info:
        ================
        
         used only if ~gate~ = .TRUE. 
         Specifies the position of the charged plate which represents 
         the counter charge in doped systems ( ~tot_charge~ .ne. 0). 
         In units of the unit cell length in *z* direction, ~zgate~ in ]0,1[ 
         Details of the gate potential can be found in 
         T. Brumme, M. Calandra, F. Mauri; PRB 89, 245406 (2014). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._zgate

    @zgate.setter
    def zgate(self, value: float):
        self._zgate = value

    @property
    def relaxz(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         used only if ~gate~ = .TRUE. 
         Allows the relaxation of the system towards the charged plate. 
         Use carefully and utilize either a layer of fixed atoms or a 
         potential barrier ( ~block=.TRUE.)~ to avoid the atoms moving to 
         the position of the plate or the dipole of the dipole 
         correction ( ~dipfield=.TRUE.).~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._relaxz

    @relaxz.setter
    def relaxz(self, value: bool):
        self._relaxz = value

    @property
    def block(self) -> bool:
        """
        Default:
        ================
        .FALSE.


        Info:
        ================
        
         used only if ~gate~ = .TRUE. 
         Adds a potential barrier to the total potential seen by the 
         electrons to mimic a dielectric in field effect configuration 
         and/or to avoid electrons spilling into the vacuum region for 
         electron doping. Potential barrier is from ~block_1~ to ~block_2~ and 
         has a height of block_height. 
         If ~dipfield~ = .TRUE. then ~eopreg~ is used for a smooth increase and 
         decrease of the potential barrier. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._block

    @block.setter
    def block(self, value: bool):
        self._block = value

    @property
    def block_1(self) -> float:
        """
        Default:
        ================
        0.45


        Info:
        ================
        
         used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
         lower beginning of the potential barrier, in units of the 
         unit cell size along *z,* ~block_1~ in ]0,1[ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._block_1

    @block_1.setter
    def block_1(self, value: float):
        self._block_1 = value

    @property
    def block_2(self) -> float:
        """
        Default:
        ================
        0.55


        Info:
        ================
        
         used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
         upper beginning of the potential barrier, in units of the 
         unit cell size along *z,* ~block_2~ in ]0,1[ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._block_2

    @block_2.setter
    def block_2(self, value: float):
        self._block_2 = value

    @property
    def block_height(self) -> float:
        """
        Default:
        ================
        0.1


        Info:
        ================
        
         used only if ~gate~ = .TRUE. and ~block~ = .TRUE. 
         Height of the potential barrier in Rydberg. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._block_height

    @block_height.setter
    def block_height(self, value: float):
        self._block_height = value

