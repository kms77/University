% 13.
% a. Given a linear numerical list write a predicate to remove
% all sequences of consecutive values.
% Eg.: remove([1, 2, 4, 6, 7, 8, 10], L) will produce L=[4, 10].
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


