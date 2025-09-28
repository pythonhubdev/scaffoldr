#!/bin/bash

# Scaffoldr CLI Testing Script

set -e

TEST_DIR="/tmp/scaffoldr-tests"
cd /Users/vetrichelvan/Documents/OSS/scaffoldr

echo "🧪 Starting Scaffoldr CLI Testing..."

# Function to test a configuration
test_config() {
    local config_name="$1"
    local project_name="$2"
    local framework="$3"
    local destination="$4"
    local python_version="$5"
    local email="$6"
    local name="$7"
    local description="$8"
    local docker="$9"
    local use_cloud="${10}"
    local use_database="${11}"

    echo "Testing: $config_name"

    # Clean up any existing project
    rm -rf "$destination/$project_name"

    # Build the command
    cmd="uv run scaffoldr --no-banner generate --project-name \"$project_name\" --framework \"$framework\" --destination \"$destination\" --python-version \"$python_version\" --email \"$email\" --name \"$name\" --description \"$description\""

    if [ "$docker" = "true" ]; then
        cmd="$cmd --docker"
    else
        cmd="$cmd --no-docker"
    fi

    if [ "$use_cloud" = "true" ]; then
        cmd="$cmd --use-cloud --cloud-type aws"
    else
        cmd="$cmd --no-cloud"
    fi

    if [ "$use_database" = "true" ]; then
        cmd="$cmd --use-database"
    else
        cmd="$cmd --no-database"
    fi

    echo "Command: $cmd"

    # Run the command
    if eval "$cmd"; then
        echo "✅ Generation successful"

        # Check if project directory exists
        if [ -d "$destination/$project_name" ]; then
            echo "✅ Project directory created"

            # Try to run tests
            cd "$destination/$project_name"
            if [ -f "pyproject.toml" ]; then
                echo "✅ pyproject.toml exists"

                # Try to install dependencies and run tests
                if uv sync --quiet 2>/dev/null; then
                    echo "✅ Dependencies installed"

                    # Run tests
                    if uv run pytest tests/ -v --tb=short 2>/dev/null; then
                        echo "✅ Tests passed"
                    else
                        echo "❌ Tests failed"
                    fi
                else
                    echo "❌ Failed to install dependencies"
                fi
            else
                echo "❌ pyproject.toml missing"
            fi

            cd - >/dev/null
        else
            echo "❌ Project directory not created"
        fi
    else
        echo "❌ Generation failed"
    fi

    echo "---"
}

# Test configurations
echo "Testing basic FastAPI configuration..."
test_config "fastapi-basic" "test-fastapi-basic" "fastapi" "$TEST_DIR" "3.13" "test@example.com" "Test User" "Test project" "true" "true" "true"

echo "Testing FastAPI without Docker..."
test_config "fastapi-no-docker" "test-fastapi-no-docker" "fastapi" "$TEST_DIR" "3.13" "test@example.com" "Test User" "Test project" "false" "true" "true"

echo "Testing FastAPI without cloud..."
test_config "fastapi-no-cloud" "test-fastapi-no-cloud" "fastapi" "$TEST_DIR" "3.13" "test@example.com" "Test User" "Test project" "true" "false" "true"

echo "Testing FastAPI without database..."
test_config "fastapi-no-db" "test-fastapi-no-db" "fastapi" "$TEST_DIR" "3.13" "test@example.com" "Test User" "Test project" "true" "true" "false"

echo "Testing FastAPI minimal..."
test_config "fastapi-minimal" "test-fastapi-minimal" "fastapi" "$TEST_DIR" "3.13" "test@example.com" "Test User" "Test project" "false" "false" "false"

echo "Testing Python 3.12..."
test_config "fastapi-py312" "test-fastapi-py312" "fastapi" "$TEST_DIR" "3.12" "test@example.com" "Test User" "Test project" "true" "true" "true"

echo "Testing different destination..."
test_config "fastapi-custom-dest" "test-fastapi-dest" "fastapi" "/tmp" "3.13" "test@example.com" "Test User" "Test project" "true" "true" "true"

echo "🧪 Testing complete!"
