from typing import Optional, List
from .Namelist import Namelist
from .Choice0 import Choice0


class Inputpp(Namelist):
    """
    """

    def __init__(self,
                 prefix: Optional[str] = None,
                 outdir: Optional[str] = None,
                 filplot: Optional[str] = None,
                 plot_num: Optional[int] = None,
                 choice0: Optional[Choice0] = Choice0(),
                 ):
        """
        Parameters
        ----------
        **prefix**: str
            *Info*:             
             prefix of files saved by program pw.x 



        **outdir**: str
            *Default*:             
             value of the `t ESPRESSO_TMPDIR` environment variable if set; 
             current directory ('./') otherwise 


            *Info*:             
             directory containing the input data, i.e. the same as in pw.x 



        **filplot**: str
            *Info*:             
             file "filplot" contains the quantity selected by plot_num 
             (can be saved for further processing) 



        **plot_num**: int
            *Info*:             
             Selects what to save in filplot: 
             
             0 = electron (pseudo-)charge density 
             
             1 = total potential V_bare + V_H + V_xc 
             
             2 = local ionic potential V_bare 
             
             3 = local density of states at specific energy or grid of energies 
             (number of states per volume, in bohr^3, per energy unit, in Ry) 
             
             4 = local density of electronic entropy 
             
             5 = STM images 
             Tersoff and Hamann, PRB 31, 805 (1985) 
             
             6 = spin polarization (rho(up)-rho(down)) 
             
             7 = contribution of selected wavefunction(s) to the 
             (pseudo-)charge density. For norm-conserving PPs, 
             |psi|^2 (psi=selected wavefunction). Noncollinear case: 
             contribution of the given state to the charge or 
             to the magnetization along the direction indicated 
             by spin_component (0 = charge, 1 = x, 2 = y, 3 = z ) 
             
             8 = electron localization function (ELF) 
             
             9 = charge density minus superposition of atomic densities 
             
             10 = integrated local density of states (ILDOS) 
             from ~emin~ to ~emax~ (emin, emax in eV) 
             if ~emax~ is not specified, ~emax=E_fermi~ 
             
             11 = the V_bare + V_H potential 
             
             12 = the sawtooth electric field potential (if present) 
             
             13 = the noncollinear magnetization. 
             
             17 = all-electron valence charge density 
             can be performed for PAW calculations only 
             requires a very dense real-space grid! 
             
             18 = The exchange and correlation magnetic field in the noncollinear case 
             
             19 = Reduced density gradient 
             ( J. Chem. Theory Comput. 7, 625 (2011), doi:10.1021/ct100641a ) 
             Set the isosurface between 0.3 and 0.6 to plot the 
             non-covalent interactions (see also plot_num = 20) 
             
             20 = Product of the electron density (charge) and the second 
             eigenvalue of the electron-density Hessian matrix; 
             used to colorize the RDG plot (plot_num = 19) 
             
             21 = all-electron charge density (valence+core). 
             For PAW calculations only; requires a very dense real-space grid. 
             
             22 = kinetic energy density (for meta-GGA and XDM only) 



        **choice0**: Choice0

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._prefix: Optional[str] = prefix
        self._outdir: Optional[str] = outdir
        self._filplot: Optional[str] = filplot
        self._plot_num: Optional[int] = plot_num
        self._choice0: Optional[Choice0] = choice0

    @property
    def prefix(self) -> str:
        """
        Info:
        ================
        
         prefix of files saved by program pw.x 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._prefix

    @prefix.setter
    def prefix(self, value: str):
        self._prefix = value

    @property
    def outdir(self) -> str:
        """
        Default:
        ================
        
         value of the `t ESPRESSO_TMPDIR` environment variable if set; 
         current directory ('./') otherwise 


        Info:
        ================
        
         directory containing the input data, i.e. the same as in pw.x 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._outdir

    @outdir.setter
    def outdir(self, value: str):
        self._outdir = value

    @property
    def filplot(self) -> str:
        """
        Info:
        ================
        
         file "filplot" contains the quantity selected by plot_num 
         (can be saved for further processing) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._filplot

    @filplot.setter
    def filplot(self, value: str):
        self._filplot = value

    @property
    def plot_num(self) -> int:
        """
        Info:
        ================
        
         Selects what to save in filplot: 
         
         0 = electron (pseudo-)charge density 
         
         1 = total potential V_bare + V_H + V_xc 
         
         2 = local ionic potential V_bare 
         
         3 = local density of states at specific energy or grid of energies 
         (number of states per volume, in bohr^3, per energy unit, in Ry) 
         
         4 = local density of electronic entropy 
         
         5 = STM images 
         Tersoff and Hamann, PRB 31, 805 (1985) 
         
         6 = spin polarization (rho(up)-rho(down)) 
         
         7 = contribution of selected wavefunction(s) to the 
         (pseudo-)charge density. For norm-conserving PPs, 
         |psi|^2 (psi=selected wavefunction). Noncollinear case: 
         contribution of the given state to the charge or 
         to the magnetization along the direction indicated 
         by spin_component (0 = charge, 1 = x, 2 = y, 3 = z ) 
         
         8 = electron localization function (ELF) 
         
         9 = charge density minus superposition of atomic densities 
         
         10 = integrated local density of states (ILDOS) 
         from ~emin~ to ~emax~ (emin, emax in eV) 
         if ~emax~ is not specified, ~emax=E_fermi~ 
         
         11 = the V_bare + V_H potential 
         
         12 = the sawtooth electric field potential (if present) 
         
         13 = the noncollinear magnetization. 
         
         17 = all-electron valence charge density 
         can be performed for PAW calculations only 
         requires a very dense real-space grid! 
         
         18 = The exchange and correlation magnetic field in the noncollinear case 
         
         19 = Reduced density gradient 
         ( J. Chem. Theory Comput. 7, 625 (2011), doi:10.1021/ct100641a ) 
         Set the isosurface between 0.3 and 0.6 to plot the 
         non-covalent interactions (see also plot_num = 20) 
         
         20 = Product of the electron density (charge) and the second 
         eigenvalue of the electron-density Hessian matrix; 
         used to colorize the RDG plot (plot_num = 19) 
         
         21 = all-electron charge density (valence+core). 
         For PAW calculations only; requires a very dense real-space grid. 
         
         22 = kinetic energy density (for meta-GGA and XDM only) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._plot_num

    @plot_num.setter
    def plot_num(self, value: int):
        self._plot_num = value

    @property
    def choice0(self) -> Choice0:
        """
        """
        return self._choice0

    @choice0.setter
    def choice0(self, value: Choice0):
        self._choice0 = value

