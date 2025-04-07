
# 📈 Nifty 50 Stock Analysis using Python & Plotly

This project analyzes the historical closing prices of Nifty 50 companies using Python and interactive visualizations with Plotly. The goal is to explore trends, calculate returns and risks, and identify the best investment opportunities based on ROI and volatility.

---

## 📂 Dataset

The dataset used is `nifty50_closing_prices.csv`, containing the daily closing prices of Nifty 50 companies along with dates.

---

## 🛠️ Libraries Used

- `pandas` – For data manipulation.
- `plotly.graph_objects` & `plotly.express` – For creating interactive plots.
- `warnings` – To suppress unnecessary warnings.

---

## 🔍 Key Operations & Analysis

### 1. **Data Cleaning**
- Missing values in the `HDFC.NS` column are filled with the column’s mean.
- `Date` column is converted to datetime format.

### 2. **Trend Visualization**
- A multi-line interactive plot shows the historical closing prices of all Nifty 50 stocks.

### 3. **Volatility Calculation**
- Standard deviation is used to measure the **risk (volatility)** of each stock.
- Top 10 most volatile companies are identified.

### 4. **Return Calculation**
- **Growth Rate**: Calculated as daily percentage change.
- **Average Growth**: Mean of daily returns per company.
- **ROI (Return on Investment)**: Calculated from the first to the last available price.
- Top 10 companies with highest ROI are identified.

### 5. **High ROI, Low Volatility Stocks**
- Filters companies with ROI > median ROI and volatility < median volatility.
- These are considered stable and profitable investment options.

### 6. **Investment Allocation Strategy**
- Based on **inverse volatility**: lower volatility gets higher investment weight.
- The allocation is normalized to 100%.

### 7. **Risk Comparison Plot**
- Compares the risk (volatility) of:
  - Top 10 high-growth companies.
  - Selected stable high-ROI companies (like mutual funds).
- Visualized using a horizontal bar chart.

---

## 📊 Visual Outputs

- **Line Chart**: Stock price trends over time.
- **Bar Charts**: Risk comparison between high-growth and selected companies.

---

## 🚀 How to Run

1. Install the required libraries:
   ```bash
   pip install pandas plotly
   ```

2. Update the path to your `nifty50_closing_prices.csv` file in the script:
   ```python
   data = pd.read_csv(r'path_to_your_file.csv')
   ```

3. Run the script and explore the interactive plots.

---

## 📌 Notes

- Ensure your CSV file has a `Date` column and closing prices for all companies.
- This analysis assumes no dividend or stock split adjustment.
- You can expand the script to include other technical indicators for deeper analysis.

---

## 📬 Contact

Feel free to reach out if you want to discuss further improvements or collaborate!
