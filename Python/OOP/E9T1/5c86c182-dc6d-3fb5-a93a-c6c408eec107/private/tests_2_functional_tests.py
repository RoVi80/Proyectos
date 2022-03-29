#!/usr/bin/env python3
from unittest import TestCase

# catch potential exception from import
try:
    from public.script import ProfanityFilter
except Exception:
    # Just make sure that all tests are still executed to have a stable number of points.
    # An appropriate warning is generated by the smoke tests.
    pass

SWEAR_WORDS = ["abcd", "xxx", "foobar"]
TEMPLATE = "1234"

class PrivateFunctionalTestSuite(TestCase):

    def setUp(self):
        try:
            self.sut = ProfanityFilter(SWEAR_WORDS, TEMPLATE)
        except:
            self.fail("@@Failed to create an instance of the filter.@@")

    def test00_no_replacement(self):
        def run():
            return self.sut.filter(expected)
        expected = "aaa bb cccc"
        self._exec(run, expected, "no replacement is necessary")

    def test01_template_same_size(self):
        def run():
            return self.sut.filter("aaa abcd cccc")
        expected = "aaa 1234 cccc"
        self._exec(run, expected, "a replacement is necessary")

    def test02_template_too_long(self):
        def run():
            return self.sut.filter("aaa foobar cccc")
        expected = "aaa 123412 cccc"
        self._exec(run, expected, "the offensive word is longer than the template")

    def test03_template_too_short(self):
        def run():
            return self.sut.filter("aaa xxx cccc")
        expected = "aaa 123 cccc"
        self._exec(run, expected, "the offensive word is shorter than the template")

    def test04_template_short_definition(self):
        def run():
            sut = ProfanityFilter(SWEAR_WORDS, "1")
            return sut.filter("aaa xxx cccc")
        expected = "aaa 111 cccc"
        self._exec(run, expected, "the template is very short")

    def test05_template_casing_and_symbols(self):
        def run():
            self.sut = ProfanityFilter(SWEAR_WORDS, "aA!")
            return self.sut.filter("aaa xxx cccc")
        expected = "aaa aA! cccc"
        self._exec(run, expected, "the template contains upper/lower case chars and symbols")

    def test06_replacement_subwords(self):
        def run():
            return self.sut.filter("aaa yxxxy cccc")
        expected = "aaa y123y cccc"
        self._exec(run, expected, "the offensive word is a subword, e.g., xxduckxx")

    def test07_replacement_start(self):
        def run():
            return self.sut.filter("xxx cccc")
        expected = "123 cccc"
        self._exec(run, expected, "the offensive word is at the sentence start")

    def test08_replacement_end(self):
        def run():
            return self.sut.filter("aaa xxx")
        expected = "aaa 123"
        self._exec(run, expected, "the offensive word is at the sentence end")

    def test09_casing_of_keyword_and_text(self):
        def run():
            sut = ProfanityFilter(["xX"], "1234567890")
            return sut.filter("aaa Xx ccc")
        expected = "aaa 12 ccc"
        self._exec(run, expected, "a provided offensive word contains lower case and upper case chars")

    def test10_casing_of_remaining_text_is_not_changed(self):
        def run():
            sut = ProfanityFilter(["xX"], "1234567890")
            return sut.filter("aAa Xx CcC")
        expected = "aAa 12 CcC"
        self._exec(run, expected, "regular text that should not be changed contains mixed cases")

    def test11_keywords_contain_symbols(self):
        def run():
            sut = ProfanityFilter(["xX!"], "1234567890")
            return sut.filter("aaa Xx! ccc")
        expected = "aaa 123 ccc"
        self._exec(run, expected, "a provided keyword contains symbols")

    def test12_keywords_unordered(self):
        def run():
            sut = ProfanityFilter(["ab", "abcd", "abc"], "1234567890")
            return sut.filter("aaa abcd ccc")
        expected = "aaa 1234 ccc"
        self._exec(run, expected, "the provided keywords are not ordered by length")

    def _exec(self, run, expected, case_desc):
        try:
            actual = run()
        except:
            m = "@@Execution failure when {}.@@".format(case_desc)
            self.fail(m)
        m = "@@Incorrect result when {}.@@".format(case_desc)
        self.assertEqual(expected, actual, m)
