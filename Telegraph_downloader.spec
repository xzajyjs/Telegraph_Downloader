# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['/Users/xzajyjs/Library/Mobile Documents/com~apple~CloudDocs/xzajyjs/Code/Python/Project/Telegraph_Downloader/Telegraph_downloader.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='Telegraph_downloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='/Users/xzajyjs/Library/Mobile Documents/com~apple~CloudDocs/xzajyjs/Code/Python/Project/Telegraph_Downloader/images.png')
app = BUNDLE(exe,
             name='Telegraph_downloader.app',
             icon='/Users/xzajyjs/Library/Mobile Documents/com~apple~CloudDocs/xzajyjs/Code/Python/Project/Telegraph_Downloader/images.png',
             bundle_identifier=None)
