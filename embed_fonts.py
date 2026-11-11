"""Opsional: tanam font ke dalam SVG supaya Montserrat & Plus Jakarta Sans tampil di semua perangkat.
Taruh file .woff2 (unduh dari fonts.google.com) di folder fonts/ lalu jalankan: python embed_fonts.py
Nama file: Montserrat-ExtraBold.woff2, Montserrat-Bold.woff2, PlusJakartaSans-ExtraBold.woff2,
PlusJakartaSans-SemiBold.woff2, PlusJakartaSans-Medium.woff2"""
import base64, glob, os

F = [
    ("Montserrat", 700, "Montserrat-Bold"),
    ("Montserrat", 800, "Montserrat-ExtraBold"),
    ("Plus Jakarta Sans", 500, "PlusJakartaSans-Medium"),
    ("Plus Jakarta Sans", 600, "PlusJakartaSans-SemiBold"),
    ("Plus Jakarta Sans", 800, "PlusJakartaSans-ExtraBold"),
]

css = ""
for fam, w, f in F:
    p = f"fonts/{f}.woff2"
    if os.path.exists(p):
        with open(p, "rb") as fp:
            b = base64.b64encode(fp.read()).decode()
        css += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"

for s in glob.glob("assets/*.svg"):
    with open(s, "r", encoding="utf-8") as fp:
        t = fp.read()
    if "/*FONTS*/" in t:
        t = t.replace("/*FONTS*/", css, 1)
    with open(s, "w", encoding="utf-8") as fp:
        fp.write(t)

print("selesai")

