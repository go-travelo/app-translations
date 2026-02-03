#!/usr/bin/env python3
"""
Complete trip section translations for all remaining languages
"""

import json
import os

# Translation mapping for all languages
TRANSLATIONS = {
    "it": {  # Italian
        "tripWord": "Viaggio",
        "header": {
            "daysLabel": "${count} Giorni",
            "chooseDate": "Scegli Data",
            "inviteSomeone": "Invita qualcuno al tuo Viaggio"
        },
        "sections": {
            "yourFlights": "I Tuoi Voli",
            "yourTransports": "I Tuoi Trasporti",
            "yourStays": "I Tuoi Soggiorni",
            "yourDestinations": "Le Tue Destinazioni",
            "yourAccommodation": "Il Tuo Alloggio",
            "yourExperiences": "Le Tue Esperienze",
            "days": "Giorni"
        },
        "emptyStates": {
            "noFlightsFound": "Nessun volo trovato",
            "noTransportationFound": "Nessun trasporto trovato",
            "noStaysFound": "Nessun soggiorno trovato",
            "noDestinationsFound": "Nessuna destinazione trovata",
            "mapViewUnavailable": "Vista mappa non disponibile",
            "mapViewNoLocations": "Vista mappa - Nessuna posizione disponibile",
            "dayNotFound": "Giorno non trovato"
        },
        "flight": {
            "title": "Volo",
            "perPerson": "/persona",
            "direct": "Diretto",
            "oneStop": "1 scalo",
            "stops": "${count} scali"
        },
        "hotel": {
            "title": "Hotel",
            "yourStay": "Il Tuo Soggiorno",
            "reviews": "${count} Recensioni",
            "viewDetails": "Vedi Dettagli"
        },
        "destination": {
            "dayLabel": "Giorno ${start} - ${end}",
            "experience": "${count} Esperienza",
            "experiences": "${count} Esperienze",
            "total": "totale"
        },
        "transport": {
            "title": "Trasporto",
            "pickUp": "Ritiro",
            "dropOff": "Consegna"
        },
        "restaurant": {
            "title": "Ristorante"
        },
        "experience": {
            "title": "Esperienza",
            "activity": "Attività",
            "attraction": "Attrazione",
            "free": "Gratuito",
            "clickToSeePrice": "Clicca per vedere il prezzo",
            "reviewsCount": "${count} Recensioni"
        },
        "actions": {
            "change": "Cambia",
            "getLivePrices": "Ottieni prezzi in tempo reale",
            "bookNow": "Prenota Ora",
            "share": "Condividi",
            "delete": "Elimina",
            "invite": "Invita"
        },
        "tabs": {
            "overview": "Panoramica"
        },
        "trip_page": {
            "travel_tip": "Consiglio di Viaggio",
            "daily_itinerary": "Itinerario Giornaliero",
            "day_by_day_plan": "Piano giorno per giorno per ${destination}",
            "creator_tips": "Consigli del Creatore",
            "creator_videos": "Video del Creatore",
            "your_accommodation": "Il Tuo Alloggio",
            "guest_reviews": "Recensioni degli Ospiti",
            "pricing_details": "Dettagli del Prezzo",
            "price_per_night": "Prezzo per notte",
            "per_night": "per notte",
            "total_price": "Prezzo totale",
            "great_value": "Ottimo rapporto qualità-prezzo",
            "things_to_do": "Cose da fare",
            "activity": "Attività",
            "attraction": "Attrazione",
            "sitesAroundTitle": "Siti intorno a ${city}",
            "sitesAroundSubtitle": "Scopri luoghi vicino alla tua destinazione",
            "seeAll": "Vedi tutto",
            "videoModalComingSoon": "Galleria video completa in arrivo!",
            "videosAvailable": "video disponibili",
            "close": "Chiudi",
            "add_hotel": "Aggiungi Hotel",
            "add_transportation": "Aggiungi Trasporto",
            "retry": "Riprova",
            "map_unavailable": "Mappa non disponibile",
            "dates_tbd": "Date da definire"
        }
    },
    "pt": {  # Portuguese
        "tripWord": "Viagem",
        "header": {
            "daysLabel": "${count} Dias",
            "chooseDate": "Escolher Data",
            "inviteSomeone": "Convide alguém para sua Viagem"
        },
        "sections": {
            "yourFlights": "Seus Voos",
            "yourTransports": "Seus Transportes",
            "yourStays": "Suas Estadias",
            "yourDestinations": "Seus Destinos",
            "yourAccommodation": "Sua Acomodação",
            "yourExperiences": "Suas Experiências",
            "days": "Dias"
        },
        "trip_page": {
            "travel_tip": "Dica de Viagem",
            "daily_itinerary": "Itinerário Diário",
            "day_by_day_plan": "Plano dia a dia para ${destination}",
            "creator_tips": "Dicas do Criador",
            "creator_videos": "Vídeos do Criador",
            "your_accommodation": "Sua Acomodação",
            "guest_reviews": "Avaliações dos Hóspedes",
            "pricing_details": "Detalhes de Preço",
            "price_per_night": "Preço por noite",
            "per_night": "por noite",
            "total_price": "Preço total",
            "great_value": "Ótimo custo-benefício",
            "things_to_do": "Coisas para fazer",
            "activity": "Atividade",
            "attraction": "Atração",
            "sitesAroundTitle": "Locais em torno de ${city}",
            "sitesAroundSubtitle": "Descubra lugares perto do seu destino",
            "seeAll": "Ver tudo",
            "videoModalComingSoon": "Galeria de vídeos completa em breve!",
            "videosAvailable": "vídeos disponíveis",
            "close": "Fechar",
            "add_hotel": "Adicionar Hotel",
            "add_transportation": "Adicionar Transporte",
            "retry": "Tentar Novamente",
            "map_unavailable": "Mapa não disponível",
            "dates_tbd": "Datas a definir"
        }
    },
    "nl": {  # Dutch
        "tripWord": "Reis",
        "header": {
            "daysLabel": "${count} Dagen",
            "chooseDate": "Kies Datum",
            "inviteSomeone": "Nodig iemand uit voor je Reis"
        },
        "sections": {
            "yourFlights": "Uw Vluchten",
            "yourTransports": "Uw Vervoer",
            "yourStays": "Uw Verblijven",
            "yourDestinations": "Uw Bestemmingen",
            "yourAccommodation": "Uw Accommodatie",
            "yourExperiences": "Uw Ervaringen",
            "days": "Dagen"
        },
        "trip_page": {
            "travel_tip": "Reistip",
            "daily_itinerary": "Dagelijkse Reisroute",
            "day_by_day_plan": "Dag-tot-dag plan voor ${destination}",
            "creator_tips": "Tips van Maker",
            "creator_videos": "Video's van Maker",
            "your_accommodation": "Uw Accommodatie",
            "guest_reviews": "Beoordelingen van Gasten",
            "pricing_details": "Prijsdetails",
            "price_per_night": "Prijs per nacht",
            "per_night": "per nacht",
            "total_price": "Totale prijs",
            "great_value": "Uitstekende prijs-kwaliteit",
            "things_to_do": "Dingen om te doen",
            "activity": "Activiteit",
            "attraction": "Attractie",
            "sitesAroundTitle": "Plaatsen rond ${city}",
            "sitesAroundSubtitle": "Ontdek plaatsen bij uw bestemming",
            "seeAll": "Alles bekijken",
            "videoModalComingSoon": "Volledige videogalerij binnenkort beschikbaar!",
            "videosAvailable": "video's beschikbaar",
            "close": "Sluiten",
            "add_hotel": "Hotel Toevoegen",
            "add_transportation": "Vervoer Toevoegen",
            "retry": "Opnieuw Proberen",
            "map_unavailable": "Kaart niet beschikbaar",
            "dates_tbd": "Data nog te bepalen"
        }
    },
    "ru": {  # Russian
        "tripWord": "Поездка",
        "header": {
            "daysLabel": "${count} Дней",
            "chooseDate": "Выбрать Дату",
            "inviteSomeone": "Пригласите кого-нибудь в вашу Поездку"
        },
        "sections": {
            "yourFlights": "Ваши Рейсы",
            "yourTransports": "Ваш Транспорт",
            "yourStays": "Ваше Проживание",
            "yourDestinations": "Ваши Направления",
            "yourAccommodation": "Ваше Размещение",
            "yourExperiences": "Ваши Впечатления",
            "days": "Дни"
        },
        "trip_page": {
            "travel_tip": "Совет путешественникам",
            "daily_itinerary": "Ежедневный Маршрут",
            "day_by_day_plan": "План день за днем для ${destination}",
            "creator_tips": "Советы Создателя",
            "creator_videos": "Видео Создателя",
            "your_accommodation": "Ваше Размещение",
            "guest_reviews": "Отзывы Гостей",
            "pricing_details": "Детали Цен",
            "price_per_night": "Цена за ночь",
            "per_night": "за ночь",
            "total_price": "Общая цена",
            "great_value": "Отличное соотношение цены и качества",
            "things_to_do": "Чем заняться",
            "activity": "Активность",
            "attraction": "Достопримечательность",
            "sitesAroundTitle": "Места вокруг ${city}",
            "sitesAroundSubtitle": "Откройте для себя места рядом с вашим пунктом назначения",
            "seeAll": "Смотреть все",
            "videoModalComingSoon": "Полная видеогалерея скоро!",
            "videosAvailable": "видео доступно",
            "close": "Закрыть",
            "add_hotel": "Добавить Отель",
            "add_transportation": "Добавить Транспорт",
            "retry": "Повторить",
            "map_unavailable": "Карта недоступна",
            "dates_tbd": "Даты уточняются"
        }
    },
    "zh_CN": {  # Chinese
        "tripWord": "旅行",
        "header": {
            "daysLabel": "${count} 天",
            "chooseDate": "选择日期",
            "inviteSomeone": "邀请某人加入您的旅行"
        },
        "sections": {
            "yourFlights": "您的航班",
            "yourTransports": "您的交通",
            "yourStays": "您的住宿",
            "yourDestinations": "您的目的地",
            "yourAccommodation": "您的住宿",
            "yourExperiences": "您的体验",
            "days": "天数"
        },
        "trip_page": {
            "travel_tip": "旅行提示",
            "daily_itinerary": "每日行程",
            "day_by_day_plan": "${destination}的每日计划",
            "creator_tips": "创作者提示",
            "creator_videos": "创作者视频",
            "your_accommodation": "您的住宿",
            "guest_reviews": "客人评价",
            "pricing_details": "价格详情",
            "price_per_night": "每晚价格",
            "per_night": "每晚",
            "total_price": "总价",
            "great_value": "超值",
            "things_to_do": "旅游活动",
            "activity": "活动",
            "attraction": "景点",
            "sitesAroundTitle": "${city}周边景点",
            "sitesAroundSubtitle": "发现目的地附近的地方",
            "seeAll": "查看全部",
            "videoModalComingSoon": "完整视频库即将推出!",
            "videosAvailable": "视频可用",
            "close": "关闭",
            "add_hotel": "添加酒店",
            "add_transportation": "添加交通",
            "retry": "重试",
            "map_unavailable": "地图不可用",
            "dates_tbd": "日期待定"
        }
    },
    "ar": {  # Arabic
        "tripWord": "رحلة",
        "header": {
            "daysLabel": "${count} أيام",
            "chooseDate": "اختر التاريخ",
            "inviteSomeone": "ادع شخصًا ما إلى رحلتك"
        },
        "sections": {
            "yourFlights": "رحلاتك",
            "yourTransports": "وسائل نقلك",
            "yourStays": "إقاماتك",
            "yourDestinations": "وجهاتك",
            "yourAccommodation": "إقامتك",
            "yourExperiences": "تجاربك",
            "days": "أيام"
        },
        "trip_page": {
            "travel_tip": "نصيحة سفر",
            "daily_itinerary": "برنامج يومي",
            "day_by_day_plan": "خطة يومية لـ ${destination}",
            "creator_tips": "نصائح المنشئ",
            "creator_videos": "فيديوهات المنشئ",
            "your_accommodation": "إقامتك",
            "guest_reviews": "تقييمات الضيوف",
            "pricing_details": "تفاصيل التسعير",
            "price_per_night": "السعر لكل ليلة",
            "per_night": "لكل ليلة",
            "total_price": "السعر الإجمالي",
            "great_value": "قيمة رائعة",
            "things_to_do": "أشياء يمكن القيام بها",
            "activity": "نشاط",
            "attraction": "معلم سياحي",
            "sitesAroundTitle": "أماكن حول ${city}",
            "sitesAroundSubtitle": "اكتشف أماكن بالقرب من وجهتك",
            "seeAll": "عرض الكل",
            "videoModalComingSoon": "معرض الفيديو الكامل قريبًا!",
            "videosAvailable": "مقاطع فيديو متاحة",
            "close": "إغلاق",
            "add_hotel": "إضافة فندق",
            "add_transportation": "إضافة نقل",
            "retry": "إعادة المحاولة",
            "map_unavailable": "الخريطة غير متوفرة",
            "dates_tbd": "التواريخ لم تحدد بعد"
        }
    },
    "he": {  # Hebrew
        "tripWord": "טיול",
        "header": {
            "daysLabel": "${count} ימים",
            "chooseDate": "בחר תאריך",
            "inviteSomeone": "הזמן מישהו לטיול שלך"
        },
        "sections": {
            "yourFlights": "הטיסות שלך",
            "yourTransports": "התחבורה שלך",
            "yourStays": "השהייה שלך",
            "yourDestinations": "היעדים שלך",
            "yourAccommodation": "הלינה שלך",
            "yourExperiences": "החוויות שלך",
            "days": "ימים"
        },
        "trip_page": {
            "travel_tip": "טיפ לנסיעה",
            "daily_itinerary": "מסלול יומי",
            "day_by_day_plan": "תוכנית יום אחר יום ל-${destination}",
            "creator_tips": "טיפים מהיוצר",
            "creator_videos": "סרטונים של היוצר",
            "your_accommodation": "הלינה שלך",
            "guest_reviews": "ביקורות אורחים",
            "pricing_details": "פרטי תמחור",
            "price_per_night": "מחיר ללילה",
            "per_night": "ללילה",
            "total_price": "מחיר כולל",
            "great_value": "תמורה מצוינת",
            "things_to_do": "דברים לעשות",
            "activity": "פעילות",
            "attraction": "אטרקציה",
            "sitesAroundTitle": "אתרים סביב ${city}",
            "sitesAroundSubtitle": "גלה מקומות ליד היעד שלך",
            "seeAll": "ראה הכל",
            "videoModalComingSoon": "גלריית וידאו מלאה בקרוב!",
            "videosAvailable": "סרטונים זמינים",
            "close": "סגור",
            "add_hotel": "הוסף מלון",
            "add_transportation": "הוסף תחבורה",
            "retry": "נסה שוב",
            "map_unavailable": "מפה לא זמינה",
            "dates_tbd": "תאריכים טרם נקבעו"
        }
    },
    "bg": {  # Bulgarian
        "tripWord": "Пътуване",
        "header": {
            "daysLabel": "${count} Дни",
            "chooseDate": "Изберете Дата",
            "inviteSomeone": "Поканете някого на вашето Пътуване"
        },
        "sections": {
            "yourFlights": "Вашите Полети",
            "yourTransports": "Вашият Транспорт",
            "yourStays": "Вашите Престои",
            "yourDestinations": "Вашите Дестинации",
            "yourAccommodation": "Вашето Настаняване",
            "yourExperiences": "Вашите Преживявания",
            "days": "Дни"
        },
        "trip_page": {
            "travel_tip": "Съвет за пътуване",
            "daily_itinerary": "Дневен Маршрут",
            "day_by_day_plan": "План ден по ден за ${destination}",
            "creator_tips": "Съвети на Създателя",
            "creator_videos": "Видеа на Създателя",
            "your_accommodation": "Вашето Настаняване",
            "guest_reviews": "Отзиви на Гости",
            "pricing_details": "Детайли за Цените",
            "price_per_night": "Цена на нощувка",
            "per_night": "на нощувка",
            "total_price": "Обща цена",
            "great_value": "Страхотна стойност",
            "things_to_do": "Неща за правене",
            "activity": "Дейност",
            "attraction": "Атракция",
            "sitesAroundTitle": "Места около ${city}",
            "sitesAroundSubtitle": "Открийте места близо до вашата дестинация",
            "seeAll": "Виж всички",
            "videoModalComingSoon": "Пълна видео галерия скоро!",
            "videosAvailable": "видеа налични",
            "close": "Затвори",
            "add_hotel": "Добави Хотел",
            "add_transportation": "Добави Транспорт",
            "retry": "Опитай Отново",
            "map_unavailable": "Картата не е налична",
            "dates_tbd": "Дати за определяне"
        }
    }
}

def main():
    print("Translation data prepared for:")
    for lang in TRANSLATIONS:
        print(f"  - {lang}: {TRANSLATIONS[lang]['tripWord']}")
    print("\nThis data can be used to update the remaining translation files.")
    print("Manual application required due to file structure complexity.")

if __name__ == "__main__":
    main()
