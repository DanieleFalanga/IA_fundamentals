/***************************************
 * 			Funzioni Ausiliarie		   *
 * ************************************/

permutation([],[]).
permutation(Xs,[Z|Zs]) :- 
    select(Z,Xs,Ys), 
    permutation(Ys,Zs).

select(X,[X|Xs],Xs).
select(X,[Y|Ys],[Y|Zs]):-
    select(X,Ys,Zs).

subst(This, That, MyStr, Result) :-
    append(This, After, Rest),
    append(Before, Rest, MyStr),
    !,
    subst(This, That, After, AfterResult),
    append([Before,That,AfterResult], Result).
subst(_, _, S, S).

takeFirstList(0, _, []).
takeFirstList(Index, [Y|Ys], Zs):- 
    Ind1 is Index-1, 
    takeFirstList(Ind1, Ys, Ks), 
    append([Y], Ks, Zs).

noattack(_,[],_).
noattack(Q,[Q1|Qlist],Qdist) :-
    Q1 - Q =\= Qdist,            % check diagonal up
    Q - Q1 =\= Qdist,            % check diagonal down
    Dist1 is Qdist + 1,
    noattack(Q,Qlist,Dist1).

safe([]).
safe([Queen|OtherQueens]) :-
    safe(OtherQueens),
    noattack(Queen,OtherQueens,1).

create(Num,L):- 
    create_list(Num,[],L).

create_list(0,K,K).
create_list(Num,K,L):- Num>0,
    				 N1 is Num-1,
    				 create_list(N1,[Num|K],L).

/*ALGORITMO*/

/*prende un cristo della popolazione e vede se questo va bene, nel caso si ferma*/

evaluation([P|Population], X):-
    fitness(P, 0, Fit),
    ( Fit=\=0 -> evaluation(Population, X)).
evaluation([P|Population], X):-
    fitness(P, 0, Fit),
    ( Fit==0 ->  append(P, [], X)).




fitness_function(Q, [Q1|Qlist], Qdist, X, Y):-
    K is Q-Q1,
    H is Q1-Q,
    ( (K == Qdist; H == Qdist; Q==Q1) ->  X1 is X+1, Dist is Qdist+1, fitness_function(Q, Qlist, Dist, X1, Y);
    									  Dist is Qdist+1, fitness_function(Q, Qlist, Dist, X, Y)).
fitness_function(Q, [Q1|Qlist], Qdist, X, Y):-
    K is Q-Q1,
    H is Q1-Q,
    ( (K =\= Qdist, H =\= Qdist, Q=\=Q1) ->   Dist is Qdist+1, fitness_function(Q, Qlist, Dist, X, Y)).

fitness_function(_,[],_,X, X).
  fitness([], X, X).  
fitness([Q1|Qlist], X, Y):-
    fitness_function(Q1, Qlist, 1, 0, Z),
    X1 is X+Z,
    fitness(Qlist, X1, Y).


selection([], _, _, L1, L2, L1, L2).

selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ( ( Fit < Fit1; Fit < Fit2 ) ->  ( Fit1 > Fit2 ) ->  ( append([P], L1_aux), selection(Population, Fit, Fit2, L1_aux, L2, List1, List2))).
selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ( ( Fit < Fit1; Fit < Fit2 ) ->  ( Fit1 =< Fit2 ) ->  append([P], L2_aux), selection(Population, Fit1, Fit, L1, L2_aux, List1, List2)).
selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ( ( Fit >= Fit1, Fit >= Fit2 ) -> selection(Population, Fit1, Fit2, L1, L2, List1, List2) ).



crossover(Q1, Q2, Cross1, Cross2):-
    random(1, 4, Index2),
    length(Q2, L),
    Index1 is L-Index2,
    reverse(Q1, Help1),
    takeFirstList(Index1, Help1, F1),
    reverse(F1, Final1),
    reverse(Q2, Help2),
    takeFirstList(Index1, Help2, F2),
    reverse(F2, Final2),
    subst(Final1, Final2, Q1, Cross1),
	subst(Final2, Final1, Q2, Cross2).
        
/*Deve prendere 1 elemento a caso della lista e cambiargli valore*/

mutation(X, Xs):- 
    random(1, 5, R),
    random(1, 5, I),
	select(R, X, I, Xs).

/* MAIN */

start(Solution):-		%per scacchiera NxN, cambiare Population con N
    create(4, Q),
    reverse(Q, Qreverse),
    permutation(Q, Q1),
    permutation(Qreverse, Q2), 
  
    append([[Q1, Q2]], Population),
    four_queens(Population, Solution).

/*Soluzione nella popolazione, metti la popolazione nella Solution*/

four_queens(Population, Solution):-
    print(Population),
	( evaluation(Population, X) ->  append(X, [], Solution) ).

/*Qua fa genetic algorithm*/

four_queens(Population, Solution):-
    
	print(Population),    								
    selection(Population, 100, 100, [], [], Q1, Q2),
    crossover(Q1, Q2, Cross1, Cross2),

    mutation(Cross1, Mut1),
    mutation(Cross2, Mut2),    

    /*le append aggiungono le nuove liste trovate nella popolazione da 2 passo a 4*/

	append([Q1], [], Aux1),
    append([Q2], Aux1, Aux2),
    append([Mut1], Aux2, Aux3),
        
    append([Mut2], Aux3, New),
    
    /*prendo i migliori 2 e glielo passo all' algoritmo*/
    selection(New, 100 ,100, [], [], Queen1, Queen2),
    append([Queen1], [], B1),
    append([Queen2], B1, New_Population),
    print("Nuova popolazione:"),
    four_queens(New_Population, Solution).




