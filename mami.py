import subprocess
import os

def clear_console():
    """
    Limpia la consola de forma multiplataforma.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def list_installed_packages():
    """
    Lista apps de usuario numeradas y devuelve la lista.
    """
    result = subprocess.run(
        ["adb", "shell", "pm", "list", "packages", "-3"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("Error running adb:", result.stderr)
        return []

    packages = result.stdout.strip().split("\n")
    packages = [pkg.replace("package:", "") for pkg in packages]

    print(f"\n📱 Installed user apps ({len(packages)}):")
    for idx, pkg in enumerate(packages, start=1):
        print(f"  {idx}) {pkg}")

    return packages

def pull_app_data(package_name):
    """
    Ejecuta adb pull para la carpeta data/data/<package_name>
    """
    dest_folder = f"./{package_name}_data"
    print(f"\n📂 Downloading app data from '{package_name}' in '{dest_folder}'...")
    result = subprocess.run(
        ["adb", "pull", f"/data/data/{package_name}", dest_folder],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode == 0:
        print(f"✅ Folder successfully downloaded in '{dest_folder}'.")
    else:
        print("❌ Error downloading folder:", result.stderr)

def uninstall_app(package_name):
    """
    Desinstala la aplicación con adb uninstall <package_name>
    """
    print(f"\n🗑️ Uninstalling the app '{package_name}'...")
    result = subprocess.run(
        ["adb", "uninstall", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if "Success" in result.stdout:
        print(f"✅ Application ‘{package_name}’ successfully uninstalled.")
    else:
        print(f"❌ Error while uninstalling ‘{package_name}’: {result.stdout.strip() or result.stderr.strip()}")

def app_actions(packages):
    """
    Menú para elegir acción sobre la lista.
    """
    while True:
        print("Select an option:")
        print(" 1) Download folder /data/data/{Application number}/")
        print(" 2) Uninstall application")
        print(" 3) Return to main menu")
        action = input("Select an option: ")

        if action == "1":
            app_num = input("Choose the application number: ")
            if not app_num.isdigit() or int(app_num) < 1 or int(app_num) > len(packages):
                print("❌ Invalid number.")
                continue

            clear_console()
            pkg_name = packages[int(app_num) - 1]
            pull_app_data(pkg_name)
            input("\nPress Enter to return to the main menu...")
            break  # Después de pull, vuelve al menú principal

        elif action == "3":
            break  # Vuelve al menú principal

        elif action == "2":
            app_num = input("Choose the number of the application to uninstall: ")
            if not app_num.isdigit() or int(app_num) < 1 or int(app_num) > len(packages):
                print("❌ Invalid number.")
                continue

            clear_console()
            pkg_name = packages[int(app_num) - 1]
            uninstall_app(pkg_name)
            input("\nPress Enter to return to the main menu...")
            break  # Después de desinstalar, vuelve al menú principal

        else:
            print("❌ Invalid option. Please try again.")

def main():
    """
    Menú interactivo principal.
    """
    while True:
        clear_console()
        print("===== MAIN MENU =====")
        print("1) List installed applications")
        print("0) Exit")

        choice = input("Select an option: ")

        if choice == "1":
            clear_console()
            packages = list_installed_packages()
            if packages:
                app_actions(packages)
        elif choice == "0":
            print("👋 Bye...")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_console()
        print("\n👋 Bye...")

