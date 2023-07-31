from typing import Optional, List
import string
from .Row import Row


class KpointsRow(Row):
    """
    Others:
    ================
    -start 1 -end nks 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 xk_x: Optional[float] = None,
                 xk_y: Optional[float] = None,
                 xk_z: Optional[float] = None,
                 wk: Optional[float] = None,
                 ):
        """
        Parameters
        ----------
        **xk_x**: float
            *Info*:             
             Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
             (IBZ) of the lattice (with all symmetries) and weights (wk) 
             See the literature for lists of special points and 
             the corresponding weights. 
             
             If the symmetry is lower than the full symmetry 
             of the lattice, additional points with appropriate 
             weights are generated. Notice that such procedure 
             assumes that ONLY k-points in the IBZ are provided in input 
             
             In a non-scf calculation, weights do not affect the results. 
             If you just need eigenvalues and eigenvectors (for instance, 
             for a band-structure plot), weights can be set to any value 
             (for instance all equal to 1). 



        **xk_y**: float
            *Info*:             
             Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
             (IBZ) of the lattice (with all symmetries) and weights (wk) 
             See the literature for lists of special points and 
             the corresponding weights. 
             
             If the symmetry is lower than the full symmetry 
             of the lattice, additional points with appropriate 
             weights are generated. Notice that such procedure 
             assumes that ONLY k-points in the IBZ are provided in input 
             
             In a non-scf calculation, weights do not affect the results. 
             If you just need eigenvalues and eigenvectors (for instance, 
             for a band-structure plot), weights can be set to any value 
             (for instance all equal to 1). 



        **xk_z**: float
            *Info*:             
             Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
             (IBZ) of the lattice (with all symmetries) and weights (wk) 
             See the literature for lists of special points and 
             the corresponding weights. 
             
             If the symmetry is lower than the full symmetry 
             of the lattice, additional points with appropriate 
             weights are generated. Notice that such procedure 
             assumes that ONLY k-points in the IBZ are provided in input 
             
             In a non-scf calculation, weights do not affect the results. 
             If you just need eigenvalues and eigenvectors (for instance, 
             for a band-structure plot), weights can be set to any value 
             (for instance all equal to 1). 



        **wk**: float
            *Info*:             
             Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
             (IBZ) of the lattice (with all symmetries) and weights (wk) 
             See the literature for lists of special points and 
             the corresponding weights. 
             
             If the symmetry is lower than the full symmetry 
             of the lattice, additional points with appropriate 
             weights are generated. Notice that such procedure 
             assumes that ONLY k-points in the IBZ are provided in input 
             
             In a non-scf calculation, weights do not affect the results. 
             If you just need eigenvalues and eigenvectors (for instance, 
             for a band-structure plot), weights can be set to any value 
             (for instance all equal to 1). 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._xk_x: Optional[float] = xk_x
        self._xk_y: Optional[float] = xk_y
        self._xk_z: Optional[float] = xk_z
        self._wk: Optional[float] = wk

    @property
    def xk_x(self) -> float:
        """
        Info:
        ================
        
         Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
         (IBZ) of the lattice (with all symmetries) and weights (wk) 
         See the literature for lists of special points and 
         the corresponding weights. 
         
         If the symmetry is lower than the full symmetry 
         of the lattice, additional points with appropriate 
         weights are generated. Notice that such procedure 
         assumes that ONLY k-points in the IBZ are provided in input 
         
         In a non-scf calculation, weights do not affect the results. 
         If you just need eigenvalues and eigenvectors (for instance, 
         for a band-structure plot), weights can be set to any value 
         (for instance all equal to 1). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xk_x

    @xk_x.setter
    def xk_x(self, value: float):
        self._xk_x = value

    @property
    def xk_y(self) -> float:
        """
        Info:
        ================
        
         Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
         (IBZ) of the lattice (with all symmetries) and weights (wk) 
         See the literature for lists of special points and 
         the corresponding weights. 
         
         If the symmetry is lower than the full symmetry 
         of the lattice, additional points with appropriate 
         weights are generated. Notice that such procedure 
         assumes that ONLY k-points in the IBZ are provided in input 
         
         In a non-scf calculation, weights do not affect the results. 
         If you just need eigenvalues and eigenvectors (for instance, 
         for a band-structure plot), weights can be set to any value 
         (for instance all equal to 1). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xk_y

    @xk_y.setter
    def xk_y(self, value: float):
        self._xk_y = value

    @property
    def xk_z(self) -> float:
        """
        Info:
        ================
        
         Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
         (IBZ) of the lattice (with all symmetries) and weights (wk) 
         See the literature for lists of special points and 
         the corresponding weights. 
         
         If the symmetry is lower than the full symmetry 
         of the lattice, additional points with appropriate 
         weights are generated. Notice that such procedure 
         assumes that ONLY k-points in the IBZ are provided in input 
         
         In a non-scf calculation, weights do not affect the results. 
         If you just need eigenvalues and eigenvectors (for instance, 
         for a band-structure plot), weights can be set to any value 
         (for instance all equal to 1). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._xk_z

    @xk_z.setter
    def xk_z(self, value: float):
        self._xk_z = value

    @property
    def wk(self) -> float:
        """
        Info:
        ================
        
         Special k-points (xk_x/y/z) in the irreducible Brillouin Zone 
         (IBZ) of the lattice (with all symmetries) and weights (wk) 
         See the literature for lists of special points and 
         the corresponding weights. 
         
         If the symmetry is lower than the full symmetry 
         of the lattice, additional points with appropriate 
         weights are generated. Notice that such procedure 
         assumes that ONLY k-points in the IBZ are provided in input 
         
         In a non-scf calculation, weights do not affect the results. 
         If you just need eigenvalues and eigenvectors (for instance, 
         for a band-structure plot), weights can be set to any value 
         (for instance all equal to 1). 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._wk

    @wk.setter
    def wk(self, value: float):
        self._wk = value

