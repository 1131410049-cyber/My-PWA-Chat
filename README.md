# PWA Chat App with Flask & Firebase

這是一個基於 Flask 後端與 PWA 技術開發的手機 Web 應用程式。

## 功能特點
* **PWA 支援**: 可安裝至手機桌面，具備基本離線快取。
* **Firebase 整合**: 即時留言儲存與讀取。
* **響應式設計**: 使用 Bootstrap 確保手機與桌面端皆能正常顯示。

## 快速啟動
1. 安裝依賴：`pip install flask requests`
2. 執行應用：`python app.py`
3. 訪問：`http://localhost:5000`

## 資料庫資訊
* **Firebase RTDB**: `https://chat-app-1131410049-default-rtdb.firebaseio.com/`

## 目錄結構
- `app.py`: 後端邏輯。
- `static/`: 靜態資源 (manifest, service worker)。
- `templates/`: 前端頁面模板。