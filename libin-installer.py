try:
    import os
except ImportError:
    print("Module can't be imported:")
    print("    Error when importing module 'os'")

if os.geteuid() != 0:
    print("Error: Running with sudo is needed!")
    raise SystemExit(1)

os.system("clear")

print("Installer Wizard v2.1 | by 4a")
print()
print("=============================")
print("Installer Wizard:")
print("    name: libin (library bin) pack-unpack")
print("    vers: v1.0")
print("    lang: en-US")
print("    sudo: yes")
print("    publ: 23/4/2026")
print("============================")
print("Launch Installation?")
print("   y/Y = yes")
print("   n/N = yes")
print()
ghi = input("~> ")

if ghi == "y" or ghi == "Y":
    os.system("wget -P /usr/local/bin https://raw.githubusercontent.com/EshanGemuk5447/4a-repository/master/libin")
    os.system("chmod +x /usr/local/bin/libin")
    print("Installation Finished.")
elif ghi == "n" or ghi == "N":
    print("Installation cancelled")
    raise SystemExit(1)
else:
    print("Unknown alphabet! Quitting...")
    raise SystemExit(1)
