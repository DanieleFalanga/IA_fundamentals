selection([], _, _, L1, L2, L1, L2).

selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ((Fit < Fit1; Fit < Fit2) ->  (Fit1 > Fit2) ->  
        (append([P], L1_aux), 
        selection(Population, Fit, Fit2, L1_aux, L2, List1, List2))).

selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ((Fit < Fit1; Fit < Fit2) ->  (Fit1 =< Fit2) ->  
        append([P], L2_aux), 
        selection(Population, Fit1, Fit, L1, L2_aux, List1, List2)).

selection([P|Population], Fit1, Fit2, L1, L2, List1, List2):-
    fitness(P, 0, Fit),
    ((Fit >= Fit1, Fit >= Fit2) -> 
    selection(Population, Fit1, Fit2, L1, L2, List1, List2) ).