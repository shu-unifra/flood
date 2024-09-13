#!/bin/bash

# 默认RPC URL
RPC_URL="https://l2-rpc.unifra.xyz"

# 方法列表
methods=(
  "eth_call"                  #OK
  "eth_feeHistory"            #OK
  "eth_getBlockByNumber"      #OK
  "eth_getLogs"               #OK
  "eth_getLogsLusdTransfersL" #OK
  "eth_getLogsLusdTransfersM" #OK
  "eth_getLogsLusdTransfersS" #OK

  
  "eth_getTransactionReceipt" #ethereum_transactions_samples__L__v1_0_0.parquet
  "eth_getTransactionByHash"    #ethereum_transactions_samples__L__v1_0_0.parquet

  
  "eth_getBalance"            #ethereum_contracts_samples__L__v1_0_0.parquet 文件
  "eth_getCode"               #ethereum_contracts_samples__L__v1_0_0.parquet

  "eth_getStorageAt"          #ethereum_slots_samples__L__v1_0_0.parquet
  "eth_getTransactionCount"   #ethereum_eoas_samples__L__v1_0_0.parquet
  
  # "trace_block"               #OK  !!![the method trace_block does not exist/is not available]
  # "trace_replayBlockTransactions" #OK !!![the method trace_replayBlockTransactions does not exist/is not available]
  # "trace_replayBlockTransactionsStateDiff" #OK "the method trace_replayBlockTransactions does not exist/is not available"
  # "trace_replayBlockTransactionsVmTrace" #OK "the method trace_replayBlockTransactions does not exist/is not available"
  # "trace_replayTransaction"       #ethereum_transactions_samples__L__v1_0_0.parquet  "the method trace_replayTransaction does not exist/is not available"
  # "trace_replayTransactionStateDiff"  #ethereum_transactions_samples__L__v1_0_0.parquet the method trace_replayTransaction does not exist/is not available"
  # "trace_replayTransactionVmTrace" #ethereum_transactions_samples__L__v1_0_0.parquet "the method trace_replayTransaction does not exist/is not available"
  # "trace_transaction"              #ethereum_transactions_samples__L__v1_0_0.parquet "the method trace_transaction does not exist/is not available"
)

# export FLOOD_SAMPLES_DIR="./out"

# 如果没有提供参数，则遍历所有方法
if [ $# -eq 0 ]; then
  unset http_proxy
  unset https_proxy
  rm -rf ./out
  mkdir out
  for method in "${methods[@]}"; do
    
    cmd="flood ${method} NODE1_NAME=${RPC_URL} --rates 800 1600 3200 4500 6400 --duration 15 -o ./out/${method}"

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
  export http_proxy=127.0.0.1:8080
  export https_proxy=127.0.0.1:8080

  # 执行选定的方法
  rm -rf "./out/${selected_method}"
  #800 1600 3200 4200 6400
  cmd="flood ${selected_method} NODE1_NAME=${RPC_URL} --rates 800 1600 3200 4500 6400 --duration 15 -o ./out/${selected_method}"
  echo $cmd
  eval $cmd
fi