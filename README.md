# Sum up 25 November's world news in one image

A programmatic make.fun entry that renders a deterministic 1024×1024 PNG summarizing 25 November's world news across 9 fields and regions, designed for AI-judge readability. The image names the day prominently and covers 9 stories; the same bytes are produced on every run.

## Badges

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Frankubah1001/Sum-up-25-November-s-world-news/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Frankubah1001/Sum-up-25-November-s-world-news/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

## Description

Sum up 25 November's world news in one image — a 1024×1024 PNG entry for the make.fun "news-image-20261125" bounty ($100 in USDC). Nine stories across fields/regions, AI-judge-readable layout, byte-identical output on repeated runs.

## Run command

```sh
npm install
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Copies `entry.png` to the output directory. Outside the grader's container, `MAKEFUN_OUTPUT_DIR` stands in for `/output`.

## Transcripts

The agent build sessions are bundled in `transcripts.tar.gz` (produced with the make.fun kit CLI).

[View this bounty on make.fun](https://make.fun/bounty/news-image-20261125)