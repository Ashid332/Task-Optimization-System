"""Evaluation script for Task Optimization System."""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import json
from src.optimizer import TaskOptimizer


def load_test_data(test_path='data/processed/test_data.csv'):
    """Load test data."""
    print(f"Loading test data from {test_path}...")
    df = pd.read_csv(test_path)
    return df


def load_model(model_path='models/trained_model.pkl'):
    """Load trained model and scaler."""
    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)
    scaler = joblib.load(model_path.replace('trained_model', 'scaler'))
    return model, scaler


def evaluate_model(model, scaler, X_test, y_test):
    """Evaluate model performance."""
    print("Evaluating model...")
    
    # Scale test data
    X_test_scaled = scaler.transform(X_test)
    
    # Make predictions
    y_pred = model.predict(X_test_scaled)
    
    # Calculate metrics
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    rmse = np.sqrt(mse)
    
    metrics = {
        'MSE': float(mse),
        'MAE': float(mae),
        'RMSE': float(rmse),
        'R2_Score': float(r2)
    }
    
    return metrics, y_pred


def print_results(metrics):
    """Print evaluation results."""
    print("\n" + "="*50)
    print("MODEL EVALUATION RESULTS")
    print("="*50)
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
    print("="*50 + "\n")


def save_results(metrics, output_path='models/evaluation_metrics.json'):
    """Save evaluation results to JSON."""
    print(f"Saving results to {output_path}...")
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print("Results saved successfully!")


if __name__ == '__main__':
    # Load test data
    test_df = load_test_data()
    
    # Prepare features and target
    X_test = test_df.drop('completion_time', axis=1)
    y_test = test_df['completion_time']
    
    # Load model
    model, scaler = load_model()
    
    # Evaluate
    metrics, predictions = evaluate_model(model, scaler, X_test, y_test)
    
    # Print and save results
    print_results(metrics)
    save_results(metrics)
    
    print("\nEvaluation completed!")
