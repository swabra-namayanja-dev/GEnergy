import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from django.shortcuts import render
from io import BytesIO
import base64
import pandas as pd


# Home page
def index(request):
    return render(request, 'GEnergyWebsite/index.html')

# Dashboard view
def dashboard(request):
    # Inbound data (example TPH readings)
    data = {
        'Date': [
            '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01',
            '2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01'
        ],
        'Site': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
        'TPH (mg/kg)': [1500, 1200, 900, 600, 1800, 1500, 1100, 700]
    }

    # Load into DataFrame
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])

    # Plot the data
    plt.figure(figsize=(10, 6))
    for site in df['Site'].unique():
        site_df = df[df['Site'] == site]
        plt.plot(site_df['Date'], site_df['TPH (mg/kg)'], marker='o', label=f"Site {site}")

    plt.title("TPH Decline Over Time")
    plt.xlabel("Date")
    plt.ylabel("TPH (mg/kg)")
    plt.grid(True)
    plt.legend()

    # Save to base64 for embedding in HTML
    buffer = BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'GEnergyWebsite/dashboard.html', {
        'chart_base64': image_base64
    })
