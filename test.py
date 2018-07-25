import Lisa
import unittest
from numpy.testing import assert_array_equal, assert_allclose

fname_reference = __file__+"/test.h5"

fname_test = __file__+"/../test.h5"


class FileTest(unittest.TestCase):
    def setUp(self):
        self.reference_file = Lisa.File(fname_reference)
        self.test_file = Lisa.File(fname_test)
        self.ref_cfg_file = fname_reference+".cfg"
        self.test_cfg_file = fname_test+".cfg"

    def test_config_file(self):
        with open(self.ref_cfg_file) as ref_cfg:
            with open(self.test_cfg_file) as test_cfg:
                ref_cfg_c = ref_cfg.read().split('\n')
                test_cfg_c = test_cfg.read().split('\n')

        for line in ref_cfg_c:
            if line.startswith("output") or line.startswith("#"):  # skip output and comment
                continue
            self.assertTrue(line in test_cfg_c, msg=line+" not found in new configuration file")

    def test_bunch_length_data(self):
        reference_data = self.reference_file.bunch_length()
        test_data = self.test_file.bunch_length()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_bunch_length_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.bunch_length()
        test_data = self.test_file.bunch_length()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_bunch_population(self):
        reference_data = self.reference_file.bunch_population()
        test_data = self.test_file.bunch_population()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_bunch_population_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.bunch_population()
        test_data = self.test_file.bunch_population()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_bunch_position_data(self):
        reference_data = self.reference_file.bunch_position()
        test_data = self.test_file.bunch_position()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_bunch_position_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.bunch_position()
        test_data = self.test_file.bunch_position()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_bunch_profile_data(self):
        reference_data = self.reference_file.bunch_profile()
        test_data = self.test_file.bunch_profile()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_bunch_profile_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.bunch_profile()
        test_data = self.test_file.bunch_profile()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_csr_intensity_data(self):
        reference_data = self.reference_file.csr_intensity()
        test_data = self.test_file.csr_intensity()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_csr_intensity_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.csr_intensity()
        test_data = self.test_file.csr_intensity()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_csr_spectrum_data(self):
        reference_data = self.reference_file.csr_spectrum()
        test_data = self.test_file.csr_spectrum()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_csr_spectrum_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.csr_spectrum()
        test_data = self.test_file.csr_spectrum()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_energy_profile_data(self):
        reference_data = self.reference_file.energy_profile()
        test_data = self.test_file.energy_profile()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_energy_profile_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.energy_profile()
        test_data = self.test_file.energy_profile()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_energy_spread_data(self):
        reference_data = self.reference_file.energy_spread()
        test_data = self.test_file.energy_spread()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_energy_spread_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.energy_spread()
        test_data = self.test_file.energy_spread()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_impedance_data(self):
        reference_data = self.reference_file.impedance()
        test_data = self.test_file.impedance()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_impedance_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.impedance()
        test_data = self.test_file.impedance()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_particles_data(self):
        reference_data = self.reference_file.particles()
        test_data = self.test_file.particles()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_particles_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.particles()
        test_data = self.test_file.particles()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_wake_potential_data(self):
        reference_data = self.reference_file.wake_potential()
        test_data = self.test_file.wake_potential()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_wake_potential_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.wake_potential()
        test_data = self.test_file.wake_potential()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

    def test_phase_space_data(self):
        reference_data = self.reference_file.phase_space()
        test_data = self.test_file.phase_space()
        for refdata, testdata in zip(reference_data, test_data):
            assert_allclose(refdata[1], testdata[1])

    def test_phase_space_conv_factors(self):  # Probably include these in the data tests
        reference_data = self.reference_file.phase_space()
        test_data = self.test_file.phase_space()
        for refdata, testdata in zip(reference_data, test_data):
            for refattrs, testattrs in zip(refdata[1].attrs.items(), testdata[1].attrs.items()):
                self.assertAlmostEqual(refattrs[1], testattrs[1], msg="Attribute mismatch for '"+testattrs[0]+"'")

