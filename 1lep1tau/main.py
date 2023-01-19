# Three prong Tau analysis using CERN OpenData

import ROOT
from data import chains


str_nTracks = '''
    ROOT::VecOps::RVec<int> get_nTracks(ROOT::VecOps::RVec<int> &v, ROOT::VecOps::RVec<float> &m){
        ROOT::VecOps::RVec<int> result;
        for (int i = 0; i < v.size(); i++){
            if (v[i] == 3){
                result.push_back(m[i]);
            }
        }

        return result;
    }
'''

ROOT.gInterpreter.Declare(str_nTracks)





data_df = ROOT.RDataFrame(chains[0])
data_df = data_df.Define("tau_track_count", "tau_nTracks")
data_df = data_df.Define("ditau_mass", "ditau_m")

zmumu_df = ROOT.RDataFrame(chains[2])
zmumu_df = zmumu_df.Define("tau_track_count", "tau_nTracks")
zmumu_df = zmumu_df.Define("ditau_mass", "ditau_m")

zee_df = ROOT.RDataFrame(chains[1])
zee_df = zee_df.Define("tau_track_count", "tau_nTracks")
zee_df = zee_df.Define("ditau_mass", "ditau_m")

ztautau_df = ROOT.RDataFrame(chains[3])
ztautau_df = ztautau_df.Define("tau_track_count", "tau_nTracks")
ztautau_df = ztautau_df.Define("ditau_mass", "ditau_m")

hist_ditau_m = data_df.Histo1D(("Di-Tau Mass", "ditaumass", 200, 0, 500),"ditau_mass")
hist_zmumu = zmumu_df.Histo1D(("Di-Tau Mass", "ditaumass", 200, 0, 500),"ditau_mass")
hist_zee = zee_df.Histo1D(("Di-Tau Mass", "ditaumass", 200, 0, 500),"ditau_mass")
hist_ztautau = ztautau_df.Histo1D(("Di-Tau Mass", "ditaumass", 200, 0, 500),"ditau_mass")
hist_zmumu.SetFillColor(ROOT.kRed)
hist_zee.SetFillColor(ROOT.kBlue)
hist_ztautau.SetFillColor(ROOT.kGreen)
c_ditau_m = ROOT.TCanvas("Z#rightarrow 1l1#tau", "Z#rightarrow 1l1#tau", 700, 500)

hist_ditau_m.SetTitle("Z#rightarrow 1l1#tau")
hist_ditau_m.Draw()

hist_zee.Draw("SAME")
hist_zmumu.Draw("SAME")
hist_ztautau.Draw("SAME")

legend = ROOT.TLegend(0.7,0.7,0.48,0.9)
legend.SetHeader("Z #rightarrow 1l1#tau Background")
legend.AddEntry("hist_ditau_m", "Data")
legend.AddEntry("hist_zmumu", "Z #rightarrow #mu #mu")
legend.AddEntry("hist_zee", "Z #rightarrow ee")
legend.Draw()

input()

