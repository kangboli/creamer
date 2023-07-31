from typing import Optional, List
from .Card import Card
from .FlagKpointTypeOptions import FlagKpointTypeOptions
from .FlagKpointTypeOptions import FlagKpointTypeOptions
from .Choice1 import Choice1


class KPoints(Card):
    """
    """

    def __init__(self,
                 flag_kpoint_type: Optional[FlagKpointTypeOptions] = None,
                 choice1: Optional[Choice1] = Choice1(),
                 ):
        """
        Parameters
        ----------
        **flag_kpoint_type**: FlagKpointTypeOptions
            *Default*:             tbipa



        **choice1**: Choice1
            *Info*:             
             Occupations of individual states (MAX 10 PER ROW). 
             For spin-polarized calculations, these are majority spin states. 
            
             Occupations of minority spin states (MAX 10 PER ROW) 
             To be specified only for spin-polarized calculations. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._flag_kpoint_type: Optional[FlagKpointTypeOptions] = flag_kpoint_type
        self._choice1: Optional[Choice1] = choice1

    @property
    def flag_kpoint_type(self) -> FlagKpointTypeOptions:
        """
        Default:
        ================
        tbipa



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._flag_kpoint_type

    @flag_kpoint_type.setter
    def flag_kpoint_type(self, value: FlagKpointTypeOptions):
        self._flag_kpoint_type = value

    @property
    def choice1(self) -> Choice1:
        """
        Info:
        ================
        
         Occupations of individual states (MAX 10 PER ROW). 
         For spin-polarized calculations, these are majority spin states. 
        
         Occupations of minority spin states (MAX 10 PER ROW) 
         To be specified only for spin-polarized calculations. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._choice1

    @choice1.setter
    def choice1(self, value: Choice1):
        self._choice1 = value

