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

    weight_change = df['weight'].iloc[-1] - df['weight'].iloc[0]
    weight_progress = f"Weight change: {weight_change} kg"

    avg_caloric_intake = df['caloric_intake'].mean()
    avg_protein_intake = df['protein_intake'].mean()
    avg_carb_intake = df['carb_intake'].mean()
    avg_fat_intake = df['fat_intake'].mean()

    gemini_response = gemini_analyze(logs)

    advice = f"""
    Your average daily intake is as follows:
    - Calories: {avg_caloric_intake} kcal
    - Protein: {avg_protein_intake} g
    - Carbohydrates: {avg_carb_intake} g
    - Fats: {avg_fat_intake} g

    Analysis and Advice:
    {gemini_response}
    """

    return {
        'weight_progress': weight_progress,
        'advice': advice,
        'logs': df.to_dict(orient='records')
    }
