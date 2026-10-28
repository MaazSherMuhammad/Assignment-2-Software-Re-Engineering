
import unittest

from triage import triage
from variant_data import CHANGES, MY_CLASS


class TestTriage(unittest.TestCase):
    def test_all_change_requests(self):
        for cr_id, release, hours, description in CHANGES:
            with self.subTest(cr=cr_id):
                self.assertEqual(
                    triage(description),
                    MY_CLASS[cr_id],
                    f"{cr_id}: {description}"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
