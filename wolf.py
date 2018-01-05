import wolframalpha

client = wolframalpha.Client("TP9TEK-3EUL4W3A6L")

#equation = input("Give me an equation: ")
#equation = "lim x->infinity x*e^(-2x)"
equation = "11x+18=172"
params = (
    ('podstate', 'Solution__Step-by-step+solution'),
)
res = client.query(f"{equation}", params=params)
res2 = client.query(f"{equation}")
print(res==res2)


