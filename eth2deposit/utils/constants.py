import os


ZERO_BYTES32 = b'\x00' * 32

# Eth2-spec constants taken from https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-chain.md
DOMAIN_DEPOSIT = bytes.fromhex('03000000')
BLS_WITHDRAWAL_PREFIX = bytes.fromhex('00')
ETH1_ADDRESS_WITHDRAWAL_PREFIX = bytes.fromhex('01')

ETH2GWEI = 10 ** 9
MIN_DEPOSIT_AMOUNT = 2 ** 0 * ETH2GWEI
MAX_DEPOSIT_AMOUNT = 2 ** 5 * ETH2GWEI


# File/folder constants
WORD_LISTS_PATH = os.path.join('eth2deposit', 'key_handling', 'key_derivation', 'word_lists')
DEFAULT_VALIDATOR_KEYS_FOLDER_NAME = 'validator_keys'

# Internationalisation constants
INTL_CONTENT_PATH = os.path.join('eth2deposit', 'intl')
INTL_LANG_OPTIONS = {
    'ar': ('العربية', 'ar', 'Arabic'),
    'el': ('ελληνικά', 'el', 'Greek'),
    'en': ('English', 'en'),
    'fr': ('Français', 'Francais', 'fr', 'French'),
    'id': ('Bahasa melayu', 'Melayu', 'id', 'Malay'),
    'it': ('Italiano', 'it', 'Italian'),
    'ja': ('日本語', 'ja', 'Japanese'),
    'ko': ('한국어', '조선말', '韓國語', 'ko', 'Korean'),
    'pt-BR': ('Português do Brasil', 'Brasil', 'pt-BR', 'Brazilian Portuguese'),
    'ro': ('român', 'limba română', 'ro', 'Romainian'),
    'zh-CN': ('简体中文', 'zh-CN', 'zh', 'Chinease'),
}
MNEMONIC_LANG_OPTIONS = {
    'chinease_simplified': ('简体中文', 'zh', 'zh-CN', 'Chinese Simplified'),
    'chinease_traditional': ('繁體中文', 'zh-tw', 'Chinese Traditional'),
    'czech': ('čeština', 'český jazyk', 'cs', 'Czech'),
    'english': ('English', 'en'),
    'italian': ('Italiano', 'it', 'Italian'),
    'korean': ('한국어', '조선말', '韓國語', 'ko', 'Korean'),
    # Portuguese mnemonics are in both pt & pt-BR
    'portuguese': ('Português', 'Português do Brasil', 'pt', 'pt-BR', 'Portuguese'),
    'spanish': ('Español', 'es', 'Spanish'),
}

# Sundry constants
UNICODE_CONTROL_CHARS = list(range(0x00, 0x20)) + list(range(0x7F, 0xA0))
