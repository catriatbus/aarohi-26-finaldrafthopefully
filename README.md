Place the provided AAROHI logo image here as `aarohi25-logo.png`.

Steps (Windows):
1. Right-click the image in the chat attachment and choose "Save image as...".
2. Save it to this folder as `c:\PROJECTS\assets\aarohi25-logo.png`.

Optional: run the background removal script to make gray transparent:

```powershell
python scripts\remove_bg.py assets\aarohi25-logo.png assets\aarohi25-logo.png --r 200 --g 200 --b 200 --t 60
```

If the background shade is different, tweak `--r --g --b` and `--t`.
