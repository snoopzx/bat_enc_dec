# bat_enc_dec

![Logo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3g2emE1aTc5bDZxMzg5eXR6b3VoMDVubWJseHpqdnVrN2YxaGplYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/jzHFPlw89eTqU/giphy.gif)

converts any .bat file into a visually “corrupted” Japanese-style batch file

'-------------'![Static Badge](https://img.shields.io/badge/Made_in-KSA-white)'-------------'


## Explain bat_enc_dec

It injects the header:

```
FF FE 0A 0D
```

and then appends the raw ASCII bytes of the original BAT file
Editors interpret it as UTF-16LE To the text appears as Japanese/Asian symbols,
but Windows CMD still executes the commands normally LOL

### Perfect for:

* Batch file obfuscation

* Visual corruption effects

* Fun experiments

* Light content hiding

## Quick Usage
Encrypt a BAT file
```
python bat_enc.py file.bat
```
Decrypt a BAT file
```
python bat_dec.py file_enc.bat
```

## License
Educational and authorized security research use only. See LICENSE file.
[MIT](https://choosealicense.com/licenses/mit/)

