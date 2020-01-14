# Elastalert

Forked from upstream (see original README). This installs a docker container on the ELK host to generate alerts to the #alerting and #print-monitoring slack channels.

## Install

Process to be confirmed. Checkout this repo directly on the ELK box, or copy the contents onto it (yuk, yes!). Build and run the docker container.

## Usage

The `rules/` directory contains all the rules we currently use. This includes a hardcoded slack hook from "BB Webhooks" (https://api.slack.com/apps/AGRT37UDQ) which will need updating when ops admins leave.
Currently elastalert is setup to bindmounted the `rules/` directory to the containers `/opt/elastalert/rules` directory. Any changes made to the rules then requires a restart to the container.