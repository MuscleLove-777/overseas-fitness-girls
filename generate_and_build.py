"""overseas-fitness-girls 自動記事生成エントリ"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, r"C:\Users\atsus\000_ClaudeCode\007_自動投稿ブログ")
import fitness_auto_post_lib as lib  # noqa: E402

CLAUDE_MD = (HERE / "CLAUDE.md").read_text(encoding="utf-8") if (HERE / "CLAUDE.md").exists() else ""

CFG = {
    "site_dir": HERE,
    "blog_name": "海外フィットネスガールズ",
    "site_url": "https://musclelove-777.github.io/overseas-fitness-girls",
    "twitter_site": "@MuscleGirlLove7",
    "accent_color": "#00bcd4",
    "categories": [
        "海外インフルエンサー紹介", "海外大会レポート", "海外ジム文化",
        "海外発トレーニング法", "海外発メソッド・食事", "コラム",
    ],
    "seed_topics": CLAUDE_MD,
    "image_query": "fitness women international",
}

if __name__ == "__main__":
    res = lib.run(CFG)
    print(res)
