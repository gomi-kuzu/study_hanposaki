1章
===
# 第1話
## 1.1
### とりあえず基本的な話
<div><video controls src="https://github.com/user-attachments/assets/729d594c-6af8-40cf-ac03-2c7aedc27c20" muted="true"></video></div>

- あたり前だが、ベクトル空間も集合の一種
## 1.2
### ベクトルの公理の一部について説明
<div><video controls src="https://github.com/user-attachments/assets/cf40c602-aec8-4475-b3ca-85f5e5a9b61c" muted="true"></video></div>

- 1次結合に閉じている
- もうちょいちゃんとしたベクトル空間の定義等は[こういうの](https://manabitaizen.com/books/linear-algebra/chapter1/article2)を参照

### １次結合：「分解する」という視点
<div><video controls src="https://github.com/user-attachments/assets/807d19b8-e990-4389-8759-3e83da5597eb"></video></div>

- この動画みたいに2次元で考えると、同じ（もしくは対向）方向のベクトルの組だけが分解できない例になっちゃうが、３次元を想像すると、、、
    - 2本のベクトルの平面上に乗らない点はそのベクトルらに分解はできないってカンジかな？
  
### １次結合：「空間を生成する」という視点
<div><video controls src="https://github.com/user-attachments/assets/2c0825be-4953-4f45-8277-7916f5c8f10c"></video></div>

- 一つの制約があると、ベクトル空間の次元も落ちる
  - ３変数の場合は、３次元空間の部分空間の平面を描く
      - 4変数以上の場合は、いわゆる「超平面」になる
  - このとき基底も１本減っている 
# 第2話
## 2.1
### ”線形独立”ってなんだって話
<div><video controls src="https://github.com/user-attachments/assets/0d84b634-d750-41b7-bf42-e46cd505bbcf"></video></div>

<div><video controls src="https://github.com/user-attachments/assets/66c1a153-74fd-4eff-9014-0034ab9b9e9d"></video></div>

- 従属してなければ独立
- 従属は「組」に対する概念
- 互いに置き換えがきくメンバ構成になっていることが従属
    - 主従関係はない（従属っていうより共依存！？）
### "基底"ってなんだって話
<div><video controls src="https://github.com/user-attachments/assets/44fc8234-b01a-4d64-a205-4da3d6f4b41a
"></video></div>

- "注目している"空間を表現するのに必定十分な線形独立のベクトルが基底

### おまけ：ロボティクスとの関連

作業空間を$`\mathcal{P}`$、関節空間を$`\mathcal{Q}`$とし、$`\boldsymbol{p}\in\mathcal{P},\boldsymbol{q}\in\mathcal{Q}`$とする。

## 2.2
### 座標ってなんだって話
<div><video controls src="https://github.com/user-attachments/assets/db7ddbe9-a834-4d06-a9df-aa5bc3d5862b"></video></div>

- あれ？でもこの例って、最初のベクトルが正規直行基底下での座標だったってこと？なんか鶏たまごっぽくね？…
- なんにせよ、「ベクトルは基底とあわせて初めて意味のあるもの」ってことかな
- ちなみに原点と基底のセットで、座標系になるっぽい
    - [参考](https://shiroyasu.github.io/teaching/dendai/2013/im3-f/im3-1009-text08.pdf)
 
# 第3話
## 3.1
### 内積とは？の話

<div><video controls src="https://github.com/user-attachments/assets/a765131e-9eb6-427f-a0f5-eccffe67b94e"/video></div>

- 内積の公理については↓この辺を参照
    - https://math.jp/textbooks/go4AEA3oTU6iQIozVIaR/Jq4zeUmQb0sIADUvxK8W
        - 実数ベクトルか複素ベクトルかで、微妙に話が変わるので注意

## 3.2
### 内積を使った尺度の話とか

<div><video controls src="https://github.com/user-attachments/assets/1c16e934-ab06-485c-a578-b15748285825"/video></div>

<div><video controls src="https://github.com/user-attachments/assets/00369cc0-3961-4433-9fcd-bb08bb4c4985"/video></div>

# 第4話
## 4.1
### 想像できないベクトルも”なす角”を定義できるって話
<div><video controls src="https://github.com/user-attachments/assets/22dc66d8-e713-4554-b767-325b2bbcd5ae"/video></div>

### 直交基底は便利という話
<div><video controls src="https://github.com/user-attachments/assets/71d63768-a081-4de6-bf5b-8fc56b060472"/video></div>

## 4.2
### 直交化の具体的なやり方
<div><video controls src="https://github.com/user-attachments/assets/55b3e6bd-32e9-4f70-aee5-a7c3cf894796"/video></div>

# 第5話
## 5.1
### 行列の積も色んな解釈ができるよって話
<div><video controls src="https://github.com/user-attachments/assets/15e6447e-f4f8-4ce0-8292-ba8ee11dd04a"/video></div>

## 5.2
### 行列はベクトルを変換する
<div><video controls src="https://github.com/user-attachments/assets/c5b45443-a0f7-4b30-8e94-c3025f5e1a5c"/video></div>

# 第6話
## 6.2
### 正規化ベクトルとの内積が”影”の長さになるって話
<div><video controls src="https://github.com/user-attachments/assets/66346e1b-8ca7-4e13-9f56-5cdad0ec6bcc"/video></div>

### 再考：シュミットの直交化法
<div><video controls src="https://github.com/user-attachments/assets/8e2188df-1d10-4e2d-b6fc-8e06d00d8ad3
"/video></div>

