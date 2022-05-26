:-use_rendering(chess).
:-use_module(library(random)).


/*utils*/

permutation([],[]).
permutation(Xs,[Z|Zs]) :- 
    select(Z,Xs,Ys), 
    permutation(Ys,Zs).


subst(This, That, MyStr, Result) :-
    append(This, After, Rest),
    append(Before, Rest, MyStr),
    !,
    subst(This, That, After, AfterResult),
    append([Before,That,AfterResult], Result).
subst(_, _, S, S).

sublist(0, _, []).
sublist(I, [Y|Ys], Zs):- 
    Ind1 is I-1,
    sublist(Ind1, Ys, Ks), 
    append([Y], Ks, Zs).

gen(Num,L):- 
    gen_list(Num,[],L).

gen_list(0,K,K).
gen_list(Num,K,L):- 
    Num>0,
    N1 is Num-1,
    gen_list(N1,[Num|K],L).

/*ALGORITMO*/

/*seleziona un elemento della popolazione, testa se questo se va bene,
    se si, passo passo base, lo inserisce in una lista vuota e restituisce X, si ferma
    altrimenti chiama ricorsivamente sul resto della lista
*/

isResult([P|_], X):-
    fitness(P, 0, Fit),
    (Fit==0 ->  append(P, [], X)).
isResult([P|Population], X):-
    fitness(P, 0, Fit),
    (Fit=\=0 -> isResult(Population, X)).

/*La fitness function fa check delle collisioni e ne salva il numero, 
utile per fare selection dei migliori*/

fitness_function(Q, [Q1|Qlist], Qdist, X, Y):-
    K is Q-Q1,
    H is Q1-Q,
    ((K == Qdist; H == Qdist; Q==Q1) ->  
        X1 is X+1, 
        Dist is Qdist+1, 
        fitness_function(Q, Qlist, Dist, X1, Y);
    Dist is Qdist+1, 
    fitness_function(Q, Qlist, Dist, X, Y)).

fitness_function(Q, [Q1|Qlist], Qdist, X, Y):-
    K is Q-Q1,
    H is Q1-Q,
    ((K =\= Qdist, H =\= Qdist, Q=\=Q1) ->   
        Dist is Qdist+1, 
        fitness_function(Q, Qlist, Dist, X, Y)).

fitness_function(_,[],_,X, X).
  fitness([], X, X).  

fitness([Q1|Qlist], X, Y):-
    fitness_function(Q1, Qlist, 1, 0, Z),
    X1 is X+Z,
    fitness(Qlist, X1, Y).


/*Prende i 2 migliori della poplazione*/

selection([], _, _, L1, L2, L1, L2).

selection([P|Population], Fit1, Fit2, _, L2, List1, List2):-
    fitness(P, 0, Fit),
    (( Fit < Fit1; Fit < Fit2 ) ->  ( Fit1 > Fit2 ) ->  
        ( append([P], L1_aux), 
        selection(Population, Fit, Fit2, L1_aux, L2, List1, List2))).

selection([P|Population], Fit1, Fit2, L1, _, List1, List2):-
    fitness(P, 0, Fit),
    (( Fit < Fit1; Fit < Fit2 ) ->  ( Fit1 =< Fit2 ) ->  
        append([P], L2_aux), 
        selection(Population, Fit1, Fit, L1, L2_aux, List1, List2)).

selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    (( Fit >= Fit1, Fit >= Fit2 ) -> 
        selection(Population, Fit1, Fit2, L1, L2, List1, List2) ).



crossover(Q1, Q2, Cross1, Cross2):-            
    random(1, 4, I2),                          % Scelgo numero random
    length(Q2, L),                             % calcolo lunghezza di Q2 e salvo in L
    I1 is L-I2,                                % Salvo la differenza tra 
    reverse(Q1, Aux1),                         % salvo l'inversa di Q1 in Help1
    sublist(I1, Aux1, F1),                     % prendo la sotto lista di Aux1 fino a I1 e salvo in F1
    reverse(F1, Final1),                       % ne faccio l'inversa
    reverse(Q2, Aux2),                         % Faccio la stessa cosa con Q2
    sublist(I1, Aux2, F2),                     %
    reverse(F2, Final2),                       %
    subst(Final1, Final2, Q1, Cross1),         % Faccio cross tra le due liste 
	subst(Final2, Final1, Q2, Cross2).         %
        
/*Deve prendere 1 elemento a caso della lista e cambiargli valore*/

mutation(X, Xs):- 
    random(1, 5, R),
    random(1, 5, I),
	select(R, X, I, Xs).

/*Passo base dell' algoritmo genetico, soluzione trovata 
inserisci nella lista solution Solution*/

genetic_4Q(Population, Solution):-
    %print(Population),
	(isResult(Population, X) ->  
        append(X, [], Solution)).

/*Qua fa genetic algorithm*/

genetic_4Q(Population, Solution):-
    
	%print(Population),    								
    selection(Population, 100, 100, [], [], Q1, Q2),
    crossover(Q1, Q2, Cross1, Cross2),

    mutation(Cross1, Mut1),
    mutation(Cross2, Mut2),    

    /*le append aggiungono le nuove liste trovate nella nuova popolazione*/

	append([Q1], [], Aux1),
    append([Q2], Aux1, Aux2),
    append([Mut1], Aux2, Aux3),
        
    append([Mut2], Aux3, New),
    
    /*prendo i migliori 2 e glielo passo all' algoritmo*/
    
    selection(New, 100 ,100, [], [], Queen1, Queen2),
    append([Queen1], [], B1),
    append([Queen2], B1, New_Population),
    %print("Nuova popolazione:"),
    genetic_4Q(New_Population, Solution).

/* MAIN */

main(Solution):-		%per scacchiera NxN, cambiare Population con N
    gen(4, Q),          %genera una popolazione random 
    reverse(Q, Qreverse), % ne fa l'inversa
    /*
    permutation(Q, Q1),
    permutation(Qreverse, Q2), 
    */
    %appende i risultati in population

    append([[Q, Qreverse]], Population),
    genetic_4Q(Population, Solution).   %chiama l'algoritmo





