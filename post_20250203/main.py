import io

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
import uvicorn
import pandas as pd


app = FastAPI()


# アップロードされたデータを格納する辞書
UPLOAD_DATA = {"file": None}


@app.get("/")
def main_page() -> HTMLResponse:
    """htmlファイルを読み込んで表示するAPI
    """
    with open("./index.html", mode='r', encoding='utf-8') as f:
        content = f.read()
        
    return HTMLResponse(content=content)


@app.post("/upload")
async def upload(upload_file: UploadFile = File(...)) -> str:
    """frontendからアップロードされたデータを読み込むAPI
    """
    # バイナリデータで読み込み
    upload_data = await upload_file.read()
    # csvをpandasで読み込む
    try:
        df = pd.read_csv(io.StringIO(upload_data.decode("utf-8")))
    except:
        # csvのファイル形式でない場合はエラー
        raise HTTPException(status_code=400, detail="File format is invalid.")
    
    # 読み込んだデータを保存
    UPLOAD_DATA["file"] = df
    
    return "OK"


@app.get("/download_from_df")
async def download_from_df(ext: str) -> StreamingResponse:
    """DataFrameを指定ファイル形式でダウンロードするAPI
       (ローカルにファイル保存せず、データをファイル化して返す)
    """
    df = UPLOAD_DATA["file"]
    if df is None:
        raise HTTPException(status_code=400, detail="File has not been uploaded.")
    
    if ext == "csv":
        stream = io.StringIO()
        df.to_csv(stream, encoding='utf-8', index=False)
        stream.seek(0)
    elif ext == "xlsx":
        stream = io.BytesIO()
        df.to_excel(stream, index=False)
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
