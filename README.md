# VidVort

Upload videos, automate transcoding, and manage workflows with ease. Designed for scalability, it supports cloud/local storage.

## Roadmap

- [x] File upload to local storage
- [x] Trigger transcoding by filename and store transcoded video in local storage
- [ ] Upload validation to check if file is a video 
- [ ] Job status table - on upload return ID and trigger based on ID instead of file name
- [ ] API to list jobs with their status
- [ ] Video encoder - hardware acceleration based on system(OS, GPU available - macos, nvidia gpu etc)
- [ ] Containerization - Dockerfile and docker-compose
- [ ] Introduce support for presets based on video quality and resolution (eg. 1080p/720p/360p and 500kbps/800kbps)
- [ ] Event driven queue for transcoding jobs
- [ ] Support multiple transcodes in a single trigger
- [ ] Time estimations based on popular format/resolution conversions