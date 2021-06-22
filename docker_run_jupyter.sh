docker run \
    --gpus all \
    --name fp_nets_container_jupyter \
    --shm-size=1g \
    --rm -p 8888:8888 -v $(pwd):/workingdir -v /nfshome/wegener/Documents/data:/data dl_workingdir_fp_nets jupyter lab . \
    --ip=0.0.0.0 \
    --no-browser \
    --allow-root
