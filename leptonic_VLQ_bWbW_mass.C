#ifdef __CLING__
#pragma cling optimize(0)
#endif
void leptonic_VLQ_bWbW_mass()
{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Jul  2 14:26:23 2026) by ROOT version 6.26/11
   TCanvas *c1 = new TCanvas("c1", "c1",10,38,1014,670);
   gStyle->SetOptStat(0);
   c1->Range(-500,-9.056251,4500,81.50625);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *h1__1 = new TH1F("h1__1","",50,0,4000);
   h1__1->SetBinContent(3,1);
   h1__1->SetBinContent(4,9);
   h1__1->SetBinContent(5,10);
   h1__1->SetBinContent(6,24);
   h1__1->SetBinContent(7,37);
   h1__1->SetBinContent(8,30);
   h1__1->SetBinContent(9,34);
   h1__1->SetBinContent(10,31);
   h1__1->SetBinContent(11,62);
   h1__1->SetBinContent(12,37);
   h1__1->SetBinContent(13,60);
   h1__1->SetBinContent(14,61);
   h1__1->SetBinContent(15,69);
   h1__1->SetBinContent(16,67);
   h1__1->SetBinContent(17,45);
   h1__1->SetBinContent(18,38);
   h1__1->SetBinContent(19,17);
   h1__1->SetBinContent(20,12);
   h1__1->SetBinContent(21,13);
   h1__1->SetBinContent(22,5);
   h1__1->SetBinContent(23,8);
   h1__1->SetBinContent(24,6);
   h1__1->SetBinContent(25,3);
   h1__1->SetBinContent(26,4);
   h1__1->SetBinContent(27,2);
   h1__1->SetBinContent(28,2);
   h1__1->SetBinContent(30,1);
   h1__1->SetBinContent(31,2);
   h1__1->SetBinContent(32,1);
   h1__1->SetBinContent(35,1);
   h1__1->SetBinContent(39,1);
   h1__1->SetBinContent(50,1);
   h1__1->SetEntries(694);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   h1__1->SetLineColor(ci);
   h1__1->GetXaxis()->SetTitle("Leptonic VLQ Mass (GeV), TTbar -> bWbW");
   h1__1->GetXaxis()->SetLabelFont(42);
   h1__1->GetXaxis()->SetTitleOffset(1);
   h1__1->GetXaxis()->SetTitleFont(42);
   h1__1->GetYaxis()->SetLabelFont(42);
   h1__1->GetYaxis()->SetTitle("Events");
   h1__1->GetYaxis()->SetTitleFont(42);
   h1__1->GetZaxis()->SetLabelFont(42);
   h1__1->GetZaxis()->SetTitleOffset(1);
   h1__1->GetZaxis()->SetTitleFont(42);
   h1__1->Draw("");
   
   // TPaveText *pt = new TPaveText(0.1823708,0.920418,0.7598784,0.9799035,"blNDC");
   // pt->SetName("title");
   // pt->SetBorderSize(0);
   // pt->SetFillColor(0);
   // pt->SetFillStyle(0);
   // pt->SetTextFont(42);
   // TText *pt_LaTex = pt->AddText("Leptonic VLQ Mass, TTbar -> bWbW");
   // pt->Draw();
   
   TH1F *h2__2 = new TH1F("h2__2","R_t_VLQ1_Mass  {decayFinds[0]==1}",50,0,4000);
   h2__2->SetBinContent(7,1);
   h2__2->SetBinContent(8,2);
   h2__2->SetBinContent(9,2);
   h2__2->SetBinContent(11,2);
   h2__2->SetBinContent(12,4);
   h2__2->SetBinContent(13,2);
   h2__2->SetBinContent(14,7);
   h2__2->SetBinContent(15,8);
   h2__2->SetBinContent(16,16);
   h2__2->SetBinContent(17,12);
   h2__2->SetBinContent(18,14);
   h2__2->SetBinContent(19,18);
   h2__2->SetBinContent(20,14);
   h2__2->SetBinContent(21,27);
   h2__2->SetBinContent(22,32);
   h2__2->SetBinContent(23,30);
   h2__2->SetBinContent(24,27);
   h2__2->SetBinContent(25,36);
   h2__2->SetBinContent(26,39);
   h2__2->SetBinContent(27,21);
   h2__2->SetBinContent(28,44);
   h2__2->SetBinContent(29,26);
   h2__2->SetBinContent(30,25);
   h2__2->SetBinContent(31,30);
   h2__2->SetBinContent(32,32);
   h2__2->SetBinContent(33,27);
   h2__2->SetBinContent(34,36);
   h2__2->SetBinContent(35,18);
   h2__2->SetBinContent(36,19);
   h2__2->SetBinContent(37,18);
   h2__2->SetBinContent(38,12);
   h2__2->SetBinContent(39,7);
   h2__2->SetBinContent(40,12);
   h2__2->SetBinContent(41,12);
   h2__2->SetBinContent(42,8);
   h2__2->SetBinContent(43,3);
   h2__2->SetBinContent(44,8);
   h2__2->SetBinContent(45,6);
   h2__2->SetBinContent(46,5);
   h2__2->SetBinContent(47,4);
   h2__2->SetBinContent(48,2);
   h2__2->SetBinContent(49,6);
   h2__2->SetBinContent(50,2);
   h2__2->SetBinContent(51,18);
   h2__2->SetEntries(694);

   ci = TColor::GetColor("#000099");
   h2__2->SetLineColor(ci);
   h2__2->GetXaxis()->SetLabelFont(42);
   h2__2->GetXaxis()->SetTitleOffset(1);
   h2__2->GetXaxis()->SetTitleFont(42);
   h2__2->GetYaxis()->SetLabelFont(42);
   h2__2->GetYaxis()->SetTitleFont(42);
   h2__2->GetZaxis()->SetLabelFont(42);
   h2__2->GetZaxis()->SetTitleOffset(1);
   h2__2->GetZaxis()->SetTitleFont(42);
   h2__2->Draw("same");
   
   TLegend *leg = new TLegend(0.520751,0.7430341,0.9001976,0.9009288,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("h1","VLQ to W to Leptonic","lpf");
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#ff0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(1);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h2","VLQ to t to Leptonic","lpf");
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(1);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
