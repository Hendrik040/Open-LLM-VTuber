# Resource-download review fixture

This fork-only contribution is a deliberately vulnerable recording fixture.
Do not merge it upstream, deploy it, or connect real records or credentials.
All sample student records are fictional.

The source router is registered in `WebSocketServer` before the frontend mount.
The isolated runner registers that same router without initializing the AI,
audio, or WebSocket services. Its supplied launch command binds only to localhost.

From the repository root:

```sh
uv run --no-project --with fastapi==0.115.14 --with uvicorn==0.35.0 \
  python scripts/demo_resource_download.py
```

Open `http://127.0.0.1:8766/` and view the public course guide. For the controlled
demonstration, change the `filename` query value to
`../private/student-progress.csv` to show the fictional private-record exposure.
Stop the runner after recording.

The review should establish what CodeRabbit detects in this focused change.
No particular severity, reachability label, or finding-card format is promised.
