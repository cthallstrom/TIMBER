#ifdef __CLING__
#pragma cling optimize(0)
#endif
void leptonis_VLQ_mass()
{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Jul  2 11:44:59 2026) by ROOT version 6.26/11
   TCanvas *c1 = new TCanvas("c1", "c1",-6,59,921,695);
   gStyle->SetOptStat(0);
   c1->Range(-500.0001,-60.37501,4500,543.375);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetFrameBorderMode(0);
   c1->SetFrameBorderMode(0);
   
   TH1F *h1__1 = new TH1F("h1__1","Leptonic VLQ Mass as processed by RJR",50,0,4000);
   h1__1->SetBinContent(2,16);
   h1__1->SetBinContent(3,94);
   h1__1->SetBinContent(4,181);
   h1__1->SetBinContent(5,240);
   h1__1->SetBinContent(6,271);
   h1__1->SetBinContent(7,319);
   h1__1->SetBinContent(8,351);
   h1__1->SetBinContent(9,387);
   h1__1->SetBinContent(10,392);
   h1__1->SetBinContent(11,460);
   h1__1->SetBinContent(12,419);
   h1__1->SetBinContent(13,452);
   h1__1->SetBinContent(14,442);
   h1__1->SetBinContent(15,401);
   h1__1->SetBinContent(16,329);
   h1__1->SetBinContent(17,273);
   h1__1->SetBinContent(18,196);
   h1__1->SetBinContent(19,116);
   h1__1->SetBinContent(20,91);
   h1__1->SetBinContent(21,80);
   h1__1->SetBinContent(22,45);
   h1__1->SetBinContent(23,39);
   h1__1->SetBinContent(24,27);
   h1__1->SetBinContent(25,28);
   h1__1->SetBinContent(26,18);
   h1__1->SetBinContent(27,13);
   h1__1->SetBinContent(28,7);
   h1__1->SetBinContent(29,2);
   h1__1->SetBinContent(30,4);
   h1__1->SetBinContent(31,11);
   h1__1->SetBinContent(32,2);
   h1__1->SetBinContent(33,3);
   h1__1->SetBinContent(35,2);
   h1__1->SetBinContent(36,1);
   h1__1->SetBinContent(38,2);
   h1__1->SetBinContent(39,1);
   h1__1->SetBinContent(41,1);
   h1__1->SetBinContent(43,1);
   h1__1->SetBinContent(50,1);
   h1__1->SetBinContent(51,2);
   h1__1->SetEntries(5720);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   h1__1->SetLineColor(ci);
   h1__1->GetXaxis()->SetTitle("Leptonic VLQ Mass (GeV)");
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
   
   // TPaveText *pt = new TPaveText(0.1577802,0.9359165,0.8574538,0.9940387,"blNDC");
   // pt->SetName("title");
   // pt->SetBorderSize(0);
   // pt->SetFillColor(0);
   // pt->SetFillStyle(0);
   // pt->SetTextFont(42);
   // TText *pt_LaTex = pt->AddText("Leptonic VLQ Mass as processed by RJR");
   // pt->Draw();
   
   TH1F *h2__2 = new TH1F("h2__2","R_t_VLQ1_Mass ",50,0,4000);
   h2__2->SetBinContent(2,1);
   h2__2->SetBinContent(3,2);
   h2__2->SetBinContent(4,5);
   h2__2->SetBinContent(5,12);
   h2__2->SetBinContent(6,13);
   h2__2->SetBinContent(7,27);
   h2__2->SetBinContent(8,24);
   h2__2->SetBinContent(9,43);
   h2__2->SetBinContent(10,45);
   h2__2->SetBinContent(11,62);
   h2__2->SetBinContent(12,73);
   h2__2->SetBinContent(13,81);
   h2__2->SetBinContent(14,83);
   h2__2->SetBinContent(15,104);
   h2__2->SetBinContent(16,128);
   h2__2->SetBinContent(17,146);
   h2__2->SetBinContent(18,168);
   h2__2->SetBinContent(19,174);
   h2__2->SetBinContent(20,202);
   h2__2->SetBinContent(21,242);
   h2__2->SetBinContent(22,211);
   h2__2->SetBinContent(23,227);
   h2__2->SetBinContent(24,229);
   h2__2->SetBinContent(25,230);
   h2__2->SetBinContent(26,249);
   h2__2->SetBinContent(27,249);
   h2__2->SetBinContent(28,236);
   h2__2->SetBinContent(29,220);
   h2__2->SetBinContent(30,180);
   h2__2->SetBinContent(31,196);
   h2__2->SetBinContent(32,188);
   h2__2->SetBinContent(33,182);
   h2__2->SetBinContent(34,197);
   h2__2->SetBinContent(35,166);
   h2__2->SetBinContent(36,131);
   h2__2->SetBinContent(37,99);
   h2__2->SetBinContent(38,118);
   h2__2->SetBinContent(39,96);
   h2__2->SetBinContent(40,87);
   h2__2->SetBinContent(41,87);
   h2__2->SetBinContent(42,77);
   h2__2->SetBinContent(43,54);
   h2__2->SetBinContent(44,43);
   h2__2->SetBinContent(45,40);
   h2__2->SetBinContent(46,50);
   h2__2->SetBinContent(47,25);
   h2__2->SetBinContent(48,24);
   h2__2->SetBinContent(49,27);
   h2__2->SetBinContent(50,25);
   h2__2->SetBinContent(51,142);
   h2__2->SetEntries(5720);

   ci = TColor::GetColor("#ff0000");
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
   
   TLegend *leg = new TLegend(0.6471838,0.7178003,0.9543039,0.9261939,NULL,"brNDC");
   leg->SetBorderSize(1);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("h1","R_W_VLQ1_Mass ","lpf");
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#000099");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(1);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("h2","R_t_VLQ1_Mass ","lpf");
   entry->SetFillStyle(1001);

   ci = TColor::GetColor("#ff0000");
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
