# Build static files
build-static:
    npm run build

# Build the project
build: build-static docs
    uv build

# Clean build artifacts
clean:
    rm -rf dist/ build/ *.egg-info
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

# Deploy to PyPI
pypi: clean build
    uv publish

# Install development dependencies
install:
    uv sync --all-groups

# Format code
fmt:
    uvx ruff format .

# Lint code
lint:
    uvx ruff check .

docs:
    uv run marimo export html-wasm --mode edit -o docs --force example.py

serve port="8000": 
    python3 -m webbrowser -t "http://0.0.0.0:{{port}}"
    uv run python -m http.server --directory docs {{port}}