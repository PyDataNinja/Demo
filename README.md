

```markdown
# Mutual Funds Analysis and Visualization

This program analyzes and visualizes stock market data from the Nifty 50 index. It identifies high-risk, high-return, and optimal investment opportunities based on volatility and return on investment (ROI). The program also compares the risk of selected mutual fund companies with high-growth companies.

## Features

1. **Data Preprocessing**:
   - Reads stock market data from a CSV file.
   - Handles missing values by filling them with the mean of the respective column.
   - Converts the `Date` column to a datetime format.

2. **Visualization**:
   - Plots the trend of all stocks over time using Plotly.

3. **Risk Analysis**:
   - Calculates the volatility (standard deviation) of all companies.
   - Identifies the top 10 companies with the highest volatility.

4. **Return Analysis**:
   - Calculates the percentage growth of all companies.
   - Identifies the top 10 companies with the highest average growth.

5. **ROI Analysis**:
   - Calculates the ROI for all companies.
   - Identifies the top 10 companies with the highest ROI.

6. **Optimal Investment Selection**:
   - Selects companies with high ROI and low volatility based on median thresholds.
   - Allocates investment percentages inversely proportional to volatility.

7. **Risk Comparison**:
   - Compares the risk of selected mutual fund companies with high-growth companies using a bar chart.

## Dependencies

The program requires the following Python libraries:
- `pandas`
- `plotly`
- `warnings`

Install the dependencies using:
```bash
pip install pandas plotly
```

## Usage

1. Place the `nifty50_closing_prices.csv` file in the same directory as the script.
2. Run the script to:
   - Visualize stock trends.
   - Analyze risk and return.
   - Identify optimal investment opportunities.
   - Compare risks between mutual funds and high-growth companies.

## Output

- **Visualizations**:
  - Line chart showing the trend of all stocks.
  - Bar chart comparing risks of mutual fund companies and high-growth companies.

- **Console Outputs**:
  - Top 10 companies with the highest volatility.
  - Top 10 companies with the highest average growth.
  - Top 10 companies with the highest ROI.
  - Selected companies with high ROI and low volatility.
  - Investment percentages for selected companies.

## File Structure

- `mutual_funds.py`: The main script for analysis and visualization.
- `nifty50_closing_prices.csv`: Input data file containing Nifty 50 stock prices.

## Example

Run the script:
```bash
python mutual_funds.py
```

Example output:
```
Top 10 companies with the highest volatility:
...
Top 10 companies with the highest average growth:
...
Investment percentages for selected companies:
...
```

