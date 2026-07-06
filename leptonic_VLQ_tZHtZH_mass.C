#ifdef __CLING__
#pragma cling optimize(0)
#endif
void leptonic_VLQ_tZHtZH_mass()
{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Jul  2 14:47:30 2026) by ROOT version 6.26/11
   TCanvas *c1 = new TCanvas("c1", "c1",10,38,979,654);
   gStyle->SetOptStat(0);
   c1->Range(-500,-27.69375,4500,249.2438);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *h1__1 = new TH1F("h1__1"," ",50,0,4000);
   h1__1->SetBinContent(2,12);
   h1__1->SetBinContent(3,52);
   h1__1->SetBinContent(4,91);
   h1__1->SetBinContent(5,145);
   h1__1->SetBinContent(6,135);
   h1__1->SetBinContent(7,147);
   h1__1->SetBinContent(8,192);
   h1__1->SetBinContent(9,182);
   h1__1->SetBinContent(10,188);
   h1__1->SetBinContent(11,190);
   h1__1->SetBinContent(12,211);
   h1__1->SetBinContent(13,201);
   h1__1->SetBinContent(14,172);
   h1__1->SetBinContent(15,145);
   h1__1->SetBinContent(16,109);
   h1__1->SetBinContent(17,75);
   h1__1->SetBinContent(18,70);
   h1__1->SetBinContent(19,40);
   h1__1->SetBinContent(20,29);
   h1__1->SetBinContent(21,25);
   h1__1->SetBinContent(22,17);
   h1__1->SetBinContent(23,14);
   h1__1->SetBinContent(24,7);
   h1__1->SetBinContent(25,12);
   h1__1->SetBinContent(26,7);
   h1__1->SetBinContent(27,7);
   h1__1->SetBinContent(28,2);
   h1__1->SetBinContent(31,3);
   h1__1->SetBinContent(36,1);
   h1__1->SetBinContent(41,1);
   h1__1->SetBinContent(51,1);
   h1__1->SetEntries(2483);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ff0000");
   h1__1->SetLineColor(ci);
   h1__1->GetXaxis()->SetTitle("Leptonic VLQ mass (GeV), TTbar -> tZHtZH");
   h1__1->GetXaxis()->SetLabelFont(42);
   h1__1->GetXaxis()->SetTitleOffset(1);
   h1__1->GetXaxis()->SetTitleFont(42);
   h1__1->GetYaxis()->SetTitle("Events");
   h1__1->GetYaxis()->SetLabelFont(42);
   h1__1->GetYaxis()->SetTitleFont(42);
   h1__1->GetZaxis()->SetLabelFont(42);
   h1__1->GetZaxis()->SetTitleOffset(1);
   h1__1->GetZaxis()->SetTitleFont(42);
   h1__1->Draw("");
   
   // TPaveText *pt = new TPaveText(0.15,0.9344958,0.7450487,0.995,"blNDC");
   // pt->SetName("title");
   // pt->SetBorderSize(0);
   // pt->SetFillColor(0);
   // pt->SetFillStyle(0);
   // pt->SetTextFont(42);
   // TText *pt_LaTex = pt->AddText("Leptonic VLQ Mass, TTbar -> tZHtZH");
   // pt->Draw();
   
   TH1F *h2__2 = new TH1F("h2__2","R_t_VLQ1_Mass  {decayFinds[0]==2||decayFinds[0]==3||decayFinds[0]==4}",50,0,4000);
   h2__2->SetBinContent(2,1);
   h2__2->SetBinContent(4,3);
   h2__2->SetBinContent(5,6);
   h2__2->SetBinContent(6,9);
   h2__2->SetBinContent(7,13);
   h2__2->SetBinContent(8,13);
   h2__2->SetBinContent(9,20);
   h2__2->SetBinContent(10,23);
   h2__2->SetBinContent(11,40);
   h2__2->SetBinContent(12,40);
   h2__2->SetBinContent(13,48);
   h2__2->SetBinContent(14,48);
   h2__2->SetBinContent(15,53);
   h2__2->SetBinContent(16,70);
   h2__2->SetBinContent(17,68);
   h2__2->SetBinContent(18,82);
   h2__2->SetBinContent(19,76);
   h2__2->SetBinContent(20,97);
   h2__2->SetBinContent(21,110);
   h2__2->SetBinContent(22,89);
   h2__2->SetBinContent(23,85);
   h2__2->SetBinContent(24,92);
   h2__2->SetBinContent(25,98);
   h2__2->SetBinContent(26,94);
   h2__2->SetBinContent(27,108);
   h2__2->SetBinContent(28,89);
   h2__2->SetBinContent(29,96);
   h2__2->SetBinContent(30,68);
   h2__2->SetBinContent(31,87);
   h2__2->SetBinContent(32,68);
   h2__2->SetBinContent(33,80);
   h2__2->SetBinContent(34,85);
   h2__2->SetBinContent(35,70);
   h2__2->SetBinContent(36,56);
   h2__2->SetBinContent(37,41);
   h2__2->SetBinContent(38,51);
   h2__2->SetBinContent(39,43);
   h2__2->SetBinContent(40,28);
   h2__2->SetBinContent(41,30);
   h2__2->SetBinContent(42,29);
   h2__2->SetBinContent(43,21);
   h2__2->SetBinContent(44,14);
   h2__2->SetBinContent(45,17);
   h2__2->SetBinContent(46,20);
   h2__2->SetBinContent(47,7);
   h2__2->SetBinContent(48,10);
   h2__2->SetBinContent(49,9);
   h2__2->SetBinContent(50,13);
   h2__2->SetBinContent(51,65);
   h2__2->SetEntries(2483);

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
   
   TLegend *leg = new TLegend(0.5905834,0.6730159,0.8904811,0.8825397,NULL,"brNDC");
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
