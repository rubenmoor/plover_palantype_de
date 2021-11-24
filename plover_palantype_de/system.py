from plover.system import english_stenotype

KEYS = (
    'S-', 'B-', 'G-', 'H-', 'D-', 'F-', 'M-', 'J-', 'W-', 'L-', 'N-', 'R-',
    'Ä-', 'E-', 'A-', '~-',
    '-U', '-I', '-O', '-Ü',
    '-+', '-L', '-M', '-N', '-K', '-P', '-F', '-S', '-ʃ', '-s', '-n', '-D'
)

IMPLICIT_HYPHEN_KEYS = ('R-', 'Ä-', 'E-', 'A-', '~-', '-U', '-I', '-O', '-Ü', '-+')

SUFFIX_KEYS = () # TODO: verify: what are suffix keys? ## ('-S',)

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = 'ILKSn'

ORTHOGRAPHY_RULES = [] # TODO: verify correct syntax
##english_stenotype.ORTHOGRAPHY_RULES

ORTHOGRAPHY_RULES_ALIASES = {} # TODO: verify correct syntax
##english_stenotype.ORTHOGRAPHY_RULES_ALIASES

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        'S-': 'q',
        'B-': 'a',
        'G-': 'z',
        'H-': '2',
        'D-': 'w',
        'F-': 's',
        'M-': '3',
        'J-': 'e',
        'W-': 'd',
        'L-': '4',
        'N-': 'r',
        'R-': 'f',
        'Ä-': 'c',
        'E-': 'v',
        'A-': 'b',
        '~-': 'g',
        '-U': 'h',
        '-I': 'n',
        '-O': 'm',
        '-Ü': ',',
        '-+': '7',
        '-L': 'u',
        '-M': 'j',
        '-N': '8',
        '-K': 'i',
        '-P': 'k',
        '-F': '9',
        '-S': 'o',
        '-ʃ': 'l',
        '-s': 'p',
        '-n': ';',
        '-D': '/',
        'arpeggiate': 'space',
    },
}

DICTIONARIES_ROOT = 'plover_palantype_de/dictionaries'
DEFAULT_DICTIONARIES = ( 'palantype_de.json',)
