# PaddleOCR Web Application

This is a simple web application built with Flask and PaddleOCR that allows users to upload an image and extract text from it. The application supports multiple languages for OCR and visualizes the recognized text on the uploaded image.

## Features

* **Image Upload:** Users can upload images through a web form.
* **Multi-language OCR:** Supports a variety of languages for text recognition, including Chinese, English, Japanese, and more (selectable via a dropdown).
* **Text Visualization:** The recognized text and its bounding boxes are drawn on the uploaded image, providing a visual representation of the OCR results.
* **Text Output:** The extracted text is also displayed below the visualized image.

## Prerequisites

Before running this application, ensure you have the following installed:

* **Python 3.x**
* **pip** (Python package installer)

You will also need to install the required Python libraries:

```bash
pip install Flask Pillow paddlepaddle paddleocr

# PaddleOCR ウェブアプリケーション

これは Flask と PaddleOCR を使用して構築されたシンプルなウェブアプリケーションで、ユーザーが画像をアップロードして画像からテキストを抽出できます。アプリケーションは OCR 用に複数の言語をサポートし、認識されたテキストをアップロードされた画像に視覚化します。

## 機能

* **画像アップロード:** ユーザーはウェブフォームを通じて画像をアップロードできます。
* **多言語 OCR:** 中国語、英語、日本語など、さまざまな言語のテキスト認識をサポートします（ドロップダウンで選択可能）。
* **テキストの視覚化:** 認識されたテキストとそのバウンディングボックスがアップロードされた画像に描画され、OCR の結果を視覚的に表現します。
* **テキスト出力:** 抽出されたテキストは、視覚化された画像の下にも表示されます。

## 前提条件

このアプリケーションを実行する前に、以下がインストールされていることを確認してください。

* **Python 3.x**
* **pip** (Python パッケージインストーラー)

また、必要な Python ライブラリをインストールする必要があります。

```bash
pip install Flask Pillow paddlepaddle paddleocr
