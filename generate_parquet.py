import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd


def generate_contracts(filename):
    # 创建 contract_address 数据
    addr="aF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d"

    block_numbers = list(range(1, 101))  # 从 1 到 100 的区块号

    data = {
        'contract_address': [bytes.fromhex('aF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d')]*100,  # 示例数据
        'block_number':block_numbers
    }
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df, preserve_index=False)
    
    schema = pa.schema([
        ('contract_address', pa.binary()),
        ('block_number', pa.int64())
    ])
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    
    # 写入 Parquet 文件
    pq.write_table(table, filename)

def generate_tx(filename):
    block_numbers = list(range(1, 101))  # 从 1 到 100 的区块号
    data = {
        'transaction_hash': [bytes.fromhex('eda275ac58072f98e347789a1428728df3da008315bb10c18d45c4ad7c35a21b')]*100,  # 示例数据
        'block_number': block_numbers
    }
    
    # 创建 DataFrame
    df = pd.DataFrame(data)
    
    # 将 `transaction_hash` 列的字符串转换为二进制数据
    # df['transaction_hash'] = df['transaction_hash'].apply(lambda x: int(x,16))

    # 将 DataFrame 转换为 PyArrow Table
    table = pa.Table.from_pandas(df, preserve_index=False)
    
    # 确保 `transaction_hash` 列的类型为 `binary`
    schema = pa.schema([
        ('transaction_hash', pa.binary()),
        ('block_number', pa.int64())
    ])
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    
    # 写入 Parquet 文件
    pq.write_table(table, filename)

# 调用函数创建并写入 Parquet 文件
generate_tx('ethereum_transactions_samples__L__v1_0_0.parquet')
generate_contracts("ethereum_contracts_samples__L__v1_0_0.parquet")



