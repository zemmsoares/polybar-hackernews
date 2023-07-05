![Polybar-hackernews](/assets/example.gif?raw=true "Polybar-hackernews")

## Dependencies

- [requests](https://pypi.org/project/requests/) - python requests
- [zscroll](https://github.com/noctuid/zscroll#installation) - for **polybar** scroll *(optional)*
- [scroll](https://github.com/Anachron/i3blocks#scroll) - for **i3blocks** scroll *(optional)*

## Polybar Modules

```ini
; Fetches news from API and saves it into articles.json
[module/hackernews-fetcher]
type = custom/script
exec = ~/.my_python_envs/polybar_hackernews_env/bin/python ~/.config/polybar/custom-modules/polybar-hackernews/hackernews_fetcher.py
interval = 900

; Rotates through the list of news articles in articles.json 
; and saves the current article's title and URL in separate text files
; This module runs every X seconds to change the displayed article
[module/hackernews-rotator]
type = custom/script
interval = 60
exec = ~/.my_python_envs/polybar_hackernews_env/bin/python ~/.config/polybar/custom-modules/polybar-hackernews/hackernews_rotator.py

; Displays the current news article title
; Refreshes every second to ensure updated information is displayed 
; On left click, opens the current article's URL in the default web browser
[module/hackernews-display]
type = custom/script
tail = true
interval = 1
format-prefix = "  "
format = <label>
label-padding = 1
;label-maxlen = 50
exec = ~/.config/polybar/custom-modules/polybar-hackernews/print_current_article.sh ; For scrolling change to scroll_current_article.sh
click-left = < ~/.config/polybar/custom-modules/polybar-hackernews/current_article_url.txt xargs -I % xdg-open %

```
