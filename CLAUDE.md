# 海外フィットネス美女ナビ - 運用ガイド

## サイト概要
- **サイト名**: 海外フィットネス美女ナビ (FITNESSBEAUTYNAVI)
- **運営**: MuscleLove
- **URL**: https://musclelove-777.github.io/overseas-fitness-girls/
- **テーマ**: 海外のIFBB Pro・CrossFit・フィットネスモデルの情報を日本語で毎日発信

## SNS
- X: @MuscleGirlLove7
- Patreon: https://www.patreon.com/MuscleLove
- GitHub: https://github.com/MuscleLove-777

## 掲載対象（ロスター）
記事対象の選手リストは必ず `references/roster.md` を読んで参照すること。リストの追加・更新もそのファイルに対して行う。

## 記事テンプレート

### ファイル構造
```
articles/
  YYYY-MM-DD-slug.html    ← 記事ファイル
```

### 記事作成ルール
1. **言語**: 日本語
2. **文字数**: 200〜400文字（本文）
3. **トーン**: 海外選手の魅力を日本のファンにわかりやすく紹介する。敬意を持ちつつ親しみやすい文体。
4. **構成**: 導入 → 選手/大会の背景 → 注目ポイント → まとめ
5. **画像**: Unsplash のフリー画像を使用（選手本人の写真は使用不可）
   - ヒーロー画像: `?w=1200&h=400&fit=crop`
   - サムネイル: `?w=600&h=300&fit=crop`
6. **タグ**: 3〜5個、#付き
7. **SEO**: title, description, og:title, og:type を必ず設定
8. 全記事とindex.htmlのフッター直前に MuscleLove広告カード（ML_PROMO_CARDマーカー）を必ず含める。広告カードにはX / Patreon / ゲームポータルの3導線を必ず入れる

### 記事テーマ例
- 選手プロフィール紹介
- 大会結果速報・レビュー
- トレーニング哲学・メソッド紹介
- ビフォーアフター・トランスフォーメーション
- 栄養・食事戦略
- 怪我からの復帰ストーリー
- ランキング・比較記事
- シーズンプレビュー・展望

### HTMLテンプレート
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【記事タイトル】 | 海外フィットネス美女ナビ</title>
  <meta name="description" content="【記事説明 80文字程度】">
  <meta property="og:title" content="【記事タイトル】">
  <meta property="og:type" content="article">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&family=Oswald:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    /* ダークテーマスタイル（既存記事からコピー） */
  </style>
</head>
<body>
  <header>...</header>
  <img class="hero-img" src="https://images.unsplash.com/photo-XXXXXXXXX?w=1200&h=400&fit=crop" alt="【説明】">
  <article>
    <div class="meta">YYYY-MM-DD | カテゴリ</div>
    <h1>【記事タイトル】</h1>
    <div class="tag-list">
      <span class="tag">#タグ1</span>
      <span class="tag">#タグ2</span>
    </div>
    <div class="content">
      <p>【本文200-400文字】</p>
    </div>
  </article>
<!-- ML_PROMO_CARD_START -->
<section style="max-width:800px;margin:32px auto;padding:0 20px;">
  <div style="background:#111827;border:1px solid rgba(255,255,255,0.14);border-radius:10px;padding:24px;text-align:center;">
    <p style="margin:0 0 6px;color:#f0f0f5;font-weight:800;">MuscleLove 公式</p>
    <p style="margin:0 0 14px;color:#9ca3af;font-size:0.9rem;">最新情報・限定コンテンツはこちら</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;">
      <a href="https://x.com/MuscleGirlLove7" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#1d9bf0;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">X @MuscleGirlLove7</a>
      <a href="https://www.patreon.com/MuscleLove" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#ff424d;color:#fff;border-radius:6px;font-weight:800;text-decoration:none;">Patreon 限定コンテンツ</a>
      <a href="https://musclelove-games.vercel.app/?utm_source=blog&amp;utm_medium=promo_card&amp;utm_campaign=overseas-fitness-girls" target="_blank" rel="noopener" style="display:inline-block;padding:10px 18px;background:#22c55e;color:#0b1220;border-radius:6px;font-weight:800;text-decoration:none;">🎮 無料ゲーム95本</a>
    </div>
  </div>
</section>
<!-- ML_PROMO_CARD_END -->
  <footer>...</footer>
</body>
</html>
```

## 毎日更新ルール

### 更新手順
1. CLAUDE.md を読んで方針確認
2. WebSearch で海外フィットネス選手の最新ニュースを検索
3. 記事を3本生成し articles/ に保存
4. index.html のブログセクションを更新（最新3記事を表示）
5. sitemap.xml を更新（新しい記事URLを追加）
6. git add → commit → push

### 検索キーワード例
- "IFBB Pro results 2026"
- "CrossFit Games 2026 news"
- "female fitness athlete news"
- "bodybuilding competition results"
- "fitness model news 2026"

### コミットメッセージ形式
```
記事更新: YYYY-MM-DD - 記事タイトル1 / 記事タイトル2 / 記事タイトル3
```

## Unsplash画像URL集（フィットネス系）
- gym workout: https://images.unsplash.com/photo-1534438327276-14e5300c3a48
- woman training: https://images.unsplash.com/photo-1550345332-09e3ac987658
- woman fitness: https://images.unsplash.com/photo-1518611012118-696072aa579a
- crossfit: https://images.unsplash.com/photo-1526506118085-60ce8714f8c5
- deadlift: https://images.unsplash.com/photo-1581009146145-b5ef050c2e1e
- kettlebell: https://images.unsplash.com/photo-1517838277536-f5f99be501cd
- dumbbell curl: https://images.unsplash.com/photo-1583454110551-21f2fa2afe61
- squat rack: https://images.unsplash.com/photo-1574680096145-d05b474e2155
- stretching: https://images.unsplash.com/photo-1518310383802-640c2de311b2
- competition: https://images.unsplash.com/photo-1533681904393-9ab6ebed60d0
- yoga fitness: https://images.unsplash.com/photo-1594381898411-846e7d193883
- boxing: https://images.unsplash.com/photo-1549060279-7e168fcee0c2
- running: https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b
- pull up: https://images.unsplash.com/photo-1541534741688-6078c6bfb5c5
- barbell: https://images.unsplash.com/photo-1606889464198-fcb18894cf71
- abs workout: https://images.unsplash.com/photo-1548690312-e3b507d8c110
