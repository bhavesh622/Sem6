go:-
    write('Enter a list'),nl,
    createList(L),nl,
    write('The list is : '),
    printList(L),nl,
    maxList(L,R),
    write('The maximum number in the list is : '),
    write(R).

    max(X,Y,Z) :- X =< Y , ! , Z = Y.
    max(X,Y,X).

    maxList([H], H):-!.
    maxList([X1,X2|T], R):- max(X1, X2, X),
                            maxList([X|T], R). 

enter(X):-
    write('Enter element:'),
    read(X).

createList(L):-
    enter(X),createList(X,L).
createList(-1,[]):-!.
createList(X,[X|T]):-
    enter(X1),createList(X1,T).

printList([]):-!.
printList([H|T]):-
    write(' '),write(H),printList(T).

:-initialization(go).