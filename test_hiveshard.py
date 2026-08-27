# test_hiveshard.py
"""
Tests for HiveShard module.
"""

import unittest
from hiveshard import HiveShard

class TestHiveShard(unittest.TestCase):
    """Test cases for HiveShard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HiveShard()
        self.assertIsInstance(instance, HiveShard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HiveShard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
