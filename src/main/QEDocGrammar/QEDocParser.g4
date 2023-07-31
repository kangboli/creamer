parser grammar QEDocParser;

options { tokenVocab=QEDocLexer; }

def: block;

block: plainTextBlock
     | structureBlock 
     | smartAssBlock  
     ;

plainTextBlock: IntroBegin textBlockBody   # IntroBlock
              | DefaultBegin textBlockBody # DefaultBlock
              | InfoBegin textBlockBody    # InfoBlock
              | OptBegin textBlockBody     # OptBlock
              | StatusBegin textBlockBody  # StatusBlock
              | TextBegin textBlockBody    # TextBlock
              | LabelBegin textBlockBody   # LabelBlock
              | MessageBegin textBlockBody # MessageBlock
              | TOCBegin textBlockBody     # TocBlock
              | SeeBegin textBlockBody     # SeeBlock
              | EnumBegin textBlockBody    # EnumBlock
              ;

textBlockBody: phrase* EndText;

phrase: Ref         # Ref
      | BoldText    # BoldText
      | IText       # IText
      | TTText      # TTText
      | StringText  # StringText
      | LogicalText # LogicalText
      | ScopedText  # ScopedText
      | WordText    # WordText 
      ;

structureBlock: Card structureBlockBody             # CardBlock
              | CardFlag structureBlockBody         # CardFlagBlock
              | Choose structureBlockBody           # ChooseBlock
              | Col structureBlockBody              # ColBlock
              | ColGroup structureBlockBody         # ColGroupBlock
              | Cols structureBlockBody             # ColsBlock
              | Conditional structureBlockBody      # ConditionalBlock
              | Dim structureBlockBody              # DimBlock
              | DimensionGroup structureBlockBody   # DimensionGroupBlock
              | ElseWhen structureBlockBody         # ElseWhenBlock
              | Group structureBlockBody            # GroupBlock
              | InputDescription structureBlockBody # InputDescriptionBlock
              | Line structureBlockBody             # LineBlock
              | NameList structureBlockBody         # NameListBlock
              | Optional structureBlockBody         # OptionalBlock
              | Options structureBlockBody          # OptionsBlock
              | Otherwise structureBlockBody        # OtherwiseBlock
              | Row structureBlockBody              # RowBlock
              | RowGroup structureBlockBody         # RowGroupBlock
              | Rows structureBlockBody             # RowsBlock
              | Section structureBlockBody          # SectionBlock
              | Subsection structureBlockBody       # SubsectionBlock
              | Syntax structureBlockBody           # SyntaxBlock
              | Table structureBlockBody            # TableBlock
              | Var structureBlockBody              # VarBlock
              | VarGroup structureBlockBody         # VarGroupBlock
              | When structureBlockBody             # WhenBlock
              ;

structureBlockBody: ID? SwitchText* OB block* CB;

smartAssBlock: Intro ID          # SmartIntroBlock
             | Opt ID            # SmartOptBlock
             | Default ID        # SmartDefaultBlock
             | Info ID           # SmartInfoBlock
             | Status ID         # SmartStatusBlock
             | Text ID           # SmartTextBlock
             | Label ID          # SmartLabelBlock
             | Message ID        # SmartMessageBlock
             | Enum ID           # SmartEnumBlock
             | Toc ID            # SmartTocBlock
             | See ID            # SmartSeeBlock
             | Card ID           # SmartCardBlock
             | CardFlag ID       # SmartCardFlagBlock
             | Choose ID         # SmartChooseBlock
             | Col ID            # SmartColBlock
             | ColGroup ID       # SmartColGroupBlock
             | Cols ID           # SmartColsBlock
             | Conditional ID    # SmartConditionalBlock
             | Dim ID            # SmartDimBlock
             | DimensionGroup ID # SmartDimensionGroupBlock
             | ElseWhen ID       # SmartElseWhenBlock
             | Group ID          # SmartGroupBlock
             | Line ID           # SmartLineBlock
             | NameList ID       # SmartNameListBlock
             | Optional ID       # SmartOptionalBlock
             | Options ID        # SmartOptionsBlock
             | Otherwise ID      # SmartOtherwiseBlock
             | RowGroup ID       # SmartRowGroupBlock
             | Row ID            # SmartRowBlock
             | Rows ID           # SmartRowsBlock
             | Section ID        # SmartSectionBlock
             | Subsection ID     # SmartSubsectionBlock
             | Syntax ID         # SmartSyntaxBlock
             | Table ID          # SmartTableBlock
             | VarGroup ID       # SmartVarGroupBlock
             | Var ID            # SmartVarBlock
             | When ID           # SmartWhenBlock
             ;

