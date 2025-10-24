『線形代数の半歩先』を勉強したときのイメージを可視化していくためのリポジトリ
===
# 環境
- Makiさんが公開しているDockerFileを使わせてもらっている→[Manim-Examples-Docker](https://github.com/Sunwood-ai-labs/Manim-Examples-Docker/)
- dockerとdocker composeをインスコしておく
```bash
git clone --recurse-submodules https://github.com/gomi-kuzu/study_hanposaki.git
cd study_hanposaki/
docker compose up -d
```
# コマンド例
- mp4を生成
```
manim sec1_1.py VectorAsNumbers
```
- movを生成
```
manim --format=mov sec1_1.py VectorAsNumbers
```
- gifを生成（qmで品質を下げないとサイズが大きくなる）
```
manim -iqm sec1_1.py VectorAsNumbers
```

# しおり
- [1章](./doc/sec1.md)