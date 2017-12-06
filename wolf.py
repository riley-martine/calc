import wolframalpha

client = wolframalpha.Client("TP9TEK-3EUL4W3A6L")

#equation = input("Give me an equation: ")
equation = "lim x->infinity x*e^(-2x)"
res = client.query(f"{equation}")



