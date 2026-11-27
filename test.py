import unittest
from main import extract_iso_datetimes


class TestExtractIsoDatetimes(unittest.TestCase):
    def test_extract_all(self) -> None:
        text = (
            'On Sun, 13 Oct 2024 19:01:18 +0800, Test User <test@test.me> wrote:", '
            'On Tue, Oct 1, 2024 at 19:23 Test User <test@test.me> wrote:", '
            'On Mon, Oct 14, 2024, 8:06 PM Test User <test@test.me> wrote:", '
            'On Wed, 9 Oct 2024, 2:04 am Test User, <test@test.me> wrote:", '
            'On 25-Sep-2024 3:37 am, Test User <test@test.me> wrote:", '
            'On Fri, 27 Sept 2024, 17:32 Test User, <test@test.me> wrote:"'
        )
        expected = [
            "2024-10-13T11:01:18Z",
            "2024-10-01T19:23:00Z",
            "2024-10-14T20:06:00Z",
            "2024-10-09T02:04:00Z",
            "2024-09-25T03:37:00Z",
            "2024-09-27T17:32:00Z",
        ]
        self.assertEqual(extract_iso_datetimes(text), expected)

    def test_invalid(self) -> None:
        with self.assertRaises(ValueError):
            extract_iso_datetimes("No date here")


if __name__ == "__main__":
    unittest.main()