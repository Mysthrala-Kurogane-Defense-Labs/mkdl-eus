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
