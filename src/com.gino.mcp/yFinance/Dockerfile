# First stage: build with uv
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS build

WORKDIR /app

# Copy project metadata first (to cache deps install)
COPY pyproject.toml ./

# Install dependencies (without editable mode)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --system .

# Copy source code
COPY . .

# Second stage: runtime image (still with uv)
FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Copy installed packages and code from build stage
COPY --from=build /usr/local /usr/local
COPY --from=build /app /app

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

EXPOSE 8080

# Run MCP server
CMD ["uv", "run", "main.py"]
