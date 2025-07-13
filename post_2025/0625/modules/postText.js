// 入力フォームのデータを受け取り、Backendに送信

document.getElementById('textForm').addEventListener('submit', function (e) {
  e.preventDefault(); // デフォルトの送信を防ぐ

  const inputText = document.getElementById('inputText').value;

  fetch('http://localhost:8000/text', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ text: inputText })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('responseArea').innerText = 'サーバー応答: ' + JSON.stringify(data);
  })
  .catch(error => {
    document.getElementById('responseArea').innerText = 'エラー: ' + error;
  });
});