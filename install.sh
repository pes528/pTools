#!/bin/bash


system=$(uname -o)
hom=$($HOME)

android(){

    clear
    echo -e "PREPARANDO INSTALACION...."
    rm -rf pTools
    sleep 3
    apt update && apt upgrade -y
    apt install python -y
    apt install git -y
    sleep 2
    rm -rf Ptools
    pip install requests 
    pip install pytest
    pip install aiohttp

    git clone https://github.com/pes528/pTools
    clear 
    echo "INSTALACION CASI FINALIZADA."
    sleep 2
    echo -e -n "REALIZANDO PRUEBAS...."
    sleep 2
    python -m pytest > pTools/test.log 2>&1 

    i=${i:-0}
    while [ $i -ne 15 ];do
    log=$(grep -o "3 passed, 1 skipped, 1 warning" pTools/test.log)
    if [[ $log == "3 passed, 1 skipped, 1 warning" ]];then 
        echo "PASS"
        echo "INICIANDO..."
        sleep 3
        i=15
    else 

        echo -e -n "."
        ((i++))
        if [ $i -eq 15 ];then 
        echo "ERROR"

        grep -w "ERROR" pTools/test.log

        echo -e "\nNO SE PUEDE INICIAR EL PROGRAMA DEBIDO A UN ERROR INTERNO"
        fi  

    fi
    done
    if [ $i -eq 15 ];then 
        rm install.sh
	rm pTools/install.sh
        cd pTools
        python Ptools.py
    fi 

}
ubuntu(){
    clear
    echo -e "Esta herramienta esta hecha para dispositivos android\nPuedes hacer la instalacion copiando el repositorio de forma manual"
}

if [ $system == "Android" ];then
    android
elif [ $system == "GNU/Linux" ];then
    ubuntu

fi
