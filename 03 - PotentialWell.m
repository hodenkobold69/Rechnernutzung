(* ::Package:: *)

a =1/4

V[x_, v_] := Piecewise[{{v, -a<=x<=a}}, 0] (*since wavefunction vanishes at infinite potential, don't care for these ranges*)

sol = ParametricNDSolveValue[{(V[x, v] - en)*psi[x] - 1/2*psi''[x]==0, psi[-1]==0, psi'[-1]==1}, psi, {x, -1, 1}, {v, en}]

PlotSol[v_, enrange_]:=Plot[Evaluate[Table[sol[v, en][x],{en,enrange}]], {x, -1, 1}, PlotLegends->enrange, PlotLabel->Row[{"V1 = ", v}]]

PlotSol[0, Range[0.75, 5.25, 0.5]]         (* (i) *) 
PlotSol[30, Range[5, 7, 0.4]]              (* (ii) *) 
PlotSol[-30, Range[-21.73, -21.7, 0.005]]  (* (iii) *) 
PlotSol[-30, Range[-3, -1.2, 0.3]]         (* (iii) *) 


grounden0 = en /. {FindRoot[sol[0, en][1], {en, 0.75}], FindRoot[sol[0, en][1], {en, 3}]}
grounden30 = en /. {FindRoot[sol[30, en][1], {en, 5}], FindRoot[sol[30, en][1], {en, 7}]}
groundenneg30 = en /. {FindRoot[sol[-30, en][1], {en, -21.73}], FindRoot[sol[-30, en][1], {en, -3}]}


PlotNormed[v_, enrange_]:=Module[{norm, rim},

norm = Table[Sqrt[NIntegrate[sol[v, en][x]^2, {x, -1, 1}]], {en, enrange}];
rim=AssociationThread[enrange->norm];

Plot[Evaluate[Table[sol[v, en][x]/rim[en],{en,enrange}]], {x, -1, 1}, PlotLegends->enrange, PlotLabel->Row[{"V1 = ", v}]]
]
PlotNormed[0, grounden0]
PlotNormed[30, grounden30]
PlotNormed[-30, groundenneg30]






