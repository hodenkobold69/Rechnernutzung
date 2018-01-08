(* ::Package:: *)

$HPLPath = "/home/hodenkobold/Git stuff/Rechnernutzung/HPL/";$Path = Flatten[{$Path,$HPLPath}];
<<HPL`;
b[x_]:=HPL[{3}, x]/(x(1+x)(1-x))
a[x_]:=-(1/x)
(*Homogeneous part of de*)
A = Integrate[a[x], x];
yhom = c*Exp[A]

(*Particular part of de*)
$HPLAutoConvertToKnownFunctions = False;

B = Expand[2*Apart[b[x]*Exp[-A], x]] /. {1/(-1+x) -> -1/(1-x)}
Ca = 1/2 * (Integrate[B[[1]], {x, 0, t}] + Integrate[B[[2]], {x, 0, t}]);

ypart = Ca*Exp[A]
y = yhom + ypart /. {c->0, t->x} (* Solution has to be finite at x=0 --> c=0 *)


CompareSolutions[imax_]:=Module[{},
	
	c[0]=0;
	ysum[x_]=Sum[c[i]x^i, {i, 0, imax}];
	
	hplseries[x_]=Series[b[x], {x, 0, imax}];
	eq[x_] = hplseries[x] + ysum[x]a[x] - ysum'[x];
	
	list=CoefficientList[eq[x], x];
	csol=Table[c[i]/.Solve[list[[i]]==0, c[i]][[1]], {i, 1, imax}];
	
	ysol[x_]=Sum[csol[[k]]*x^k, {k, 1, imax}];
	Plot[{y, ysol[x]}, {x, -1, 1}]
	]


CompareSolutions[50]
