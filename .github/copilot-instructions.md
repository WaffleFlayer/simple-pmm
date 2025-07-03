<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# PMM Project Instructions

This is a Simple Plex Media Manager (PMM) project designed to run on Windows Surface with Docker support.

## Project Context
- **Target Platform**: Windows Surface
- **Container Runtime**: Docker (already installed)
- **Primary Language**: Python 3.11+
- **Architecture**: Lightweight, container-ready media management

## Key Components
- `pmm.py`: Main application with Plex API integration
- `config/pmm_config.yml`: Configuration file for library and maintenance settings  
- `Dockerfile` & `docker-compose.yml`: Container deployment files
- `setup.py`: Initial setup and dependency installation script

## Development Guidelines
- Follow Python best practices and PEP 8 styling
- Use type hints where appropriate for better code clarity
- Maintain compatibility with Plex API and Docker environment
- Keep logging comprehensive for debugging on headless systems
- Ensure all file paths work correctly on Windows

## Dependencies
- PlexAPI for Plex server communication
- Docker SDK for container management
- PyYAML for configuration management
- Schedule for automated maintenance tasks

## Common Tasks
- Adding new media management features should extend the SimplePMM class
- Configuration changes should be made in `config/pmm_config.yml`
- Docker-related changes require updating both Dockerfile and docker-compose.yml
- Always test changes work both in direct Python execution and containerized environments
