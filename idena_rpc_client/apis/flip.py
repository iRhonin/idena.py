from typing import List, Tuple

from .. import types
from ..method import method


@method('flip_submit')
def submit_flip(
    publicHex:  str = None,
    privateHex: str = None,
    pairId:     str = None,
    hex:        str = None
) -> types.FlipSubmit: pass

@method('flip_shorthashes')
def get_short_flip_hashes() -> List[types.FlipHashes]: pass

@method('flip_longHashes')
def get_long_flip_hashes() -> List[types.FlipHashes]: pass

@method('flip_get')
def get_flip(hash: str) -> types.Flip: pass

@method('flip_getRaw')
def get_raw_flip(hash: str) -> types.RawFlip: pass

@method('flip_words')
def flip_words(hash: str) -> Tuple[int, int]: pass

@method('flip_delete')
def delete_flip(hash: str) -> str: pass

@method('flip_submitShortAnswers')
def submit_short_answers(answers: types.FlipAnswers) -> str: pass

@method('flip_submitLongAnswers')
def submit_long_answers(answers: types.FlipAnswers) -> str: pass

