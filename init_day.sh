#!/bin/bash

# Navegar al directorio 'adv2024'
cd adv2024

# Encontrar el directorio con el número más alto 'dia?'
last_day=$(ls -d dia* | sed 's/dia//g' | sort -n | tail -1)


echo "El último día es $last_day"

# Extraer el número del nombre del directorio
last_day_number=${last_day#dia}

echo "El número del último día es $last_day_number"

# Sumar uno al número extraído
new_day_number=$((last_day_number + 1))

echo "El número del nuevo día es $new_day_number"

# Crear un nuevo directorio con el nombre 'dia' seguido del número obtenido
new_day="dia$new_day_number"

# Crear y cambiar a una nueva rama
git checkout -b feature/dia${new_day_number}

mkdir $new_day

cp ../template/README_DIAX_ES.md ../README_DIA${new_day_number}_ES.md
cp ../template/README_DIAX_EN.md ../README_DIA${new_day_number}_EN.md
cp ../template/diaX/diaX.py $new_day/dia${new_day_number}.py
cp ../template/diaX/dataX_1.txt $new_day/data${new_day_number}_1.txt
cp ../template/diaX/dataX_2.txt $new_day/data${new_day_number}_2.txt
cp ../template/diaX/testX_1.txt $new_day/test${new_day_number}_1.txt
cp ../template/diaX/testX_2.txt $new_day/test${new_day_number}_2.txt

# Navegar al nuevo directorio
cd $new_day

# Para cada archivo .py, reemplazar todas las ocurrencias de 'X' en el contenido del archivo por el número obtenido
for file in *.py; do
    # Crear un archivo temporal
    sed "s/X/${new_day_number}/g" "$file" > "${file}.tmp"
    # Mover el archivo temporal sobre el original
    mv "${file}.tmp" "$file"
done

cd ../..

# Modificar el fichero README.md
# sed -i "/## Español/a\\\n${new_day_number}. [Dia ${new_day_number}](./README_DIA${new_day_number}_ES.md)" README.md
# sed -i "/## English/a\\\n${new_day_number}. [Day ${new_day_number}](./README_DIA${new_day_number}_EN.md)" README.md

# Modificar el fichero README.md - Tengo dudas con este nuevo codigo
sed -i "/## Español/!b;n;:a;n;/^[0-9]\+. \[Dia [0-9]\+\](.\/README_DIA[0-9]\+_ES.md)/ba;i\\${new_day_number}. [Dia ${new_day_number}](./README_DIA${new_day_number}_ES.md)" README.md
sed -i "/## English/!b;n;:a;n;/^[0-9]\+. \[Day [0-9]\+\](.\/README_DIA[0-9]\+_EN.md)/ba;i\\${new_day_number}. [Day ${new_day_number}](./README_DIA${new_day_number}_EN.md)" README.md


# Añadir y commitear los cambios
git add .
git commit -m "Añadidos archivos y enlaces para el día ${new_day_number}"