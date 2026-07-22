import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "docs" / "source"


class ProcessAndNetworkPolicyTests(unittest.TestCase):
    def test_process_page_records_training_without_scheduling_claim(self):
        processes = (SOURCE / "1-lab-overview" / "2-processes.rst").read_text(encoding="utf-8")

        self.assertIn("so the training is recorded.", processes)
        self.assertNotIn("recorded in the CTP scheduling system", processes)
        self.assertNotIn("Requesting a Static IP", processes)
        self.assertNotIn("sxp8070", processes)

    def test_booking_policy_preserves_reporting_and_duration_rules(self):
        processes = (SOURCE / "1-lab-overview" / "2-processes.rst").read_text(encoding="utf-8")

        self.assertIn("support operational reporting", processes)
        self.assertIn("reflect when the equipment", processes)
        self.assertIn("more than two consecutive weeks", processes)

    def test_shared_workstation_table_is_the_only_allocation_workflow(self):
        addresses = (SOURCE / "3-computing" / "networks" / "ip-allocation.rst").read_text(
            encoding="utf-8"
        )

        self.assertIn("Personal and temporary devices use DHCP", addresses)
        self.assertNotIn("Requesting a Static IP", addresses)
        self.assertNotIn("Configuring a Static IP", addresses)

        for workstation in ("DGX Spark", "Lambda AI Workstation", "Linux Workstation", "Vicon PC"):
            with self.subTest(workstation=workstation):
                self.assertIn(workstation, addresses)


if __name__ == "__main__":
    unittest.main()
