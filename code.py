def function1(a):
    '''
    Count the number of distinct elements in a string list.
    
    Parameters
    ----------
    a :   [str]
    
    Returns
    -------
    {str : int}
        the count of distinct elements in a string list
    '''
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    '''
    Print the prabablity of each string character.
    '''
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
