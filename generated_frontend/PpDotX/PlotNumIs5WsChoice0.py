from typing import Optional, List
from .Choice import Choice
from .Choice0 import Choice0


class PlotNumIs5WsChoice0(Choice, Choice0):
    """
    Label:
    ================
    
     Options for STM images (plot_num=5): 


    """

    def __init__(self,
                 sample_bias: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **sample_bias**: float
            *Info*:             
             the bias of the sample (Ry) in stm images 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._sample_bias: Optional[float] = sample_bias

    @property
    def sample_bias(self) -> float:
        """
        Info:
        ================
        
         the bias of the sample (Ry) in stm images 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._sample_bias

    @sample_bias.setter
    def sample_bias(self, value: float):
        self._sample_bias = value

