# python ai_portfolio.py --tickers AAPL MSFT AMZN GOOGL TSLA META NVDA JPM V MA
# Imports and Argument Parsing
import argparse
import pandas as pd
import numpy as np
import yfinance as yf
import torch
import torch.nn as nn
import torch.optim as optim
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Data Input and Preprocessing
# Fetch historical stock data for the given tickers.
# Returns a DataFrame with adjusted close prices and basic features.
def fetch_stock_data(tickers, start_date='2024-01-01', end_date='2024-12-31'):
    data = {}
    returns = []
    volatility=[]
    for ticker in tickers:
        stock = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
        print("stock for ticker:\n", stock , "" , ticker)
        if stock.empty:
            print(f'Warning: No data for {ticker}')
            continue
        data[ticker] = [stock['Close']]

        df = pd.DataFrame(stock['Close'])
        # Feature engineering: calculate returns and volatilities
        returns.append(df.pct_change().mean())
        volatility.append(df.pct_change().std())

    features = pd.DataFrame({
            'Return': returns,
            'Volatility': volatility
            }, index=tickers)
    # Set the option to disable silent downcasting
    pd.set_option('future.no_silent_downcasting', True)
    features = features.fillna(0)
    return features

# PyTorch Model Design
# Simple feedforward neural network for stock feature analysis.
class StockRankNet(nn.Module):
    def __init__(self, input_dim, hidden_dim=16):
        super(StockRankNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, 1)

    def forward(self, x):
            out = self.fc1(x)
            out = self.relu(out)
            out = self.fc2(out)
            return out

# Train the PyTorch model to predict a target score for each stock.
# For demonstration, we'll use returns as a proxy target.
def train_model(features, targets, epochs=50):
    X = torch.tensor(features.values.astype(np.float32), dtype=torch.float32)
    y = torch.tensor(targets.values.astype(np.float32), dtype=torch.float32).view(-1, 1)
    model = StockRankNet(input_dim=X.shape[1])
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(epochs):
        model.train()
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    return model

# Use the trained model to generate scores for stocks.
def predict_scores(model, features):
    X = torch.tensor(features.values.astype(np.float32), dtype=torch.float32)
    with torch.no_grad():
        scores = model(X).numpy().flatten()
    return scores

# Greedy Search Heuristic
# Greedy algorithm to rank stocks based on predicted scores.
# Selects the highest scoring stock in each round.
def greedy_rank(scores, tickers):
    ranking = []
    used = set()
    scores_copy = scores.copy()
    for _ in range(len(scores)):
        idx = np.argmax(scores_copy)
        ranking.append((tickers[idx], scores_copy[idx]))
        scores_copy[idx] = -np.inf  # Exclude selected stock
    return ranking

# Integration and Results Output
def main():
    parser = argparse.ArgumentParser(description='AI Portfolio Project: Rank Stocks using PyTorch and Greedy Search')
    parser.add_argument('--tickers', nargs=10, required=True, help='List of 10 stock tickers')
    args = parser.parse_args()
    tickers = args.tickers
    print("Fetching and preprocessing data...")
    features = fetch_stock_data(tickers)
    print("Features:\n", features)
    # For demonstration, use 'Return' as the target
    targets = features['Return']
    print("Training PyTorch model...")
    model = train_model(features, targets)
    print("Predicting scores...")
    scores = predict_scores(model, features)
    print("Ranking stocks using Greedy Search...")
    ranking = greedy_rank(scores, features.index.tolist())
    print("\nFinal Ranked List:")
    print("{:<6} {:<10} {:<10}".format("Rank", "Ticker", "Score"))
    for i, (ticker, score) in enumerate(ranking, 1):
        print("{:<6} {:<10} {:<10.4f}".format(i, ticker, score))
# Optionally, export results to CSV
    results_df = pd.DataFrame(ranking, columns=['Ticker', 'Score'])
    results_df.to_csv('Top_ranked_stocks.csv', index=False)
    print("\nResults exported to Top_ranked_stocks.csv.")

if __name__ == '__main__':
    main()
