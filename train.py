"""Training script for Task Optimization System."""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import os
from src.optimizer import TaskOptimizer


def load_data(data_path='data/processed/training_data.csv'):
    """Load training data from CSV."""
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    return df


def preprocess_data(df):
    """Preprocess data for training."""
    print("Preprocessing data...")
    # Handle missing values
    df = df.fillna(df.mean())
    
    # Separate features and target
    X = df.drop('completion_time', axis=1)
    y = df['completion_time']
    
    return X, y


def train_model(X, y):
    """Train the optimization model."""
    print("Training model...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=15,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    train_score = model.score(X_train_scaled, y_train)
    test_score = model.score(X_test_scaled, y_test)
    
    print(f"Training score: {train_score:.4f}")
    print(f"Testing score: {test_score:.4f}")
    
    return model, scaler


def save_model(model, scaler, model_path='models/trained_model.pkl'):
    """Save trained model and scaler."""
    print(f"Saving model to {model_path}...")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(scaler, model_path.replace('trained_model', 'scaler'))
    print("Model saved successfully!")


if __name__ == '__main__':
    # Load data
    df = load_data()
    
    # Preprocess
    X, y = preprocess_data(df)
    
    # Train
    model, scaler = train_model(X, y)
    
    # Save
    save_model(model, scaler)
    
    print("\nTraining completed!")
    print("Model ready for deployment.")
