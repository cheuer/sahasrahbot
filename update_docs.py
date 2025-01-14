#!/usr/bin/python3
import os

import yaml

# update presets

markdown_contents = """---
layout: default
title:  Presets
---
* Table of contents
{:toc}
# SahasrahBot Presets
"""

for game in [d for d in sorted(os.listdir('presets')) if os.path.isdir(os.path.join('presets', d))]:
    markdown_contents += f"## {game.upper()}\n\n| Preset | Description | |\n|---|---|---|\n"

    for preset in [f for f in sorted(os.listdir(f'presets/{game}')) if f.endswith('.yaml')]:
        with open(os.path.join('presets', game, preset)) as f:
            preset_file = yaml.safe_load(f)
        description = preset_file.get('description', '').replace('\n', ' ')
        markdown_contents += f"| [{preset.split('.')[0]}](https://github.com/tcprescott/sahasrahbot/blob/master/presets/{game}/{preset}) |"
        markdown_contents += f"{description}| {'*Customizer*' if preset_file.get('customizer', False) else ''} {'*Festive-only*' if preset_file.get('festive', False) else ''} {'*Door Randomizer*' if preset_file.get('doors', False) else ''}|\n"
    markdown_contents += "\n"

with open(os.path.join('docs', 'presets.md'), mode='w+') as f:
    f.write(markdown_contents)

markdown_contents = """---
layout: default
title:  Mystery Weights
---
* Table of contents
{: toc}
# SahasrahBot Mystery Weightsets

"""
markdown_contents += "| Preset | Description | |\n|---|---|---|\n"

for weight in [f for f in sorted(os.listdir(f'weights')) if f.endswith('.yaml') and not f == 'bot_testing.yaml']:
    with open(os.path.join('weights', weight)) as f:
        weight_file = yaml.safe_load(f)
    description = weight_file.get('description', '').replace('\n', ' ')
    markdown_contents += f"| [{weight.split('.')[0]}](https://github.com/tcprescott/sahasrahbot/blob/master/weights/{weight}) | {description} | {'*Customizer*' if weight_file.get('customizer', False) else ''}{'*Festive-only*' if weight_file.get('festive', False) else ''}{'*Subweights*' if weight_file.get('subweights', False) else ''} {'*Door Randomizer*' if preset_file.get('door_shuffle', False) else ''}|\n"

with open(os.path.join('docs', 'mystery.md'), mode='w+') as f:
    f.write(markdown_contents)
