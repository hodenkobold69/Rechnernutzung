(* ::Package:: *)

SetAttributes[GaussQuad, HoldAll];
GaussQuad[fn_, {var_, a_, b_}, poly_, w_:1, {polyn_, polyvar_, xminp_, xmaxp_}, order_] := Module[{polyt, ft, wt, weights, factor},
   
   If[b == Infinity, factor = 1, factor = (b - a)/(xmaxp-xminp)];
   
   polyt[y_, n_] := poly /. {polyvar -> y, polyn -> n};
   ft[y_] = fn /. {var -> (a + (y - xminp)*factor)};
   wt[y_] := w /. {polyvar -> y};
   
   an = Coefficient[polyt[x, order], x, order];
   anminus = Coefficient[polyt[x, order - 1], x, order - 1];
   
   weights[y_] = an/(anminus*(D[polyt[y, order], y])*polyt[y, order - 1]);
   roots = x /. Solve[polyt[x, order] == 0, x];
   
   Return[N[factor*Sum[ft[y]/wt[y]*weights[y], {y, roots}]]];
   ];
   


(* a) *)
f1[x_]:= Exp[-((x*x)/2)]+Exp[-x*x]
f2[x_]:= x/10+Sin[x]+Cos[3x]

poly[n_, x_] = LegendreP[n, x]/Sqrt[2/(2n+1)] ;

gaussints = Table[GaussQuad[f1[x], {x, -5, 3}, poly[n, x], {n, x, -1, 1}, k], {k, 2, 12}];
Show[ListPlot[gaussints, AxesLabel->{order-1, Integral}], Plot[NIntegrate[f1[x], {x, -5, 3}], {n, 0, 12}, PlotStyle->{Dashed, Orange}]]

gaussints = Table[GaussQuad[f2[x], {x, -5, 3}, poly[n, x], {n, x, -1, 1}, k], {k, 2, 12}];
Show[ListPlot[gaussints, AxesLabel->{order-1, Integral}], Plot[NIntegrate[f2[x], {x, -5, 3}], {n, 0, 12}, PlotStyle->{Dashed, Orange}]]


(* b) *)
f3[x_]:=Exp[-x]*(Sin[x]+Cos[1+x])/(1+x*x)
   
GaussQuad[f3[x], {x, 0, Infinity}, LaguerreL[n, x], Exp[-x], {n, x, 0, Infinity}, 30]
NIntegrate[f3[x], {x, 0, Infinity}]



