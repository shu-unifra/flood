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
    table = pa.Table.from_pandas(df, preserve_index=False)
    schema = pa.schema([
        ('transaction_hash', pa.binary()),
        ('block_number', pa.int64())
    ])
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    
    # 写入 Parquet 文件
    pq.write_table(table, filename)

def generate_slot(filename:str):
    """
    {"contract_address":{"0":31,"1":152,"2":64,"3":168,"4":93,"5":90,"6":245,"7":191,"8":29,"9":23,"10":98,"11":249,"12":37,"13":189,"14":173,"15":220,"16":66,"17":1,"18":249,"19":132},"slot":{"0":250,"1":175,"2":42,"3":98,"4":135,"5":89,"6":246,"7":44,"8":130,"9":239,"10":92,"11":25,"12":30,"13":123,"14":229,"15":209,"16":110,"17":119,"18":66,"19":149,"20":96,"21":71,"22":201,"23":95,"24":33,"25":205,"26":245,"27":247,"28":165,"29":75,"30":224,"31":94},"block_number":15489279}
    {"contract_address":{"0":16,"1":227,"2":4,"3":165,"4":51,"5":81,"6":178,"7":114,"8":220,"9":65,"10":90,"11":208,"12":73,"13":173,"14":6,"15":86,"16":94,"17":189,"18":254,"19":52},"slot":{"0":188,"1":227,"2":196,"3":140,"4":47,"5":200,"6":68,"7":72,"8":190,"9":132,"10":67,"11":142,"12":185,"13":140,"14":181,"15":152,"16":211,"17":149,"18":32,"19":209,"20":233,"21":135,"22":133,"23":138,"24":51,"25":123,"26":5,"27":27,"28":15,"29":50,"30":46,"31":93},"block_number":11517931}

    contract_address: large_binary
    slot: large_binary
    block_number: int32
    """
    data = {
        'contract_address': [bytes.fromhex('aF40C1529dAa78CaB6E8E5F3752620Ea2204Be6d')]*100,
        'slot':[bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000001'),
                bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000002'),
                bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000003'),
                bytes.fromhex('0000000000000000000000000000000000000000000000000000000000000000')]*25,
        'block_number': list(range(85, 95))*10
    }
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df, preserve_index=False)
    schema = pa.schema([
        ('contract_address', pa.binary()),
        ('slot', pa.binary()),
        ('block_number', pa.int64())
    ])
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    pq.write_table(table, filename)

def generate_eoa(filename:str):
    """
    {"eoa":{"0":91,"1":247,"2":235,"3":0,"4":125,"5":137,"6":227,"7":10,"8":179,"9":84,"10":70,"11":161,"12":134,"13":231,"14":81,"15":92,"16":227,"17":16,"18":76,"19":33},"block_number":12998553}

    eoa: large_binary
    block_number: int64
    """
    # 1	0xd7d858a4960f962E5f5F2ef62349bF83e54bea01	
    # 2	0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266	
    # 3	0x718f27d1b55f1f54025183683690038421AE3a1e	
    # 4	0x1BBAb2FC5A9ddaB7DfabaCE20F05c71F4e02B95e
    # 5	0xc3AC8F4Ec5031E167DF8fAAAc6596bFa6f617Ad6
    block_numbers = list(range(1, 101))
    data = {
        'eoa': [bytes.fromhex('d7d858a4960f962E5f5F2ef62349bF83e54bea01'),
                bytes.fromhex('f39Fd6e51aad88F6F4ce6aB8827279cffFb92266'),
                bytes.fromhex('718f27d1b55f1f54025183683690038421AE3a1e'),
                bytes.fromhex('1BBAb2FC5A9ddaB7DfabaCE20F05c71F4e02B95e'),
                bytes.fromhex('c3AC8F4Ec5031E167DF8fAAAc6596bFa6f617Ad6')
                ]*20,
        'block_number': block_numbers
    }
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df, preserve_index=False)
    schema = pa.schema([
        ('eoa', pa.binary()),
        ('block_number', pa.int64())
    ])
    table = pa.Table.from_pandas(df, schema=schema, preserve_index=False)
    pq.write_table(table, filename)

# generate_tx('ethereum_transactions_samples__L__v1_0_0.parquet')
# generate_contracts("ethereum_contracts_samples__L__v1_0_0.parquet")
generate_eoa("./ethereum_eoas_samples__L__v1_0_0.parquet")
generate_slot("./ethereum_slots_samples__L__v1_0_0.parquet")

# table = pq.read_table('./aaa/ethereum_slots_samples__L__v1_0_0.parquet')
# print(table.schema)



