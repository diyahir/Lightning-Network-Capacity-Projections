# Bitcoin Lightning Implications Dashboard

This Streamlit dashboard provides insights into the implications of Bitcoin Lightning Network based on various parameters and calculations.

## Features

- Calculate on-chain capacity and security costs.
- Analyze cost per transaction and logical channel sizes.
- Determine the maximum number of channels and nodes.
- Estimate the time required to open all channels.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/bitcoin-lightning-dashboard.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Adjust the parameters using the sidebar inputs.
3. Explore the calculated metrics and implications of Bitcoin Lightning Network.

## Parameters

- **Bitcoin Price:** The current price of Bitcoin in USD.
- **vBytes Per Average Ln Transaction:** The average virtual bytes (vBytes) per Lightning Network transaction.
- **Security Budget Rate Basis Points:** The security budget rate in basis points (0.3% by default).
- **Logical Max Fee to Pay Basis Points:** The logical maximum fee to pay in basis points (1% by default).
- **Average Txs per Node per Year:** The average number of transactions per Lightning Network node per year.

## Calculations

- **On-Chain Capacity:** Calculates on-chain capacity, security costs, and cost per block.
- **Cost per Transaction:** Determines the cost per transaction in satoshis, USD, and satoshis per virtual byte (sat/vB).
- **Logical Channel Sizes:** Estimates implied channel sizes based on cost per transaction and logical maximum fee to pay.
- **Max Number of Channels and Nodes:** Calculates the maximum number of channels and implied number of nodes based on total supply and implied channel size.
- **Time required to open all channels:** Estimates the time required to open all channels based on the maximum number of channels and transactions per year.
