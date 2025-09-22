import os
import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from classify_main import classify

app = FastAPI()


@app.post("/classify/")
async def classify_logs(file: UploadFile):
    # Check that uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")

    try:
        # Read uploaded CSV into a DataFrame
        df = pd.read_csv(file.file)

        # Ensure required columns exist
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform log classification
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        print("Dataframe:", df.to_dict())

        # Save classified DataFrame to CSV
        output_file = "files/output.csv"
        df.to_csv(output_file, index=False)
        print("File saved to output.csv")

        # Return CSV file as response
        return FileResponse(output_file, media_type='text/csv')

    except Exception as e:
        # Return 500 error if any exception occurs
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        # Close uploaded file
        file.file.close()
        # Cleanup: remove output.csv after serving
        if os.path.exists("output.csv"):
            os.remove("output.csv")
