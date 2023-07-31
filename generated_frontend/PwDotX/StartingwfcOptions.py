from typing import Optional, List
from .Options import Options


class StartingwfcOptions(Options):
    """
    Others:
    ================
    Available options are:


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """
    random = 0
    """   
    Start from random wfcs. Slower start of scf but safe. 
    It may also reduce memory usage in conjunction with 
    ~diagonalization='cg'.~ 

    """
    file = 1
    """   
    Start from an existing wavefunction file in the 
    directory specified by variables ~prefix~ and ~outdir.~ 

    """
    atomic+random = 2
    """   
    As above, plus a superimposed "randomization" 
    of atomic orbitals. Prevents the "loss" of states 
    mentioned above. 

    """
    atomic = 3
    """   
    Start from superposition of atomic orbitals. 
    If not enough atomic orbitals are available, 
    fill with random numbers the remaining wfcs 
    The scf typically starts better with this option, 
    but in some high-symmetry cases one can "loose" 
    valence states, ending up in the wrong ground state. 

    """
