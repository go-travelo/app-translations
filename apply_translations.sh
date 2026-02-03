#!/bin/bash

# Script to update tripWord in all remaining language files

cd /Users/luko/work/bd/adeo/assets/i18n

# Italian
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"Viaggio"/' translations_it.i18n.json

# Portuguese
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"Viagem"/' translations_pt.i18n.json

# Dutch
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"Reis"/' translations_nl.i18n.json

# Russian
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"Поездка"/' translations_ru.i18n.json

# Chinese
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"旅行"/' translations_zh_CN.i18n.json

# Arabic
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"رحلة"/' translations_ar.i18n.json

# Hebrew
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"טיול"/' translations_he.i18n.json

# Bulgarian
sed -i.bak 's/"tripWord":"Trip"/"tripWord":"Пътуване"/' translations_bg.i18n.json

echo "Updated tripWord in all files"

# Clean up backup files
rm -f *.bak

echo "Done!"
