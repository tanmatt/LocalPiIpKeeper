import socket
import time

README = "README.md"
README_TEMPLATE = "README_TEMPLATE.md"
LOCAL_IP_ADDRESS = "{LOCAL_IP_ADDRESS}"
HOST_NAME = "{HOST_NAME}"
LOG_LINE = "{LOG_LINE}"


def _get_local_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def _get_host_name():
    return socket.gethostname()


def _update_readme():
    log = time.asctime(time.localtime()) + " | "

    # load the template
    f = open(README_TEMPLATE, "r")
    content = f.read()
    f.close()

    # replace the placeholders
    try:
        content = content.replace(LOCAL_IP_ADDRESS, _get_local_ip_address())
        content = content.replace(HOST_NAME, _get_host_name())
        content = content.replace(LOG_LINE, log + "Success")
    except Exception as ex:
        content = content.replace(LOG_LINE, log + "Failure | " + ex.__str__())
    finally:
        f = open(README, "w")
        f.write(content)
        f.write("\n")
        f.close()


if __name__ == "__main__":
    _update_readme()
