# SCM Operations Support Tool

A web-based Supply Chain Management (SCM) Operations Support Tool for managing customers, materials, sales orders, and support requests through a centralized application.

---

# English

## 1. Project Overview

The **SCM Operations Support Tool** is a business-oriented web application designed to support day-to-day SCM operations.

The application provides a centralized interface for managing:

- Customer master data
- Material master data
- Sales orders
- Support requests
- Operational status information

The application uses **Flask** for the backend, **PostgreSQL** for data storage, and HTML/CSS/Jinja2 for the frontend.

---

## 🚀 Live Demo / ライブデモ

**Production Application / 本番アプリケーション:**  
https://scm-operations-support-tool.onrender.com/

> The application is deployed on Render and connected to PostgreSQL.
>
> Render上にデプロイされ、PostgreSQLデータベースに接続されています。

---

## 2. Key Features

### Dashboard

- Total customer count
- Total material count
- Total sales order count
- Total support request count
- Sales order status summary
- Support request status summary

### Customer Management

- View customer records
- Search customers
- Filter records
- Sort records
- Add customers
- Edit customers
- Delete customers
- Export data

### Material Management

- View material master data
- Search materials
- Filter by category
- Filter by plant
- Filter by status
- Sort records
- Add materials
- Edit materials
- Delete materials
- Export data to CSV
- Export data to Excel

### Sales Order Management

- View sales orders
- Search and filter orders
- Sort order records
- Add sales orders
- Edit sales orders
- Delete sales orders
- View order status

### Support Request Management

- View support requests
- Search and filter requests
- Sort records
- Add support requests
- Edit support requests
- Delete support requests
- Track request status

---

## 3. Technology Stack

### Backend

- Python
- Flask
- psycopg2
- python-dotenv

### Frontend

- HTML
- CSS
- Jinja2 Templates
- JavaScript

### Database

- PostgreSQL

### Development & Deployment

- Git
- GitHub
- GitHub Codespaces
- Render

---

## 4. Database

The application uses PostgreSQL as the primary relational database.

### Main Tables

| Table              | Purpose                      |
| ------------------ | ---------------------------- |
| `customers`        | Customer master data         |
| `materials`        | Material master data         |
| `sales_orders`     | Sales order transaction data |
| `support_requests` | SCM support request data     |

The database schema, backup, and seed scripts are available in the `database/` directory.

---

## 5. Project Structure

```text
scm-operations-support-tool/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   ├── schema.sql
│   ├── scm_operations_support.sql
│   ├── seed_customers.py
│   ├── seed_materials.py
│   ├── seed_sales_orders.py
│   └── seed_support_requests.py
│
├── modules/
│   ├── db.py
│   ├── customer/
│   ├── material/
│   ├── salesorder/
│   ├── support/
│   └── validation/
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
```

---

# 6. Running the Application

## 6.1 Local Development

### Prerequisites

Install the following:

- Python 3.x
- PostgreSQL
- Git

### Step 1: Clone the Repository

Clone this GitHub repository and move into the project directory.

```bash
git clone https://github.com/dranandraj/scm-operations-support-tool
cd scm-operations-support-tool
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Configure PostgreSQL

Create a PostgreSQL database named:

```text
scm_support_db
```

Configure the following environment variables:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=scm_support_db
DB_USER=postgres
DB_PASSWORD=your_password
```

These values should be stored in a local `.env` file.

> Do not commit `.env` or database credentials to the repository.

### Step 6: Initialize the Database

The project includes database schema and seed scripts under the `database/` directory.

Use the provided schema and seed scripts to create the required tables and sample data.

### Step 7: Start the Application

```bash
python app.py
```

The Flask application can then be accessed through the local development URL displayed in the terminal.

---

# 7. GitHub Codespaces

GitHub Codespaces provides a browser-based development environment for this project.

### Steps

1. Open the GitHub repository.
2. Select **Code**.
3. Select **Codespaces**.
4. Create a new Codespace from the `main` branch.
5. Wait for the development environment to start.
6. Create or activate the Python virtual environment if required.
7. Install project dependencies:

```bash
pip install -r requirements.txt
```

8. Configure the required environment variables.
9. Start the application:

```bash
python app.py
```

10. Open the forwarded application port from the Codespaces **Ports** panel.

### Codespaces Notes

The Codespaces environment is useful for:

- Development
- Testing
- Debugging
- Database connectivity testing
- Running the Flask application without configuring a local IDE

---

# 8. Render Deployment

The application can be deployed using Render.

### Deployment Architecture

```text
GitHub Repository
       │
       ▼
Render Web Service
       │
       ▼
Flask Application
       │
       ▼
Render PostgreSQL
```

### Step 1: Create PostgreSQL Database

Create a PostgreSQL database on Render.

Configure the database and note the required connection information.

### Step 2: Create a Web Service

Create a Render Web Service connected to the GitHub repository.

Select the `main` branch.

### Step 3: Configure Environment Variables

Add the following environment variables to the Render Web Service:

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

Use the PostgreSQL database connection details provided by Render.

### Step 4: Configure Build Command

Example:

```bash
pip install -r requirements.txt
```

### Step 5: Configure Start Command

Example:

```bash
python app.py
```

### Step 6: Deploy

Deploy the service and wait for the build and deployment process to complete.

Once deployed, Render provides a public application URL.

### Render Free Resource Note

The current demo deployment uses Render free resources.

Free resources may have limitations such as:

- Service spin-down after inactivity
- Cold-start delays
- Database expiration or availability limitations
- Resource limitations

The source code, database schema, and seed scripts remain available in the GitHub repository even if the current demo deployment becomes unavailable.

---

# 9. Environment Variables

The application reads database configuration from environment variables.

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

Example local configuration:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=scm_support_db
DB_USER=postgres
DB_PASSWORD=your_password
```

For production, configure these values through the hosting platform's environment-variable settings.

---

# 10. Security

Sensitive configuration should not be committed to source control.

The following should remain private:

- Database passwords
- `.env` files
- Production credentials
- Other secrets

The `.gitignore` file is used to prevent sensitive local configuration from being committed.

---

# 11. Project Purpose

This project demonstrates practical application development for an SCM / business operations environment.

The project covers:

- Business-oriented CRUD operations
- PostgreSQL database integration
- Data validation
- Search and filtering
- Sorting
- Dashboard reporting
- CSV and Excel export
- Environment-based configuration
- Cloud deployment
- Git and GitHub workflow

The application is designed around common SCM operational activities such as customer management, material management, sales order processing, and support request tracking.

---

# 12. Future Enhancements

Potential future improvements include:

- Role-based access control
- User authentication improvements
- Pagination for large datasets
- Audit logging
- REST API integration
- Advanced operational reports
- Automated testing
- Email or notification functionality
- Advanced dashboard analytics

---

# 13. Author

**Anand Raj D**

SCM Operations | Business System Support | Python | PostgreSQL | Web Development

---

# 日本語 / Japanese

## 1. プロジェクト概要

**SCM Operations Support Tool** は、サプライチェーン・マネジメント（SCM）業務をサポートするためのWebアプリケーションです。

顧客、品目、販売注文、サポート依頼などの業務データを一元管理することを目的としています。

主な管理対象は以下のとおりです。

- 顧客マスタ
- 品目マスタ
- 販売注文
- サポート依頼
- 業務ステータス情報

バックエンドには **Flask / Python**、データベースには **PostgreSQL** を使用しています。

---

## 2. 主な機能

### ダッシュボード

- 顧客数の表示
- 品目数の表示
- 販売注文数の表示
- サポート依頼数の表示
- 販売注文ステータスの集計
- サポート依頼ステータスの集計

### 顧客管理

- 顧客情報の表示
- 顧客検索
- フィルター
- ソート
- 顧客追加
- 顧客編集
- 顧客削除
- データエクスポート

### 品目管理

- 品目マスタの表示
- 品目検索
- カテゴリによるフィルター
- プラントによるフィルター
- ステータスによるフィルター
- ソート
- 品目追加
- 品目編集
- 品目削除
- CSVエクスポート
- Excelエクスポート

### 販売注文管理

- 販売注文の表示
- 検索・フィルター
- ソート
- 販売注文追加
- 販売注文編集
- 販売注文削除
- 注文ステータス確認

### サポート依頼管理

- サポート依頼の表示
- 検索・フィルター
- ソート
- サポート依頼追加
- サポート依頼編集
- サポート依頼削除
- サポート依頼ステータス管理

---

## 3. 使用技術

### バックエンド

- Python
- Flask
- psycopg2
- python-dotenv

### フロントエンド

- HTML
- CSS
- Jinja2
- JavaScript

### データベース

- PostgreSQL

### 開発・デプロイ

- Git
- GitHub
- GitHub Codespaces
- Render

---

## 4. データベース

本アプリケーションでは、リレーショナルデータベースとして PostgreSQL を使用しています。

### 主なテーブル

| テーブル           | 用途                  |
| ------------------ | --------------------- |
| `customers`        | 顧客マスタ            |
| `materials`        | 品目マスタ            |
| `sales_orders`     | 販売注文データ        |
| `support_requests` | SCMサポート依頼データ |

データベースのスキーマ、バックアップ、初期データ用スクリプトは `database/` ディレクトリに含まれています。

---

# 5. アプリケーションの実行方法

## 5.1 ローカル環境

### 必要な環境

以下をインストールしてください。

- Python 3.x
- PostgreSQL
- Git

### 手順1：リポジトリを取得

GitHubリポジトリをCloneして、プロジェクトディレクトリに移動します。

```bash
git clone https://github.com/dranandraj/scm-operations-support-tool
cd scm-operations-support-tool
```

### 手順2：仮想環境を作成

```bash
python -m venv venv
```

### 手順3：仮想環境を有効化

#### Windows

```powershell
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 手順4：必要なパッケージをインストール

```bash
pip install -r requirements.txt
```

### 手順5：PostgreSQLを設定

以下のデータベースを作成します。

```text
scm_support_db
```

環境変数を設定します。

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=scm_support_db
DB_USER=postgres
DB_PASSWORD=your_password
```

ローカル環境では `.env` ファイルに設定します。

> `.env` ファイルやデータベースのパスワードをGitHubにコミットしないでください。

### 手順6：データベースを初期化

必要なテーブルと初期データは `database/` ディレクトリにあるスキーマおよびSeedスクリプトを使用して作成できます。

### 手順7：アプリケーションを起動

```bash
python app.py
```

ターミナルに表示されたローカルURLからアプリケーションにアクセスできます。

---

# 6. GitHub Codespaces

GitHub Codespacesを使用すると、ブラウザ上で開発環境を起動できます。

### 手順

1. GitHubリポジトリを開きます。
2. **Code** を選択します。
3. **Codespaces** を選択します。
4. `main` ブランチからCodespaceを作成します。
5. 開発環境が起動するまで待ちます。
6. 必要に応じてPython仮想環境を有効化します。
7. 必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

8. 必要な環境変数を設定します。
9. Flaskアプリケーションを起動します。

```bash
python app.py
```

10. Codespacesの **Ports** パネルから転送されたポートを開きます。

### Codespacesの用途

- 開発
- 動作確認
- デバッグ
- データベース接続確認
- ブラウザベースの開発

---

# 7. Renderへのデプロイ

本アプリケーションはRenderを使用してWebサービスとしてデプロイできます。

### デプロイ構成

```text
GitHub Repository
       │
       ▼
Render Web Service
       │
       ▼
Flask Application
       │
       ▼
Render PostgreSQL
```

### 手順1：PostgreSQLを作成

Render上でPostgreSQLデータベースを作成します。

### 手順2：Web Serviceを作成

GitHubリポジトリをRenderに接続し、`main` ブランチを使用してWeb Serviceを作成します。

### 手順3：環境変数を設定

以下の環境変数をRender Web Serviceに設定します。

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

Render PostgreSQLから提供される接続情報を使用します。

### 手順4：Build Command

```bash
pip install -r requirements.txt
```

### 手順5：Start Command

```bash
python app.py
```

### 手順6：デプロイ

Deployを実行し、BuildおよびDeploymentが完了するまで待ちます。

デプロイ完了後、Renderから公開URLが提供されます。

### Render Free Resourceについて

現在のデモ環境ではRenderのFreeリソースを使用しています。

Freeリソースには以下のような制限がある場合があります。

- 非アクティブ時のサービス停止
- Cold Startによる起動遅延
- データベースの有効期限
- リソース制限

ただし、ソースコード、データベーススキーマ、SeedスクリプトはGitHubリポジトリに保存されています。

---

# 8. 環境変数

データベース接続情報は環境変数から読み込まれます。

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

本番環境では、使用するホスティングサービスのEnvironment Variables機能を使用して設定します。

---

# 9. セキュリティ

機密情報はソースコードに直接保存しないでください。

以下の情報は公開しないでください。

- データベースパスワード
- `.env` ファイル
- 本番環境の認証情報
- その他のSecret情報

`.gitignore` を使用して、ローカルの機密設定ファイルがGitHubにコミットされないようにします。

---

# 10. プロジェクトの目的

本プロジェクトでは、SCMおよび業務システム環境で使用されるWebアプリケーションの開発を実践しています。

主に以下の技術・機能を使用しています。

- 業務向けCRUD処理
- PostgreSQLデータベース連携
- データバリデーション
- 検索・フィルター
- ソート
- ダッシュボード
- CSV / Excelエクスポート
- 環境変数による設定管理
- クラウドデプロイ
- Git / GitHubワークフロー

---

# 11. 今後の改善

今後、以下の機能を追加することを検討しています。

- ロールベースアクセス制御
- ユーザー認証の強化
- 大量データ向けページネーション
- 監査ログ
- REST API連携
- 高度な業務レポート
- 自動テスト
- メール・通知機能
- 高度なダッシュボード分析

---

# 12. 作成者

DURAIRAJ ANAND RAJ

SCM Operations | Business System Support | Python | PostgreSQL | Web Development
