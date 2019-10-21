# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/lawrencenyakiso/Dev/QT/SonoffToolMac/src/main/python/main.py'],
             pathex=['/Users/lawrencenyakiso/Dev/QT/SonoffToolMac/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/lawrencenyakiso/anaconda3/envs/qtenv/lib/python3.7/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/lawrencenyakiso/Dev/QT/SonoffToolMac/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SonoffToolMac',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/lawrencenyakiso/Dev/QT/SonoffToolMac/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='SonoffToolMac')
app = BUNDLE(coll,
             name='SonoffToolMac.app',
             icon='/Users/lawrencenyakiso/Dev/QT/SonoffToolMac/target/Icon.icns',
             bundle_identifier='com.lawrencenyakiso.sonofftoolmac')
