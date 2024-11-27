import subprocess


subprocess.run(['flyway', 'migrate', '-url',
               '-user', '-password'])
