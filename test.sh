#!/bin/bash

RPC_URL="https://l2-rpc.unifra.xyz"

methods=(
  "eth_call"
  "eth_feeHistory"
  "eth_getBalance"
  "eth_getBlockByNumber"
  "eth_getCode"
  "eth_getLogs"
  "eth_getLogsLusdTransfersL"
  "eth_getLogsLusdTransfersM"
  "eth_getLogsLusdTransfersS"
  "eth_getStorageAt"
  "eth_getTransactionByHash"
  "eth_getTransactionCount"
  "eth_getTransactionReceipt"
  "trace_block"
  "trace_replayBlockTransactions"
  "trace_replayBlockTransactionsStateDiff"
  "trace_replayBlockTransactionsVmTrace"
  "trace_replayTransaction"
  "trace_replayTransactionStateDiff"
  "trace_replayTransactionVmTrace"
  "trace_transaction"
)

for method in "${methods[@]}"; do
  echo "test.sh Calling $method..."

  rm -rf ${method}_out
  cmd="flood ${method} NODE1_NAME=https://l2-rpc.unifra.xyz --rates 400 800 1200 1600 --duration 30 -o ${method}_out"
  echo $cmd
  eval $cmd
done
