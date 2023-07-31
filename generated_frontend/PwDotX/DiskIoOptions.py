from typing import Optional, List
from .Options import Options


class DiskIoOptions(Options):
    """
    Others:
    ================
    
     Specifies the amount of disk I/O activity: 
     (only for binary files and xml data file in data directory; 
     other files printed at each molecular dynamics / structural 
     optimization step are not controlled by this option ) 
    
     **Default** is **'low'** for the scf case, **'medium' otherwise.
                        Note that the needed RAM increases as disk I/O decreases!
                        It is no longer needed to specify 'high'** in order to be able 
     to restart from an interrupted calculation (see ~restart_mode)~ 
     but you cannot restart in ~disk_io=='nowf'~ or 'none' 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    high = 0
    """   
    save charge to disk at each SCF step, 
    keep wavefunctions on disk (in "distributed" format), 
    save mixing data as well. 
    Do not use this option unless you have a good reason to 

    """
    nowf = 1
    """   
    save to disk only the xml data file, 
    never save wavefunctions and charge density 

    """
    low = 2
    """   
    save charge to disk at each SCF step, 
    keep wavefunctions in memory (for all k-points), 
    save them to disk only at the end (in "portable" format). 
    Reduces I/O but increases memory wrt the previous cases 

    """
    medium = 3
    """   
    save charge to disk at each SCF step, 
    keep wavefunctions on disk only if more than one k-point, 
    per process is present, otherwise keep them in memory; 
    save them to disk only at the end (in "portable" format) 

    """
    none = 4
    """   
    do not save anything to disk 

    """
