from pathlib import Path
import subprocess
root = Path(__file__).resolve().parents[1]
for name in subprocess.check_output(['git', 'ls-files'], cwd=root, text=True).splitlines():
    p = root / name
    if p.exists() and (p.suffix in {'.html', '.md', '.txt', '.xml', '.py'} or name == '.gitignore'):
        p.write_bytes(p.read_bytes().replace(b'\r\n', b'\n'))
p = root / 'index.html'
s = p.read_text(encoding='utf-8').replace('hreflang="es" href="https://mkdl.eus/"', 'hreflang="es" href="https://mkdl.jp/"').replace('href="https://mkdl.eus/" lang="es"', 'href="https://mkdl.jp/" lang="es"')
p.write_text(s, encoding='utf-8', newline='\n')
from html.parser import HTMLParser
class PublicText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.body = False
    def handle_starttag(self, tag, attrs):
        if tag == 'body': self.body = True
    def handle_data(self, data):
        if self.body and data.strip(): self.parts.append(data.strip())
page = PublicText(); page.feed(s)
(root / 'index.md').write_text('# MKDL — OT Check\n\nhttps://mkdl.eus/\n\n' + '\n\n'.join(page.parts) + '\n', encoding='utf-8', newline='\n')
