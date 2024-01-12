# Sistema de Renta de Automóviles

## Descripción del Proyecto

Este es un proyecto de vacaciones realizado en Django para practicar el uso de este framework web. El proyecto consiste en un sistema de renta de automóviles, en el cual se pueden registrar usuarios, administradores, automóviles, rentas y devoluciones. Los usuarios pueden rentar automóviles y los administradores pueden administrar los automóviles, las rentas y las devoluciones.

## Requisitos Previos

- Python (versión 3.11.X o mayor) 🐍
- Pip (versión 22.3.X o mayor) 📦
- Git (versión 2.40.X o mayor) 🗄️

## Configuración del Entorno de Desarrollo

1. Clona el repositorio: 📥

```shell
git clone https://github.com/Alejandro347/sistemaCatalogo.git
```

2. Crea y activa un entorno virtual: ⚙️

```shell
python -m venv venv
```

- En Windows:
  ```shell
  .\venv\Scripts\activate
  ```

- En macOS/Linux:
  ```shell
  source venv/bin/activate
  ```

3. Instala las dependencias del proyecto: ⚡

```shell
pip install -r requirements.txt
```

## Puesta en Marcha del Proyecto

1. Realiza las migraciones de la base de datos: 🗃️

```shell
python manage.py migrate
```

2. Inicia el servidor de desarrollo: 🚀

```shell
python manage.py runserver
```

3. Accede a la aplicación en tu navegador web: 🌐 http://localhost:8000

## Contribución

Si deseas contribuir al proyecto, sigue los siguientes pasos: 🤝

1. Crea una rama nueva desde la rama `dev`: 🌿

```shell
git checkout dev
git pull
git checkout -b feature/nombre_de_la_rama
```

2. Realiza los cambios y realiza commits con mensajes descriptivos: ✏️

```shell
git add .
git commit -m "Mensaje descriptivo"
```

3. Sincroniza tu rama con la rama `dev`: 🔄

```shell
git checkout dev
git pull
git merge nombre_de_la_rama
```

4. Soluciona cualquier conflicto de fusión (si los hay). 🛠️
5. Realiza un push de tus cambios a la rama remota: 📤

```shell
git push origin dev
```

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
