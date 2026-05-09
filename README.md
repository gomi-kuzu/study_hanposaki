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
- [1部](./doc/sec1.md)
- [2部](./doc/sec2.md)
- [3部](./doc/sec3.md)

# その他
- [勉強会リンク](https://connpass.com/search/?q=%E6%95%B0%E5%AD%A6%E3%81%8B%E3%81%9F%E3%82%89%E3%83%8A%E3%82%A4%E3%83%88&start_from=2026%2F05%2F09&start_to=2026%2F11%2F09)
