from __future__ import annotations

import typing

import flood


def get_all_equality_tests(
    start_block: int = 1_0,
    end_block: int = 9_0,
    range_size: int = 100,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[flood.EqualityTest]:
    return list(
        get_vanilla_equality_tests(
            start_block=start_block,
            end_block=end_block,
            range_size=range_size,
            random_seed=random_seed,
        )
    ) + list(
        get_trace_equality_tests(
            start_block=start_block,
            end_block=end_block,
            random_seed=random_seed,
        )
    )


def get_vanilla_equality_tests(
    start_block: int = 1_0,
    end_block: int = 9_0,
    range_size: int = 100,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[flood.EqualityTest]:
    import ctc.rpc

    start_block, end_block = flood.generators.generate_block_ranges(
        n=1,
        range_size=range_size,
        start_block=start_block,
        end_block=end_block,
        random_seed=random_seed,
    )[0]

    return [
        (
            'eth_getChainId',
            ctc.rpc.construct_eth_chain_id,
            [],
            {},
        ),
        (
            'eth_getLogs',
            ctc.rpc.construct_eth_get_logs,
            [],
            {
                #shutest
                #'address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'start_block': start_block,
                'end_block': end_block,
            },
        ),
        (
            'eth_gasPrice',
            ctc.rpc.construct_eth_chain_id,
            [],
            {},
        ),
        (
            'eth_getBalance',
            ctc.rpc.construct_eth_get_balance,
            #shutest
            #['0xeb27d00030033c29307daa483171d22eb0c93342'],
            ['0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d'],
            {
                'block_number': start_block,
            },
        ),
        (
            'eth_getTransactionCount',
            ctc.rpc.construct_eth_get_transaction_count,
            ['0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d'],
            {
                'block_number': start_block,
            },
        ),
        (
            'eth_getStorageAt',
            ctc.rpc.construct_eth_get_storage_at,
            [],
            {
                'address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'position': '0x0000000000000000000000000000000000000000000000000000000000000001',  # noqa: E501
                'block_number': start_block,
            },
        ),
        (
            'eth_getCode',
            ctc.rpc.construct_eth_get_code,
            ['0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d'],
            {},
        ),
        (
            'eth_getBlockByNumber',
            ctc.rpc.construct_eth_get_block_by_number,
            [start_block],
            {},
        ),
        (
            'eth_getBlockByHash',
            ctc.rpc.construct_eth_get_block_by_hash,
            [
                '0xc22cb0bdfd2be6ce3b420f2486209c6617d07ea9525619a4b5e2fd75379b4f94'  # noqa: E501
            ],
            {},
        ),
        (
            'eth_getTransactionByHash',
            ctc.rpc.construct_eth_get_transaction_by_hash,
            [
                '0xc165114273046a2a0aa907c2a25c1c39cda2e07b6ccdde4814888cbf815663f8'  # noqa: E501
            ],
            {},
        ),
        (
            'eth_getTransactionReceipt',
            ctc.rpc.construct_eth_get_transaction_receipt,
            [
                '0xc165114273046a2a0aa907c2a25c1c39cda2e07b6ccdde4814888cbf815663f8'  # noqa: E501
            ],
            {},
        ),
        (
            'eth_call',
            ctc.rpc.construct_eth_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'function_abi': {
                    'constant': True,
                    'inputs': [
                        {
                            'internalType': 'address',
                            'name': '',
                            'type': 'address',
                        }
                    ],
                    'name': 'balanceOf',
                    'outputs': [
                        {
                            'internalType': 'uint256',
                            'name': '',
                            'type': 'uint256',
                        }
                    ],
                    'payable': False,
                    'stateMutability': 'view',
                    'type': 'function',
                },
                'function_parameters': [
                    '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                ],
                'block_number': start_block,
            },
        ),
        (
            'eth_feeHistory',
            ctc.rpc.construct_eth_fee_history,
            [
                #shutest
                #512,
                52,
                int(start_block),
            ],
            {},
        ),
    ]


def get_trace_equality_tests(
    start_block: int = 1_0,
    end_block: int = 9_0,
    random_seed: flood.RandomSeed | None = None,
) -> typing.Sequence[flood.EqualityTest]:
    """
    ## Trace
    https://docs.alchemy.com/reference/trace-api
    https://www.quicknode.com/docs/ethereum/trace_rawTransaction
    https://openethereum.github.io/JSONRPC-trace-module

    ## Debug
    https://docs.alchemy.com/reference/debug-api-endpoints
    https://www.quicknode.com/docs/ethereum/debug_traceBlockByNumber

    not currently testing:
    - trace_rawTransaction (not sure whether this is working in Erigon)
    - trace_filter
    - trace_get
    """
    import ctc.rpc

    block_number = flood.generators.generate_block_numbers(
        n=1,
        start_block=start_block,
        end_block=end_block,
        random_seed=random_seed,
    )[0]

    function_abi = {
        'constant': True,
        'inputs': [{'internalType': 'address', 'name': '', 'type': 'address'}],
        'name': 'balanceOf',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'payable': False,
        'stateMutability': 'view',
        'type': 'function',
    }

    return [
        (
            'trace_transaction',
            ctc.rpc.construct_trace_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704'  # noqa: E501
            ],
            {},
        ),
        (
            'trace_block',
            ctc.rpc.construct_trace_block,
            [],
            {'block_number': block_number},
        ),
        (
            'trace_call',
            ctc.rpc.construct_trace_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'trace_type': ['trace'],
                'function_abi': function_abi,
                'function_parameters': [
                    '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                ],
                'block_number': block_number,
            },
        ),
        (
            'trace_call_state_diff',
            ctc.rpc.construct_trace_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'trace_type': ['stateDiff'],
                'function_abi': function_abi,
                'function_parameters': [
                    '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                ],
                'block_number': block_number,
            },
        ),
        (
            'trace_call_vm_trace',
            ctc.rpc.construct_trace_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'trace_type': ['vmTrace'],
                'function_abi': function_abi,
                'function_parameters': [
                    '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                ],
                'block_number': block_number,
            },
        ),
        (
            'trace_call_many',
            ctc.rpc.construct_trace_call_many,
            [],
            {
                'calls': [
                    {
                        'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',  # noqa: E501
                        'function_abi': function_abi,
                        'function_parameters': [
                            '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                        ],
                        'trace_type': ['trace'],
                    },
                ],
                'trace_type': ['trace'],
            },
        ),
        (
            'trace_call_many_state_diff',
            ctc.rpc.construct_trace_call_many,
            [],
            {
                'calls': [
                    {
                        'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',  # noqa: E501
                        'function_abi': function_abi,
                        'function_parameters': [
                            '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                        ],
                        'trace_type': ['stateDiff'],
                    },
                ],
                'trace_type': ['stateDiff'],
            },
        ),
        (
            'trace_call_many_vm_trace',
            ctc.rpc.construct_trace_call_many,
            [],
            {
                'calls': [
                    {
                        'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',  # noqa: E501
                        'function_abi': function_abi,
                        'function_parameters': [
                            '0x5d3a536e4d6dbd6114cc1ead35777bab948e3643'
                        ],
                        'trace_type': ['vmTrace'],
                    },
                ],
                'trace_type': ['vmTrace'],
            },
        ),
        #     (
        #         'trace_filter',
        #         ctc.rpc.construct_trace_filter,
        #         [],
        #         {
        #             'to_addresses': ['0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d'],  # noqa: E501
        #             'start_block': 10_000_000,
        #             'end_block': 10_000_001,
        #             'count': 10,
        #         }
        #     ),
        #     (
        #         'trace_get',
        #         ctc.rpc.construct_trace_get,
        #         [],
        #         {}
        #     ),
        # (
        #     'trace_raw_transaction',
        #     ctc.rpc.construct_trace_raw_transaction,
        #     ['0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675'],  # noqa: E501
        #     {'trace_type': ['trace']},
        # ),
        (
            'trace_replay_block_transactions',
            ctc.rpc.construct_trace_replay_block_transactions,
            [],
            {
                'block_number': block_number,
                'trace_type': ['trace'],
            },
        ),
        (
            'trace_replay_block_transactions_state_diff',
            ctc.rpc.construct_trace_replay_block_transactions,
            [],
            {
                'block_number': block_number,
                'trace_type': ['stateDiff'],
            },
        ),
        (
            'trace_replay_block_transactions_vm_traces',
            ctc.rpc.construct_trace_replay_block_transactions,
            [],
            {
                'block_number': block_number,
                'trace_type': ['vmTrace'],
            },
        ),
        (
            'trace_replay_transaction',
            ctc.rpc.construct_trace_replay_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704'  # noqa: E501
            ],
            {'trace_type': ['trace']},
        ),
        (
            'trace_replay_transaction_state_diff',
            ctc.rpc.construct_trace_replay_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704'  # noqa: E501
            ],
            {'trace_type': ['stateDiff']},
        ),
        (
            'trace_replay_transaction_vm_trace',
            ctc.rpc.construct_trace_replay_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704'  # noqa: E501
            ],
            {'trace_type': ['vmTrace']},
        ),
        # debug
        (
            'debug_traceBlockByHash',
            ctc.rpc.construct_debug_trace_block_by_hash,
            [
                "0xb0d8a1d393f8df60c75fac14294c7f8822ce2ea7be35a3b8e44bddf749899d8a",
                {"tracer": "callTracer", 'tracerConfig': {}},
            ],
            {},
        ),
        (
            'debug_traceBlockByHash_prestateTracer',
            ctc.rpc.construct_debug_trace_block_by_hash,
            [
                "0xb0d8a1d393f8df60c75fac14294c7f8822ce2ea7be35a3b8e44bddf749899d8a",
                {"tracer": "prestateTracer"},
            ],
            {},
        ),
        (
            'debug_traceBlockByNumber',
            ctc.rpc.construct_debug_trace_block_by_number,
            [
                '0xccde12',
                {'tracer': 'callTracer', 'tracerConfig': {}},
            ],
            {},
        ),
        (
            'debug_traceBlockByNumber_prestateTracer',
            ctc.rpc.construct_debug_trace_block_by_number,
            [
                '0xccde12',
                {'tracer': 'prestateTracer'},
            ],
            {},
        ),
        (
            'debug_traceCall',
            ctc.rpc.construct_debug_trace_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'call_data': '0x70a082310000000000000000000000006e0d01a76c3cf4288372a29124a26d4353ee51be',  # noqa: E501
                'block_number': '0x7d',
                'gas_price': '0x6ba9382b14',
                'trace_type': {'tracer': 'callTracer'},
            },
        ),
        (
            'debug_traceCall_prestateTracer',
            ctc.rpc.construct_debug_trace_call,
            [],
            {
                'to_address': '0xaF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d',
                'call_data': '0x70a082310000000000000000000000006e0d01a76c3cf4288372a29124a26d4353ee51be',  # noqa: E501
                'block_number': '0x7d',
                'gas_price': '0x6ba9382b14',
                'trace_type': {'tracer': 'prestateTracer'},
            },
        ),
        (
            'debug_traceTransaction',
            ctc.rpc.construct_debug_trace_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704',
                {'tracer': 'callTracer', 'tracerConfig': {}},
            ],
            {},
        ),
        (
            'debug_traceTransaction_prestateTracer',
            ctc.rpc.construct_debug_trace_transaction,
            [
                '0xd6427ec6b8737e3f683f5d45f7061192c36a38d04ef68d30c577ea777a006704',
                {'tracer': 'prestateTracer', 'tracerConfig': {}},
            ],
            {},
        ),
    ]

