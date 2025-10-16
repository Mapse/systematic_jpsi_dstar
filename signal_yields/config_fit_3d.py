# Cases for systematic uncertainty
# 1: nominal fit
# 2: J/ψ signal: change crystal ball + gaussian to crystal ball only.
# 3: J/ψ background: change exponential function to linear function.
# 4: J/ψ prompt: change Resolution function to gaussian.
# 5: D∗ background: change threshold function to phenomenological threshold function

case = 1

set = 'Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100'

# PDFs

if case == 1:

    dstar_pdf = {'signal': 'johnson', # signal: johnson (default), doubleG (?)
                'background': 'ntf'} # background: ntf (default), ptf

    jpsi_mass_pdf = {'signal': 'CBG', # signal: CBG (default), CB
                    'background': 'exp'} #background: exp (default), linear

    jpsi_pdf = {'prompt' : 'resolG',  # prompt: resolG (default), GA (gaussian)
                'non_prompt' : 'resol'} # non_prompt: resol (default), GA (gaussian)

elif case == 2:

    dstar_pdf = {'signal': 'johnson', # signal: johnson (default), doubleG (?)
                'background': 'ntf'} # background: ntf (default), ptf

    jpsi_mass_pdf = {'signal': 'CB', # signal: CBG (default), CB
                    'background': 'exp'} #background: exp (default), linear

    jpsi_pdf = {'prompt' : 'resolG',  # prompt: resolG (default), GA (gaussian)
                'non_prompt' : 'resol'} # non_prompt: resol (default), GA (gaussian)
    
elif case == 3:

    dstar_pdf = {'signal': 'johnson', # signal: johnson (default), doubleG (?)
                'background': 'ntf'} # background: ntf (default), ptf

    jpsi_mass_pdf = {'signal': 'CBG', # signal: CBG (default), CB
                    'background': 'linear'} #background: exp (default), linear

    jpsi_pdf = {'prompt' : 'resolG',  # prompt: resolG (default), GA (gaussian)
                'non_prompt' : 'resol'} # non_prompt: resol (default), GA (gaussian)
    
elif case == 4:

    dstar_pdf = {'signal': 'johnson', # signal: johnson (default), doubleG (?)
                'background': 'ntf'} # background: ntf (default), ptf

    jpsi_mass_pdf = {'signal': 'CBG', # signal: CBG (default), CB
                    'background': 'exp'} #background: exp (default), linear

    jpsi_pdf = {'prompt' : 'GA',  # prompt: resolG (default), GA (gaussian)
                'non_prompt' : 'resol'} # non_prompt: resol (default), GA (gaussian)
    
elif case == 5:

    dstar_pdf = {'signal': 'johnson', # signal: johnson (default), doubleG (?)
                'background': 'ptf'} # background: ntf (default), ptf

    jpsi_mass_pdf = {'signal': 'CBG', # signal: CBG (default), CB
                    'background': 'exp'} #background: exp (default), linear

    jpsi_pdf = {'prompt' : 'resolG',  # prompt: resolG (default), GA (gaussian)
                'non_prompt' : 'resol'} # non_prompt: resol (default), GA (gaussian)

                                                                                                                                                                                                                                                                                                                                                       
option={set : [{'fit_parameters' : {# Jpsi Mass
                                                     #'mean_jpsi' : [3.09423e+00, 3.08, 3.10], 
                                                     'mean_jpsi' : [3.09423e+00, 3.08, 3.10], 
                                                     'sigma_gauss' : [3.90710e-02, 0.009, 0.070], 
                                                     #'sigma_cb' : [2.10832e-02, 0.009, 0.070],
                                                     'sigma_cb' : [2.10832e-02, 0.009, 0.070],
                                                     'frac_gauss_jpsi' : [3.13573e-01, 0.001, 1.0],  
                                                     #'frac_gauss_jpsi' : [0.0],  
                                                     'frac_cb' : [0.6, 0.0001, 1.0], 
                                                     'alpha' : 1.4, #1.4
                                                     'n' : 8.8, #(8.8)
                                                     'linear_coef0' : [1., -100., 100.],
                                                     'linear_coef1' : [-.01, -1., 1.],
                                                     'exp_coef' : [-1.82143e+00 , -4, 3], 
                                                     'frac_exp_mass' : [0.4, 0.0, 1.0],
                                                     # Jpsi Decay Lenght
                                                     'jpsi_dlErr' : [4 ,0.001, 10],
                                                     'mean_prompt' : [0, -0.005, 0.005], # [3.67710e-05, 0.00001, 0.00005], [0.000109852] 0.00433729
                                                     'sigma_prompt1' : [1.47960e-02, 0.005, 0.1], # [1.47960e-02, 0.005, 0.03], [0.014579] 0.0093857, 0.0383986 (2017), 0.0103444 (2018)
                                                     'sigma_prompt2' : [1.47960e-02, 0.005, 0.1], # [6.10019e-03, 0.001, 0.01], [0.014579] 0.0093857, 0.0383986 (2017), 0.0103444 (2018)
                                                     'sigma_prompt3' : [1.47960e-02, 0.005, 0.1], # [6.10019e-03, 0.001, 0.01], [0.014579] 0.0093857, 0.0383986 (2017), 0.0103444 (2018)
                                                     'frac_prompt' : [0.5, 0, 1.0],
                                                     'mean_pv' : [-1.02496e-04, -3.65E-04, 1.60E-04], #[1.18699e-04, -0.3, 0.3]
                                                     'sigma_pv' : [1.37666e-02, 1.33E-02, 1.43E-02], #[1.41996e-02, 0.005, 0.03]
                                                     'mean_ge' : [0, -0.3, 0.3], #  gaussian: Prompt [0, -0.3, 0.3]
                                                     'sigma_ge' : [0.01, 0, 0.3], #  gaussian: Prompt [0.01, 0, 0.3]
                                                     'exp_coef_pv' : [-0.19 , -0.2, 0], 
                                                     'frac_np1' : [0.1, 0.0, 0.5],
                                                     'mean_non_prompt' : [0.004, -0.009, 0.009], 
                                                     'sigma_non_prompt' : [1.47960e-02, 0.007, 0.03],  #0.000100075
                                                     'mean_non_prompt2' : [0.1, -0.1, 0.1],
                                                     'sigma_non_prompt2' : [0.05, 0, 0.1],  
                                                     'tau' : [0.19, 0.01, 3],
                                                     'frac_exp_dl' : [7.17152e-01, 0.0, 1.0],
                                                     'frac_gauss_dl' : [0.5, 0.0, 1.0],
                                                     ## Dstar delta mass 
                                                     'dstar_mean' : [1.45431e-01, 0.142, 0.158],
                                                     'dstar_lambda' : [6.69130e-04, 0.00001, 0.01], 
                                                     'dstar_gamma' : [1.64257e-02, 0.001, 0.1], 
                                                     'dstar_delta' : [1.47542e+00, -3, 4], 
                                                     'dstar_sigma_john' : [3.90710e-02, 0.009, 0.070], 
                                                     'dstar_sigma_g1' : [0.0002, 0.00001, 1.0], 
                                                     'dstar_sigma_g2' : [0.0004, 0.00001, 1.0], 
                                                     'dstar_frac' : [1.00157e-01, 0, 1], 
                                                     # PTF coeficients
                                                     'p0' : [2.75881e-03, 0.0001, 0.1], 
                                                     'p1' : [2.56644e-01, -15, 10], 
                                                     'p2' : [2.02447e+00, -20, 20],
                                                     # New threshold function coeficients
                                                     'A' :  [2.02447e+00, -20, 20],
                                                     'B' :  [2.56644e-01, -15, 10], 
                                                     'C' :  [-9, -20, 5],

                                                     # Model componets fractions
                                                     'signal_frac' : [0.13, 0.0001, 1],
                                                     'bkg1_frac' : [0.61, 0.0001, 1],
                                                     'bkg2_frac' : [0.10, 0.0001, 1],
                                                     'bkg3_frac' : [0.10, 0.0001, 1],
                                                     'bkg4_frac' : [0.15, 0.0001, 1],
                                                     'bkg5_frac' : [0.50, 0.0001, 1],
                                                     'bkg6_frac' : [0.10, 0.0001, 1],}},
                                                     
                                            {'files' : ['fit_plots/' + set + '_Jpsi_mass_component_3Dfit' + '_case_' +str(case)+ '.png',
                                                        'fit_plots/' + set + '_Jpsi_mass_pull' + '_case_' +str(case)+ '.png',
                                                        'fit_plots/' + set + '_Jpsi_dl_component_3Dfit' + '_case_' +str(case)+ '.png',
                                                        'fit_plots/' + set + '_Jpsi_dl_pull' + '_case_' +str(case)+ '.png',
                                                        'fit_plots/' + set + '_Dstar_component_3Dfit' + '_case_' +str(case)+ '.png',
                                                        'fit_plots/' + set + '_Dstar_pull' + '_case_' +str(case)+ '.png',
                                                         set +'_wspace' + '_case_' +str(case) , 
                                                        'fit_root_files/' + set + '_case_' +str(case)+ '_3Dfit.root',
                                                        'data_root_files/' + set + '.root']}],} 


lumi = "126.8 fb^{-1}" # Run 2

# Chi square
nparm_jpsi_mass = 4
nparm_jpsi_dl = 8
nparm_dstar = 8

# Dict with gourmetization for plotting
colors = {"model" : 2, "signal" : 4, "background" : 3}

styles = {"model" : 1, "signal" : 1, "background" : 2}

###################################### Config for yields and fom ######################################
yield_files = ['fit_root_files/' + set + '_wspace' + '_case_' +str(case),]

csv_name = 'csv/' + set + '_case_' +str(case)+ '_3Dfit.csv'

#case = [3.0, 2.9, 2.8, 2.7, 2.6, 2.5, 2.0, 1.5, 1.0]

#type = 'dl Significance'