import os

if os.geteuid() != 0:
    print("Error: Running with sudo is needed!")
    raise SystemExit(1)

os.system("clear")

print("Installer Wizard v2.1 | by 4a")
print()
print("=============================")
print("Installer Wizard:")
print("    name: tinyjens")
print("    vers: v1.0")
print("    lang: en-US")
print("    sudo: yes")
print("    publ: 23/4/2026")
print("=============================")
print("Launch Installation?")
print("    y/Y = yes")
print("    n/N = no")
print()
abc = input("~> ")

if abc == "y" or abc == "Y":
    os.system("mkdir -p /install_path")
    os.system("wget -P /install_path https://raw.githubusercontent.com/EshanGemuk5447/4a-repository/master/tinyjens-4a.libin")
    print("Installation finished")
    print("Installed on: /install_path")
elif abc == "n" or abc == "N":
    print("Installation Cancelled")
    raise SystemExit(1)
else:
    print("unknown alphabet! count as Cancelling. Quitting...")
    raise SystemExit(1)
