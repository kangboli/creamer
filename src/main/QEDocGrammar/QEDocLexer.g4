lexer grammar QEDocLexer;
Comments: '#'~[\n]*'\n' -> skip;

IntroBegin: Intro WS? SwitchText* WS? OB -> pushMode(richText);
OptBegin: Opt WS? SwitchText* WS? OB -> pushMode(richText);
DefaultBegin: Default WS? SwitchText* WS? OB -> pushMode(richText);
InfoBegin: Info WS? SwitchText* WS? OB -> pushMode(richText);
StatusBegin: Status WS? SwitchText* WS? OB -> pushMode(richText);
TextBegin: Text WS? SwitchText* WS? OB -> pushMode(richText);
LabelBegin: Label WS? SwitchText* WS? OB -> pushMode(richText);
MessageBegin: Message WS? SwitchText* WS? OB -> pushMode(richText);
EnumBegin: Enum WS? SwitchText* WS? OB ->pushMode(richText);
TOCBegin: Toc WS? SwitchText* WS? OB ->pushMode(richText);
SeeBegin: See WS? SwitchText* WS? OB ->pushMode(richText);

Intro: 'intro';
Opt: 'opt';
Default: 'default';
Info: 'info';
Status: 'status';
Text: 'text';
Label: 'label';
Message: 'message';
Enum: 'enum';
Toc: 'toc';
See: 'see';

InputDescription: 'input_description';
Card: 'card';
CardFlag: 'flag';
Choose: 'choose';
Col: 'col';
ColGroup: 'colgroup';
Cols: 'cols';
Conditional: 'conditional';
Dim: ('dimension'|'multidimension');
DimensionGroup: 'dimensiongroup';
ElseWhen: 'elsewhen';
Group: 'group';
Line: 'line';
NameList: 'namelist';
Optional: 'optional';
Options: 'options';
Otherwise: 'otherwise';
RowGroup: 'rowgroup';
Row: 'row';
Rows: 'rows';
Section: 'section';
Subsection: 'subsection';
Syntax: 'syntax';
Table: 'table';
VarGroup: 'vargroup';
Var: 'var';
When: 'when';

SwitchText: Flag WS ~['"{}-]+
          | Flag WS OB ~[{}]+ CB
          | Flag WS '\'' ~[']+ '\''
          | Flag WS '"' ~["]+ '"'
          ;

Flag: '-'ID ;
String: '\''WS? (WS? ID WS?)* WS?'\'';
ID: Elem([-+]Elem)?;
fragment
Elem: [._a-zA-Z0-9()]+ ;

Semicolon: ';' -> skip;
WS : [ \t\r\n]+ -> skip;
OB: '{';
CB: '}';

mode richText;
Ref: '@ref' WST? WordText;
IText: '@i' WST? (StringText|LogicalText|ScopedText|WordText);
BoldText: '@b' WST? (StringText|LogicalText|ScopedText|WordText);
TTText: '@tt' WST? (StringText|LogicalText|ScopedText|WordText);

StringText: '\''WST? (WST? WordText WST?)* WST?'\'';
LogicalText: ('.FALSE.'|'.TRUE.');
ScopedText: '{' (WST? WordText WST?)* WST? '}';
WordText: ~[@{} \r\t\n]+ | [\n];
WST : [ \t\r]+ -> skip;
EndText: '}' -> popMode;

//Mul: '*';
//Plus: '+';
//DQ: '"';
//COMMA: ',';
//EQ: '=';
//PIPE: '|';
