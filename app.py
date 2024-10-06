from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import math

# Import the Cython-optimized permanent function
from permanent import permanent

app = FastAPI()

class MatrixInput(BaseModel):
    matrix: List[List[float]]

@app.post("/calculate_permanent")
async def calculate_permanent(input_data: MatrixInput):
    if not all(len(row) == len(input_data.matrix) for row in input_data.matrix):
        raise HTTPException(status_code=400, detail="Matrix must be square")
    
    try:
        result = permanent(input_data.matrix)
        return {"permanent": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)