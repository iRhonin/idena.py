from dataclasses import dataclass

from idena.method import parse_result


def test_parse_result():
    sample_result_1 = {
        'syncing': False,
        'from': '0x01',
    }

    @dataclass
    class SampleType:
        syncing: bool
        from_: str

    expected_result_1 = SampleType(syncing=False, from_='0x01')

    assert parse_result(sample_result_1, SampleType) == expected_result_1

    assert parse_result(None, SampleType) == None

    assert parse_result([1], int) == 1
