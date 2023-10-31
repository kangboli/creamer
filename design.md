The `.def` files are basically `.json/.yaml` but worse.

## Inheritance 

To model `namelist conrol`, we need two classes. One is an abstract class
called `namelist` and the other one is `control`, where `control` inherits
`namelist`.  Similarly, to model `card atomic_species`, we have an abstract
`card` class and a concrete `atomic_species` class. In practice, the additional
keywords `namelist` and `card` are redundant, and we are keeping them for completeness.


## Group

A vargroup in the `.def` files is a few related variables such as `nx, ny`.
This is a headache since this is basically a anonymous class (also known as
named tuples), which is not available in most languages. The current approach
is to just call them `group0`, `group1`, etc, but the groups should be replaced
with a `namelist` and given a name.

## Choose

If a set of parameters can be specified in a few different ways, the `choose`
block lets you choose a way of specifying them. This is an ad-hoc way to allow
multiple constructors for the same object. Since Python doesn't support
multiple constructors (can be simulated with optional arguments to `__init__`),
we take the approach of providing multiple classes that inherit from an
abstract class that represents the choice. Here, we face the same problem as
with groups that the `choice` doesn't have a name, and we currently just name
them `choice0`, `choice1`, etc.


## Test and Strings

A design in the `.def` file that looks awful to me is that **strings have
semantics** and its not string interpolation. For example, in the `-test
"calculation == 'bands' OR calculation == 'nscf'"`, the equality and logical or
have to be tokenized and that requires an island grammar. `ANTLR` supports one
island grammar, which I'm already using for info, label, and messages.

Currently, we are not enforcing the tests because it has to be checked during
run time and we don't have an island grammar for strings.

## Some other things

- The `start` and the `end` of dimension is ignored since list/vector in Python
  and Julia are dynamically allocated. Conceivably, we could check the size
  during run time in the future, but they probably are doing that in Fortran
  already.


The output classes should not only contain the information of the `.def` file,
they also need to support behaviors such as serialization into input files.
Currently, adding behavior is done by inheritance and the implementation of
`choice` unnecessarily uses multiple inheritance, which some languages don't
support.


