:-use_rendering(chess).
:-use_module(library(random)).

fill(0,L,L).
fill(N,R,L):-
    N>0,
    N1 is N-1,
    fill(N1,[N|R],L).


permutation(Xs,[Z|Zs]) :- select(Z,Xs,Ys),
permutation(Ys,Zs).
permutation([],[]).

select(X,[Y|Ys],[Y|Zs]):-
    select(X,Ys,Zs).
select(X,[X|Xs],Xs).

crossover(Q1, Q2, Queens1,Queens2,_):-
    random(1, 4, R2),
%    print(R2),
    length(Q2, L),
    R1 is L-R2,
%    print(R1),
    reverse(Q1, H1),
    splitList(R1, H1,F1),
    reverse(F1, T1),
%    print(T1),
    reverse(Q2, H2),
    splitList(R1, H2, F2),
    reverse(F2, T2),
%    print(T2),
    subst(T1, T2, Q1, Queens1),
	subst(T2,T1,Q2,Queens2).

crossover([],Q2,Queens1,Queens2,N):-
    	fill(N,[],Q1),
    	crossover(Q1, Q2, Queens1,Queens2,N).

crossover(Q1,[],Queens1,Queens2,N):-
    	fill(N,[],Q2),
    	crossover(Q1, Q2, Queens1,Queens2,N).

crossover([],[],Queens1,Queens2,N):-
    	fill(N,[],La),
   		permutation(La, Q1),
    	permutation(Q1, Q2),
    	crossover(Q1, Q2, Queens1,Queens2,N).


splitList(0, _, []).
splitList(I, [Y|Ys], Zs):- K is I-1, splitList(K, Ys, Ks), append([Y], Ks, Zs).

migliore([L|_],Sol):-
    fit(L,0,F),
    (F==0 ->	append(L,[],Sol)).

migliore([_|OthersL],Sol):-
    migliore(OthersL,Sol).

migliore([],_).


/*start*/
qu(N,Ls):-
    fill(N,[],La),
    permutation(La, Q1),
    permutation(Q1, Q2),
	append([[Q1,Q2]], L),
    queenso(L,[],N,50,50,Ls).


queens(L,Ls,N,Maggiore1,Maggiore2):-
    queenso(L,Ls,N,Maggiore1,Maggiore2,Ls).



queenso(L,[],N,,,Ls):- 		
    											migliore(L,Sol),
    											append(Sol,[],Lz),
   		 										four_queen(L,50,50,[],[],Z1,Z2),
   			 									crossover(Z1,Z2,Z1f,Z2f,N),
        										mutation(Z1f,Finale1),
    											mutation(Z2f,Finale2),
        										append([Z1], [], K1),	
        										append([Z2], K1, K2),
												append([Finale1], K2, K3),
												append([Finale2], K3, K),
    											print(K),
    											fit(Z1,0,M1),
    											fit(Z2,0,M2),
        										four_queen(K,M1,M2, [], [],Mig1, Mig2),
       											append([Mig1], [], Q1),
												append([Mig2], Q1, F),
    											queenso(F,Lz,N,M1,M2,Ls).

queenso(,Ls,,,,Ls).


fourX([L|OthersL],X,Y,_,Ys,Z1,Z2):-
    fit(L,0,F),
    (F =< X ->  Xf is F,
        	   append([L],Xl),
        	   fourX(OthersL,Xf,Y,Xl,Ys,Z1,Z2)).

fourX([_|OthersL],X,Y,Xs,Ys,Z1,Z2):-
      fourX(OthersL,X,Y,Xs,Ys,Z1,Z2).

fourX([],,,Z1,,Z1,).

fourY([L|OthersL],X,Y,Xs,_,Z1,Z2):-
    fit(L,0,F),
    (F =< Y ->  Yf is F,
        	   append([L],Yl),
        	   fourY(OthersL,X,Yf,Xs,Yl,Z1,Z2)).

fourY([_|OthersL],X,Y,Xs,Ys,Z1,Z2):-
    fourY(OthersL,X,Y,Xs,Ys,Z1,Z2).

fourY([],,,,Z2,,Z2).



four_queen(L,X,Y,Xs,Ys,Z1,Z2):-
    fourX(L,X,Y,Xs,Ys,Z1,Z2),
    delete(L,Z1,L2),
    fourY(L2,X,Y,Xs,Ys,Z1,Z2).
    

subst(This, That, MyStr, Result) :-
    append(This, After, Rest),
    append(Before, Rest, MyStr),
    !,
    subst(This, That, After, AfterResult),
    append([Before,That,AfterResult], Result).
subst(_, _, S, S).

fit([], X, X).
fit([Queen|OtherQueens], X, Z):- 
    fitness(Queen, OtherQueens, 1, 0, Y),
    X1 is X+Y,
    fit(OtherQueens, X1, Z).


fitness(_,[], _, X, X).
fitness(Q, [Q1|Qlist], Qdist, X, Y):- 
    K is Q1-Q,
    W is Q-Q1,
    ((K==Qdist ; W==Qdist; Q==Q1)-> X1 is X+1,
        								Dist is Qdist +1,
        								fitness(Q, Qlist, Dist, X1, Y);	Dist is Qdist+1,
        																	fitness(Q, Qlist, Dist, X, Y)).
mutation(X, Xs):- 
    random(1, 5, R),
    random(1, 5, I),
    length(X,L),
    J is I-1,
    K is L-I,
    splitList(J,X,Ys),
    reverse(X,Hs),
    splitList(K,Hs,Ts),
    reverse(Ts,Zs),
    append(Ys,[R],Rs),
    append(Rs,Zs,Xs).