from pathlib import Path

repo_root = Path(__file__).resolve().parent
root = repo_root / 'client'

# local_auth 3.x: AuthenticationOptions was replaced by flat parameters.
p = root / 'lib/core/services/auth_service.dart'
s = p.read_text(encoding='utf-8')
s = s.replace(
    "options: const AuthenticationOptions(biometricOnly: true, stickyAuth: true),",
    "biometricOnly: !Platform.isWindows,\n        persistAcrossBackgrounding: true,",
)
p.write_text(s, encoding='utf-8')

# file_picker 11.x: API moved from FilePicker.platform to static methods.
for rel in [
    'lib/core/services/backup_service.dart',
    'lib/core/services/image_service.dart',
    'lib/features/backups/backups_page.dart',
]:
    p = root / rel
    s = p.read_text(encoding='utf-8')
    s = s.replace('FilePicker.platform.getDirectoryPath', 'FilePicker.getDirectoryPath')
    s = s.replace('FilePicker.platform.pickFiles', 'FilePicker.pickFiles')
    p.write_text(s, encoding='utf-8')

# flutter create adds a sample widget test that targets MyApp, which this app does not use.
sample_test = root / 'test/widget_test.dart'
if sample_test.exists():
    sample_test.unlink()
