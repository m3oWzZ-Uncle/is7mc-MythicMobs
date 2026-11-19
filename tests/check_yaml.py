#!/usr/bin/env python3
"""Simple YAML syntax checker, NOT MythicMobs schema/gameplay validator."""
import pathlib, sys
try:
    import yaml
except ImportError:
    print("Thiếu PyYAML. Cài: python3 -m pip install pyyaml")
    sys.exit(2)
if len(sys.argv)<2:
    print("Dùng: python3 tests/check_yaml.py <thu_muc_hoac_file>")
    sys.exit(2)
p=pathlib.Path(sys.argv[1])
files=[p] if p.is_file() else sorted([*p.rglob('*.yml'),*p.rglob('*.yaml')])
if not files: print('Không tìm thấy YAML'); sys.exit(2)
failed=0
for f in files:
    try:
        with f.open(encoding='utf-8-sig') as h:
            list(yaml.safe_load_all(h))
        print('OK',f)
    except Exception as ex:
        failed+=1
        print('LỖI',f,ex)
print(f'Đã kiểm tra {len(files)} file, lỗi {failed}. Chưa kiểm tra tính hợp lệ MythicMobs hoặc gameplay.')
sys.exit(1 if failed else 0)
