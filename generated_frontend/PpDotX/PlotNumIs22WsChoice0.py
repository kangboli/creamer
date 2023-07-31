from typing import Optional, List
from .Choice import Choice
from .Choice0 import Choice0


class PlotNumIs22WsChoice0(Choice, Choice0):
    """
    Label:
    ================
    
     Options for kinetic energy density (plot_num=22), 
     LSDA case only: 


    """

    def __init__(self,
                 spin_component: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **spin_component**: int
            *Info*:             
             0 = total density (default value), 
             1 = spin up density, 
             2 = spin down density. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._spin_component: Optional[int] = spin_component

    @property
    def spin_component(self) -> int:
        """
        Info:
        ================
        
         0 = total density (default value), 
         1 = spin up density, 
         2 = spin down density. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: int):
        self._spin_component = value

