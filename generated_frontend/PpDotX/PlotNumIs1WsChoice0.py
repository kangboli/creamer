from typing import Optional, List
from .Choice import Choice
from .Choice0 import Choice0


class PlotNumIs1WsChoice0(Choice, Choice0):
    """
    Label:
    ================
    
     Options for total potential (plot_num=1): 


    """

    def __init__(self,
                 spin_component: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **spin_component**: int
            *Info*:             
             0 = spin averaged potential (default value), 
             1 = spin up potential, 
             2 = spin down potential. 



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
        
         0 = spin averaged potential (default value), 
         1 = spin up potential, 
         2 = spin down potential. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: int):
        self._spin_component = value

