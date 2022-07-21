import nltk


grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked" | 'likes' 
  NP -> "Sarah" | "Jane" | "I" |  Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N ->  "dog" | "cat"  | "sushi" | "me" 
  P -> "in"  
  """)

sent = "Sarah saw Jane".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = "I walked the dog".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = "Jane likes the cat".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = "I ate the sushi".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

sent = "Jane saw the sushi".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)

