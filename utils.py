from subprocess import Popen
from subprocess import PIPE

def get_container_ip():
    """Quick function to get the subprocess
    """
    # get the container id of the web application container
    result = Popen(["docker", "ps", "-aqf", "name=slide_classifier_web"], stdout=PIPE).communicate()
    container_id = clean_popen_results(result)

    # get the ip address of the web application container
    result = Popen(["docker", "inspect", "-f", "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}", container_id], stdout=PIPE).communicate()
    return clean_popen_results(result)

def clean_popen_results(result):
    """clean up the results from subprocess
    """
    output = result[0]
    decoded_output = output.decode('utf-8')
    clean_output = decoded_output.strip()
    return clean_output


if __name__ == "__main__":
    print('the web app is running at:', get_container_ip())
    
