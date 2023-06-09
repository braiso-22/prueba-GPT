# prueba-GPT

Este proyecto es una implementación simple en Python para hablar con GPT-3, un modelo de lenguaje avanzado
de OpenAI, utilizando su API.

## Instalación

### Clonación del repositorio

Para instalar el proyecto, simplemente clonar el repositorio y ejecutar el siguiente comando:

```bash
git clone https://github.com/braiso-22/prueba-GPT.git
cd hands-position-classifier
```

### Instalacion de dependencias

```bash
conda env create -f environment.yaml prueba-GPT
```

### Activar el entorno

```bash
conda activate prueba-GPT
```

### Configurar la API

Para poder utilizar la API de GPT-3, es necesario tener una cuenta en [OpenAI](https://openai.com/).
Una vez creada la cuenta, se debe obtener el token de acceso.

Con el token de acceso, se debe crear un archivo llamado `.env` en la raíz del proyecto, con el siguiente comando:

```bash
echo "OPENAI_API_KEY=TU_TOKEN_DE_ACCESO" > .env
```

## Uso

### Ejecutar el programa

```bash
python main.py
```

El programa se ejecutará y mostrará un menú con las opciones disponibles.

* **1.** Ingresar texto para generar una respuesta rápida.
* **2.** Iniciar un chat con GPT-3 pudiendo pasarle una configuración inicial.
* **3.** Salir del programa.