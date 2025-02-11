import plotly.express as px
import plotly.io as pio

def create_dashboard(df):
    # Buat visualisasi
    fig1 = px.bar(df, x='item_name', y='stock_level', color='status')
    fig2 = px.pie(df, names='category', title='Inventory Distribution')
    
    # Gabungkan visualisasi
    dashboard = pio.to_html(fig1) + pio.to_html(fig2)
    
    # Inject narrative report
    with open('narrative_report.txt', 'r') as f:
        narrative = f.read()
    
    return dashboard.replace('</body>', f'<div>{narrative}</div></body>')
