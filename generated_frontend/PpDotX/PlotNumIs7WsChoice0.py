from typing import Optional, List
from .Choice import Choice
from .Choice0 import Choice0


class PlotNumIs7WsChoice0(Choice, Choice0):
    """
    Label:
    ================
    
     Options for |psi|^2 (plot_num=7): 


    """

    def __init__(self,
                 kpoint: Optional[List[int]] = None,
                 kband: Optional[List[int]] = None,
                 lsign: Optional[bool] = None,
                 spin_component: Optional[List[int]] = None,
                 ):
        """
        Parameters
        ----------
        **kpoint**: List[int]
            *Info*:             
             Unpolarized and noncollinear case: 
             k-point(s) to be plotted 
             LSDA: 
             k-point(s) and spin polarization to be plotted 
             (spin-up and spin-down correspond to different k-points!) 
             
             To plot a single kpoint ikpt, specify kpoint=ikpt or kpoint(1)=ikpt 
             To plot a range of kpoints [imin, imax], specify kpoint(1)=imin and kpoint(2)=imax 


            *Others*:             Start - 1; End - 2



        **kband**: List[int]
            *Info*:             
             Band(s) to be plotted. 
             
             To plot a single band ibnd, specify kband=ibnd or kband(1)=ibnd 
             To plot a range of bands [imin, imax], specify kband(1)=imin and kband(2)=imax 


            *Others*:             Start - 1; End - 2



        **lsign**: bool
            *Info*:             
             if true and k point is Gamma, plot |psi|^2 sign(psi) 



        **spin_component**: List[int]
            *Info*:             
             **Noncollinear case only:** 
             plot the contribution of the given state(s) to the charge 
             or to the magnetization along the direction(s) indicated 
             by spin_component: 
             0 = charge (default), 
             1 = x, 
             2 = y, 
             3 = z. 
             
             Ignored in unpolarized or LSDA case 
             
             To plot a single component ispin, specify spin_component=ispin or spin_component(1)=ispin 
             To plot a range of components [imin, imax], specify spin_component(1)=imin and spin_component(2)=imax 


            *Others*:             Start - 1; End - 2



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._kpoint: Optional[List[int]] = kpoint
        self._kband: Optional[List[int]] = kband
        self._lsign: Optional[bool] = lsign
        self._spin_component: Optional[List[int]] = spin_component

    @property
    def kpoint(self) -> List[int]:
        """
        Info:
        ================
        
         Unpolarized and noncollinear case: 
         k-point(s) to be plotted 
         LSDA: 
         k-point(s) and spin polarization to be plotted 
         (spin-up and spin-down correspond to different k-points!) 
         
         To plot a single kpoint ikpt, specify kpoint=ikpt or kpoint(1)=ikpt 
         To plot a range of kpoints [imin, imax], specify kpoint(1)=imin and kpoint(2)=imax 


        Others:
        ================
        Start - 1; End - 2

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._kpoint

    @kpoint.setter
    def kpoint(self, value: List[int]):
        self._kpoint = value

    @property
    def kband(self) -> List[int]:
        """
        Info:
        ================
        
         Band(s) to be plotted. 
         
         To plot a single band ibnd, specify kband=ibnd or kband(1)=ibnd 
         To plot a range of bands [imin, imax], specify kband(1)=imin and kband(2)=imax 


        Others:
        ================
        Start - 1; End - 2

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._kband

    @kband.setter
    def kband(self, value: List[int]):
        self._kband = value

    @property
    def lsign(self) -> bool:
        """
        Info:
        ================
        
         if true and k point is Gamma, plot |psi|^2 sign(psi) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._lsign

    @lsign.setter
    def lsign(self, value: bool):
        self._lsign = value

    @property
    def spin_component(self) -> List[int]:
        """
        Info:
        ================
        
         **Noncollinear case only:** 
         plot the contribution of the given state(s) to the charge 
         or to the magnetization along the direction(s) indicated 
         by spin_component: 
         0 = charge (default), 
         1 = x, 
         2 = y, 
         3 = z. 
         
         Ignored in unpolarized or LSDA case 
         
         To plot a single component ispin, specify spin_component=ispin or spin_component(1)=ispin 
         To plot a range of components [imin, imax], specify spin_component(1)=imin and spin_component(2)=imax 


        Others:
        ================
        Start - 1; End - 2

        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._spin_component

    @spin_component.setter
    def spin_component(self, value: List[int]):
        self._spin_component = value

