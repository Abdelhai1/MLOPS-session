from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI app
app = FastAPI()

# Load your pre-trained model
model = joblib.load("regression_model.pkl")

# Define a Pydantic model for input validation
class PredictionInput(BaseModel):
    feature1: int
    feature2: float
    feature3: float
    feature4: float
    feature5: float
    feature6: float
    feature7: float
    feature8: float
    feature9: float
    feature10: float
    feature11: float
    feature12: float
    feature13: float

# Define the prediction endpoint
@app.post("/predict")
def predict(input_data: PredictionInput):
    try:
        # Prepare input data for prediction
        input_features = np.array([
            [
                input_data.feature1,
                input_data.feature2,
                input_data.feature3,
                input_data.feature4,
                input_data.feature5,
                input_data.feature6,
                input_data.feature7,
                input_data.feature8,
                input_data.feature9,
                input_data.feature10,
                input_data.feature11,
                input_data.feature12,
                input_data.feature13,
            ]
        ])
        
        # Make a prediction
        prediction = model.predict(input_features)
        
        # Return the prediction
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)