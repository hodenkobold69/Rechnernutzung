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

	//Create canvas and divide into subpads
	TCanvas *c1 = new TCanvas("c1", "Gauss Distribution", 500, 500);
	c1->Divide(2,2);

	//Version 1 of Gauss dist.
	TF1 *ngauss1 = new TF1("ngauss1", Gauss, 0., 10., 2);
	ngauss1->SetParameter(0, 5.);
	ngauss1->SetParameter(1, 1.5);

	//Version 2 of Gauss dist.
	TF1 *ngauss2 = new TF1("ngauss2", "1/sqrt(2*pi)/[1]*exp(-0.5*((x-[0])/[1])^2)", 0., 10.);
	ngauss2->SetParameter(0, 5.);
	ngauss2->SetParameter(1, 1.5);

	//Get pads
	TPad *c1_1 = (TPad*) c1->GetListOfPrimitives()->FindObject("c1_1");
	TPad *c1_2 = (TPad*) c1->GetListOfPrimitives()->FindObject("c1_2");
	TPad *c1_3 = (TPad*) c1->GetListOfPrimitives()->FindObject("c1_3");
	TPad *c1_4 = (TPad*) c1->GetListOfPrimitives()->FindObject("c1_4");

	/*TODO: SetTitle does not work. TPads actually correspond to their
	primitive variables (proof: SetLogx() works fine) but the TPaveLabel
	is not changed properly.*/

	c1_1->cd(); ngauss1->Draw(); c1_1->SetTitle("Gauss (Ver.1)");
	c1_2->cd(); ngauss2->Draw(); c1_2->SetTitle("Gauss (Ver.2)");
	c1_3->cd(); ngauss1->DrawDerivative(); c1_3->SetTitle("Derivative");
	c1_4->cd(); ngauss1->DrawIntegral(); c1_4->SetTitle("Integral");

	//Save everything to a pdf-file
	c1->Print("gauss.pdf");

}

#ifndef __CINT__
int main()	{

	gauss();
	return 0;

}
#endif
