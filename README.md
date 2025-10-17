# J/ψD* CMS run 2 analysis - Systematic uncertainties  

<!---
To see the preview type ctr+shift+v
--->

## Pile-up dependency and yield instability

TO BE DONE

## Pile-up reweighting

TO BE DONE

## Signal yields

For this systematic you have two python scripts:

- **`config_fit_3d.py`**: configuration file
- **`fit3D_JpsiDstar.py`**: script to get fit plots and yields

On top of this you have different folders:

- **`data_root_files`**: folder where the input data is stored. Ex: _Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100.root_ (all subsequent files commentd in this tutorial will use this file as base)
- **`fit_plots`**: folder where the fit plots are produced.
- **`fit_root_files`**: when you run _fit3D_JpsiDstar.py_ using the fit option (don't worry, you will learn this below) these two files are produced:
    - **`Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit.root`**: RooWorkspace with the fit information
    - **`Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit.txt`**: text file with the $\chi^2/n.d.f$ for each distribution (J/ψ mass, J/ψ decay length, and D* delta mass)
When you run _fit3D_JpsiDstar.py_ using the yield option these two files are produced:
    - **`Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit_pdf_params.csv`**: csv file with some fit parameters to future checks
    - **`Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit_yields.csv`**: csv file with yields (signal, background and non-prompt J/ψ yields)
- **`csv`**: This folder contains the final csv file with all relevant information: case, number of events (signal, background and non-prompt J/ψ yields), $\chi^2/n.d.f$, and some figure of merits (Z<sub>sb</sub>, Z<sub>ssb</sub>, Z<sub>12</sub>)

### To run the scripts

In the _config_fit_3d.py_ you will need to change two lines according to what you want to do:

- **line 8**:

`case = 1`
Available cases: 1, 2, 3, 4, 5

- **line 10**:
set = 'Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100'
This is the name of the input file without ".root"

Now, you are ready to obtain the fits and the yields:

a) Fits

You run this command:

`python3 fit3D_JpsiDstar.py -f`

If everything worked well you will see the $\chi^2/n.d.f$ for each distribution in the terminal and the plots will be created at _fit_plots_ folder. The files _Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit.root_ and _Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit.txt_ are created at _fit_root_files_ .

b) Yields

Before doing this, you must perform step a) first! Then, you run  this command:

`python3 fit3D_JpsiDstar.py -f`

If everything worked well you will see in the end the yield values in the terminal and the files _Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit_pdf_params.csv_ and _Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit_yields.csv_ are created at _fit_root_files_  folder and Charmonium_all_vtx0p05_sigma_eff_jpsi_pt_bin1_25_100_case_1_3Dfit.csv is created at csv folder.