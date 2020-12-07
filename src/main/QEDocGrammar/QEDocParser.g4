parser grammar QEDocParser;

options { tokenVocab=QEDocLexer; }

def: preamble OB block+ CB;

preamble: InputDiscription preambleFlag+;
preambleFlag: Flag ID
             | distribution
             ;
distribution: DistributionBegin phrase* EndText;

block: TOC
    | intro
    | nameList
    | section
    | card
        ;

intro: IntroBegin phrase* EndText;

nameList: NameList ID OB nameListEntry* CB ;

nameListEntry: variable
            | nameListGroup
            | label
            ;
nameListGroup: Group OB nameListGroupEntry* CB;
nameListGroupEntry: label
                    | variable
                    ;
variable: varSingle
        | varGroup
        ;
varSingle: (Var|Dim) ID (Flag args)* OB variableContent* CB;
args: args Plus args
    | args Mul args
    | args ArgOr args
    | args COMMA args
    | ID;
varGroup: VarGroup (Flag ID)* OB variableDeclaration* variableContent* CB;
variableDeclaration: Var ID;
variableContent: default
               | info
               | status
               | opts
               | see
               ;

see: See OB ID (COMMA ID)* CB;
default: DefaultBegin phrase* EndText ;
opts: Options OB optContent* CB;
optContent: opt
          | info
          ;
info: InfoBegin phrase* EndText;
opt: OptBegin phrase* EndText;
status: StatusBegin phrase* EndText;
//card: 'card' Word '{' cardFlag cardLabel cardSyntax '}';

phrase:  Ref
        | BoldText
        | IText
        | TTText
        | StringText
        | LogicalText
        | ScopedText
        | WordText
        ;

section: Section title OB sectionContent* CB;
sectionContent: text
               | subsection;
text: TextBegin phrase* EndText;
subsection: Subsection title OB text* CB;
title: simpleTitle
    | scopedTitle ;
simpleTitle: Flag ID;
scopedTitle: ScopedTitleBegin phrase* EndText;

card: Card ID OB cardEntry* CB;
cardEntry: cardFlag
         | syntax
         | choose
         | message
         | label
         ;
cardFlag: CardFlag ID (OptionalSwitch|Flag ID) OB flagEntry* CB;
flagEntry: enum
         | default
         | opts
         | info
         ;

label: LabelBegin phrase* EndText;
message: MessageBegin phrase* EndText;

enum: Enum OB (ID PIPE)* ID CB;
choose: Choose OB when elsewhen* otherwise? CB;

when: When ConditionalPredicates OB syntax CB;
elsewhen: ElseWhen ConditionalPredicates OB syntax CB;
otherwise: Otherwise OB syntax CB;

syntax: Syntax (Flag OB (ID PIPE)* ID CB)? OB syntaxEntry* CB
        | message;
syntaxEntry: line
            | table;

line: Line OB lineContent+ CB;
lineContent: variable
            | optional;

optional: Optional OB variable+ CB
        | Optional OB innerGroup+ CB
        | Optional OB innerVar+ CB
        ;

table: Table ID OB outer CB;
outer: (Rows|Cols) (Flag ID)* OB inner+ CB;
inner: innerVar
     | conditional
     | innerGroup
     | optional
     ;

innerVar: (Row|Col) ID (Flag ID)* OB opts? info? CB;
conditional: Conditional OB innerVar CB
           | Conditional OB innerGroup CB
           | Conditional OB groupVar* CB;

innerGroup: (RowGroup|ColGroup) (Flag ID)* OB groupEntry+ CB;
groupEntry: groupVar
            | info
            | conditional
            | default
            ;
groupVar: (Row|Col) ID;