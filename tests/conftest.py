# -*- coding: utf-8 -*-
import os

import pytest
from pymatgen import Structure

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope='module')
def get_cn5_paddlewheel_structure():
    return Structure.from_file(
        os.path.join(THIS_DIR, 'test_files', 'paddlewheel_cn5.cif'))


@pytest.fixture(scope='module')
def get_cn4_structre():
    return Structure.from_file(os.path.join(THIS_DIR, 'test_files', 'cn4.cif'))


@pytest.fixture(scope='module')
def get_testdict():

    d = {
        str(os.path.join(THIS_DIR, 'test_files', 'ABEXEM_clean.cif')): True,
        str(os.path.join(THIS_DIR, 'test_files', 'ABEXIQ_clean.cif')): True,
        str(os.path.join(THIS_DIR, 'test_files', 'ZUSNOS_clean.cif')): True,
        str(os.path.join(THIS_DIR, 'test_files', 'ac403674p_si_001_clean.cif')):
        False,
        str(os.path.join(THIS_DIR, 'test_files', 'ZUQBUK_clean.cif')): False,
        str(os.path.join(THIS_DIR, 'test_files', 'ABAVIJ_clean.cif')): False,
        str(os.path.join(THIS_DIR, 'test_files', 'FAPXIG_clean.cif')): False,
        str(os.path.join(THIS_DIR, 'test_files', 'ADABIS_clean.cif')):
        False,  # https://onlinelibrary.wiley.com/doi/epdf/10.1002/anie.201202992
        str(os.path.join(THIS_DIR, 'test_files', 'ALUJOH_clean.cif')): True,
        str(os.path.join(THIS_DIR, 'test_files', 'AMUFIZ_clean.cif')):
        True,  # CN=2 error is caught here
        str(os.path.join(THIS_DIR, 'test_files', 'DEJCIF_clean.cif')): True,
        str(os.path.join(THIS_DIR, 'test_files', 'DAWWEF_clean.cif')):
        True,  # CN=4 see-saw

        #str(os.path.join(THIS_DIR, 'test_files', 'ELIYUU_clean.cif')): False
    }

    return d
