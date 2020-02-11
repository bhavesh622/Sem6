splitlist(L,0,[],L).
splitlist([H|T1],N, [H|T2],L2):- N>0,
                                N1 is N-1,
                                splitlist(T1, N1,T2, L2 ).