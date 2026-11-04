"""Build the original V22 multipage site and check its deployment resources."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import runpy
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
runpy.run_path(str(ROOT / 'generate_site.py'), run_name='__main__')
pages = sorted(ROOT.glob('*.html')) + sorted((ROOT / 'projects').glob('*.html'))
assert len(pages) == 15, f'Expected 15 pages, got {len(pages)}'
assert len(list((ROOT / 'assets/portfolio').glob('*-page-*.webp'))) == 30
assert len(list((ROOT / 'assets/portfolio').glob('*.webp'))) == 52

errors = []
def check_url(value, relative_to):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc or not parts.path:
        return
    if parts.path.startswith('/'):
        errors.append(f'{relative_to.name}: root-relative URL {value} breaks project hosting')
        return
    target = (relative_to.parent / unquote(parts.path)).resolve()
    if not target.is_relative_to(ROOT) or not target.exists():
        errors.append(f'{relative_to.name}: missing or invalid {value}')

class Resources(HTMLParser):
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for name in ('href', 'src', 'data-full'):
            if values.get(name):
                check_url(values[name], self.path)
        if tag == 'meta' and values.get('name') == 'lm-audio-source':
            check_url(values['content'], self.path)

for page in pages:
    parser = Resources()
    parser.path = page
    parser.feed(page.read_text(encoding='utf-8'))
css_path = ROOT / 'assets/styles.css'
for url in re.findall(r'url\(\s*[\"\']?([^\)\"\']+)', css_path.read_text(encoding='utf-8')):
    check_url(url, css_path)

manifest = json.loads((ROOT / 'scripts/asset-integrity.json').read_text(encoding='utf-8'))
for name, expected in manifest.items():
    data = (ROOT / name).read_bytes()
    if name == 'assets/i18n.js':
        data = data.replace(b'\r\n', b'\n')
        (ROOT / name).write_bytes(data)
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected:
        errors.append(f'Asset differs from V22: {name}')
if errors:
    raise SystemExit('\n'.join(errors))

output = ROOT / '_site'
output.mkdir(exist_ok=True)
for page in pages:
    target = output / page.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(page, target)
shutil.copytree(ROOT / 'assets', output / 'assets', dirs_exist_ok=True)
(output / '.nojekyll').write_text('', encoding='utf-8')
print(f'Validated {len(pages)} pages, 52 WebP images, 30 full-resolution pages, and {len(manifest)} unchanged V22 assets.')
