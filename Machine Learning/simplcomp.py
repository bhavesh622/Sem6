import itertools
pr,xr,tim= int(input('Enter the premium')),int(input('Enter interest rate')),int(input('Enter number of months'))
#xr= int(input('Enter interest rate'))
#tim=int(input('Enter number of months'))
def simpl(pr,xr,tim):
    return((pr * xr *tim)/100)
def comp(pr,xr,tim):
    fin=pr
    for _ in itertools.repeat(None, tim):
        fin+=(fin*xr/100)
    return(fin-pr)
print(simpl(pr,xr,tim))
print(comp(pr,xr,tim))
    
    
    
