# cli-text-tool

## Help output
```
$ cli-text-tool --help
usage: cli-text-tool [-h] [--selectsplit SelectPart SplitString]
                     [--contains Contains] [--replacespace] [--replacespecial]
                     [--remove Remove]
                     text

positional arguments:
  text                  Text to modify

optional arguments:
  -h, --help            show this help message and exit
  --selectsplit SelectPart SplitString
                        Splits text at SplitString and selects SelectPart
                        (number)
  --contains Contains   Sets text to "True" if text contains string or to
                        "False" if not.
  --replacespace        Replaces all spaces in text with "_"
  --replacespecial      Replaces special characters
  --remove Remove       Removes string "Remove" from text
```

## Examples

```
$ cli-text-tool "The Killer Robot Instability" --replacespace
The_Killer_Robot_Instability
```

```
$ cli-text-tool "Der Hüpfburg-Enthusiasmus" --selectsplit 0 "-" --replacespecial
Der_Huepfburg
```

```
$ cli-text-tool "298_AfC11_-_Auf_den_Spuren_meines_Vaters.mp4" --selectsplit 1 "_-_" --remove ".mp4"
Auf_den_Spuren_meines_Vaters
```

```
$ cli-text-tool "298_AfC11_-_Auf_den_Spuren_meines_Vaters.mp4" --selectsplit 1 "_-_" --replace "_" " " --remove ".mp4"
Auf den Spuren meines Vaters
```
