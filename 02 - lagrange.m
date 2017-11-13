(* ::Package:: *)

Needs["VariationalMethods`"]
g = 9.81

h[t_] := a*Sin[\[Omega]*t]
x[t_] := l*Sin[\[CapitalTheta][t]]
y[t_] := h[t]+l*Cos[\[CapitalTheta][t]]
T[t_] := 1/2 * (D[x[t], t]^2 + (D[y[t], t]^2))
V[t_] := g*l*y[t]
L[t_] := T[t] - V[t]
s := EulerEquations[L[t], \[CapitalTheta][t], t]

plotPendulum[theta_Real, t_Real, subs_List ] := Module[
  {w, p1, p2, le, ps, ra, lines, dots, ceil, text, text2, all, pendulum},
  w = 1; (* width *)
  
  (* points *)
  p1 = {0, h[t]} /. subs;
  p2 = {l*Sin[theta], h[t] + l*Cos[theta]} /. subs;
  
  (* scale *)
  le = (l + a) /. subs;
  
  (* ceiling size *)
  ps = {{-l, -a}, {l, a}} /. subs;
  
  (* draw area *)
  ra = le*{w*{-1.05, 1.05}, {-2.15, 2.15}};
  
  (* ceiling, lines, points *)
  ceil = {Lighter[Brown], EdgeForm[Dashed], Rectangle[Sequence @@ ps]};
  lines = {Black, Thickness[0.01], Line[{{0, 0}, p1}], Thickness[0.005], Line[{p1, p2}]};
  dots = {Black, PointSize[0.04], Point[{{0, 0}, p1}], Red,PointSize[0.1], Point[{p2}]};
  
  (* text *)
  text = {Black, Background -> White,
    Text[m, p2 + {w, 0}, {-1, 0}],
    Text[l, p1 + (p2 - p1)/2 - {0.05*le, 0}, {1, 0}]};
    
  (* gather everything *)
  all = Join[lines, dots, text];
  
  (* timer *)
  If[t =!= False,
   text2 = {Text[" t = " <> ToString[t] <> " s ",ps[[1]] + {0, ps[[2, 2]]*2 + 0.1}, {-1, -1}]};
   all = Join[all, text2]
   ];
  all = Join[ceil, all];
  pendulum = Show[Graphics[all], PlotRange -> ra];
  Return[pendulum]
  ]


DoEverything[subs_List, tnull_, tpunktnull_] := Module[{deq, sol}, 
	
	deq = s /. subs;
	sol = NDSolve[{deq, \[CapitalTheta][0]==tnull, \[CapitalTheta]'[0]==tpunktnull}, \[CapitalTheta], {t, 0, 30}];
	f = \[CapitalTheta] /. First[sol];
	Animate[plotPendulum[f[t], t, subs], {t, 0, 30}]
	]

DoEverything[{l->10, a->1.5, \[Omega]->22*Pi}, 0.1, 0.01]






