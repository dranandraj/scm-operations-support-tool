# Business Operations Management System

A full-featured business operations web application developed using
Python, Flask, PostgreSQL, HTML, CSS, JavaScript, and Jinja2.

The application provides a centralized interface for managing customers,
materials, sales orders, and support requests.

This project demonstrates practical web application development
including backend routing, business logic, CRUD operations, relational
database integration, data validation, session management, search and
filtering, data export, dashboard reporting, and cloud deployment.

------------------------------------------------------------------------

## 🚀 Live Demo

**Production Application:**\
https://scm-operations-support-tool.onrender.com/

### Demo Login

-   **Username:** `admin`
-   **Password:** `admin123`

------------------------------------------------------------------------

# 1. Project Overview

The Business Operations Management System is a web-based business
application designed to manage operational data through a centralized
system.

The application demonstrates how a Python Flask backend processes
business requests, applies validation and business logic, communicates
with a PostgreSQL database, and provides data through a browser-based
user interface.

### Main Functional Areas

-   Customer Management
-   Material Management
-   Sales Order Management
-   Support Request Management
-   Dashboard and Operational Reporting
-   Search, Filtering, and Sorting
-   Data Validation
-   CSV / Excel Export
-   User Authentication and Session Management

------------------------------------------------------------------------

# 2. Key Features

## Dashboard

-   Total customer count
-   Total material count
-   Total sales order count
-   Total support request count
-   Sales order status summary
-   Support request status summary
-   Recent operational activity

## Customer Management

-   Create, view, update, and delete customer records
-   Search, filter, and sort records
-   Export customer data

## Material Management

-   Create, view, update, and delete material records
-   Search materials
-   Filter by category, plant, and status
-   Export data to CSV and Excel

## Sales Order Management

-   Create, view, update, and delete sales orders
-   Search, filter, and sort orders
-   View order status
-   Validate order-related data

## Support Request Management

-   Create, view, update, and delete support requests
-   Search, filter, and sort requests
-   Track request status

------------------------------------------------------------------------

# 3. Backend Development

The backend is developed using Python and Flask.

The application handles:

-   HTTP request processing
-   URL routing
-   Business logic
-   Form processing
-   Data validation
-   CRUD operations
-   Database communication
-   Session management
-   Error handling
-   Data export processing

PostgreSQL is used as the relational database, with Python database
connectivity used to communicate with the database.

------------------------------------------------------------------------

# 4. Database

PostgreSQL is used for persistent application data.

  Table                Purpose
  -------------------- ------------------------------
  `customers`          Customer master data
  `materials`          Material master data
  `sales_orders`       Sales order transaction data
  `support_requests`   Support request data

Database schema and seed scripts are included in the `database/`
directory.

------------------------------------------------------------------------

# 5. Frontend

The frontend is implemented using:

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2 Templates

JavaScript is used for client-side interactions and user interface
functionality.

------------------------------------------------------------------------

# 6. Technology Stack

### Backend

-   Python
-   Flask
-   psycopg2
-   python-dotenv

### Frontend

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2

### Database

-   PostgreSQL

### Development Tools

-   Git
-   GitHub
-   Visual Studio Code

### Deployment

-   Render

------------------------------------------------------------------------

# 7. Application Architecture

``` text
Web Browser
     |
     v
HTML / CSS / JavaScript
     |
     v
Jinja2 Templates
     |
     v
Flask Application
     |
     v
Business Logic
     |
     v
psycopg2
     |
     v
PostgreSQL
```

------------------------------------------------------------------------

# 8. CRUD Operations

CRUD operations are implemented for:

-   Customers
-   Materials
-   Sales Orders
-   Support Requests

------------------------------------------------------------------------

# 9. Data Validation

The application performs validation and error handling for business
data, including required-field checks, data-format validation,
invalid-input handling, and business data consistency checks.

------------------------------------------------------------------------

# 10. Search, Filtering, and Sorting

Users can:

-   Search records
-   Filter records
-   Sort records
-   View status information
-   Navigate through records

------------------------------------------------------------------------

# 11. Data Export

The application supports:

-   CSV export
-   Excel export

------------------------------------------------------------------------

# 12. Authentication and Session Management

The application includes login functionality and session-based
authentication to maintain the user's login state.

------------------------------------------------------------------------

# 13. Project Structure

``` text
business-operations-management-system/
|
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
|
├── database/
├── modules/
├── static/
|   └── css/
└── templates/
```

------------------------------------------------------------------------

# 14. Local Development

## Prerequisites

-   Python 3.x
-   PostgreSQL
-   Git

## Clone the Repository

``` bash
git clone https://github.com/dranandraj/business-operations-management-system
cd business-operations-management-system
```

## Create Virtual Environment

``` bash
python -m venv venv
```

### Windows

``` powershell
venv\Scripts\activate
```

### Linux / macOS

``` bash
source venv/bin/activate
```

## Install Dependencies

``` bash
pip install -r requirements.txt
```

## Configure PostgreSQL

Create a PostgreSQL database and configure:

``` text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=scm_support_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Store these values in a local `.env` file. Do not commit credentials or
`.env` files to GitHub.

## Run the Application

``` bash
python app.py
```

------------------------------------------------------------------------

# 15. Deployment

The application is deployed using Render.

``` text
GitHub Repository
       |
       v
Render Web Service
       |
       v
Flask Application
       |
       v
PostgreSQL Database
```

Environment variables are used for database configuration.

------------------------------------------------------------------------

# 16. Development Skills Demonstrated

-   Python programming
-   Flask web application development
-   Backend routing
-   Business logic
-   CRUD implementation
-   PostgreSQL database integration
-   SQL / database operations
-   Data validation
-   Form processing
-   Session management
-   HTML / CSS
-   JavaScript
-   Jinja2 templating
-   Search and filtering
-   Data export
-   Dashboard development
-   Git and GitHub
-   Cloud deployment

------------------------------------------------------------------------

# 17. Project Purpose

The purpose of this project is to demonstrate practical web application
development by building a complete business-oriented application across
the backend, database, and frontend layers.

``` text
Python
   |
Flask
   |
Business Logic
   |
PostgreSQL
   |
Jinja2
   |
HTML / CSS / JavaScript
   |
Web Application
```

------------------------------------------------------------------------

# 18. Future Improvements

Possible future enhancements include:

-   REST API development
-   Automated testing
-   Role-based access control
-   Advanced authentication
-   Audit logging
-   Advanced dashboard analytics
-   Notification functionality
-   Improved pagination for large datasets
-   API-based frontend architecture

> These are future enhancements and are not currently implemented.

------------------------------------------------------------------------

# 日本語版

# Business Operations Management System

Python、Flask、PostgreSQL、HTML、CSS、JavaScript、Jinja2を使用して開発した、業務管理Webアプリケーションです。

顧客、品目、受注、サポート依頼などの業務データを、一つのWebシステム上で管理できるように設計しています。

本プロジェクトでは、バックエンドのルーティング、業務ロジック、CRUD処理、リレーショナルデータベース連携、データバリデーション、セッション管理、検索・フィルタリング、データ出力、ダッシュボード、クラウドへのデプロイなど、Webアプリケーション開発に必要な技術を実装しています。

------------------------------------------------------------------------

# 1. プロジェクト概要

Business Operations Management
Systemは、業務データを一元管理するためのWebアプリケーションです。

Python
Flaskを使用したバックエンドでユーザーからのリクエストを処理し、入力データのバリデーションや業務ロジックを実行しながら、PostgreSQLデータベースと連携します。

### 主な機能領域

-   顧客管理
-   品目管理
-   受注管理
-   サポート依頼管理
-   ダッシュボード
-   データ検索・フィルタリング・ソート
-   データバリデーション
-   CSV / Excel出力
-   ログイン・セッション管理

------------------------------------------------------------------------

# 2. 主な機能

## ダッシュボード

-   顧客数
-   品目数
-   受注数
-   サポート依頼数
-   受注ステータス集計
-   サポート依頼ステータス集計
-   最近の活動状況

## 顧客管理

-   顧客データの登録・表示・編集・削除
-   検索・フィルタリング・ソート
-   顧客データの出力

## 品目管理

-   品目データの登録・表示・編集・削除
-   品目検索
-   カテゴリー・プラント・ステータスによるフィルタリング
-   CSV / Excel出力

## 受注管理

-   受注データの登録・表示・編集・削除
-   検索・フィルタリング・ソート
-   受注ステータス確認
-   データバリデーション

## サポート依頼管理

-   サポート依頼の登録・表示・編集・削除
-   検索・フィルタリング・ソート
-   ステータス管理

------------------------------------------------------------------------

# 3. バックエンド開発

バックエンドにはPythonとFlaskを使用しています。

主な処理：

-   HTTPリクエスト処理
-   URLルーティング
-   業務ロジック
-   フォーム処理
-   データバリデーション
-   CRUD処理
-   データベース連携
-   セッション管理
-   エラーハンドリング
-   データ出力処理

PostgreSQLをリレーショナルデータベースとして使用し、Pythonからデータベースへ接続しています。

------------------------------------------------------------------------

# 4. データベース

PostgreSQLを使用してアプリケーションデータを保存しています。

  テーブル             内容
  -------------------- --------------------
  `customers`          顧客マスタ
  `materials`          品目マスタ
  `sales_orders`       受注データ
  `support_requests`   サポート依頼データ

データベースのスキーマと初期データ作成用スクリプトは`database/`ディレクトリに含まれています。

------------------------------------------------------------------------

# 5. フロントエンド

フロントエンドには以下を使用しています。

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2 Templates

JavaScriptを使用して、画面上の操作やユーザーインターフェースの機能を実装しています。

------------------------------------------------------------------------

# 6. 技術スタック

### バックエンド

-   Python
-   Flask
-   psycopg2
-   python-dotenv

### フロントエンド

-   HTML5
-   CSS3
-   JavaScript
-   Jinja2

### データベース

-   PostgreSQL

### 開発ツール

-   Git
-   GitHub
-   Visual Studio Code

### デプロイ

-   Render

------------------------------------------------------------------------

# 7. アプリケーション構成

``` text
Web Browser
     |
     v
HTML / CSS / JavaScript
     |
     v
Jinja2 Templates
     |
     v
Flask Application
     |
     v
業務ロジック
     |
     v
psycopg2
     |
     v
PostgreSQL
```

------------------------------------------------------------------------

# 8. CRUD処理

以下の業務モジュールでCRUD処理を実装しています。

-   顧客
-   品目
-   受注
-   サポート依頼

------------------------------------------------------------------------

# 9. データバリデーション

以下のようなデータチェックとエラー処理を実装しています。

-   必須項目チェック
-   データ形式チェック
-   不正入力への対応
-   データ整合性チェック
-   エラー処理

------------------------------------------------------------------------

# 10. 検索・フィルタリング・ソート

-   データ検索
-   条件によるフィルタリング
-   ソート
-   ステータス確認
-   データ一覧表示

------------------------------------------------------------------------

# 11. データ出力

以下の形式でデータを出力できます。

-   CSV
-   Excel

------------------------------------------------------------------------

# 12. 認証・セッション管理

ログイン機能を実装しています。

セッションを利用して、ログイン状態を管理しています。

------------------------------------------------------------------------

# 13. プロジェクト構成

``` text
business-operations-management-system/
|
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
|
├── database/
├── modules/
├── static/
|   └── css/
└── templates/
```

------------------------------------------------------------------------

# 14. ローカル環境での実行

## 必要な環境

-   Python 3.x
-   PostgreSQL
-   Git

## リポジトリをClone

``` bash
git clone https://github.com/dranandraj/business-operations-management-system
cd business-operations-management-system
```

## 仮想環境の作成

``` bash
python -m venv venv
```

### Windows

``` powershell
venv\Scripts\activate
```

### Linux / macOS

``` bash
source venv/bin/activate
```

## パッケージのインストール

``` bash
pip install -r requirements.txt
```

## PostgreSQLの設定

PostgreSQLにデータベースを作成し、以下の環境変数を設定します。

``` text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=scm_support_db
DB_USER=postgres
DB_PASSWORD=your_password
```

`.env`ファイルに設定し、GitHubへパスワードなどの機密情報をアップロードしないようにしてください。

## アプリケーションの起動

``` bash
python app.py
```

------------------------------------------------------------------------

# 15. デプロイ

本アプリケーションはRenderにデプロイしています。

``` text
GitHub Repository
       |
       v
Render Web Service
       |
       v
Flask Application
       |
       v
PostgreSQL Database
```

データベース接続情報には環境変数を使用しています。

------------------------------------------------------------------------

# 16. 実装を通して身につけた技術

-   Python
-   Flask
-   Webアプリケーション開発
-   バックエンドルーティング
-   業務ロジック
-   CRUD処理
-   PostgreSQL
-   SQL / データベース操作
-   データバリデーション
-   フォーム処理
-   セッション管理
-   HTML / CSS
-   JavaScript
-   Jinja2
-   検索・フィルタリング
-   データ出力
-   ダッシュボード
-   Git / GitHub
-   クラウドデプロイ

------------------------------------------------------------------------

# 17. プロジェクトの目的

本プロジェクトでは、バックエンド、データベース、フロントエンドを組み合わせたWebアプリケーションを実際に開発することで、実践的なWebアプリケーション開発スキルを身につけることを目的としています。

``` text
Python
   |
Flask
   |
業務ロジック
   |
PostgreSQL
   |
Jinja2
   |
HTML / CSS / JavaScript
   |
Web Application
```

業務システムを想定したアプリケーションを開発することで、エンタープライズ向けWebアプリケーション開発に必要な基礎的な技術を実践しています。

------------------------------------------------------------------------

# 18. 今後の改善予定

今後の機能拡張候補：

-   REST API開発
-   自動テスト
-   ロールベースアクセス制御
-   高度な認証機能
-   監査ログ
-   高度なダッシュボード分析
-   通知機能
-   大規模データ向けページネーション改善
-   APIベースのフロントエンド構成

> ※上記は今後の改善候補であり、現在の実装には含まれていません。

------------------------------------------------------------------------

# Author

**Anand Raj D**

Python \| Flask \| PostgreSQL \| Web Application Development
