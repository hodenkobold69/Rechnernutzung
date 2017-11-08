(* ::Package:: *)

MyPrime[n_]:=Module[{j, samples, multiples},

	j = N[Sqrt[n]];
	samples = Range[2, n];

	For[i=1, samples[[i]] <= j, i++,
		multiples = Table[k*samples[[i]], {k, samples[[i]], Floor[n/samples[[i]]]}];
		samples = Complement[samples, multiples];
	];

	Return[samples]]

MathPrimes[n_]:=Module[{x=1, primes={}},
	
	While[NextPrime[x]<= n,
		x=NextPrime[x];
		primes=Append[primes, x];
	];
	
	Return[primes]]

CheckPrimes[f_, bound_] := Module[{r, t}, {t, r} = Timing@f[bound];
  Print["running time: ", t];
  Print["# of found primes: ", Length[r]];
  Print["non-prime entries: ", Select[r, ! PrimeQ[#] &]]]

CheckPrimes[MyPrime, 100]
CheckPrimes[MathPrimes, 100]



