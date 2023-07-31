# Creamer for Quantum Espresso 

## Intro

This DSL is created by parsing the `.def` files with `ANTLR4` and generating an OOP Python framework.
This is rather different from writing the Quantum Espresso input file
as a Python dictionary in the sense that we treat the input options as code
instead of data. The benefits are

1. Autocompletion: The available fields of a block as well as their possible options shows up as autocompletion.
2. Syntax checking: Your editor gives you a warning if you
   1. put in a field that does not exist or in the wrong block.
   2. put in the wrong type for a parameter.
   3. put in a string that is not an available option.
3. Quick documentation: The description and type of each field of the input pops up through quick documentation.

The most common feedback I got on this is that quantum espresso has "hidden parameters".
The obvious solution is to add a "hidden_parameters" field as a dictionary,
but I think supporting hidden parameters in any shape or form is a questionable idea.

## Project Structure

The `ANTLR4` grammar is in `src/main/QEDocGrammar/QEDocLexer.g4`,
and `src/main/QEDocGrammar/QEDocParser.g4`.
The gradle tasks `compileQELexer` and `compileQEParser`
compiles the `.g4` grammar into a base parser in
`src/main/java/GeneratedQEGrammar`. The actual implementation
are subclasses of the base grammar and I put them in `src/main/java/DSLGen`.
All of this get compiled to a `.jar` that compiles 
a `.def` file into a python library. The Python code generation is handled
by the `freemarker` template engine and the template is in `src/main/resources/frontendTemplates`

The choice of Java is not ideal because no one in this field
uses Java. I used it because the `ANTLR` book is written with only Java examples.
The choice of `ANTLR` is because its the easiest-to-use  one 
I could find largely due to its excellent documentation
and editor integration.

The generated output is in `generated_frontend`, and
you can already use them to build a quantum espresso input.
I haven't built the code to 




