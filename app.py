import streamlit as st

TOTAL_SUPPLY = 21_000_000.00
SATS_PER_BTC = 100_000_000.00
BLOCKS_PER_YEAR = 6 * 24 * 365 # 6 blocks per hour, 24 hours per day, 365 days per year
VBYTES_PER_BLOCK = 1_000_000

def calculate_security_cost_yearly(tx_per_year, security_budget_rate):
    return TOTAL_SUPPLY * security_budget_rate 

def calculate_cost_per_tx(security_cost, tx_per_year):
    return security_cost / tx_per_year

def calculate_cost_in_sats(cost_per_tx, sats_per_btc):
    return cost_per_tx * sats_per_btc

def calculate_txs_per_block(vbytes_per_tx):
    return VBYTES_PER_BLOCK / vbytes_per_tx

def main():
    st.title("Bitcoin Lightning Implications")

    st.sidebar.title("Parameters")
    price = st.sidebar.number_input("Bitcoin Price", value=1_000_000.00)
    vbytes_per_tx = st.sidebar.number_input("vBytes Per Average Ln Transaction", value=164.25)
    tx_per_year = calculate_txs_per_block(vbytes_per_tx) * BLOCKS_PER_YEAR
    security_budget_rate = st.sidebar.slider("Security Budget Rate Basis Points", value=30, min_value=1, max_value=300, step=1) / 10_000
    logical_max_fee_to_pay = st.sidebar.slider("Logical Max Fee to Pay Basis Points", value=100, min_value=1, max_value=300, step=1) / 10_000
    average_txs_per_node_per_year = st.sidebar.slider("Average Txs per Node per Year", value=1, min_value=1, max_value=10, step=1)
    
    st.write("## On-Chain Capacity")
    st.write("Bitcoin has a fixed supply of 21 million BTC. The security budget is a percentage of the total supply that must go to miners to maintain the security of the network. Currently, the security budget is set at 30 basis points, or 0.3% of the total supply. This is the cost of securing the network for a year. This assumes the subsidy is zero and the only income for miners is the transaction fees.")
    txs_per_block = calculate_txs_per_block(vbytes_per_tx)
    security_cost = calculate_security_cost_yearly(tx_per_year, security_budget_rate)
    cost_per_block = security_cost / BLOCKS_PER_YEAR
    
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Txs Per Block", f"{txs_per_block:,.0f}", "")
    col2.metric("Security Cost Yearly", f"{security_cost:,.0f} BTC", "")
    col3.metric("Cost Per Block", f"{cost_per_block:,.2f} BTC", "")

    cost_per_tx = SATS_PER_BTC * cost_per_block / txs_per_block
    
    st.write("## Cost per Transaction")
    st.write("The cost per transaction is the cost of securing the network divided by the number of transactions per year. This is the cost of securing the network per transaction incurred by the users.")
    col4, col5, col6 = st.columns(3)
    col4.metric("Cost Per Transaction", f"{cost_per_tx:,.0f} sats", "")
    col5.metric("Cost Per Transaction", f"${cost_per_tx / SATS_PER_BTC * price:,.2f}", "")
    col6.metric("Cost Per Transaction", f"{cost_per_tx / vbytes_per_tx :,.0f} sat/vB", "")
    
    implied_channel_size =  cost_per_tx / logical_max_fee_to_pay
    st.write("## Logical Channel Sizes")
    st.write("The logical channel size is based on the cost per transaction and the logical max fee to pay. This is the implied channel size that can be supported by the cost per transaction. For example no one would open a channel with a capacity of 100,000 sats if the cost per transaction is 20k sats, a 20% fee. I suspect the logical max fee to pay is around 100 basis points or 1% of the channel size.")
    col7, col8, col9 = st.columns(3)
    
    col7.metric("Implied Channel Size", f"{implied_channel_size:,.0f} sats", "")
    col8.metric("Implied Channel Size", f"${implied_channel_size / SATS_PER_BTC * price:,.0f}", "")
    col9.metric("Implied Channel Size", f"{implied_channel_size / vbytes_per_tx :,.0f} sat/vB", "")
    
    st.write("## Max number of channels and nodes")
    st.write("The max number of channels and nodes is based on the total supply of bitcoin and the implied channel size. This is the maximum number of channels and nodes that can be supported by the total supply of bitcoin.")
    max_channels = TOTAL_SUPPLY*SATS_PER_BTC / implied_channel_size
    st.write(f"Max Channels: {max_channels:,.0f}")
    st.write(f"Implied Number of Nodes: {max_channels / average_txs_per_node_per_year:,.0f}")
    
    st.write("## Time required to open all channels")
    time_to_open_all_channels = max_channels / tx_per_year
    st.write(f"Time to Open All Channels: {time_to_open_all_channels:,.2f} years")
    
    



if __name__ == "__main__":
    main()
