import os
import pytest
from typing import (
    List,
)

from eth2deposit.utils.constants import (
    INTL_LANG_OPTIONS,
    MNEMONIC_LANG_OPTIONS,
)
from eth2deposit.utils.intl import (
    fuzzy_reverse_dict_lookup,
    get_first_options,
    load_text,
)


@pytest.mark.parametrize(
    'params, file_path, func, lang, found_str', [
        (['arg_mnemonic_language', 'prompt'], os.path.join('eth2deposit', 'cli', 'new_mnemonic.json'),
         'new_mnemonic', 'en', 'Please choose your mnemonic language'),
        (['arg_mnemonic_language', 'prompt'], os.path.join('eth2deposit', 'cli', 'new_mnemonic.json'),
         'new_mnemonic', 'ja', 'ニーモニックの言語を選択してください'),
    ]
)
def test_load_text(params: List[str], file_path: str, func: str, lang: str, found_str: str) -> None:
    assert found_str in load_text(params, file_path, func, lang)


@pytest.mark.parametrize(
    'options, first_options', [
        ({'a': ['a', 1], 'b': range(5), 'c': [chr(i) for i in range(65, 90)]}, ['a', 0, 'A']),
    ]
)
def test_get_first_options(options, first_options):
    assert get_first_options(options) == first_options


@pytest.mark.parametrize(
    'test, match, options', [
        ('English', 'english', MNEMONIC_LANG_OPTIONS),
        ('한국어', 'korean', MNEMONIC_LANG_OPTIONS),
        ('Roman', 'ro', INTL_LANG_OPTIONS),
    ]
)
def test_fuzzy_reverse_dict_lookup(test, match, options):
    assert fuzzy_reverse_dict_lookup(test, options) == match
