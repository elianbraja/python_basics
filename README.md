1. Gjithmone pare se te besh run applikacionin ekzekuto:
. venv/bin/activate

2. Starto serverin:
flask --app hello_app run --host=0.0.0.0 --port=3000

3. Kujdes! Nese ndryshon path e projektit do te ndryshojne dhe te dhenat qe jane tek folderi venv pasi perndryshe nuk gjen dot paketat e instaluara tek ai venv. Duhen ndryshuar dhe aty.

Per te bere deploy ne fly.io:
fly deploy

Per te bere launch deployment nga e para:
fly launch
