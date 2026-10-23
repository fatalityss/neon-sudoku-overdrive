# Changelog

All notable changes to Neon Sudoku: Overdrive are recorded here. The project uses `V<major>.<minor>` build numbers; the current number lives in the [`VERSION`](VERSION) file and is stamped into `index.html` by `build/build.py`.

## [Unreleased]

- Single source of truth for the build number: `VERSION` file read by `build/build.py`; the page title, the embedded patch header and `globalThis.NEON_VERSION` are generated from it instead of being hand-edited.
- This changelog.

## [1.51] – 2026-10-21

- First public source release on GitHub (MIT for code; see `ASSETS.md` for media terms).
- Single-file offline build (`index.html`) with all media embedded.

## [1.50]

- Timer rebalance (`src/v1-denge.js`): starting time is `30 + max(0, moves − 12) × 0.9` seconds, giving 30–52 seconds per level; bonuses are scaled to this base.

## [1.46]

- Button press feedback (`src/v1-dokunus.js`): press darkening, ember sparks, edge glow and a new click sound.

[Unreleased]: https://github.com/fatalityss/neon-sudoku-overdrive/compare/main...HEAD
[1.51]: https://github.com/fatalityss/neon-sudoku-overdrive/tree/main
[1.50]: https://github.com/fatalityss/neon-sudoku-overdrive/blob/main/src/v1-denge.js
[1.46]: https://github.com/fatalityss/neon-sudoku-overdrive/blob/main/src/v1-dokunus.js
