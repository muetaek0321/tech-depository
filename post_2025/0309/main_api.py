import io
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn
import pandas as pd


app = FastAPI()

# サンプルデータ
filepath = Path("./sample.csv")
sample_data = {
    "last_name": ["Miyamoto", "Ishimori", "Takamidori", "Tominaga"],
    "age": [58, 57, 58, 58], # 2025年1月現在
    "part": ["Vo./Gt.", "Gt.", "Ba.", "Dr."]
}
sample_df = pd.DataFrame(sample_data)
sample_df.to_csv(filepath, encoding='utf-8', index=False)


class AddData(BaseModel):
    first_name: list


@app.get("/sample_data")
def get_sample_data() -> dict:
    """サンプルデータの内容を取得するAPI
    """
    return sample_data


@app.post("/sample_data")
def get_sample_data_add(obj: AddData) -> dict:
    """受信したデータを追加したサンプルデータの内容を取得するAPI
    """
    add_data = obj.model_dump()
    print(add_data)
    
    sample_data_new = add_data | sample_data
    
    global sample_df
    sample_df = pd.DataFrame(sample_data_new)
    
    return sample_data_new


@app.get("/download_from_df")
def download_from_df(ext: str) -> StreamingResponse:
    """DataFrameを指定ファイル形式でダウンロードするAPI
       (ローカルにファイル保存せず、データをファイル化して返す)
    """
    if ext == "csv":
        stream = io.StringIO()
        sample_df.to_csv(stream, encoding='utf-8', index=False)
        stream.seek(0)
    elif ext == "xlsx":
        stream = io.BytesIO()
        sample_df.to_excel(stream, index=False)
        stream.seek(0)
    else:
        raise HTTPException(status_code=400, detail="Illegal extension.")
        
    filename = f"sample.{ext}"
    media_type = f"file/{ext}"
    
    return StreamingResponse(
        content=stream, 
        media_type=media_type,
        headers={'Content-Disposition': f'attachment; filename={filename}'}
    )


if __name__ == "__main__":
    uvicorn.run(app)
