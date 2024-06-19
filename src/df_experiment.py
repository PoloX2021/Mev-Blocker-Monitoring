"""
Columns in the df:
  triple ids:
    - block_number
    - tx_hash
    - builder
  data:
    - refund_value
    - refund_cost = refund_value + 21000*base_gas_fee
    - builder_tip = direct_transfer + amount_gas*prioritry_fee (amount_gas migth be missing)
    - backrun_hash
    - winner : True or False
 """

import pandas as pd

def analysis(df):

    #90% test
    df['90%'] = ~(df['refund_cost']/df['builder_tip']<0.9)
    print(df[['builder','90%']])

    

    #relative mean comparison accross builders
    #expectance(1-refund(builder)/(largest refund for tx and block))
    df['refund_max'] = df.groupby(['block_number', 'tx_hash'])['refund_cost'].transform('max')
    df['refund_relative'] = df['refund_cost'] / df['refund_max']
    average = df.groupby('builder')['refund_relative'].mean()
    print(average)

    #



df = pd.DataFrame({
    'block_number': [1, 1, 1, 1, 1],
    'tx_hash': ['tx1', 'tx1', 'tx2', 'tx2', 'tx3'],
    'builder': ['builder1', 'builder2', 'builder1', 'builder2', 'builder1'],
    'refund_cost': [1100, 2200, 3300, 4000, 1000],
    'refund_value': [1000, 2000, 3000, 4000, 1000],
    'builder_tip': [10000, 20, None, 40, 2000]
})

analysis(df)