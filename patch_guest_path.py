from pathlib import Path

index = Path('index.html')
text = index.read_text(encoding='utf-8')

old = '''const rawGuestQuery = window.location.search.slice(1);\nlet guestParam = "";\n\nif (rawGuestQuery && !rawGuestQuery.includes("=")) {\n    try {\n        guestParam = decodeURIComponent(rawGuestQuery.replace(/\\+/g, " "));\n    } catch (error) {\n        guestParam = rawGuestQuery.replace(/\\+/g, " ");\n    }\n} else {\n    const params = new URLSearchParams(window.location.search);\n    guestParam = params.get("guest") || "";\n}\n\nconst guest = (guestParam || "ضيفنا العزيز").trim() || "ضيفنا العزيز";\n'''

new = '''const rawGuestQuery = window.location.search.slice(1);\nconst rawGuestPath = window.location.pathname.replace(/^\\/+|\\/+$/g, "");\nlet guestParam = "";\n\nif (rawGuestPath && rawGuestPath !== "index.html" && rawGuestPath !== "404.html") {\n    try {\n        guestParam = decodeURIComponent(rawGuestPath.replace(/\\+/g, " "));\n    } catch (error) {\n        guestParam = rawGuestPath.replace(/\\+/g, " ");\n    }\n} else if (rawGuestQuery && !rawGuestQuery.includes("=")) {\n    try {\n        guestParam = decodeURIComponent(rawGuestQuery.replace(/\\+/g, " "));\n    } catch (error) {\n        guestParam = rawGuestQuery.replace(/\\+/g, " ");\n    }\n} else {\n    const params = new URLSearchParams(window.location.search);\n    guestParam = params.get("guest") || "";\n}\n\nconst guest = (guestParam || "ضيفنا العزيز").trim() || "ضيفنا العزيز";\n'''

if old not in text:
    raise SystemExit('Guest query block not found')

text = text.replace(old, new, 1)
index.write_text(text, encoding='utf-8')

fallback = '''<!DOCTYPE html>\n<html lang="ar">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Teim & Judy Wedding</title>\n<style>html,body{margin:0;min-height:100%;background:#681017}body{display:grid;place-items:center;color:#fff8ed;font-family:serif}</style>\n</head>\n<body>\n<div>...</div>\n<script>\nfetch('/index.html', {cache:'no-store'})\n  .then(function(response){ return response.text(); })\n  .then(function(html){ document.open(); document.write(html); document.close(); })\n  .catch(function(){ document.body.innerHTML = '<div>تعذّر فتح الدعوة</div>'; });\n<\\/script>\n</body>\n</html>\n'''
Path('404.html').write_text(fallback, encoding='utf-8')
