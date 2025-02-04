#!/bin/bash

BACKUP_DIR="/mnt/d/work/sysss/Challenge2/backup_dir"
LOG_FILE="/mnt/d/work/sysss/Challenge2/backup_restore.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

log_message() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}

list_volumes() {
  docker volume ls --format "{{.Name}}"
}

backup_volumes() {
  log_message "Starting backup process..."
  mkdir -p "$BACKUP_DIR"
  
  for volume in $(list_volumes); do
    ARCHIVE="${BACKUP_DIR}/${volume}_${TIMESTAMP}.tar.gz"
    log_message "Backing up volume: $volume"
    docker run --rm -v "$volume":/data -v "$BACKUP_DIR":/backup busybox tar czf /backup/$(basename $ARCHIVE) -C /data .
    log_message "Backup created: $ARCHIVE"
  done

  log_message "Backup process completed."
}

restore_volumes() {
  BACKUP_FILE=$1
  VOLUME=$2

  if [ -z "$BACKUP_FILE" ] || [ -z "$VOLUME" ]; then
    log_message "Usage: $0 restore <backup_file> <volume_name>"
    exit 1
  fi

  log_message "Restoring volume: $VOLUME from $BACKUP_FILE"
  docker run --rm -v "$VOLUME":/data -v "$(dirname $BACKUP_FILE)":/backup busybox tar xzf /backup/$(basename $BACKUP_FILE) -C /data
  log_message "Restore completed for volume: $VOLUME"
}

case "$1" in
  backup)
    backup_volumes
    ;;
  restore)
    restore_volumes "$2" "$3"
    ;;
  *)
    log_message "Usage: $0 {backup|restore <backup_file> <volume_name>}"
    exit 1
    ;;
esac
