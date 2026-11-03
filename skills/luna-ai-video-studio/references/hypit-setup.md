# Hypit setup and evidence

Reviewed 2026-11-02 against upstream commit 0762c6be56c0af43fff3cdbdb285e21414dd249b
(package version 0.3.1). Recheck installed CLI help before using version-specific options.

Official sources:
- https://github.com/hypit-ai/hypit/blob/0762c6be56c0af43fff3cdbdb285e21414dd249b/README.md
- https://github.com/hypit-ai/hypit/blob/0762c6be56c0af43fff3cdbdb285e21414dd249b/package.json
- https://github.com/hypit-ai/hypit/blob/0762c6be56c0af43fff3cdbdb285e21414dd249b/skills/hypit/references/environment/distribution.md
- https://github.com/hypit-ai/hypit/blob/0762c6be56c0af43fff3cdbdb285e21414dd249b/skills/hypit/references/creation/reference-video.md

Node >=22.15.0 is required. pnpm 10.33.0 is upstream's contributor package manager;
ordinary npm executable installation does not require a source build or pnpm installation.
Check `node --version`, `hypit version`, `hypit paths`, `hypit --help`, and npm package records.
Never print credential values while checking the environment.

Official agent-skill install:
```sh
npx skills add hypit-ai/hypit -g
```
This installs instructions, not the executable or model accounts. In ChatGPT's managed personal
skill environment, use its supported skill installation route rather than claiming that this
command installed a visible ChatGPT skill. Preserve other skills and custom edits.

Choose ONE executable scope. Prefer isolated project installation for verification:
```sh
npm install --save-dev --save-exact @hypit/hypit@0.3.1
npm exec --no -- hypit version
npm exec --no -- hypit --help
```
Or, when machine-wide installation is wanted:
```sh
npm install --global @hypit/hypit
hypit version
```
Keep the project lockfile and record selected version and host. An npm download failure is a
blocked install, not success. No key/credits/browser/WhisperX model is supplied by these commands.

After checking help, the documented reference-inspection commands include:
```sh
hypit media probe source.mp4
hypit media tile source.mp4 --start 0 --end 6 --every 1 --to overview.jpg
hypit media tiles source.mp4 --start 2 --end 3 --every-frame --to action-frames
hypit transcribe source.mp4 --language ko --to transcript.json
```
Only run transcription after its service, resources and any spending scope are established.
For a synthetic offline smoke test, use a short FFmpeg-generated video with and without audio.
Verify probe duration and dimensions, output frames and audio/no-audio behavior. Mark this as
media-tool verification; it proves neither semantic analysis nor external generation.
