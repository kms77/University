% 13.
% b. For a heterogeneous list, formed from integer numbers and list of numbers;
% write a predicate to delete from every sublist all sequences of consecutive values.
% Eg.: [1, [2, 3, 5], 9, [1, 2, 4, 3, 4, 5, 7, 9], 11, [5, 8, 2], 7] =>
% [1, [5], 9, [4, 7, 9], 11, [5, 8, 2], 7]
%
% Solution:
% Function which remove all sequences of consecutive values from a
% linear numerical list;
% remove_consecutive(L: list, R: list);
% Flow model: remove_consecutive(i,o);
remove_consecutive([],[]).
remove_consecutive([E],[E]).
remove_consecutive([H1, H2], []):- H2 =:= H1+1.
remove_consecutive([H1, H2], [H1, H2]) :- H2 =\= H1+1.
remove_consecutive([H1, H2, H3|T], R) :- H2 =:= H1+1,H3 =:= H2+1, remove_consecutive([H2, H3|T], R).
remove_consecutive([H1, H2, H3|T], R) :- H2 =:= H1+1, H3 =\= H2+1, remove_consecutive([H3|T],R).
remove_consecutive([H1, H2, H3|T], [H1|R]) :- H2 =\= H1+1, remove_consecutive( [H2, H3|T], R).

% Function which delete from every sublist of a heterogeneous list all
% sequences of consecutive values (there are only numbers and list of
% numbers);
% heterogeneous_list(L- list, R- list);
% Flow model: homogeneous_list(i,o);
heterogeneous_list([],[]).
heterogeneous_list([H|T], [HR|R]) :- is_list(H), !, remove_consecutive(H, HR), heterogeneous_list(T, R).
heterogeneous_list([H|T], [H|R]) :- heterogeneous_list(T, R).
