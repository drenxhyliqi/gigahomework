#!/bin/bash
case "$1" in
  up)   docker compose up -d ;;
  down) docker compose down ;;
  seed) docker exec -i giga_mentees_db psql -U giga -d giga_mentees < sql/seed.sql ;;
  test) python -c "from queries import list_mentees; print(list_mentees())" ;;
esac
