import requests
from bs4 import BeautifulSoup
import os
import csv
import datetime

starttime = datetime.datetime.now()
starttime1 = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')

urls = [
    'https://shop.miele.ua/catalog/cnbh/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vertik/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/c_cei/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/sushilnye_mashiny_3/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/gladilnye_mashiny_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_sushilnym_mashinam/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/otdelno_stoyashchie_posudomoechnye_mashiny_45_sm/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vstraivaemye_posudomoechnye_mashiny_60_sm_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/polnovstraivaemye_posudomoechnye_mashiny_45_sm_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/polnovstraivaemye_posudomoechnye_mashiny_60_sm_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/dukhovye_shkafy_s_svch/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/dukhovye_shkafy_60_sm/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/dukhovye_shkafy_shirinoy_90_sm/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/parovye_shkafy_kompaktnye/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/parovye_shkafy_s_svch/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/kombinirovannye_parovye_shkafy_kompaktnye/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/kombinirovannye_parovye_shkafy/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/mikrovolnovye_pechi_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/gazovye_varochnye_poverkhnosti/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/induktsionnye_varochnye_poverkhnosti/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/elektricheskie_varochnye_poverkhnosti/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/tepany/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/elektricheskie_paneli/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/gazovye_paneli/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vytyazhnoy_modul/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/podogrevateli_posudy_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vakuumatory/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vytyazhki_vstraivaemye_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vytyazhki_nastennye_dekorativnye_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vytyazhki_ostrovnye_dekorativnye_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/solo_kofemashiny_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vstraivaemye_kofemashiny/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/otdelnostoyashchie_kholodilniki_morozilniki/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/otdelnostoyashchie_kholodilniki/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/otdelnostoyashchie_morozilniki/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vstraivaemye_kholodilniki_morozilniki_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vstraivaemye_kholodilniki_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vstraivaemye_morozilniki_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/vinnye_kholodilniki_1/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/mastercool_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_mastercool/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_vytyazhkam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_kofemashinam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_modulnym_panelyam_smartline/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_varochnym_poverkhnostyam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_parovym_shkafam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_posudomoechnym_mashinam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_dukhovym_shkafam/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/bezmeshkovye_pylesosy/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/pylesosy_s_meshkom_pylesbornikom/?SHOWALL_1=1',
    'https://shop.miele.ua/catalog/besprovodnye_akkumulyatornye_pylesosy/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_pylesosam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_stiralnykh_i_sushilnykh_mashin/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_gladilnykh_sistem_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_dukhovykh_shkafov_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_parovykh_shkafov/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_posudomoechnykh_mashin_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/dlya_kofemashin_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_dlya_gladilnykh_mashin/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_vakuumatoram/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_vytyazhkam_2/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_kofemashinam_2/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_modulnym_panelyam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_varochnym_poverkhnostyam_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_posudomoechnym_mashinam_2/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_pylesosam_2/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_stiralnym_i_sushilnym_mashinam_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_kholodilnikam_i_morozilnikam/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/aksessuary_k_dukhovym_shkafam_1/?SHOWALL_1=1',
    # 'https://shop.miele.ua/catalog/miele_home_1/?SHOWALL_1=1'
]

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

count = 1
for url in urls:
    req = requests.get(url, headers=headers)
    src = req.text
    with open(f'html/{count}_index.html', 'w', encoding="utf-8") as file:
        file.write(src)
    count += 1

dir_name = "C:\Python\Parsing\Miele\html"
list = os.listdir(dir_name)

for item in list:
    with open(f"C:\Python\Parsing\Miele\html\{item}", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_products_hrefs = soup.find_all(class_="item-title")

    all_tov_dict = {}
    for item in all_products_hrefs:
        item_title = item.find('a').text
        item_href = 'https://shop.miele.ua' + item.find('a').get('href')
        all_tov_dict[item_title] = item_href

    for tov_name, tov_href in all_tov_dict.items():
        req = requests.get(url=tov_href, headers=headers)
        src = req.text

        try:
            with open(f"html_tov/{tov_name}.html", "w", encoding="utf-8") as file:
                file.write(src)
        except FileNotFoundError:
            print(f'Error - {tov_name}.html')

dir_name = "C:\Python\Parsing\Miele\html_tov"
list = os.listdir(dir_name)

with open(f"miele_{starttime1}.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "name",
            "sku",
            "price",
            # "old_price",
            "image_href",
            "out_of_stock",
            "date"
        )
    )

for item in list:
    with open(f'C:\Python\Parsing\Miele\html_tov\{item}', encoding="utf-8") as file:
        src = file.read()

    try:
        soup = BeautifulSoup(src, "lxml")
        name = soup.find('h1').text.strip()
        sku = soup.find(class_='product-number').find('span').text.strip()
        price = soup.find(class_='product-price').find(class_='current-price').text.strip()
        image_href = 'https://shop.miele.ua' + soup.find(class_='product-img').get('href')
        stock_status = soup.find(class_='product-status').find('span').text
        if stock_status == 'у наявності':
            out_of_stock = 'В наявності'
        elif stock_status == 'Немає в наявності':
            out_of_stock = 'Під замовлення'
        date = soup.find(class_='date-availability').find('span').text
    except Exception as ex:
        print(ex)

    try:
        with open(f"miele_{starttime1}.csv", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    name,
                    sku,
                    price,
                    # old_price,
                    image_href,
                    out_of_stock,
                    date
                )
            )
    except Exception as ex:
        print(ex)
diftime = datetime.datetime.now() - starttime
print(f'Elapsed time : {diftime}')
