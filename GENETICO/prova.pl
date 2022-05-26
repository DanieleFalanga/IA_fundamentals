crossover(Q1, Q2, Cross1, Cross2):-            
    random(1, 4, I2),                          % Scelgo numero random
    length(Q2, L),                             % calcolo lunghezza di Q2 e salvo in L
    I1 is L-I2,                                % Salvo la differenza tra 
    reverse(Q1, Aux1),                         % salvo l'inversa di Q1 in Help1
    sublist(I1, Aux1, F1),                     % prendo la 
    reverse(F1, Final1),                       %
    reverse(Q2, Aux2),                         %
    sublist(I1, Aux2, F2),                     %
    reverse(F2, Final2),                       %
    subst(Final1, Final2, Q1, Cross1),         %
	subst(Final2, Final1, Q2, Cross2).         %