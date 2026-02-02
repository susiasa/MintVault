# test_mintvault.py
"""
Tests for MintVault module.
"""

import unittest
from mintvault import MintVault

class TestMintVault(unittest.TestCase):
    """Test cases for MintVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintVault()
        self.assertIsInstance(instance, MintVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
