import subprocess

def configure_apache():
    # Créer un fichier de configuration Apache
    subprocess.run(["echo", "'<Configuration Apache>'", "|", "sudo", "tee", "/etc/apache2/sites-available/000-default.conf" ])

def restart_apache():
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

if __name__ == "__main__":
    configure_apache()
    restart_apache()