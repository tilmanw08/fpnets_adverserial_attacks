docker run -it \
    --gpus all \
    --name dl \
    --rm -v $(pwd):/workingdir -v /nfshome/wegener/Documents/data:/data \
    --user $(id -u):$(id -g) \
    --env="DISPLAY" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --shm-size=16g \
    dl_workingdir_fp_nets bash 