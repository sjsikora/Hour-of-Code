import enchant

# English dictionary
dictionary = enchant.Dict("en_US")


opratorDict = {
    "equal": "=",
    "equals": "=",

    "not equal": "=/",

    "approximately": "≈",
    "approximately equal": "≈",

    "less than": "<",
    "less than or equal to": ">=",

    "greater than": ">",
    "greater than or equal to": ">=",

    "round brackets": "(",
    "parentheses": "(",
    "parenthesis": "(",

    "end": ")",
    "end round brackets": ")",
    "end parentheses": ")",
    "end parenthesis": ")",
    "end bracket": "]",

    "and": ")",
    "and round brackets": ")",
    "and parentheses": ")",
    "and parenthesis": ")",
    "and bracket": "]",

    "plus": "+",
    "added": "+",

    "minus": "-",
    "subtracted": "-",
    "negative": "-",

    "plus and minus": "±",
    "plus or minus": "±",

    "times": "*",
    "multiplied": "*",

    "slash": "/",
    "divided": "/",

    "dot": ".",
    "period": ".",
    "point": ".",

    "the power": "^",
    "exponent": "^",
    "caret": "^",

    "percent": "%",
    "pi": "π",
    "pie": "π",
    "delta": "∆",
    "infinity": "∞",
    "prime": "'",


    "cube root": "^(1/3)",
    "fourth root": "^(1/4)",
    "fifth root": "^(1/5)",
    "sixth root": "^(1/6)",
    "seventh root": "^(1/7)",
    "eighth root": "^(1/8)",
    "ninth root": "^(1/9)",
    "tenth root": "^(1/10)",

}


operationsDict = {
    
    "square root": "sqrt",

    "sine": "sin",
    "arc sine": "arcsin",
    "sine inverse": "arcsin",
    "arcsin": "arcsin",

    "cosine": "cos",
    "arc cosine": "arccos",
    "cosine inverse": "arcos",
    "arccos": "arccos",

    "tan": "tan",
    "arc tan": "arctan",
    "tan inverse": "arctan",
    "arctan": "arctan",
    "caught": "cot",

    "tangent": "tan",
    "arc tangent": "arctan",
    "tangent inverse": "arctan",
    "arctangent": "arctangent",

    "natural log": "ln",

    "break": "\n"
    
}

vaildSymbols = [
    "+",
    "-",
    "*",
    "/",
    "=",
    "±",
    ".",
    "^",
    "√",
    "π",
    "∆",
    "%",
    "∞"
]
