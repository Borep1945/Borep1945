from pathlib import Path
import re
import xml.etree.ElementTree as ET
root = Path(__file__).resolve().parent
text = (root / 'README.md').read_text()
for name in re.findall(r'src="([^"]+)"', text):
    assert (root / name).is_file(), f'Missing profile asset {name}'
for path in (root / 'assets').glob('*.svg'):
    ET.parse(path)
    assert '<script' not in path.read_text().lower(), 'SVG scripts are unsupported'
for heading in ['Introduction','Tech stack','Featured projects','What I build','Open source','GitHub activity','Development philosophy','Contact']:
    assert f'## {heading}' in text, f'Missing {heading}'
print('Profile assets, SVGs and eight required sections verified')
