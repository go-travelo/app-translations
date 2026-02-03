#!/bin/bash

cd /Users/luko/work/bd/adeo/assets/i18n

# Italian (it)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} Giorni"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "Scegli Data"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "Invita qualcuno al tuo Viaggio"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "I Tuoi Voli"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "I Tuoi Trasporti"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "I Tuoi Soggiorni"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "Le Tue Destinazioni"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "Il Tuo Alloggio"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "Le Tue Esperienze"/g' \
  translations_it.i18n.json

# Portuguese (pt)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} Dias"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "Escolher Data"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "Convide alguém para sua Viagem"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "Seus Voos"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "Seus Transportes"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "Suas Estadias"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "Seus Destinos"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "Sua Acomodação"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "Suas Experiências"/g' \
  translations_pt.i18n.json

# Dutch (nl)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} Dagen"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "Kies Datum"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "Nodig iemand uit voor je Reis"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "Uw Vluchten"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "Uw Vervoer"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "Uw Verblijven"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "Uw Bestemmingen"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "Uw Accommodatie"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "Uw Ervaringen"/g' \
  translations_nl.i18n.json

# Russian (ru)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} Дней"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "Выбрать Дату"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "Пригласите кого-нибудь в вашу Поездку"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "Ваши Рейсы"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "Ваш Транспорт"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "Ваше Проживание"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "Ваши Направления"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "Ваше Размещение"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "Ваши Впечатления"/g' \
  translations_ru.i18n.json

# Chinese (zh_CN)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} 天"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "选择日期"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "邀请某人加入您的旅行"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "您的航班"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "您的交通"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "您的住宿"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "您的目的地"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "您的住宿"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "您的体验"/g' \
  translations_zh_CN.i18n.json

# Arabic (ar)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} أيام"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "اختر التاريخ"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "ادع شخصًا ما إلى رحلتك"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "رحلاتك"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "وسائل نقلك"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "إقاماتك"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "وجهاتك"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "إقامتك"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "تجاربك"/g' \
  translations_ar.i18n.json

# Hebrew (he)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} ימים"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "בחר תאריך"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "הזמן מישהו לטיול שלך"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "הטיסות שלך"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "התחבורה שלך"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "השהייה שלך"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "היעדים שלך"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "הלינה שלך"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "החוויות שלך"/g' \
  translations_he.i18n.json

# Bulgarian (bg)
sed -i.bak \
  -e 's/"daysLabel": "\${count} Days"/"daysLabel": "${count} Дни"/g' \
  -e 's/"chooseDate": "Choose Date"/"chooseDate": "Изберете Дата"/g' \
  -e 's/"inviteSomeone": "Invite someone on your Trip"/"inviteSomeone": "Поканете някого на вашето Пътуване"/g' \
  -e 's/"yourFlights": "Your Flights"/"yourFlights": "Вашите Полети"/g' \
  -e 's/"yourTransports": "Your Transports"/"yourTransports": "Вашият Транспорт"/g' \
  -e 's/"yourStays": "Your Stays"/"yourStays": "Вашите Престои"/g' \
  -e 's/"yourDestinations": "Your Destinations"/"yourDestinations": "Вашите Дестинации"/g' \
  -e 's/"yourAccommodation": "Your Accommodation"/"yourAccommodation": "Вашето Настаняване"/g' \
  -e 's/"yourExperiences": "Your Experiences"/"yourExperiences": "Вашите Преживявания"/g' \
  translations_bg.i18n.json

# Clean up backup files
rm -f *.bak

echo "Updated trip headers and sections in all files!"
