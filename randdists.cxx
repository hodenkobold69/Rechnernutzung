#ifndef __CINT__
#include "TMath.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TF1.h"
#include <math.h>
#endif

const int N = 100000;
const int bin_size = 100;

Double_t t1(Double_t x)	{

	return TMath::Power(x, 2);
}

Double_t t2(Double_t x)	{

	return TMath::Exp(x);
}

Double_t t3(Double_t x)	{

	return TMath::Tan(x);
}

Double_t t4(Double_t x)	{

	return TMath::Log(1. + x);
}

void randdists()	{

	//Create canvas and divide into subpads
	TCanvas *c1 = new TCanvas("c1", "Various Distributions", 500, 500);
	c1->Divide(2,2);

	TH1F *h1 = new TH1F("h1", "t1", bin_size, 0, 1);
	TH1F *h2 = new TH1F("h2", "t2", bin_size, 1, TMath::E());
	TH1F *h3 = new TH1F("h3", "t3", bin_size, 0, TMath::Pi()/4.);
	TH1F *h4 = new TH1F("h4", "t4", bin_size, 0, 0.69);

	for (int i = 0; i < N; i++)	{

		h1->Fill(t1(gRandom->Uniform(0, 1)));
		h2->Fill(t2(gRandom->Uniform(0, 1)));
		h3->Fill(t3(gRandom->Uniform(0, 1)));
		h4->Fill(t4(gRandom->Uniform(0, 1)));
	}

	c1->cd(1); h1->Draw();
	c1->cd(2); h2->Draw();
	c1->cd(3); h3->Draw();
	c1->cd(4); h4->Draw();

	// TF1 *f1 = new TF1("f1", t1, 0., 1., 1);
	// f1->SetParameter(0, N / bin_size);
	// TF1 *f2 = new TF1("f2", t2, 0., 1., 1);
	// f2->SetParameter(0, N / bin_size * (TMath::E()-1) );
	// TF1 *f3 = new TF1("f3", t3, 0., 1., 1);
	// f3->SetParameter(0, N / bin_size * (TMath::Pi()/4.) );
	// TF1 *f4 = new TF1("f4", t4, 0., 1., 1);
	// f4->SetParameter(0, N / bin_size * 0.69);

	// c1->cd(1); f1->Draw("same");
	// c1->cd(2); f2->Draw("same");
	// c1->cd(3); f3->Draw("same");
	// c1->cd(4); f4->Draw("same");

	c1->Print("dists.pdf");

	delete c1, h1, h2, h3, h4;
}
