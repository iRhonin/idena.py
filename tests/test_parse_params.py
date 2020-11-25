from idena_rpc_client.method import parse_params

def f0(x: int = 0):
    pass

def f1(x: int, y: int = 0):
    pass

def f2():
    pass

def test_parse_params():
    assert parse_params(f0) == [0]
    assert parse_params(f0, 1) == [1]

    assert parse_params(f1, 1) == [dict(x=1, y=0)]
    assert parse_params(f1, 1, 1) == [dict(x=1, y=1)]
    assert parse_params(f1, 2, y=2) == [dict(x=2, y=2)]
    assert parse_params(f1, x=3, y=3) == [dict(x=3, y=3)]

    assert parse_params(f2) == []
