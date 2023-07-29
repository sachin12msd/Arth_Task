import os

def clear_screen():
    os.system('clear')

def welcome_message():
    print("\033[95mWelcome to Linux Command Menu\033[0m")
    print("\033[95m----------------------------\033[0m")
    print("\033[92mSelect your choice:\033[91m")
    print("\033[92m---------------------\033[91m")
    print("\033[94m 1. \033[93mBasic Linux Commands\033[91m")
    print("\033[94m 2. \033[93mManage YUM Packages\033[91m")
    print("\033[94m 3. \033[93mWork with Docker\033[91m")
    print("\033[94m 4. \033[93mExit\033[91m")
    print("\033[0m")

def basic_linux_commands():
    while True:
        clear_screen()
        print("\033[95m-----------------------------------------\033[0m")
        print("\033[95m Welcome to Basic Linux Commands\033[0m")
        print("\033[95m-----------------------------------------\033[0m")
        print("\033[92mSelect your choice:\033[91m")
        print("\033[92m---------------------\033[91m")
        print("\033[94m 1. \033[93mCheck current directory\033[91m")
        print("\033[94m 2. \033[93mList files in current directory\033[91m")
        print("\033[94m 3. \033[93mCreate a new directory\033[91m")
        print("\033[94m 4. \033[93mChange directory\033[91m")
        print("\033[94m 5. \033[93mShow system information\033[91m")
        print("\033[94m 6. \033[93mShow disk space usage\033[91m")
        print("\033[94m 7. \033[93mList running processes\033[91m")
        print("\033[94m 8. \033[93mKill a process\033[91m")
        print("\033[94m 9. \033[93mShow date and time\033[91m")
        print("\033[94m10. \033[93mGo back to main menu\033[91m")
        print("\033[0m")

        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == "1":
            os.system("pwd")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "2":
            os.system("ls")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "3":
            new_dir = input("\033[92mEnter the name of the new directory: \033[0m")
            os.system(f"mkdir {new_dir}")
            print(f"\033[92mDirectory '{new_dir}' created successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "4":
            target_dir = input("\033[92mEnter the path of the target directory: \033[0m")
            os.chdir(target_dir)
            print(f"\033[92mChanged directory to '{target_dir}'\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "5":
            os.system("uname -a")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "6":
            os.system("df -h")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "7":
            os.system("ps aux")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "8":
            process_id = input("\033[92mEnter the process ID to kill: \033[0m")
            os.system(f"kill {process_id}")
            print(f"\033[92mProcess with ID {process_id} killed successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "9":
            os.system("date")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "10":
            break
        else:
            print("\033[91mInvalid Option\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")

def manage_yum_packages():
    while True:
        clear_screen()
        print("\033[95m--------------------------------------\033[0m")
        print("\033[95m Welcome to YUM Package Management\033[0m")
        print("\033[95m--------------------------------------\033[0m")
        print("\033[92mSelect your choice:\033[91m")
        print("\033[92m---------------------\033[91m")
        print("\033[94m 1. \033[93mConfigure YUM Repository\033[91m")
        print("\033[94m 2. \033[93mInstall Package\033[91m")
        print("\033[94m 3. \033[93mRemove Package\033[91m")
        print("\033[94m 4. \033[93mCheck Available Packages\033[91m")
        print("\033[94m 5. \033[93mExit\033[91m")
        print("\033[0m")

        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == "1":
            repo_name = input("\033[92mEnter the name of the repository: \033[0m")
            base_url = input("\033[92mEnter the base URL of the repository: \033[0m")
            gpg_check = input("\033[92mEnable GPG check? (y/n): \033[0m")
            gpg_check = "1" if gpg_check.lower() == "y" else "0"
            repo_config = f"[{repo_name}]\nbaseurl={base_url}\ngpgcheck={gpg_check}\n"
            with open("/etc/yum.repos.d/custom.repo", "w") as f:
                f.write(repo_config)
            print("\033[92mYUM repository configured successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "2":
            package_name = input("\033[92mEnter the name of the package to install: \033[0m")
            os.system(f"yum install {package_name} -y")
            print(f"\033[92mPackage '{package_name}' installed successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "3":
            package_name = input("\033[92mEnter the name of the package to remove: \033[0m")
            os.system(f"yum remove {package_name} -y")
            print(f"\033[92mPackage '{package_name}' removed successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "4":
            os.system("yum list all")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "5":
            break
        else:
            print("\033[91mInvalid Option\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")

def work_with_docker():
    while True:
        clear_screen()
        print("\033[95m----------------------------------\033[0m")
        print("\033[95m Welcome to Docker Commands\033[0m")
        print("\033[95m----------------------------------\033[0m")
        print("\033[92mSelect your choice:\033[91m")
        print("\033[92m---------------------\033[91m")
        print("\033[94m 1. \033[93mConfigure Docker Repository\033[91m")
        print("\033[94m 2. \033[93mInstall Docker\033[91m")
        print("\033[94m 3. \033[93mCheck Docker Status\033[91m")
        print("\033[94m 4. \033[93mCheck Docker Images\033[91m")
        print("\033[94m 5. \033[93mDownload Docker Image\033[91m")
        print("\033[94m 6. \033[93mList Running Containers\033[91m")
        print("\033[94m 7. \033[93mDelete Docker Image\033[91m")
        print("\033[94m 8. \033[93mCreate a Container\033[91m")
        print("\033[94m 9. \033[93mCheck All Created Containers\033[91m")
        print("\033[94m10. \033[93mDelete All Created Containers\033[91m")
        print("\033[94m11. \033[93mStart Docker Container Network Connectivity\033[91m")
        print("\033[94m12. \033[93mCreate and Configure Web Server\033[91m")
        print("\033[94m13. \033[93mDelete a Container\033[91m")
        print("\033[94m14. \033[93mExit\033[91m")
        print("\033[0m")

        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == "1":
            with open("/etc/yum.repos.d/docker.repo", "w") as f:
                f.write("[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0\n")
            print("\033[92mDocker repository configured successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "2":
            print("\033[92mPlease wait while installing Docker...\033[0m")
            os.system("yum install docker-ce --nobest -y")
            os.system("systemctl start docker")
            print("\033[92mDocker installed and started successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "3":
            print("\033[92mPlease wait while checking Docker status...\033[0m")
            os.system("systemctl status docker")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "4":
            print("\033[92mPlease wait while listing Docker images...\033[0m")
            os.system("docker images")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "5":
            docker_image = input("\033[92mEnter the name of Docker image to pull (Default: latest): \033[0m")
            if not docker_image:
                docker_image = "latest"
            print("\033[92mPlease wait while pulling Docker image...\033[0m")
            os.system(f"docker pull {docker_image}")
            print(f"\033[92mDocker image '{docker_image}' pulled successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "6":
            print("\033[92mPlease wait while listing running containers...\033[0m")
            os.system("docker ps")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "7":
            image_name = input("\033[92mEnter the name of Docker image to delete (with version): \033[0m")
            os.system(f"docker rmi {image_name}")
            print(f"\033[92mDocker image '{image_name}' deleted successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "8":
            os_name = input("\033[92mEnter the name for the new container: \033[0m")
            image_name = input("\033[92mEnter the name of Docker image (with version): \033[0m")
            os.system(f"docker run -dit --name {os_name} {image_name}")
            print(f"\033[92mContainer '{os_name}' created and started successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "9":
            print("\033[92mPlease wait while listing all containers...\033[0m")
            os.system("docker ps -a")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "10":
            os.system("docker rm -f $(docker ps -a -q)")
            print("\033[92mAll created containers deleted successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "11":
            print("\033[92mPlease wait while configuring Docker container network connectivity...\033[0m")
            os.system("firewall-cmd --zone=public --add-masquerade --permanent")
            os.system("firewall-cmd --zone=public --add-port=80/tcp")
            os.system("firewall-cmd --zone=public --add-port=443/tcp")
            os.system("firewall-cmd --reload")
            print("\033[92mDocker container network connectivity configured successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "12":
            print("\033[92mPlease wait while creating and configuring the web server...\033[0m")
            os.system("docker run -dit -p 1234:80 --name myos centos:7")
            os.system("docker exec -it myos yum install httpd -y")
            os.system("docker exec -it myos /usr/sbin/httpd")
            os.system("docker exec -it myos ./usr/sbin/httpd")
            print("\033[92mWeb server container created and configured successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "13":
            print("\033[92mPlease wait while deleting a Docker container...\033[0m")
            os.system("docker ps -a")
            container_name = input("\033[92mEnter the container name or the first 4 characters of the ID: \033[0m")
            os.system(f"docker rm -f {container_name}")
            print(f"\033[92mContainer '{container_name}' deleted successfully!\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")
        elif choice == "14":
            break
        else:
            print("\033[91mInvalid Option\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")


def main():
    while True:
        clear_screen()
        welcome_message()
        choice = input("\033[92mEnter your choice: \033[0m")

        if choice == "1":
            basic_linux_commands()
        elif choice == "2":
            manage_yum_packages()
        elif choice == "3":
            work_with_docker()
        elif choice == "4":
            print("\033[95mGoodbye!\033[0m")
            input("\033[92mPress Enter to exit...\033[0m")
            clear_screen()
            break
        else:
            print("\033[91mInvalid Option\033[0m")
            input("\033[92mPress Enter to continue...\033[0m")

if __name__ == "__main__":
    main()
