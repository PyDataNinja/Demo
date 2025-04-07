import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
data=pd.read_csv(r'nifty50_closing_prices.csv')
data.head()

data.isna().sum()

data['HDFC.NS']=data['HDFC.NS'].fillna(data['HDFC.NS'].mean())

data.info()

data['Date'] = pd.to_datetime(data['Date'])

# now let's see the trend of all stocks
import plotly.graph_objects as go
import plotly.express as px
fig=go.Figure()
for comp in data.columns[1:]:
    fig.add_trace(go.Scatter(x=data['Date'],y=data[comp],name=comp))
fig.update_layout(title='Nifty 50 Closing Prices',xaxis_title='Date',yaxis_title='Closing Price(INR)')
plt.savefig('closing Prices')
fig.show()  

# Calculate teh companies with high risk
all_companies=data.columns[1:]
#returns_of_all_companies = data[all_companies].pct_change()
voltality_all_companies =data[all_companies].std()
print(voltality_all_companies.sort_values(ascending=False).head(10))

# calculate the companies with high return
growth_all_companies=data[all_companies].pct_change()*100
average_growth_allcompanies=growth_all_companies.mean()
print(average_growth_allcompanies.sort_values(ascending=False).head(10))

# companies with high ROI
initial_price_all=data[all_companies].iloc[0]
Final_price_all=data[all_companies].iloc[-1]
roi_all_companies = ((Final_price_all - initial_price_all)/initial_price_all) * 100
print(roi_all_companies.sort_values(ascending=False).head(10))



# top 10 companies with high ROI and less Votality
votalty_threshhold=voltality_all_companies.median()
ROI_threshhold=roi_all_companies.median()
selected_companies=roi_all_companies[(roi_all_companies>ROI_threshhold) & (voltality_all_companies<votalty_threshhold)]
print(selected_companies.sort_values(ascending=False))

# select the percentage of investment based on lower voltality
selected_voltality=voltality_all_companies[selected_companies.index]
inverse_voltality = 1/selected_voltality
investment_ratio = (inverse_voltality/inverse_voltality.sum() ) * 100
print(investment_ratio.sort_values(ascending=False))

# let’s analyze and compare our mutual fund plan by comparing it with the high-performing companies in the stock market. Let’s start by comparing the risks in our mutual fund with the risk in the high growth companies:
top_growth_companies = average_growth_allcompanies.sort_values(ascending=False).head(10)
risk_growth_rate_companies = voltality_all_companies[top_growth_companies.index]
risk_mutual_fund_companies = voltality_all_companies[selected_companies.index]
fig = go.Figure()
fig.add_trace(go.Bar(y=top_growth_companies.index, x=risk_growth_rate_companies, name='Risk Growth Rate Companies',orientation='h'))
fig.add_trace(go.Bar(y=selected_companies.index, x=risk_mutual_fund_companies, name='Risk Mutual Fund Companies',orientation='h'))
fig.update_layout(title='Risk Comparison', xaxis_title='Companies', yaxis_title='Risk')
fig.show()


