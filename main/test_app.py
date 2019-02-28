import unittest
from unittest import TestCase
import main

class TestApp(TestCase):
    def test_hc(self):
        main.app.BUILD_METADATA = {}
        main.app.BUILD_METADATA["version"] = "1"
        main.app.BUILD_METADATA["lastcommitsha"] = "abc123"
        print(main.app.prepare_health_check_payload())
