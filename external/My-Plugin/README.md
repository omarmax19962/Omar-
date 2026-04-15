# My-Plugin placeholder

This directory is reserved for the upstream plugin repository:

- URL: `https://github.com/omarmax19962/My-Plugin.git`

The execution environment currently cannot access GitHub (HTTP 403), so the plugin source could not be fetched automatically.

To populate this folder in a network-enabled environment:

```bash
git submodule add https://github.com/omarmax19962/My-Plugin.git external/My-Plugin
git submodule update --init --recursive
```
