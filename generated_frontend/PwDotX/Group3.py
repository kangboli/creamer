from typing import Optional, List
from .Group import Group


class Group3(Group):
    """
    Label:
    ================
    
     keywords used only in BFGS calculations 


    """

    def __init__(self,
                 upscale: Optional[float] = None,
                 bfgs_ndim: Optional[int] = None,
                 trust_radius_max: Optional[float] = None,
                 trust_radius_min: Optional[float] = None,
                 trust_radius_ini: Optional[float] = None,
                 w_1: Optional[float] = None,
                 w_2: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **upscale**: float
            *Default*:             100.D0


            *Info*:             
             Max reduction factor for ~conv_thr~ during structural optimization 
             ~conv_thr~ is automatically reduced when the relaxation 
             approaches convergence so that forces are still accurate, 
             but ~conv_thr~ will not be reduced to less that ~conv_thr~ / ~upscale.~ 



        **bfgs_ndim**: int
            *Default*:             1


            *Info*:             
             Number of old forces and displacements vectors used in the 
             PULAY mixing of the residual vectors obtained on the basis 
             of the inverse hessian matrix given by the BFGS algorithm. 
             When ~bfgs_ndim~ = 1, the standard quasi-Newton BFGS method is 
             used. 
             (bfgs only) 



        **trust_radius_max**: float
            *Default*:             0.8D0


            *Info*:             
             Maximum ionic displacement in the structural relaxation. 
             (bfgs only) 



        **trust_radius_min**: float
            *Default*:             1.D-3


            *Info*:             
             Minimum ionic displacement in the structural relaxation 
             BFGS is reset when ~trust_radius~ < ~trust_radius_min.~ 
             (bfgs only) 



        **trust_radius_ini**: float
            *Default*:             0.5D0


            *Info*:             
             Initial ionic displacement in the structural relaxation. 
             (bfgs only) 



        **w_1**: float
            *Default*:             0.01D0



        **w_2**: float
            *Default*:             0.5D0


            *Info*:             
             Parameters used in line search based on the Wolfe conditions. 
             (bfgs only) 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._upscale: Optional[float] = upscale
        self._bfgs_ndim: Optional[int] = bfgs_ndim
        self._trust_radius_max: Optional[float] = trust_radius_max
        self._trust_radius_min: Optional[float] = trust_radius_min
        self._trust_radius_ini: Optional[float] = trust_radius_ini
        self._w_1: Optional[float] = w_1
        self._w_2: Optional[float] = w_2

    @property
    def upscale(self) -> float:
        """
        Default:
        ================
        100.D0


        Info:
        ================
        
         Max reduction factor for ~conv_thr~ during structural optimization 
         ~conv_thr~ is automatically reduced when the relaxation 
         approaches convergence so that forces are still accurate, 
         but ~conv_thr~ will not be reduced to less that ~conv_thr~ / ~upscale.~ 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._upscale

    @upscale.setter
    def upscale(self, value: float):
        self._upscale = value

    @property
    def bfgs_ndim(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         Number of old forces and displacements vectors used in the 
         PULAY mixing of the residual vectors obtained on the basis 
         of the inverse hessian matrix given by the BFGS algorithm. 
         When ~bfgs_ndim~ = 1, the standard quasi-Newton BFGS method is 
         used. 
         (bfgs only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._bfgs_ndim

    @bfgs_ndim.setter
    def bfgs_ndim(self, value: int):
        self._bfgs_ndim = value

    @property
    def trust_radius_max(self) -> float:
        """
        Default:
        ================
        0.8D0


        Info:
        ================
        
         Maximum ionic displacement in the structural relaxation. 
         (bfgs only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._trust_radius_max

    @trust_radius_max.setter
    def trust_radius_max(self, value: float):
        self._trust_radius_max = value

    @property
    def trust_radius_min(self) -> float:
        """
        Default:
        ================
        1.D-3


        Info:
        ================
        
         Minimum ionic displacement in the structural relaxation 
         BFGS is reset when ~trust_radius~ < ~trust_radius_min.~ 
         (bfgs only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._trust_radius_min

    @trust_radius_min.setter
    def trust_radius_min(self, value: float):
        self._trust_radius_min = value

    @property
    def trust_radius_ini(self) -> float:
        """
        Default:
        ================
        0.5D0


        Info:
        ================
        
         Initial ionic displacement in the structural relaxation. 
         (bfgs only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._trust_radius_ini

    @trust_radius_ini.setter
    def trust_radius_ini(self, value: float):
        self._trust_radius_ini = value

    @property
    def w_1(self) -> float:
        """
        Default:
        ================
        0.01D0



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._w_1

    @w_1.setter
    def w_1(self, value: float):
        self._w_1 = value

    @property
    def w_2(self) -> float:
        """
        Default:
        ================
        0.5D0


        Info:
        ================
        
         Parameters used in line search based on the Wolfe conditions. 
         (bfgs only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._w_2

    @w_2.setter
    def w_2(self, value: float):
        self._w_2 = value

