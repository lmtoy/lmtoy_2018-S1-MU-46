#! /usr/bin/env python
#
#   script generator for project="2018-S1-MU-46"
#
#   8 in CO (3 regions), 11 in HCN (1 region)

import os
import sys

from lmtoy import runs

project="2018-S1-MU-46"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on['Region_J-K_CO']   = [85776, 85778, 85824]
on['Region_H_CO']     = [85818, 85826, 85882]
on['Region_D-E_CO']   = [85820, 85878]
on['Region_J-K_HCN']  = [86090, 86094, 86098, 86102, 86106, 86110,
                         86133, 86137, 86139, 86243, 86247]

#        common parameters per source on the first dryrun (run1, run2)
pars1 = {}
pars1['L1157-B1'] = "dv=250 dw=250 extent=180"

pars1['Region_J-K_CO']   = "dv=200 dw=200 b_order=1"
pars1['Region_H_CO']     = "dv=200 dw=200 b_order=1"
pars1['Region_D-E_CO']   = "dv=200 dw=200 b_order=1"
pars1['Region_J-K_HCN']  = "dv=200 dw=200 b_order=1"

#        common parameters per source on subsequent runs (run1a, run2a)
pars2 = {}
pars2['Region_J-K_CO']   = ""
pars2['Region_H_CO']     = ""
pars2['Region_D-E_CO']   = ""
pars2['Region_J-K_HCN']  = ""

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)

