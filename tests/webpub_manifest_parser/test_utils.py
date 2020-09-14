from unittest import TestCase

from nose.tools import eq_
from parameterized import parameterized

from webpub_manifest_parser.utils import first_or_default


class UtilsTest(TestCase):
    @parameterized.expand(
        [
            ("returns_None_in_the_case_of_empty_collection", [], None, None),
            (
                "returns_default_value_in_the_case_of_empty_collection",
                [],
                "default",
                "default",
            ),
            ("returns_first_non_empty_value", [1, 2, 3], 1),
        ]
    )
    def test_first_or_default(self, _, collection, expected_result, default_value=None):
        result = first_or_default(collection, default_value)

        eq_(result, expected_result)