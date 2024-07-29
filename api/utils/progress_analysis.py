from datetime import datetime
import pandas as pd
from .gemini_analysis import gemini_analyze

def analyze_progress(user):
    logs = []
    for log in user.daily_logs:
        logs.append({
            'date': log.date,
            'caloric_intake': log.caloric_intake,
            'protein_intake': log.protein_intake,
            'carb_intake': log.carb_intake,
            'fat_intake': log.fat_intake,
            'weight': log.weight
        })
    
    df = pd.DataFrame(logs)

    weight_change = df['weight'].iloc[-1] - df['weight'].iloc[0] if df['weight'].notna().any() else 0
    weight_progress = f"Weight change: {weight_change:.2f} kg"

    avg_caloric_intake = df['caloric_intake'].mean()
    avg_protein_intake = df['protein_intake'].mean()
    avg_carb_intake = df['carb_intake'].mean()
    avg_fat_intake = df['fat_intake'].mean()

    gemini_response = gemini_analyze(logs)
    parsed_response = parse_gemini_response(gemini_response)
    advice_structure = {
    'average_intake': {
        'calories': round(avg_caloric_intake, 2),
        'protein': round(avg_protein_intake, 2),
        'carbohydrates': round(avg_carb_intake, 2),
        'fats': round(avg_fat_intake, 2)
    },
    'analysis': parsed_response[0],
    'advice': parsed_response[1]
}

    return {
        'weight_progress': weight_progress,
        'advice': advice_structure,
        'logs': df.to_dict(orient='records')
    }

def parse_gemini_response(response):
    analysis = ""
    advice = ""

    # Split the response into sections
    sections = response.split('##')

    for section in sections:
        if section.strip().startswith('Analysis:'):
            analysis = section.replace('Analysis:', '').strip()
        elif section.strip().startswith('Advice:'):
            advice = section.replace('Advice:', '').strip()
    analysis = analysis.replace('*', '')
    advice = advice.replace('*', '')
    return analysis, advice