#!/bin/bash
# Convenience script to start all infrastructure services

echo "Starting MentorAI infrastructure services..."
echo "- Postgres database"
echo "- Chroma vector database"

docker-compose up -d

echo ""
echo "Services started! Check status with:"
echo "  docker-compose ps"
echo ""
echo "To stop services:"
echo "  docker-compose down"