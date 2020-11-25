import functools
import os
from inspect import signature
from typing import Any, get_type_hints

import requests

from .exceptions import IdenaException

req_id: int = 0
RPC_NODE: str = os.environ.get('IDENA_RPC_NODE')
API_KEY: str = os.environ.get('IDENA_API_KEY')


def parse_params(f, *args, **kwargs):
    bind_params = signature(f).bind(*args, **kwargs)
    bind_params.apply_defaults()
    bind_args = bind_params.arguments
    
    for k,v in bind_args.items():
        if v is None:
            del bind_args[k]

    if len(bind_args) == 1:
        return list(bind_args.values())
    elif len(bind_args) == 0:
        return []

    return [dict(bind_args)]


def parse_result(data: dict, type_: Any):
    if data is None:
        return

    if 'from' in data:
        data['from_'] = data['from']
        del data['from']

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

