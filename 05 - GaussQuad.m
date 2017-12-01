(* ::Package:: *)

GaussQuad[fn_, poly_, n_, intvar_, normint_, w_:1]:=Block[{var = intvar[[1]], a=intvar[[2]], b=intvar[[3]], n1=normint[[1]], n2=normint[[2]]},
	
	ft[var]=(b-a)/2*fn/w;
	No = Sqrt[Integrate[poly[n, var]^2, {var, n1, n2}]];
	Nminus = Sqrt[Integrate[poly[n-1, var]^2, {var, n1, n2}]];
	
	roots = Solve[poly[n, var]/No ==0, var];
	
	an = Coefficient[poly[n, var]/No, var, n];
	anminus = Coefficient[poly[n-1, var]/Nminus, var, n-1];
	
	G = Table[(an*No*Nminus )/(anminus*D[poly[n, var], var]*poly[n-1, var]) /. roots[[i]], {i, n}];
	
	
	fk = Table[ft[var] /. roots[[i]], {i, n}];
	Return[N[Sum[G[[i]]*fk[[i]], {i, n}]]]
	]
	


GaussQuad[Exp[x], LegendreP, 5, {x, 0, 10}, {-1, 1}]
