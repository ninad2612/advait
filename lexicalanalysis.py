keywords = {"auto","break","case","char","const","continue","default","do",
"double","else","enum","extern","float","for","goto",
"if","int","long","register","return","short","signed",
"sizeof","static","struct","switch","typedef","union",
"unsigned","void","volatile","while","printf","scanf","%d","include","stdio.h","main"}

operators = {"+","-","*","/","<",">","=","<=",">=","==","!=","++","--","%"}

delimiters = {'(',')','{','}','[',']','"',"'",';','#',',',''}

def detect_keywords(tokens):
    return list(set(tokens) & keywords)

def detect_operators(tokens):
    return list(set(tokens) & operators)

def detect_delimiters(tokens):
    return list(set(tokens) & delimiters)

def detect_num(tokens):
    return [token for token in tokens if token.isdigit()]

def detect_identifiers(tokens):
    k = detect_keywords(tokens)
    o = detect_operators(tokens)
    d = detect_delimiters(tokens)
    n = detect_num(tokens)
    not_ident = k + o + d + n
    return [token for token in tokens if token not in not_ident]

text = input('write here: ')

tokens = ''.join(c if c not in delimiters else f' {c} ' for c in text).split()

print("Keywords: ", detect_keywords(tokens))
print("Operators: ", detect_operators(tokens))
print("Delimiters: ", detect_delimiters(tokens))
print("Identifiers: ", detect_identifiers(tokens))
print("Numbers: ", detect_num(tokens))
