docker service create \
--replicas 6 \
--publish published=7500,target=7500 \
--name web_app \
95.216.191.176:5000/kc_l5