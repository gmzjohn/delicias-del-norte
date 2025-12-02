# Delicias del Norte

## Project description

Delicias del Norte is a centralized platform designed to digitize and automate the core business logic of a restaurant. It acts as the operational backbone of the establishment, bridging the gap between customer orders and kitchen execution.

## Project scope

The project encompasses a comprehensive kitchen simulation system where customers place orders that are managed via a processing queue.

## Project Stack

- **Language**: Python 3
- **Containerization**: Podman

## Project Setup

To set up and run the project locally:

**Clone the repository**:

```bash
git clone https://github.com/gmzjohn/delicias-del-norte.git
cd delicias-del-norte
```

## Containerization (Podman)

### 1. Build the image
```bash
podman build -t delicias-del-norte:{VERSION} .
```

### 2. Run the container (Development Mode)

```bash
podman run -it --rm -p 8080:8080 -v .:/app:Z --userns=keep-id delicias-del-norte:{VERSION} /bin/sh
```

Once inside, you can run your Python scripts:
```bash
python main.py
```

