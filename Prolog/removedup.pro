go:-
    write('Enter a list'),nl,
    createList(L),nl,
    write('The list is : '),
    printList(L),nl,
    remove_dup(L,R),
    write('The list after removing duplicate is : '),
    printList(R).

memb([],Y):-!,fail.
memb([X|T],X):-!.
memb([X|T],Y):-
    memb(T,Y).

remove_dup([],[]).
remove_dup([X|T],T1):-
    memb(T,X),!,
    remove_dup(T,T1).
remove_dup([X|T],[X|T1]):-
    remove_dup(T,T1).
    

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