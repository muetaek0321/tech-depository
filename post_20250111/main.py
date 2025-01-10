import io
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
import uvicorn
import pandas as pd


app = FastAPI()

# サンプルデータ
filepath = Path("./sample.csv")
sample_data = {
    "name": ["Miyamoto", "Ishimori", "Takamidori", "Tominaga"],
    "age": [58, 57, 58, 58], # 2025年1月現在
    "part": ["Vo./Gt.", "Gt.", "Ba.", "Dr."]
}
sample_df = pd.DataFrame(sample_data)
sample_df.to_csv(filepath, encoding='utf-8', index=False)


@app.get("/")
def main_page() -> HTMLResponse:
    """htmlファイルを読み込んで表示するAPI
    """
    with open("./index.html", mode='r', encoding='utf-8') as f:
        content = f.read()
        
    return HTMLResponse(content=content)


@app.get("/download_from_file")
def download_from_file() -> FileResponse:
    """ファイルをダウンロードするAPI
    """
    return FileResponse(filepath, media_type="file/csv", filename=filepath.name)


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
