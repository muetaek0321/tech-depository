
function fetchData(path) {
  // メッセージ取得APIエンドポイント（実際のAPIに置き換えてください）
  const apiUrl = `http://localhost:8000/${path}`;

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error("APIエラー: " + response.status);
      }
      return response.text(); // 文字列として受け取る場合
    })
    .then(data => {
      alert("APIからのメッセージ: " + data);
    })
    .catch(error => {
      console.error("エラー:", error);
      alert("データ取得に失敗しました。");
  });
}