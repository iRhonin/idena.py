import functools
import os
from inspect import signature
from typing import Any, get_type_hints

import requests

from .exceptions import IdenaException


req_id: int = 0
RPC_NODE: str = os.environ.get('IDENA_RPC_NODE')
API_KEY: str = os.environ.get('IDENA_API_KEY')


# TODO: theese methods differ from other single arg methods
# the other methods accept a single item list as param
# but this one need an object
SPECIAL_FUNCS = [
    'get_raw_tx', 'get_address_pending_transactions',
    'send_dna', 'send_invite', 'change_profile',
    'activate_invite_to_random_address',
    'flip_submit', 'submit_short_answers',
    'submit_long_answers', 'estimate_deploy',
    'estimate_call', 'estimate_terminate',
    'deploy_contract', 'call_contract', 'terminate_contract',
    'readonly_call_contract', 'subscribe_to_contract_event',
    'unsubscribe_from_contract_event', 'read_events',
]

def parse_params(f, *args, **kwargs):
    bind_params = signature(f).bind(*args, **kwargs)
    bind_params.apply_defaults()
    bind_args = bind_params.arguments
    params = {}

    for k,v in bind_args.items():
        if v is None:
            continue

        if k == 'from_':
            params['from'] = v
        else:
            params[k] = v

    if len(params) == 1 and f.__name__ not in SPECIAL_FUNCS:
        return list(params.values())

    elif len(params) == 0:

        # Becuase of strange behaviour of this api
        if f.__name__ in SPECIAL_FUNCS:
            return [{}]

        return []

    return [dict(params)]


def parse_result(data: dict, type_: Any):
    if data is None:
        return

    if type_ in [bool, int, float, str, bytes]:
        try:
            return type_(data)
        except TypeError:
            return type_(data[0])

    if 'from' in data:
        data['from_'] = data['from']
        del data['from']

    if isinstance(data, str):
        return type_(data)

    if isinstance(data, list) and len(type_.__args__) == 1:
        return [type_.__args__[0](**o) for o in data]

    if len(data) == 1:
        return type_(*data)

    return type_(**data)


def method(method_name: str):
    def method_factory(func):
        return_type = get_type_hints(func)['return']

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            params = parse_params(func, *args, **kwargs)
            data = dict(
                key=API_KEY,
                id=req_id,
                method=method_name,
                params=params,
            )
            result = requests.post(RPC_NODE, json=data).json()
            if 'error' in result:
                raise IdenaException(
                    result['error']['code'],
                    result['error']['message'],
                )

            return parse_result(result['result'], return_type)
        return wrapper
    return method_factory

