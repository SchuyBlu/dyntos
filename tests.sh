#!/usr/bin/bash

# The following are for my messy personal environment, uncomment if not needed
shopt -s expand_aliases
source ~/.bash_aliases

python3 -m Tests.test_wep_types
python3 -m Tests.test_wep_ids
python3 -m Tests.test_wep_fusion
python3 -m Tests.test_fuse_helpers
python3 -m Tests.test_sanitizer

