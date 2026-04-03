import pytest

from python_code.leetcode_word_break import WordBreak


@pytest.mark.parametrize(
    ("source", "word_dict", "expected"),
    [
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("bb", ["a", "b", "bbb", "bbbb"], True),
        ("cars", ["car", "ca", "rs"], True),
        ("aaaaaaa", ["aaaa", "aaa"], True),
        ("catscat", ["cat", "cats"], True),
    ],
)
def test_word_break_cases(source: str, word_dict: list[str], expected: bool) -> None:
    assert WordBreak().wordBreak(source, word_dict) is expected