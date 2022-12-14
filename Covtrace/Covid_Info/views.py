from django.shortcuts import render 
from Add_Patient.models import Positive_Detail, Patient_Detail, Recovered_Detail, Death_Detail, New_Death_Detail, \
    New_Positive_Detail, New_Recovered_Detail 
import folium 
from folium import plugins

def Covid_Info_Page(request):  

    alawihao_patients = []
    awitan_patients = []
    bagasbas_patients = []
    barangayI_patients = []
    barangayII_patients = []
    barangayIII_patients = []
    barangayIV_patients = []
    barangayV_patients = []
    barangayVI_patients = [] 
    barangayVII_patients = []
    barangayVIII_patients = []
    bibirao_patients = []
    borabod_patients = []
    calasgasan_patients = []
    camambugan_patients = []
    cobangbang_patients = []
    dogongan_patients = [] 
    gahonon_patients = []
    gubat_patients = []
    lagon_patients = []
    magang_patients = []
    mambalite_patients = []
    mancruz_patients = []
    pamorangon_patients = []
    san_isidro_patients = []  

    
    Details_Positive_Patients = Positive_Detail.objects.all()
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Alawihao':
            alawihao_patients.append(patients.barangay)

    alawihao_counts = len(alawihao_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Awitan':
            awitan_patients.append(patients.barangay)

    awitan_counts = len(awitan_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Bagasbas':
            bagasbas_patients.append(patients.barangay)

    bagasbas_counts = len(bagasbas_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay I':
            barangayI_patients.append(patients.barangay)

    barangayI_counts = len(barangayI_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay II':
            barangayII_patients.append(patients.barangay)

    barangayII_counts = len(barangayII_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay III':
            barangayIII_patients.append(patients.barangay)

    barangayIII_counts = len(barangayIII_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay IV':
            barangayIV_patients.append(patients.barangay)

    barangayIV_counts = len(barangayIV_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay V':
            barangayV_patients.append(patients.barangay)

    barangayV_counts = len(barangayV_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay VI':
            barangayVI_patients.append(patients.barangay)

    barangayVI_counts = len(barangayVI_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay VII':
            barangayVII_patients.append(patients.barangay)

    barangayVII_counts = len(barangayVII_patients)
 
    for patients in Details_Positive_Patients:
        if patients.barangay == 'Barangay VIII':
            barangayVIII_patients.append(patients.barangay)

    barangayVIII_counts = len(barangayVIII_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Bibirao':
            bibirao_patients.append(patients.barangay)

    bibirao_counts = len(bibirao_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Borabod':
            borabod_patients.append(patients.barangay)

    borabod_counts = len(borabod_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Calasgasan':
            calasgasan_patients.append(patients.barangay)

    calasgasan_counts = len(calasgasan_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Camambugan':
            camambugan_patients.append(patients.barangay)

    camambugan_counts = len(camambugan_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Cobangbang':
            cobangbang_patients.append(patients.barangay)

    cobangbang_counts = len(cobangbang_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Dogongan':
            dogongan_patients.append(patients.barangay)

    dogongan_counts = len(dogongan_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Gahonon':
            gahonon_patients.append(patients.barangay)

    gahonon_counts = len(gahonon_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Gubat':
            gubat_patients.append(patients.barangay)

    gubat_counts = len(gubat_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Lag-on':
            lagon_patients.append(patients.barangay)

    lagon_counts = len(lagon_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Magang':
            magang_patients.append(patients.barangay)

    magang_counts = len(magang_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Mambalite':
            mambalite_patients.append(patients.barangay)

    mambalite_counts = len(mambalite_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Mancruz':
            mancruz_patients.append(patients.barangay)

    mancruz_counts = len(mancruz_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'Pamorangon':
            pamorangon_patients.append(patients.barangay)

    pamorangon_counts = len(pamorangon_patients)

    for patients in Details_Positive_Patients:
        if patients.barangay == 'San Isidro':
            san_isidro_patients.append(patients.barangay)

    san_isidro_counts = len(san_isidro_patients)

    rec_alawihao_patients = []
    rec_awitan_patients = []
    rec_bagasbas_patients = []
    rec_barangayI_patients = []
    rec_barangayII_patients = []
    rec_barangayIII_patients = []
    rec_barangayIV_patients = []
    rec_barangayV_patients = []
    rec_barangayVI_patients = [] 
    rec_barangayVII_patients = []
    rec_barangayVIII_patients = []
    rec_bibirao_patients = []
    rec_borabod_patients = []
    rec_calasgasan_patients = []
    rec_camambugan_patients = []
    rec_cobangbang_patients = []
    rec_dogongan_patients = [] 
    rec_gahonon_patients = []
    rec_gubat_patients = []
    rec_lagon_patients = []
    rec_magang_patients = []
    rec_mambalite_patients = []
    rec_mancruz_patients = []
    rec_pamorangon_patients = []
    rec_san_isidro_patients = []

    #RECOVERED 
    
    Details_Recovered_Patients = Recovered_Detail.objects.all()
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Alawihao':
            rec_alawihao_patients.append(patients.barangay)

    rec_alawihao_counts = len(rec_alawihao_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Awitan':
            rec_awitan_patients.append(patients.barangay)

    rec_awitan_counts = len(awitan_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Bagasbas':
            rec_bagasbas_patients.append(patients.barangay)

    rec_bagasbas_counts = len(rec_bagasbas_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay I':
            rec_barangayI_patients.append(patients.barangay)

    rec_barangayI_counts = len(rec_barangayI_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay II':
            rec_barangayII_patients.append(patients.barangay)

    rec_barangayII_counts = len(rec_barangayII_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay III':
            rec_barangayIII_patients.append(patients.barangay)

    rec_barangayIII_counts = len(barangayIII_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay IV':
            rec_barangayIV_patients.append(patients.barangay)

    rec_barangayIV_counts = len(rec_barangayIV_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay V':
            rec_barangayV_patients.append(patients.barangay)

    rec_barangayV_counts = len(rec_barangayV_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay VI':
            rec_barangayVI_patients.append(patients.barangay)

    rec_barangayVI_counts = len(rec_barangayVI_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay VII':
            rec_barangayVII_patients.append(patients.barangay)

    rec_barangayVII_counts = len(rec_barangayVII_patients)
 
    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Barangay VIII':
            rec_barangayVIII_patients.append(patients.barangay)

    rec_barangayVIII_counts = len(rec_barangayVIII_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Bibirao':
            rec_bibirao_patients.append(patients.barangay)

    rec_bibirao_counts = len(bibirao_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Borabod':
            rec_borabod_patients.append(patients.barangay)

    rec_borabod_counts = len(rec_borabod_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Calasgasan':
            rec_calasgasan_patients.append(patients.barangay)

    rec_calasgasan_counts = len(rec_calasgasan_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Camambugan':
            rec_camambugan_patients.append(patients.barangay)

    rec_camambugan_counts = len(rec_camambugan_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Cobangbang':
            rec_cobangbang_patients.append(patients.barangay)

    rec_cobangbang_counts = len(rec_cobangbang_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Dogongan':
            rec_dogongan_patients.append(patients.barangay)

    rec_dogongan_counts = len(rec_dogongan_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Gahonon':
            rec_gahonon_patients.append(patients.barangay)

    rec_gahonon_counts = len(rec_gahonon_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Gubat':
            rec_gubat_patients.append(patients.barangay)

    rec_gubat_counts = len(rec_gubat_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Lag-on':
            rec_lagon_patients.append(patients.barangay)

    rec_lagon_counts = len(rec_lagon_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Magang':
            rec_magang_patients.append(patients.barangay)

    rec_magang_counts = len(rec_magang_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Mambalite':
            rec_mambalite_patients.append(patients.barangay)

    rec_mambalite_counts = len(rec_mambalite_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Mancruz':
            rec_mancruz_patients.append(patients.barangay)

    rec_mancruz_counts = len(rec_mancruz_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'Pamorangon':
            rec_pamorangon_patients.append(patients.barangay)

    rec_pamorangon_counts = len(rec_pamorangon_patients)

    for patients in Details_Recovered_Patients:
        if patients.barangay == 'San Isidro':
            rec_san_isidro_patients.append(patients.barangay)

    rec_san_isidro_counts = len(rec_san_isidro_patients)

    #DEATH
    
    
    death_alawihao_patients = []
    death_awitan_patients = []
    death_bagasbas_patients = []
    death_barangayI_patients = []
    death_barangayII_patients = []
    death_barangayIII_patients = []
    death_barangayIV_patients = []
    death_barangayV_patients = []
    death_barangayVI_patients = [] 
    death_barangayVII_patients = []
    death_barangayVIII_patients = []
    death_bibirao_patients = []
    death_borabod_patients = []
    death_calasgasan_patients = []
    death_camambugan_patients = []
    death_cobangbang_patients = []
    death_dogongan_patients = [] 
    death_gahonon_patients = []
    death_gubat_patients = []
    death_lagon_patients = []
    death_magang_patients = []
    death_mambalite_patients = []
    death_mancruz_patients = []
    death_pamorangon_patients = []
    death_san_isidro_patients = []  

    #DEATHS 
    
    Details_Death_Patients = Death_Detail.objects.all()
    for patients in Details_Death_Patients:
        if patients.barangay == 'Alawihao':
            death_alawihao_patients.append(patients.barangay)

    death_alawihao_counts = len(death_alawihao_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Awitan':
            death_awitan_patients.append(patients.barangay)

    death_awitan_counts = len(death_awitan_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Bagasbas':
            death_bagasbas_patients.append(patients.barangay)

    death_bagasbas_counts = len(death_bagasbas_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay I':
            death_barangayI_patients.append(patients.barangay)

    death_barangayI_counts = len(death_barangayI_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay II':
            death_barangayII_patients.append(patients.barangay)

    death_barangayII_counts = len(death_barangayII_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay III':
            death_barangayIII_patients.append(patients.barangay)

    death_barangayIII_counts = len(death_barangayIII_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay IV':
            death_barangayIV_patients.append(patients.barangay)

    death_barangayIV_counts = len(death_barangayIV_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay V':
            death_barangayV_patients.append(patients.barangay)

    death_barangayV_counts = len(death_barangayV_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay VI':
            death_barangayVI_patients.append(patients.barangay)

    death_barangayVI_counts = len(death_barangayVI_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay VII':
            death_barangayVII_patients.append(patients.barangay)

    death_barangayVII_counts = len(death_barangayVII_patients)
 
    for patients in Details_Death_Patients:
        if patients.barangay == 'Barangay VIII':
            death_barangayVIII_patients.append(patients.barangay)

    death_barangayVIII_counts = len(death_barangayVIII_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Bibirao':
            death_bibirao_patients.append(patients.barangay)

    death_bibirao_counts = len(death_bibirao_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Borabod':
            death_borabod_patients.append(patients.barangay)

    death_borabod_counts = len(death_borabod_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Calasgasan':
            death_calasgasan_patients.append(patients.barangay)

    death_calasgasan_counts = len(death_calasgasan_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Camambugan':
            death_camambugan_patients.append(patients.barangay)

    death_camambugan_counts = len(death_camambugan_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Cobangbang':
            death_cobangbang_patients.append(patients.barangay)

    death_cobangbang_counts = len(death_cobangbang_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Dogongan':
            death_dogongan_patients.append(patients.barangay)

    death_dogongan_counts = len(death_dogongan_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Gahonon':
            death_gahonon_patients.append(patients.barangay)

    death_gahonon_counts = len(death_gahonon_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Gubat':
            death_gubat_patients.append(patients.barangay)

    death_gubat_counts = len(death_gubat_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Lag-on':
            death_lagon_patients.append(patients.barangay)

    death_lagon_counts = len(death_lagon_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Magang':
            death_magang_patients.append(patients.barangay)

    death_magang_counts = len(death_magang_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Mambalite':
            death_mambalite_patients.append(patients.barangay)

    death_mambalite_counts = len(death_mambalite_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Mancruz':
            death_mancruz_patients.append(patients.barangay)

    death_mancruz_counts = len(death_mancruz_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'Pamorangon':
            death_pamorangon_patients.append(patients.barangay)

    death_pamorangon_counts = len(death_pamorangon_patients)

    for patients in Details_Death_Patients:
        if patients.barangay == 'San Isidro':
            death_san_isidro_patients.append(patients.barangay)

    death_san_isidro_counts = len(death_san_isidro_patients)


    patients_dets_count = Positive_Detail.objects.all().count
    patients_recovered_count = Recovered_Detail.objects.all().count
    patients_deaths_count = Death_Detail.objects.all().count

    new_patients_dets_count = New_Positive_Detail.objects.all().count
    new_patients_recovered_count = New_Recovered_Detail.objects.all().count    
    new_patients_death_count = New_Death_Detail.objects.all().count

    context = { 
        'patients_recovered_count': patients_recovered_count,
        'patients_deaths_count': patients_deaths_count,
        'patients_dets_count': patients_dets_count,
        'new_patients_dets_count': new_patients_dets_count,
        'new_patients_recovered_count': new_patients_recovered_count,
        'new_patients_death_count': new_patients_death_count,
        'death_alawihao_counts': death_alawihao_counts,
        'death_awitan_counts': death_awitan_counts,
        'death_bagasbas_counts': death_bagasbas_counts,
        'death_barangayI_counts': death_barangayI_counts,
        'death_barangayII_counts': death_barangayII_counts,
        'death_barangayIII_counts': death_barangayIII_counts,
        'death_barangayIV_counts': death_barangayIV_counts,
        'death_barangayV_counts': death_barangayV_counts,
        'death_barangayVI_counts': death_barangayVI_counts,
        'death_barangayVII_counts': death_barangayVII_counts,
        'death_barangayVIII_counts': death_barangayVIII_counts,
        'death_borabod_counts': death_borabod_counts,
        'death_bibirao_counts': death_bibirao_counts,
        'death_calasgasan_counts': death_calasgasan_counts,
        'death_camambugan_counts': death_camambugan_counts,
        'death_cobangbang_counts': death_cobangbang_counts,
        'death_dogongan_counts': death_dogongan_counts,
        'death_gahonon_counts': death_gahonon_counts,
        'death_gubat_counts': death_gubat_counts,
        'death_lagon_counts': death_lagon_counts,
        'death_magang_counts': death_magang_counts,
        'death_mambalite_counts': death_mambalite_counts,
        'death_mancruz_counts': death_mancruz_counts,
        'death_pamorangon_counts': death_pamorangon_counts,
        'death_san_isidro_counts': death_san_isidro_counts,
        'rec_alawihao_counts': rec_alawihao_counts,
        'rec_awitan_counts': rec_awitan_counts,
        'rec_bagasbas_counts': rec_bagasbas_counts,
        'rec_barangayI_counts': rec_barangayI_counts,
        'rec_barangayII_counts': rec_barangayII_counts,
        'rec_barangayIII_counts': rec_barangayIII_counts,
        'rec_barangayIV_counts': rec_barangayIV_counts,
        'rec_barangayV_counts': rec_barangayV_counts,
        'rec_barangayVI_counts': rec_barangayVI_counts,
        'rec_barangayVII_counts': rec_barangayVII_counts,
        'rec_barangayVIII_counts': rec_barangayVIII_counts,
        'rec_borabod_counts': rec_borabod_counts,
        'rec_bibirao_counts': rec_bibirao_counts,
        'rec_calasgasan_counts': rec_calasgasan_counts,
        'rec_rec_camambugan_counts': rec_camambugan_counts,
        'rec_cobangbang_counts': rec_cobangbang_counts,
        'rec_dogongan_counts': rec_dogongan_counts,
        'rec_gahonon_counts': rec_gahonon_counts,
        'rec_gubat_counts': rec_gubat_counts,
        'rec_lagon_counts': rec_lagon_counts,
        'rec_magang_counts': rec_magang_counts,
        'rec_mambalite_counts': rec_mambalite_counts,
        'rec_mancruz_counts': rec_mancruz_counts,
        'rec_pamorangon_counts': rec_pamorangon_counts,
        'rec_san_isidro_counts': rec_san_isidro_counts,
        'alawihao_counts': alawihao_counts,
        'awitan_counts': awitan_counts,
        'bagasbas_counts': bagasbas_counts,
        'barangayI_counts': barangayI_counts,
        'barangayII_counts': barangayII_counts,
        'barangayIII_counts': barangayIII_counts,
        'barangayIV_counts': barangayIV_counts,
        'barangayV_counts': barangayV_counts,
        'barangayVI_counts': barangayVI_counts,
        'barangayVII_counts': barangayVII_counts,
        'barangayVIII_counts': barangayVIII_counts,
        'borabod_counts': borabod_counts,
        'bibirao_counts': bibirao_counts,
        'calasgasan_counts': calasgasan_counts,
        'camambugan_counts': camambugan_counts,
        'cobangbang_counts': cobangbang_counts,
        'dogongan_counts': dogongan_counts,
        'gahonon_counts': gahonon_counts,
        'gubat_counts': gubat_counts,
        'lagon_counts': lagon_counts,
        'magang_counts': magang_counts,
        'mambalite_counts': mambalite_counts,
        'mancruz_counts': mancruz_counts,
        'pamorangon_counts': pamorangon_counts,
        'san_isidro_counts': san_isidro_counts
    }

    return render(request, "covid_info_urls/covid_news.html", context)