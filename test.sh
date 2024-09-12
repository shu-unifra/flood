#!/bin/bash

# 默认RPC URL
RPC_URL="https://l2-rpc.unifra.xyz"

# 方法列表
methods=(
  "eth_call"  #OK
  "eth_feeHistory" #OK
  "eth_getBalance" #会产生 eth_getBalance_out/ethereum_contracts_samples__L__v1_0_0.parquet 文件
  "eth_getBlockByNumber"
  "eth_getCode"   #eth_getCode_out/ethereum_contracts_samples__L__v1_0_0.parquet
  "eth_getLogs" #OK
  "eth_getLogsLusdTransfersL" #OK
  "eth_getLogsLusdTransfersM" #OK
  "eth_getLogsLusdTransfersS" #OK
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

export FLOOD_SAMPLES_DIR="./flood_samples"
# 如果没有提供参数，则遍历所有方法
if [ $# -eq 0 ]; then
  for method in "${methods[@]}"; do
    echo "Calling $method..."

    rm -rf ${method}_out
    cmd="flood ${method} NODE1_NAME=${RPC_URL} --rates 800 1600 3200 --duration 20 -o ${method}_out"

    echo $cmd
    eval $cmd
  done
else
  # 获取传递的参数
  selected_method="$1"

  # 验证方法是否在列表中
  if [[ ! " ${methods[@]} " =~ " ${selected_method} " ]]; then
    echo "Error: Invalid method '$selected_method'"
    echo "Available methods: ${methods[*]}"
    exit 1
  fi

  # 执行选定的方法
  echo "Calling $selected_method..."

  rm -rf ${selected_method}_out
  cmd="flood ${selected_method} NODE1_NAME=${RPC_URL} --rates  800 1600 3200 --duration 20 -o ${selected_method}_out"
  echo $cmd
  eval $cmd
fi