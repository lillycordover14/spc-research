# Transcribing podcasts / YouTube / call recordings

Same stack as Energy-Themes. Free, local.

```bash
pip install -U openai-whisper yt-dlp        # or faster-whisper
yt-dlp -x --audio-format mp3 -o "inbox/podcasts/%(upload_date)s__%(uploader)s__%(title)s.%(ext)s" "<youtube or podcast url>"
whisper inbox/podcasts/*.mp3 --model small --output_format txt --output_dir inbox/podcasts/
python3 scripts/ingest.py --type podcast     # ingests the .txt, keeps mp3 out of git (.gitignore)
```

Tip: name the .txt `podcast__<show>__<YYYY-MM-DD>__<title>.txt` and ingest.py fills publisher/date for you.
