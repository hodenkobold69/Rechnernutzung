(* ::Package:: *)

a:=1/4
v1[E_]:= Piecewise[...]
V[x_]:=Piecewise[{{0, -1<x<-a}, {v1, -a<=x<=a}, {0, a<x<1}}, Infinity]
Plot[V[x], {x, -3, 3}]
