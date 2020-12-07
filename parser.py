 from the documentation
class ExprParser(lrparsing.Grammar):
    #
    # Put Tokens we don't want to re-type in a TokenRegistry.
    #
    class T(lrparsing.TokenRegistry):
        integer = Token(re="[0-9]+")
        integer["key"] = "I'm a mapping!"
        ident = Token(re="[A-Za-z_][A-Za-z_0-9]*")
    #
    # Grammar rules.
    #
    expr = Ref("expr")                # Forward reference
    call = T.ident + '(' + List(expr, ',') + ')'
    atom = T.ident | T.integer | Token('(') + expr + ')' | call
    expr = Prio(                      # If ambiguous choose atom 1st, ...
        atom,
        Tokens("+ - ~") >> THIS,      # >> means right associative
        THIS << Tokens("* / // %") << THIS,
        THIS << Tokens("+ -") << THIS,# THIS means "expr" here
        THIS << (Tokens("== !=") | Keyword("is")) << THIS)
    expr["a"] = "I am a mapping too!"
    START = expr                      # Where the grammar must start
    COMMENTS = (                      # Allow C and Python comments
        Token(re="#(?:[^rn]*(?:rn?|nr?))") |
        Token(re="/[*](?:[^*]|[*][^/])*[*]/"))