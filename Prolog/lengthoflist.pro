len_of(L,K):-len_of(L,0,K).
len_of([],K,K).
len_of([_|T],K1,K):-F is K1+1,
                    len_of(T,F,K).