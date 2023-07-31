from typing import Optional, List
from .Namelist import Namelist
from .Group0 import Group0
from .InterpolationOptions import InterpolationOptions
from .Choice1 import Choice1


class Plot(Namelist):
    """
    """

    def __init__(self,
                 nfile: Optional[int] = None,
                 iflag: Optional[int] = None,
                 output_format: Optional[int] = None,
                 fileout: Optional[str] = None,
                 interpolation: Optional[InterpolationOptions] = None,
                 choice1: Optional[Choice1] = Choice1(),
                 ):
        """
        Parameters
        ----------
        **nfile**: int
            *Info*:             
             the number of data files to read 



        **iflag**: int
            *Info*:             
             0 = 1D plot of the spherical average 
             1 = 1D plot 
             2 = 2D plot 
             3 = 3D plot 
             4 = 2D polar plot on a sphere 



        **output_format**: int
            *Info*:             
             (ignored on 1D plot) 
             
             0 = format suitable for gnuplot (1D) 
             
             1 = obsolete format no longer supported 
             
             2 = format suitable for plotrho (2D) 
             
             3 = format suitable for XCRYSDEN (2D or user-supplied 3D region) 
             
             4 = obsolete format no longer supported 
             
             5 = format suitable for XCRYSDEN (3D, using entire FFT grid) 
             
             6 = format as gaussian cube file (3D) 
             (can be read by many programs) 
             
             7 = format suitable for gnuplot (2D) x, y, f(x,y) 



        **fileout**: str
            *Default*:             standard output


            *Info*:             
             name of the file to which the plot is written 



        **interpolation**: InterpolationOptions
            *Default*:             'fourier'



        **choice1**: Choice1

            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._nfile: Optional[int] = nfile
        self._iflag: Optional[int] = iflag
        self._output_format: Optional[int] = output_format
        self._fileout: Optional[str] = fileout
        self._interpolation: Optional[InterpolationOptions] = interpolation
        self._choice1: Optional[Choice1] = choice1

    @property
    def nfile(self) -> int:
        """
        Info:
        ================
        
         the number of data files to read 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._nfile

    @nfile.setter
    def nfile(self, value: int):
        self._nfile = value

    @property
    def iflag(self) -> int:
        """
        Info:
        ================
        
         0 = 1D plot of the spherical average 
         1 = 1D plot 
         2 = 2D plot 
         3 = 3D plot 
         4 = 2D polar plot on a sphere 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._iflag

    @iflag.setter
    def iflag(self, value: int):
        self._iflag = value

    @property
    def output_format(self) -> int:
        """
        Info:
        ================
        
         (ignored on 1D plot) 
         
         0 = format suitable for gnuplot (1D) 
         
         1 = obsolete format no longer supported 
         
         2 = format suitable for plotrho (2D) 
         
         3 = format suitable for XCRYSDEN (2D or user-supplied 3D region) 
         
         4 = obsolete format no longer supported 
         
         5 = format suitable for XCRYSDEN (3D, using entire FFT grid) 
         
         6 = format as gaussian cube file (3D) 
         (can be read by many programs) 
         
         7 = format suitable for gnuplot (2D) x, y, f(x,y) 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._output_format

    @output_format.setter
    def output_format(self, value: int):
        self._output_format = value

    @property
    def fileout(self) -> str:
        """
        Default:
        ================
        standard output


        Info:
        ================
        
         name of the file to which the plot is written 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._fileout

    @fileout.setter
    def fileout(self, value: str):
        self._fileout = value

    @property
    def interpolation(self) -> InterpolationOptions:
        """
        Default:
        ================
        'fourier'



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._interpolation

    @interpolation.setter
    def interpolation(self, value: InterpolationOptions):
        self._interpolation = value

    @property
    def choice1(self) -> Choice1:
        """
        """
        return self._choice1

    @choice1.setter
    def choice1(self, value: Choice1):
        self._choice1 = value

