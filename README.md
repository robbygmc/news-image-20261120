# The World Today — Friday, 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/robbygmc/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/robbygmc/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One-image summary of Friday 20 November 2026's world news, built for the
[make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120)
(`news-image-20261120`).

## The image

A newspaper front page — masthead with the date, one big lead story with a
drawn scene, then the rest of the day's stories in a clean grid:

- **Lead:** Missile hits Riyadh's tallest tower — a Houthi strike damages
  the PIF Tower's facade across seven floors; no one hurt, the financial
  district shut, and Saudi defences intercept more missiles on Friday.
- **Anthropic's debut fades to $97.17** — opened at $111.50, closed 17%
  above its $83 IPO price; a record $81.3bn listing.
- **Nikkei plunges 5.1%** — Tokyo closes down 3,008 at 56,437, its
  fifth-biggest drop ever; the S&P 500 falls 2%, a fifth straight loss.
- **Kyiv bridges hit in an overnight raid; the Senate passes its energy
  bill 62–33; Trump pardons Pete Rose; GTA 6 makes an estimated $2.36bn
  in a day; a UK–EU youth mobility deal nears; Kenya's last Ebola patient
  goes home** — plus a Europe-wide youth strike.

All text is drawn with PIL + DejaVu fonts; the Riyadh night scene is a
flat vector-style drawing made with PIL primitives. No AI-rendered text
anywhere, so nothing can come out garbled.

## How it is built

`compose.py` (in the parent workspace, kept out of this repo's history)
draws `entry.png` from scratch — masthead, date band, lead art, headlines,
grid and footer. `main.py` copies the finished `entry.png` to the output
directory, byte-for-byte identical on every run.
