#ifndef __CINT__
#include "TMath.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TF1.h"
#include <math.h>
#endif

Double_t Gauss(Double_t *x, Double_t *par)	{

	Double_t TWOPI = 2*TMath::Pi();
	Double_t arg = (x[0] - par[0]) / par[1];

	return (1. / TMath::Sqrt(TWOPI * par[1] * par[1])) * TMath::Exp(-0.5 * arg * arg);
}

void gauss()	{

	TCanvas *c1 = new TCanvas("c1", "Gauss Distribution", 500, 500);
	c1->Divide(2,2);

	//Version 1
	TF1 *ngauss1 = new TF1("ngauss1", Gauss, 0., 10., 2);
	ngauss1->SetParameter(0, 5.);
	ngauss1->SetParameter(1, 1.5);

	//Version 2
	TF1 *ngauss2 = new TF1("ngauss2", "1/sqrt(2*pi)/[1]*exp(-0.5*((x-[0])/[1])^2)", 0., 10.);
	ngauss2->SetParameter(0, 5.);
	ngauss2->SetParameter(1, 1.5);

	c1->cd(1); ngauss1->Draw();
	c1->cd(2); ngauss2->Draw();
	c1->cd(3); ngauss1->DrawDerivative();
	c1->cd(4); ngauss1->DrawIntegral();

	TFile *f1 = new TFile("gauss.root", "RECREATE", "dickbutt");
	c1->Write();
	ngauss1->Write();
	ngauss2->Write();
	f1->Close();

}

#ifndef __CINT__
int main()	{

	gauss();
	return 0;

}
#endif
