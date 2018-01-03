#ifndef __CINT__
#include "TMath.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TF1.h"
#include <math.h>
#endif

const int N = 100000;
const int bin_size = 100;

//Transformation math function declarations (Note: I don't give a shit.)
Double_t t1_m(Double_t x)	{

	return TMath::Power(x, 2);
}

Double_t t2_m(Double_t x)	{

	return TMath::Exp(x);
}

Double_t t3_m(Double_t x)	{

	return TMath::Tan(x);
}

Double_t t4_m(Double_t x)	{

	return TMath::Log(1. + x);
}

//Transformation function declarations (Note: I don't give a shit.)
Double_t t1(Double_t *x, Double_t *par)	{

	return TMath::Power(x[0], 2);
}

Double_t t2(Double_t *x, Double_t *par)	{

	return TMath::Exp(x[0]);
}

Double_t t3(Double_t *x, Double_t *par)	{

	return TMath::Tan(x[0]);
}

Double_t t4(Double_t *x, Double_t *par)	{

	return TMath::Log(1. + x[0]);
}

//Distribution function declarations (calculated using the Inversion Method) (Note: I don't give a shit.)
Double_t t1_dist(Double_t *x, Double_t *par)	{

	return 1. / 2. / TMath::Sqrt(x[0]) / bin_size;
}

Double_t t2_dist(Double_t *x, Double_t *par)	{

	return 1. / x[0] / bin_size;
}

Double_t t3_dist(Double_t *x, Double_t *par)	{

	return 1. / 0.94689 * TMath::Power(TMath::Cos(TMath::ATan(x[0])), 2) / bin_size; //Arbitrary value found by calculating the integral.
}

Double_t t4_dist(Double_t *x, Double_t *par)	{

	return TMath::Exp(x[0]) / bin_size;
}

//Main program
void randdists()	{

	//Create canvas and divide into subpads
	TCanvas *c1 = new TCanvas("c1", "Various Distributions", 500, 500);
	c1->Divide(2,2);

	//Set up histograms
	TH1F *h1 = new TH1F("h1", "t1", bin_size, 0, 1);
	TH1F *h2 = new TH1F("h2", "t2", bin_size, 1, TMath::E());
	TH1F *h3 = new TH1F("h3", "t3", bin_size, 0, TMath::Pi()/4.);
	TH1F *h4 = new TH1F("h4", "t4", bin_size, 0, 0.69);

	//Fill histograms
	for (int i = 0; i < N; i++)	{

		h1->Fill(t1_m(gRandom->Uniform(0, 1)));
		h2->Fill(t2_m(gRandom->Uniform(0, 1)));
		h3->Fill(t3_m(gRandom->Uniform(0, 1)));
		h4->Fill(t4_m(gRandom->Uniform(0, 1)));
	}

	//Draw normalized histograms
	c1->cd(1); h1->DrawNormalized();
	c1->cd(2); h2->DrawNormalized();
	c1->cd(3); h3->DrawNormalized();
	c1->cd(4); h4->DrawNormalized();

	//Tranformation functions
	TF1 *f1_traf = new TF1("f1_traf", t1, 0., 1., 0);
	TF1 *f2_traf = new TF1("f2_traf", t2, 0., 1., 0);
	TF1 *f3_traf = new TF1("f3_traf", t3, 0., 1., 0);
	TF1 *f4_traf = new TF1("f4_traf", t4, 0., 1., 0);

	//Distribution functions
	TF1 *f1_dist = new TF1("f1_dist", t1_dist, f1_traf->GetMinimum(), f1_traf->GetMaximum(), 0);
	TF1 *f2_dist = new TF1("f2_dist", t2_dist, f2_traf->GetMinimum(), f2_traf->GetMaximum(), 0);
	TF1 *f3_dist = new TF1("f3_dist", t3_dist, f3_traf->GetMinimum(), f3_traf->GetMaximum(), 0);
	TF1 *f4_dist = new TF1("f4_dist", t4_dist, f4_traf->GetMinimum(), f4_traf->GetMaximum(), 0);

	//Draw normalized distribution functions
	c1->cd(1); f1_dist->Draw("same");
	c1->cd(2); f2_dist->Draw("same");
	c1->cd(3); f3_dist->Draw("same");
	c1->cd(4); f4_dist->Draw("same");

	//Save canvas to file
	c1->Print("dists.pdf");

	//This is horrible and morally wrong
	delete c1; delete h1; delete h2; delete h3; delete h4; delete f1_dist; delete f2_dist; delete f3_dist; delete f4_dist; delete f1_traf; delete f2_traf; delete f3_traf; delete f4_traf;
}
