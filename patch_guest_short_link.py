from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = '''const params =\nnew URLSearchParams(window.location.search);\n\nconst guestParam = params.get("guest");\nconst guest = (guestParam || "ضيفنا العزيز").trim() || "ضيفنا العزيز";\n'''
new = '''const rawGuestQuery = window.location.search.slice(1);\nlet guestParam = "";\n\nif (rawGuestQuery && !rawGuestQuery.includes("=")) {\n    try {\n        guestParam = decodeURIComponent(rawGuestQuery.replace(/\\+/g, " "));\n    } catch (error) {\n        guestParam = rawGuestQuery.replace(/\\+/g, " ");\n    }\n} else {\n    const params = new URLSearchParams(window.location.search);\n    guestParam = params.get("guest") || "";\n}\n\nconst guest = (guestParam || "ضيفنا العزيز").trim() || "ضيفنا العزيز";\n'''
if old not in text:
    raise SystemExit('Guest query block not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
