import ROOT

chains = []

data = ROOT.TChain('mini')
data.Add("./Data/data_*.root")
chains.append(data)

zee = ROOT.TChain('mini')
zee.Add("./MC/mc_*.Zee.1lep1tau.root")
chains.append(zee)

z_mu_mu = ROOT.TChain('mini')
z_mu_mu.Add("./MC/mc_*.Zmumu.1lep1tau.root")
chains.append(z_mu_mu)

z_tau_tau = ROOT.TChain('mini')
z_tau_tau.Add("./MC/mc_*.Ztautau*.1lep1tau.root")
chains.append(z_tau_tau)