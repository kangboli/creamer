from typing import Optional, List
import string
from .Row import Row


class AtomicCoordinatesRow(Row):
    """
    Others:
    ================
    -start 1 -end nat 


    Quantum Espresso Version:
    =========================
    Not yet implemented.
    """

    def __init__(self,
                 X: Optional[string] = None,
                 x: Optional[float] = None,
                 y: Optional[float] = None,
                 z: Optional[float] = None,
                 if_pos__lp__1__rp__: Optional[int] = None,
                 if_pos__lp__2__rp__: Optional[int] = None,
                 if_pos__lp__3__rp__: Optional[int] = None,
                 ):
        """
        Parameters
        ----------
        **X**: string
            *Info*:             label of the atom as specified in ~ATOMIC_SPECIES~



        **x**: float
            *Info*:             
             atomic positions 
             
             NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
             To be interpreted correctly expression must NOT contain any blank 
             space and must NOT start with a "+" sign. The available expressions are: 
             
             + (plus), - (minus), / (division), * (multiplication), ^ (power) 
             
             All numerical constants included are considered as double-precision numbers; 
             i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
             not available, although sqrt can be replaced with ^(1/2). 
             
             Example: 
             C 1/3 1/2*3^(-1/2) 0 
             
             is equivalent to 
             
             C 0.333333 0.288675 0.000000 
             
             Please note that this feature is NOT supported by XCrysDen (which will 
             display a wrong structure, or nothing at all). 
             
             When atomic positions are of type crystal_sg coordinates can be given 
             in the following four forms (Wyckoff positions): 
             C 1a 
             C 8g x 
             C 24m x y 
             C 48n x y z 
             The first form must be used when the Wyckoff letter determines uniquely 
             all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
             coordinates respectively are needed. 
             
             The forms: 
             C 8g x x x 
             C 24m x x y 
             are not allowed, but 
             C x x x 
             C x x y 
             C x y z 
             are correct. 



        **y**: float
            *Info*:             
             atomic positions 
             
             NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
             To be interpreted correctly expression must NOT contain any blank 
             space and must NOT start with a "+" sign. The available expressions are: 
             
             + (plus), - (minus), / (division), * (multiplication), ^ (power) 
             
             All numerical constants included are considered as double-precision numbers; 
             i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
             not available, although sqrt can be replaced with ^(1/2). 
             
             Example: 
             C 1/3 1/2*3^(-1/2) 0 
             
             is equivalent to 
             
             C 0.333333 0.288675 0.000000 
             
             Please note that this feature is NOT supported by XCrysDen (which will 
             display a wrong structure, or nothing at all). 
             
             When atomic positions are of type crystal_sg coordinates can be given 
             in the following four forms (Wyckoff positions): 
             C 1a 
             C 8g x 
             C 24m x y 
             C 48n x y z 
             The first form must be used when the Wyckoff letter determines uniquely 
             all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
             coordinates respectively are needed. 
             
             The forms: 
             C 8g x x x 
             C 24m x x y 
             are not allowed, but 
             C x x x 
             C x x y 
             C x y z 
             are correct. 



        **z**: float
            *Info*:             
             atomic positions 
             
             NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
             To be interpreted correctly expression must NOT contain any blank 
             space and must NOT start with a "+" sign. The available expressions are: 
             
             + (plus), - (minus), / (division), * (multiplication), ^ (power) 
             
             All numerical constants included are considered as double-precision numbers; 
             i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
             not available, although sqrt can be replaced with ^(1/2). 
             
             Example: 
             C 1/3 1/2*3^(-1/2) 0 
             
             is equivalent to 
             
             C 0.333333 0.288675 0.000000 
             
             Please note that this feature is NOT supported by XCrysDen (which will 
             display a wrong structure, or nothing at all). 
             
             When atomic positions are of type crystal_sg coordinates can be given 
             in the following four forms (Wyckoff positions): 
             C 1a 
             C 8g x 
             C 24m x y 
             C 48n x y z 
             The first form must be used when the Wyckoff letter determines uniquely 
             all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
             coordinates respectively are needed. 
             
             The forms: 
             C 8g x x x 
             C 24m x x y 
             are not allowed, but 
             C x x x 
             C x x y 
             C x y z 
             are correct. 



        **if_pos__lp__1__rp__**: int
            *Default*:             1


            *Info*:             
             component i of the force for this atom is multiplied by if_pos(i), 
             which must be either 0 or 1. Used to keep selected atoms and/or 
             selected components fixed in MD dynamics or 
             structural optimization run. 
             
             With crystal_sg atomic coordinates the constraints are copied in all equivalent 
             atoms. 



        **if_pos__lp__2__rp__**: int
            *Default*:             1


            *Info*:             
             component i of the force for this atom is multiplied by if_pos(i), 
             which must be either 0 or 1. Used to keep selected atoms and/or 
             selected components fixed in MD dynamics or 
             structural optimization run. 
             
             With crystal_sg atomic coordinates the constraints are copied in all equivalent 
             atoms. 



        **if_pos__lp__3__rp__**: int
            *Default*:             1


            *Info*:             
             component i of the force for this atom is multiplied by if_pos(i), 
             which must be either 0 or 1. Used to keep selected atoms and/or 
             selected components fixed in MD dynamics or 
             structural optimization run. 
             
             With crystal_sg atomic coordinates the constraints are copied in all equivalent 
             atoms. 



            Quantum Espresso Version
            ------------------------
            Not yet implemented.
        """
        self._X: Optional[string] = X
        self._x: Optional[float] = x
        self._y: Optional[float] = y
        self._z: Optional[float] = z
        self._if_pos__lp__1__rp__: Optional[int] = if_pos__lp__1__rp__
        self._if_pos__lp__2__rp__: Optional[int] = if_pos__lp__2__rp__
        self._if_pos__lp__3__rp__: Optional[int] = if_pos__lp__3__rp__

    @property
    def X(self) -> string:
        """
        Info:
        ================
        label of the atom as specified in ~ATOMIC_SPECIES~



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._X

    @X.setter
    def X(self, value: string):
        self._X = value

    @property
    def x(self) -> float:
        """
        Info:
        ================
        
         atomic positions 
         
         NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
         To be interpreted correctly expression must NOT contain any blank 
         space and must NOT start with a "+" sign. The available expressions are: 
         
         + (plus), - (minus), / (division), * (multiplication), ^ (power) 
         
         All numerical constants included are considered as double-precision numbers; 
         i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
         not available, although sqrt can be replaced with ^(1/2). 
         
         Example: 
         C 1/3 1/2*3^(-1/2) 0 
         
         is equivalent to 
         
         C 0.333333 0.288675 0.000000 
         
         Please note that this feature is NOT supported by XCrysDen (which will 
         display a wrong structure, or nothing at all). 
         
         When atomic positions are of type crystal_sg coordinates can be given 
         in the following four forms (Wyckoff positions): 
         C 1a 
         C 8g x 
         C 24m x y 
         C 48n x y z 
         The first form must be used when the Wyckoff letter determines uniquely 
         all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
         coordinates respectively are needed. 
         
         The forms: 
         C 8g x x x 
         C 24m x x y 
         are not allowed, but 
         C x x x 
         C x x y 
         C x y z 
         are correct. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        """
        Info:
        ================
        
         atomic positions 
         
         NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
         To be interpreted correctly expression must NOT contain any blank 
         space and must NOT start with a "+" sign. The available expressions are: 
         
         + (plus), - (minus), / (division), * (multiplication), ^ (power) 
         
         All numerical constants included are considered as double-precision numbers; 
         i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
         not available, although sqrt can be replaced with ^(1/2). 
         
         Example: 
         C 1/3 1/2*3^(-1/2) 0 
         
         is equivalent to 
         
         C 0.333333 0.288675 0.000000 
         
         Please note that this feature is NOT supported by XCrysDen (which will 
         display a wrong structure, or nothing at all). 
         
         When atomic positions are of type crystal_sg coordinates can be given 
         in the following four forms (Wyckoff positions): 
         C 1a 
         C 8g x 
         C 24m x y 
         C 48n x y z 
         The first form must be used when the Wyckoff letter determines uniquely 
         all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
         coordinates respectively are needed. 
         
         The forms: 
         C 8g x x x 
         C 24m x x y 
         are not allowed, but 
         C x x x 
         C x x y 
         C x y z 
         are correct. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    @property
    def z(self) -> float:
        """
        Info:
        ================
        
         atomic positions 
         
         NOTE: each atomic coordinate can also be specified as a simple algebraic expression. 
         To be interpreted correctly expression must NOT contain any blank 
         space and must NOT start with a "+" sign. The available expressions are: 
         
         + (plus), - (minus), / (division), * (multiplication), ^ (power) 
         
         All numerical constants included are considered as double-precision numbers; 
         i.e. 1/2 is 0.5, not zero. Other functions, such as sin, sqrt or exp are 
         not available, although sqrt can be replaced with ^(1/2). 
         
         Example: 
         C 1/3 1/2*3^(-1/2) 0 
         
         is equivalent to 
         
         C 0.333333 0.288675 0.000000 
         
         Please note that this feature is NOT supported by XCrysDen (which will 
         display a wrong structure, or nothing at all). 
         
         When atomic positions are of type crystal_sg coordinates can be given 
         in the following four forms (Wyckoff positions): 
         C 1a 
         C 8g x 
         C 24m x y 
         C 48n x y z 
         The first form must be used when the Wyckoff letter determines uniquely 
         all three coordinates, forms 2,3,4 when the Wyckoff letter and 1,2,3 
         coordinates respectively are needed. 
         
         The forms: 
         C 8g x x x 
         C 24m x x y 
         are not allowed, but 
         C x x x 
         C x x y 
         C x y z 
         are correct. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._z

    @z.setter
    def z(self, value: float):
        self._z = value

    @property
    def if_pos__lp__1__rp__(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         component i of the force for this atom is multiplied by if_pos(i), 
         which must be either 0 or 1. Used to keep selected atoms and/or 
         selected components fixed in MD dynamics or 
         structural optimization run. 
         
         With crystal_sg atomic coordinates the constraints are copied in all equivalent 
         atoms. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._if_pos__lp__1__rp__

    @if_pos__lp__1__rp__.setter
    def if_pos__lp__1__rp__(self, value: int):
        self._if_pos__lp__1__rp__ = value

    @property
    def if_pos__lp__2__rp__(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         component i of the force for this atom is multiplied by if_pos(i), 
         which must be either 0 or 1. Used to keep selected atoms and/or 
         selected components fixed in MD dynamics or 
         structural optimization run. 
         
         With crystal_sg atomic coordinates the constraints are copied in all equivalent 
         atoms. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._if_pos__lp__2__rp__

    @if_pos__lp__2__rp__.setter
    def if_pos__lp__2__rp__(self, value: int):
        self._if_pos__lp__2__rp__ = value

    @property
    def if_pos__lp__3__rp__(self) -> int:
        """
        Default:
        ================
        1


        Info:
        ================
        
         component i of the force for this atom is multiplied by if_pos(i), 
         which must be either 0 or 1. Used to keep selected atoms and/or 
         selected components fixed in MD dynamics or 
         structural optimization run. 
         
         With crystal_sg atomic coordinates the constraints are copied in all equivalent 
         atoms. 



        Quantum Espresso Version:
        =========================
        Not yet implemented.
        """
        return self._if_pos__lp__3__rp__

    @if_pos__lp__3__rp__.setter
    def if_pos__lp__3__rp__(self, value: int):
        self._if_pos__lp__3__rp__ = value

