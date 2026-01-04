import io
from urllib.parse import quote

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
import uvicorn
import pandas as pd


app = FastAPI()

# サンプルデータ
sample_data = {
    "name": ["Miyamoto", "Ishimori", "Takamidori", "Tominaga"],
    "age": [58, 57, 58, 58], # 2025年1月現在
    "part": ["Vo./Gt.", "Gt.", "Ba.", "Dr."]
}
sample_df = pd.DataFrame(sample_data)


@app.get("/")
def main_page() -> HTMLResponse:
    """htmlファイルを読み込んで表示するAPI
    """
    with open("./index.html", mode='r', encoding='utf-8') as f:
        content = f.read()
        
    return HTMLResponse(content=content)


@app.get("/download")
def download_from_df() -> StreamingResponse:
    """DataFrameを指定ファイル形式でダウンロードするAPI
       (ローカルにファイル保存せず、データをファイル化して返す)
    """
    stream = io.StringIO()
    sample_df.to_csv(stream, encoding='utf-8', index=False)
    stream.seek(0)

    filename = "日本語ファイルサンプル.csv"
    media_type = "text/csv"
    
    return StreamingResponse(
        content=stream, 
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename*=UTF-8''{quote(filename)}"}
    )
    
    
@app.get("/download_error")
def download_from_df_error() -> StreamingResponse:
    """DataFrameを指定ファイル形式でダウンロードするAPI
       (ローカルにファイル保存せず、データをファイル化して返す)
    """
    stream = io.StringIO()
    sample_df.to_csv(stream, encoding='utf-8', index=False)
    stream.seek(0)

    filename = "日本語ファイルサンプル.csv"
    media_type = "text/csv"
    
    return StreamingResponse(
        content=stream, 
        media_type=media_type,
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


if __name__ == "__main__":
    uvicorn.run(app)
